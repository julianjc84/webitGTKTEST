#!/bin/bash
# Simple HTTP server to test WebKit pages in OrcaSlicer
cd "$(dirname "$0")"
echo "=========================================="
echo "WebKit Test Server"
echo "=========================================="
echo "Test pages available at: http://localhost:8765"
echo ""
echo "Test files:"
ls -1 *.html
echo ""
echo "To test in OrcaSlicer:"
echo "1. Set print_host to: localhost:8765/01_basic.html"
echo "2. Click Devices tab"
echo "3. If it works, try the next test file"
echo ""
echo "Press Ctrl+C to stop server"
echo "=========================================="
python3 -m http.server 8765
