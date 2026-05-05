# open3d-examples
Examples using the Open3D module.

## UI Launcher

A simple Python UI is included to launch the example visualization scripts from a single interface.

### Run the launcher

```bash
python run_visualization.py
```

### What it does

- lists examples in `mesh/` and `point_cloud/`
- runs the selected script in a separate Python process
- displays console output in the UI
- opens Open3D visualization windows for the selected example

### Requirements

- Python 3.8+
- `uv` installed for dependency management

```bash
python -m pip install uv
```

### Install dependencies with uv

```bash
uv sync
```

This uses the project `pyproject.toml` manifest to install required packages.

### Install Open3D manually

```bash
pip install open3d
```
