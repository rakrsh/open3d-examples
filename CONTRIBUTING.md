# Developer Documentation & Contributing Guide

Welcome to the `open3d-examples` developer documentation! This guide will help you understand the codebase, set up your development environment, and contribute to both the backend (Flask/Python) and frontend (React/TypeScript).

## 🏗️ System Overview

The project is structured as a decoupled web application:
- **Backend (`app.py`)**: A Flask REST API that scans for Python example scripts and executes them using `subprocess`.
- **Frontend (`frontend/`)**: A React 18 Single Page Application built with Vite and TypeScript. It communicates with the Flask API to list examples and trigger their execution.
- **Example Scripts (`src/scripts/`)**: Standalone Open3D Python scripts that perform the actual 3D computations and visual rendering.

*For a detailed architectural breakdown, see [ARCHITECTURE.md](ARCHITECTURE.md).*

---

## 🛠️ Local Development Environment

### 1. Prerequisites
- Python 3.12+ (We recommend `uv` for dependency management)
- Node.js 18+ and `npm`

### 2. Backend Setup
The backend runs on `localhost:5000`.

```bash
# Clone the repository
git clone https://github.com/rakrsh/open3d-examples.git
cd open3d-examples

# Install Python dependencies using uv (recommended)
uv sync
# OR using pip: pip install -r requirements.txt

# Start the Flask backend in development mode
python app.py
```

### 3. Frontend Setup
The frontend development server runs on `localhost:5173` with Hot Module Replacement (HMR).

```bash
cd frontend

# Install Node dependencies
npm install

# Start the Vite development server
npm run dev
```

During development, requests from the frontend (`/api/*`) are proxied to the Flask backend (configured in `frontend/vite.config.ts`).

---

## 🧑‍💻 How to Add a New Example

Examples are dynamically discovered by the backend based on the directory structure inside `src/scripts/`.

1. **Create the Script:**
   Navigate to the appropriate category folder (e.g., `src/scripts/mesh/` or `src/scripts/point_cloud/`) and create your Python script (e.g., `my_new_example.py`).

2. **Write the Code:**
   Keep the script self-contained. It should import `open3d`, perform its computations, and use `open3d.visualization` to show results or print to stdout.
   ```python
   # src/scripts/point_cloud/my_new_example.py
   """
   My New Example
   This is a description of what the example does. It will be parsed by the backend.
   """
   import open3d as o3d
   
   if __name__ == "__main__":
       print("Running my new example...")
       # Your Open3D code here
   ```

3. **Backend Auto-Discovery:**
   The Flask backend parses the folder structure and the docstring (or comments) at the top of the file to populate the UI automatically. No need to update any hardcoded lists!

---

## 💻 Modifying the UI (Frontend)

If you are contributing to the UI:

- **Technology Stack**: React 18, TypeScript, Vite, CSS Modules/Plain CSS.
- **Components**: UI components are located in `frontend/src/components/`. 
- **API Client**: Network requests are managed via Axios in `frontend/src/services/api.ts`.
- **Styling**: We prefer standard CSS for this project. Keep styles modular and corresponding to their components.

### Building for Production
When you're ready to test the compiled frontend served by the Flask app:
```bash
cd frontend
npm run build
```
This generates static files in `frontend/dist/`, which `app.py` is configured to serve.

---

## 🐍 Modifying the Backend (API)

The backend is kept intentionally lightweight. If you need to add endpoints or modify execution logic:

- Main entrypoint is `app.py`.
- **Script Execution**: The endpoint `/api/examples/<id>/run` handles running scripts securely using `subprocess.run()`. It enforces a timeout (default 30 seconds) to prevent frozen processes. If an example naturally takes longer, consider updating the timeout configuration.

---

## ✅ Best Practices & Guidelines

- **Follow Copilot/Agent Instructions**: Please read [copilot-instructions.md](copilot-instructions.md) and [AGENTS.md](AGENTS.md) for coding style, repository rules, and agent limitations.
- **Type Safety**: Use TypeScript in the frontend. Use Python type hints where applicable.
- **Error Handling**: The backend should catch subprocess errors gracefully and return them as JSON so the frontend can display them properly to the user.
- **Atomic Commits**: Keep your commits small, focused, and descriptive.

## 🐛 Troubleshooting Dev Issues
- **CORS Errors**: Ensure you are accessing the frontend via the Vite proxy (`localhost:5173`) during development, not the backend directly, to avoid cross-origin issues.
- **ModuleNotFoundError**: Ensure your virtual environment is active and `uv sync` / `pip install -r requirements.txt` has been run.
