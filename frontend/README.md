# React UI for Open3D Examples

A modern web-based interface for exploring and running Open3D visualization examples.

## Features

- **Interactive UI**: Browse mesh and point cloud examples
- **Real-time Execution**: Run scripts directly from the browser
- **Live Output**: View script execution results instantly
- **Responsive Design**: Works on desktop and tablet devices
- **Modern Stack**: React 18 + Vite + TypeScript

## Tech Stack

### Frontend
- **React 18** - UI library
- **Vite 5** - Build tool for fast development
- **TypeScript** - Type-safe JavaScript
- **Axios** - HTTP client for API calls
- **CSS3** - Modern styling with Flexbox/Grid

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing support

## Prerequisites

Before running the application, ensure you have:

- Python 3.12+
- Node.js 18+ (for frontend)
- npm (comes with Node.js)

## Installation

### 1. Install Python Dependencies

```bash
# Install with uv (recommended)
uv sync

# Or with pip
pip install -r requirements.txt
```

### 2. Install Frontend Dependencies

```bash
cd frontend
npm install
```

## Development

### Start Frontend Development Server

```bash
cd frontend
npm run dev
```

The frontend will run at `http://localhost:5173` with hot module replacement.

### Start Backend API Server

In a separate terminal:

```bash
python app.py
```

The API server will run at `http://localhost:5000`.

### Access the Application

Open your browser to: `http://localhost:5173`

The Vite dev server is configured to proxy API requests to the backend automatically.

## Building for Production

### Build Frontend

```bash
cd frontend
npm run build
```

This creates optimized production files in `frontend/dist/`.

### Run Production Server

```bash
# Make sure frontend is built first
cd frontend && npm run build && cd ..

# Then run the Flask server
python app.py
```

Visit `http://localhost:5000` to access the application.

## Project Structure

```
open3d-examples/
├── app.py                          # Flask backend API
├── frontend/                       # React application
│   ├── index.html                 # Entry HTML file
│   ├── package.json               # Frontend dependencies
│   ├── vite.config.ts             # Vite configuration
│   ├── tsconfig.json              # TypeScript configuration
│   └── src/
│       ├── main.tsx               # React entry point
│       ├── App.tsx                # Main App component
│       ├── types.ts               # TypeScript type definitions
│       ├── components/
│       │   ├── Header.tsx         # Application header
│       │   ├── ExamplesList.tsx   # Examples list sidebar
│       │   └── ExampleDetail.tsx  # Example details panel
│       ├── services/
│       │   └── api.ts             # API client
│       └── styles/
│           ├── index.css          # Global styles
│           ├── App.css            # App layout
│           ├── Header.css         # Header styles
│           ├── ExamplesList.css   # List styles
│           └── ExampleDetail.css  # Detail panel styles
├── src/
│   ├── scripts/
│   │   ├── mesh/                  # Mesh examples
│   │   └── point_cloud/           # Point cloud examples
│   └── open3d_examples/
├── README.md                       # Main documentation
└── pyproject.toml                 # Python project configuration
```

## API Endpoints

### GET `/api/examples`
List all available examples.

**Response:**
```json
[
  {
    "id": "point_cloud_example1",
    "name": "Example 1",
    "category": "Point Cloud",
    "description": "Load and visualize point clouds",
    "path": "src/scripts/point_cloud/example1.py"
  }
]
```

### POST `/api/examples/<example_id>/run`
Execute a specific example script.

**Response:**
```json
{
  "success": true,
  "output": "Script output here...",
  "error": null
}
```

### GET `/api/examples/<example_id>`
Get details for a specific example.

## Troubleshooting

### Frontend not loading
- Ensure the frontend is built: `cd frontend && npm run build`
- Check that Flask is running on `http://localhost:5000`

### API requests failing
- Verify Flask server is running: `python app.py`
- Check CORS is enabled in `app.py`
- Verify the proxy configuration in `vite.config.ts`

### Scripts not executing
- Ensure all example scripts exist in `src/scripts/mesh/` and `src/scripts/point_cloud/`
- Check Python version compatibility (3.12+)
- Verify Open3D is installed: `pip list | grep open3d`

### Vite dev server issues
- Clear node_modules and reinstall: `rm -rf node_modules && npm install`
- Check Node.js version: `node --version`

## Development Tips

### Hot Reloading
- Frontend: Vite provides instant hot module replacement during development
- Backend: Restart Flask manually when Python files change

### Adding New Examples
1. Create a new Python script in `src/scripts/mesh/` or `src/scripts/point_cloud/`
2. Add a docstring describing the example
3. Restart the Flask server
4. The example will appear automatically in the UI

### Styling
- Global styles in `src/styles/index.css`
- Component-specific styles in corresponding `.css` files
- Color scheme: Purple gradient (`#667eea` to `#764ba2`)

## Performance Optimization

- Vite provides fast builds and development experience
- React 18 with strict mode for development debugging
- Lazy component rendering in the examples list
- CSS Grid/Flexbox for efficient layouts

## Browser Support

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions

## Contributing

To add new features:

1. Create feature branches
2. Follow the existing component structure
3. Use TypeScript for type safety
4. Test in development mode before building

## License

Same as the main open3d-examples project.
