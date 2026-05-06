# Setup Guide for React UI

This guide walks through setting up the Open3D Examples React web interface from scratch.

## Prerequisites Checklist

- [ ] Python 3.12 or higher installed
- [ ] Node.js 18 or higher installed
- [ ] npm (comes with Node.js)
- [ ] Git (for version control)
- [ ] A code editor (VS Code recommended)

Verify installations:
```bash
python --version    # Should be 3.12+
node --version      # Should be 18+
npm --version       # Should be 9+
```

## Step-by-Step Installation

### 1. Clone/Navigate to Repository

```bash
# If you don't have the repo yet
cd path/to/open3d-examples
```

### 2. Install Python Dependencies

#### Option A: Using uv (Recommended)

```bash
# Install uv if not already installed
python -m pip install uv

# Install project dependencies
uv sync
```

#### Option B: Using pip

```bash
pip install -r requirements.txt
```

Verify Flask installation:
```bash
python -c "import flask; print(flask.__version__)"
```

### 3. Install Frontend Dependencies

```bash
cd frontend
npm install
```

This installs React, Vite, TypeScript, and other dependencies.

Verify:
```bash
npm list react
npm list vite
```

### 4. Build Frontend for Development

```bash
npm run build
cd ..
```

This creates `frontend/dist/` with the compiled React app.

## Running the Application

### Development Mode (with Hot Reload)

**Terminal 1 - Frontend Dev Server:**
```bash
cd frontend
npm run dev
```
Output should show: `Local: http://localhost:5173`

**Terminal 2 - Backend API Server:**
```bash
python app.py
```
Output should show: `Running on http://127.0.0.1:5000`

**Open in Browser:**
- Navigate to `http://localhost:5173`
- The frontend will proxy API requests to the backend automatically

### Production Mode

```bash
# Build frontend
cd frontend
npm run build
cd ..

# Run production server
python app.py
```

Then open `http://localhost:5000`

## Verification

After starting the application:

1. **Check Frontend Loads**
   - Should see the header "Open3D Visualization Examples"
   - Should see a list of examples on the left

2. **Check API Works**
   - Open DevTools (F12) → Network tab
   - You should see successful requests to `/api/examples`

3. **Check Example Execution**
   - Click an example from the list
   - Click "Run Example"
   - Should see output in the detail panel

## Configuration

### Backend Configuration

Edit `app.py` to change:
- Port (default: 5000) - line with `app.run()`
- Debug mode
- Timeout for script execution (default: 30 seconds)

Example:
```python
if __name__ == '__main__':
    app.run(
        debug=True,           # Enable/disable debug mode
        host='0.0.0.0',      # Listen on all interfaces
        port=5000             # Change port here
    )
```

### Frontend Configuration

Edit `frontend/vite.config.ts` to change:
- Frontend port (default: 5173)
- API proxy target (if backend is on different URL)
- Build output directory

Example:
```typescript
server: {
  port: 5173,  // Change frontend port
  proxy: {
    '/api': {
      target: 'http://localhost:5000',  // Change backend URL
    }
  }
}
```

## Environment Variables

### Backend Environment Variables

Create a `.env` file in the project root:

```bash
FLASK_ENV=development
FLASK_DEBUG=1
PYTHONUNBUFFERED=1
```

Then source it:
```bash
# Linux/Mac
source .env

# Windows PowerShell
Get-Content .env | ForEach-Object { $_ -split '=' | ForEach-Object { $env:$_ } }
```

## Troubleshooting

### Issue: "Frontend not found" error

**Solution:**
```bash
cd frontend
npm install
npm run build
cd ..
python app.py
```

### Issue: Port already in use

**For Port 5000 (Flask):**
```bash
# Find process on port 5000
netstat -tuln | grep 5000  # Linux/Mac
netstat -ano | findstr :5000  # Windows

# Kill the process
kill -9 <PID>  # Linux/Mac
taskkill /PID <PID> /F  # Windows
```

**For Port 5173 (Vite):**
```bash
# Kill any Vite processes
pkill -f "vite"  # Linux/Mac
```

### Issue: Module not found errors

```bash
# Clear and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run build
```

### Issue: API requests fail

Check CORS in `app.py`. The Flask app should have:
```python
from flask_cors import CORS
CORS(app)
```

### Issue: Scripts don't execute

1. Verify examples exist in `src/scripts/`
2. Check permissions: `ls -la src/scripts/point_cloud/`
3. Test directly: `python src/scripts/point_cloud/example1.py`

## Advanced Setup

### Running Behind a Proxy

Edit `app.py`:
```python
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)
```

### Using Gunicorn for Production

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker Deployment

See `Dockerfile` (if available) for containerized setup.

## Next Steps

- Read [frontend/README.md](../frontend/README.md) for React development
- Check example scripts in `src/scripts/` for implementation details
- Customize styling in `frontend/src/styles/`
- Add new examples in `src/scripts/mesh/` or `src/scripts/point_cloud/`

## Getting Help

- Check existing examples in `src/scripts/`
- Review the API endpoints in `app.py`
- Check browser console for JavaScript errors (F12)
- Check terminal output for Python errors
- Read the inline comments in source files
