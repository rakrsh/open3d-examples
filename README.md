# open3d-examples

Examples and interactive web UI for the Open3D module. Explore 3D mesh and point cloud algorithms with a modern React interface.

## 🚀 Quick Start

### Option 1: React Web UI (Recommended)

A modern web-based interface for exploring and running examples.

#### Prerequisites
- Python 3.12+
- Node.js 18+
- npm

#### Setup

```bash
# 1. Install Python dependencies
uv sync
# or: pip install flask flask-cors

# 2. Install frontend dependencies
cd frontend
npm install

# 3. Build the frontend
npm run build
cd ..

# 4. Run the application
python app.py
```

Then open `http://localhost:5000` in your browser.

**For development** with hot reload:
- Terminal 1: `cd frontend && npm run dev`
- Terminal 2: `python app.py`
- Open `http://localhost:5173`

See [frontend/README.md](frontend/README.md) for detailed frontend documentation.

### Option 2: Legacy Tkinter UI

Simple Python desktop UI (deprecated but still available).

```bash
python run_visualization.py
```

This UI:
- Lists examples in `mesh/` and `point_cloud/`
- Runs selected scripts in a separate Python process
- Displays console output in the UI
- Opens Open3D visualization windows

## 📋 Requirements

### Minimum (Python only)
- Python 3.12+
- `uv` for dependency management (recommended)

```bash
python -m pip install uv
```

### Install dependencies

```bash
# With uv (recommended)
uv sync

# Or with pip
pip install -r requirements.txt
```

### Install Open3D

```bash
pip install open3d
```

## 📁 Project Structure

```
open3d-examples/
├── app.py                    # Flask backend API
├── frontend/                 # React web UI
│   ├── src/                 # React components and styles
│   ├── package.json         # Frontend dependencies
│   ├── vite.config.ts       # Vite build configuration
│   └── README.md            # Frontend documentation
├── src/
│   ├── scripts/
│   │   ├── mesh/            # Mesh visualization examples
│   │   └── point_cloud/     # Point cloud examples
│   └── open3d_examples/
├── pyproject.toml           # Python project configuration
└── README.md                # This file
```

## 🎨 Features

### React UI
- Modern, responsive web interface
- Browse examples by category
- Run scripts with one click
- Real-time output streaming
- Interactive UI with Vite hot reload
- Built with React 18 + TypeScript

### Examples
- **Point Cloud**: Bounding volumes, clustering, convex hulls, plane segmentation, and more
- **Mesh**: Cropping, properties, surface normal estimation, visualization

## 📚 Documentation

- [Frontend Documentation](frontend/README.md) - React UI setup, development, and architecture
- [Python API](app.py) - Flask backend endpoints
- Example scripts in `src/scripts/` contain detailed comments

## 🛠️ Development

### Frontend Development
```bash
cd frontend
npm run dev
```

### Backend Development
```bash
python app.py
```

### Build for Production
```bash
cd frontend && npm run build && cd ..
python app.py
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/examples` | List all examples |
| GET | `/api/examples/<id>` | Get example details |
| POST | `/api/examples/<id>/run` | Execute an example |

## 🐛 Troubleshooting

**Frontend not loading?**
- Build the frontend: `cd frontend && npm run build`
- Check Flask is running: `python app.py`

**Scripts not executing?**
- Verify Open3D is installed: `pip list | grep open3d`
- Check Python version: `python --version`

**API requests failing?**
- Ensure Flask server is on port 5000
- Check the proxy configuration in `vite.config.ts`

## 📦 Dependencies

### Python
- numpy >= 1.26
- open3d >= 0.18
- matplotlib >= 3.8
- flask (for web UI)
- flask-cors (for web UI)

### Frontend
- react 18.2
- react-dom 18.2
- vite 5.0
- typescript 5.2
- axios 1.6

## 📝 License

MIT - See LICENSE file for details
