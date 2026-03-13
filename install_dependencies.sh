#!/bin/bash
# Install dependencies for WebKitGTK crash test suite
set -e

echo "Installing WebKitGTK test dependencies..."

if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y \
        python3 \
        python3-gi \
        gir1.2-gtk-3.0 \
        gir1.2-webkit2-4.1
elif command -v dnf &> /dev/null; then
    sudo dnf install -y \
        python3 \
        python3-gobject \
        gtk3 \
        webkit2gtk4.1
elif command -v pacman &> /dev/null; then
    sudo pacman -S --needed \
        python \
        python-gobject \
        gtk3 \
        webkit2gtk-4.1
else
    echo "Unsupported package manager. Install these packages manually:"
    echo "  - python3"
    echo "  - python3-gi (PyGObject)"
    echo "  - GTK 3"
    echo "  - WebKit2GTK 4.1"
    exit 1
fi

echo ""
echo "Done! Verify with:"
echo "  python3 -c \"import gi; gi.require_version('WebKit2', '4.1'); print('WebKit2GTK 4.1 OK')\""
