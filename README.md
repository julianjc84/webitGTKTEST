# WebKitGTK Crash Test Suite

Test pages for investigating Mainsail/Klipper web UI crashes in WebKitGTK (used by OrcaSlicer's built-in browser) on NVIDIA GPUs.

**Root cause:** The `vue-resize` library uses an `<object data="about:blank">` hack that crashes WebKitGTK on NVIDIA GPUs.
**Fix:** Replace `vue-resize` with the native `ResizeObserver` API.

## Quick Start

### 1. Install dependencies

```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

Or install manually (Debian/Ubuntu):

```bash
sudo apt install python3 python3-gi gir1.2-gtk-3.0 gir1.2-webkit2-4.1
```

### 2. Start the local test server

```bash
./start_test_server.sh
```

This serves the test HTML files at `http://localhost:8765`. Open `http://localhost:8765` in a browser to see the test index page.

### 3. Run tests

**Browse local test pages in a WebKitGTK window:**

```bash
python3 test_webkitGTK_standalone.py
```

Loads `http://localhost:8765/` (the index page). Use the URL bar to navigate between tests.

**Test against your actual printer:**

```bash
python3 test_actual_printer.py
# or pass the URL directly:
python3 test_actual_printer.py 192.168.1.96
```

Enter your printer's IP in the URL bar and click Go. This loads Mainsail/Fluidd in a standalone WebKitGTK window to reproduce crashes outside of OrcaSlicer.

## Test Files

Open `index.html` for the full list with descriptions. Tests are numbered 00-30:

| Range | Category |
|-------|----------|
| 00 | System info / diagnostics |
| 01-23 | Individual feature tests (HTML, WebSocket, Canvas, WebGL, Vue.js, etc.) |
| 24-29 | Mainsail-specific pattern tests (ECharts, ResizeObserver, Vue flow, etc.) |
| 30 | **Crash test** - the `vue-resize` `<object>` technique that triggers the bug |

## Scripts

| File | Purpose |
|------|---------|
| `install_dependencies.sh` | Install required system packages |
| `start_test_server.sh` | Start HTTP server on port 8765 |
| `test_webkitGTK_standalone.py` | WebKitGTK browser for local test pages |
| `test_actual_printer.py` | WebKitGTK browser for testing against a real printer |
