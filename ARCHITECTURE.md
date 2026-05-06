# Architecture Guide

This document describes the architecture of the Open3D Examples React UI project.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User Browser                             │
├─────────────────────────────────────────────────────────────┤
│  React 18 SPA                                               │
│  ├── Header Component                                       │
│  ├── ExamplesList Component                                │
│  └── ExampleDetail Component                               │
├─────────────────────────────────────────────────────────────┤
│  HTTP REST API Client (Axios)                              │
└────────┬────────────────────────────────────────────────────┘
         │
         │ HTTP Requests
         │
┌────────▼────────────────────────────────────────────────────┐
│            Flask Backend (port 5000)                         │
├─────────────────────────────────────────────────────────────┤
│  API Endpoints:                                             │
│  ├── GET  /api/examples                                     │
│  ├── GET  /api/examples/<id>                                │
│  └── POST /api/examples/<id>/run                            │
├─────────────────────────────────────────────────────────────┤
│  CORS Middleware                                            │
├─────────────────────────────────────────────────────────────┤
│  Script Execution Engine                                    │
│  └── subprocess module to run Python scripts                │
└────────┬────────────────────────────────────────────────────┘
         │
         │ subprocess.run()
         │
┌────────▼────────────────────────────────────────────────────┐
│            Python Example Scripts                            │
├─────────────────────────────────────────────────────────────┤
│  src/scripts/                                               │
│  ├── mesh/                                                  │
│  │   ├── crop_mesh.py                                       │
│  │   ├── mesh_properties.py                                 │
│  │   └── ...                                                │
│  └── point_cloud/                                           │
│      ├── example1.py                                        │
│      ├── bounding_volumes.py                                │
│      └── ...                                                │
└─────────────────────────────────────────────────────────────┘
```

## Component Architecture

### Frontend Component Tree

```
App
├── Header
│   └── Title & Subtitle
├── ExamplesList
│   ├── Category Sections
│   │   └── Example Items (Buttons)
│   └── Loading/Error States
└── ExampleDetail (when selected)
    ├── Title with Category Badge
    ├── Description
    ├── Run Button
    └── Output Display
```

### Component Responsibilities

| Component | Purpose | Props | State |
|-----------|---------|-------|-------|
| `App` | Main application container | none | `examples`, `selectedExample`, `loading`, `error` |
| `Header` | Application header | none | none |
| `ExamplesList` | List of available examples | `examples`, `selected`, `onSelect`, `loading`, `error` | none |
| `ExampleDetail` | Selected example details | `example`, `onBack` | `running`, `output`, `error` |

## Data Flow

### 1. Initial Load

```
App mounts
  ↓
useEffect calls fetchExamples()
  ↓
API GET /api/examples
  ↓
Flask scans directories
  ↓
Returns array of examples
  ↓
setState(examples)
  ↓
ExamplesList renders
```

### 2. Running an Example

```
User clicks "Run Example"
  ↓
ExampleDetail calls runExample(id)
  ↓
API POST /api/examples/<id>/run
  ↓
Flask finds script
  ↓
subprocess.run() executes Python
  ↓
Returns stdout & stderr
  ↓
setOutput(result)
  ↓
