"""
Flask API backend for Open3D Examples visualizer.

Provides endpoints for:
- Listing available examples
- Running example scripts
- Streaming output from running processes
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='frontend/dist', static_url_path='')
CORS(app)

# Project paths
ROOT = Path(__file__).resolve().parent
SCRIPT_DIRS = [
    ROOT / 'src' / 'scripts' / 'mesh',
    ROOT / 'src' / 'scripts' / 'point_cloud'
]


def get_example_scripts() -> dict[str, Any]:
    """Scan directories for Python example scripts."""
    examples = []
    
    for category_dir in SCRIPT_DIRS:
        if not category_dir.exists():
            continue
            
        category = category_dir.name
        for script_path in sorted(category_dir.glob('*.py')):
            if script_path.name.startswith('_'):
                continue
                
            # Parse script for docstring/description
            description = parse_script_description(script_path)
            
            examples.append({
                'id': f'{category}_{script_path.stem}',
                'name': script_path.stem.replace('_', ' ').title(),
                'category': category.replace('_', ' ').title(),
                'description': description or 'No description available',
                'path': str(script_path.relative_to(ROOT)),
            })
    
    return {'examples': examples}


def parse_script_description(script_path: Path) -> str:
    """Extract first docstring from Python script."""
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Simple docstring extraction
        for quote in ['"""', "'''"]:
            if quote in content:
                start = content.find(quote) + len(quote)
                end = content.find(quote, start)
                if end > start:
                    doc = content[start:end].strip()
                    return doc.split('\n')[0][:100]
    except Exception:
        pass
    
    return ''


def find_script_by_id(example_id: str) -> Path | None:
    """Find script path by example ID."""
    for category_dir in SCRIPT_DIRS:
        if not category_dir.exists():
            continue
        
        category = category_dir.name
        stem = example_id.replace(f'{category}_', '')
        script_path = category_dir / f'{stem}.py'
        
        if script_path.exists():
            return script_path
    
    return None


@app.route('/api/examples', methods=['GET'])
def list_examples() -> dict[str, Any]:
    """List all available example scripts."""
    return jsonify(get_example_scripts()['examples'])


@app.route('/api/examples/<example_id>/run', methods=['POST'])
def run_example(example_id: str) -> dict[str, Any]:
    """Execute an example script and return output."""
    script_path = find_script_by_id(example_id)
    
    if not script_path:
        return jsonify({
            'success': False,
            'error': f'Example not found: {example_id}'
        }), 404
    
    try:
        # Run the example script with timeout
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(script_path.parent)
        )
        
        return jsonify({
            'success': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr if result.returncode != 0 else None
        })
    
    except subprocess.TimeoutExpired:
        return jsonify({
            'success': False,
            'error': 'Execution timeout (30 seconds)'
        }), 408
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Execution error: {str(e)}'
        }), 500


@app.route('/api/examples/<example_id>', methods=['GET'])
def get_example(example_id: str) -> dict[str, Any]:
    """Get details for a specific example."""
    all_examples = get_example_scripts()['examples']
    
    for example in all_examples:
        if example['id'] == example_id:
            return jsonify(example)
    
    return jsonify({'error': 'Example not found'}), 404


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path: str) -> Any:
    """Serve React frontend files."""
    frontend_dist = ROOT / 'frontend' / 'dist'
    
    if not frontend_dist.exists():
        return jsonify({
            'error': 'Frontend not built. Run: cd frontend && npm install && npm run build'
        }), 404
    
    if path and (frontend_dist / path).exists():
        return send_from_directory(frontend_dist, path)
    
    # Serve index.html for SPA routing
    index_path = frontend_dist / 'index.html'
    if index_path.exists():
        return send_from_directory(frontend_dist, 'index.html')
    
    return jsonify({'error': 'Frontend not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