Output displays in UI
```

## File Organization

### Frontend Structure

```
frontend/
├── public/              # Static assets
├── src/
│   ├── main.tsx         # React entry point
│   ├── App.tsx          # Root component
│   ├── types.ts         # TypeScript interfaces
│   ├── components/      # React components
│   │   ├── Header.tsx
│   │   ├── ExamplesList.tsx
│   │   └── ExampleDetail.tsx
│   ├── services/        # API communication
│   │   └── api.ts
│   └── styles/          # CSS files
│       ├── index.css
│       ├── App.css
│       ├── Header.css
│       ├── ExamplesList.css
│       └── ExampleDetail.css
├── index.html           # HTML entry point
├── package.json         # Dependencies
├── vite.config.ts       # Vite configuration
└── tsconfig.json        # TypeScript config
```

### Backend Structure

```
open3d-examples/
├── app.py              # Flask application
├── src/
│   ├── scripts/
│   │   ├── mesh/
│   │   └── point_cloud/
│   └── open3d_examples/
├── frontend/           # React build output
│   └── dist/
├── pyproject.toml      # Project metadata
└── requirements.txt    # Python dependencies
```

## API Specification

### Endpoint: GET /api/examples

Fetches all available examples.

**Request:**
```
GET /api/examples
```

**Response (200 OK):**
```json
[
  {
    "id": "point_cloud_example1",
    "name": "Example 1",
    "category": "point_cloud",
    "description": "Load and visualize point clouds",
    "path": "src/scripts/point_cloud/example1.py"
  },
  {
    "id": "mesh_crop_mesh",
    "name": "Crop Mesh",
    "category": "mesh",
    "description": "Crop mesh using a bounding box",
    "path": "src/scripts/mesh/crop_mesh.py"
  }
]
```

### Endpoint: GET /api/examples/<id>

Fetches details for a specific example.

**Request:**
```
GET /api/examples/point_cloud_example1
```

**Response (200 OK):**
```json
{
  "id": "point_cloud_example1",
  "name": "Example 1",
  "category": "point_cloud",
  "description": "Load and visualize point clouds",
  "path": "src/scripts/point_cloud/example1.py"
}
```

**Response (404 Not Found):**
```json
{
  "error": "Example not found"
}
```

### Endpoint: POST /api/examples/<id>/run

Executes a specific example script.

**Request:**
```
POST /api/examples/point_cloud_example1/run
```

**Response (200 OK):**
```json
{
  "success": true,
  "output": "Point cloud loaded successfully\nFile: model.ply\nPoints: 12345",
  "error": null
}
```

**Response (200 with error):**
```json
{
  "success": false,
  "output": "",
  "error": "FileNotFoundError: model.ply not found"
}
```

**Response (408 Timeout):**
```json
{
  "success": false,
  "error": "Execution timeout (30 seconds)"
}
```

**Response (500 Internal Error):**
```json
{
  "success": false,
  "error": "Execution error: [error details]"
}
```

## Technology Choices

### Frontend

| Technology | Reason |
|-----------|--------|
| React 18 | Modern UI library with hooks and concurrent features |
| Vite 5 | Fast build tool, excellent dev experience |
| TypeScript | Type safety, better IDE support, fewer runtime errors |
| Axios | Simple HTTP client, good error handling |
| CSS3 | Modern CSS with Grid/Flexbox, no CSS framework overhead |

### Backend

| Technology | Reason |
|-----------|--------|
| Flask | Lightweight, simple API development |
| Flask-CORS | Easy cross-origin request handling |
| subprocess | Built-in Python module for script execution |

## Performance Considerations

1. **Frontend**
   - Vite provides fast builds and HMR
   - React 18 optimizes rendering with concurrent features
   - CSS Grid/Flexbox for efficient layouts
   - Lazy component rendering

2. **Backend**
   - Simple synchronous API (sufficient for single-user development)
   - 30-second timeout to prevent hanging processes
   - Direct directory scanning (could be cached for large projects)

3. **Example Execution**
   - Subprocess runs scripts in separate process
   - Captures stdout/stderr in real-time
   - Returns results to frontend

## Security Considerations

1. **Input Validation**
   - Example IDs are validated before execution
   - Script paths are constructed from whitelisted directories

2. **Execution Isolation**
   - Scripts run in separate subprocess
   - No shell execution (subprocess args are passed directly)
   - Timeout prevents indefinite execution

3. **CORS**
   - Flask-CORS allows requests from frontend dev server
   - In production, configure allowed origins

## Future Enhancements

1. **Caching**
   - Cache example list for better performance

2. **Async Execution**
   - Use async/await for long-running scripts
   - Stream output with WebSockets

3. **Error Handling**
   - Better error messages in UI
   - Fallback for visualization if Open3D fails

4. **Features**
   - Script parameters/configuration
   - Save and compare outputs
   - History of runs

5. **Backend Scaling**
   - Use Gunicorn/uWSGI for production
   - Add task queue (Celery) for long operations
   - Database for example metadata
