#!/usr/bin/env python3
"""
Minimal WebKitGTK test - loads Mainsail directly
If this crashes, it's a WebKitGTK bug
If this works, it's something OrcaSlicer-specific
"""
import os
os.environ['G_MESSAGES_DEBUG'] = 'all'
os.environ['WEBKIT_DEBUG'] = 'all'

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.1')
from gi.repository import Gtk, WebKit2

class WebKitTest(Gtk.Window):
    def __init__(self):
        super().__init__(title="WebKitGTK Test - Mainsail")
        self.set_default_size(1200, 800)

        # Create WebView with developer mode enabled
        self.webview = WebKit2.WebView()
        settings = self.webview.get_settings()
        settings.set_enable_developer_extras(True)
        settings.set_enable_write_console_messages_to_stdout(True)

        # Create scrolled window
        scrolled = Gtk.ScrolledWindow()
        scrolled.add(self.webview)

        # Layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # URL bar
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.url_entry = Gtk.Entry()
        self.url_entry.set_text("http://localhost/")
        self.url_entry.connect("activate", self.on_navigate)
        go_button = Gtk.Button(label="Go")
        go_button.connect("clicked", self.on_navigate)
        hbox.pack_start(self.url_entry, True, True, 0)
        hbox.pack_start(go_button, False, False, 0)

        vbox.pack_start(hbox, False, False, 5)
        vbox.pack_start(scrolled, True, True, 0)

        self.add(vbox)

        # Load test file - change this to test different files
        # Options:
        #   27_mainsail_exact.html - SVG ECharts + Vue reactivity
        #   28_websocket_vue_flow.html - WebSocket + JSON + Vue flow
        #   29_simultaneous_init.html - Exact Mainsail init pattern
        #   http://192.168.1.96 - Actual Mainsail (should crash)
        test_url = "http://localhost:8765/"  # Test vue-resize technique
        print(f"Loading test: {test_url}")
        self.webview.load_uri(test_url)

    def on_navigate(self, widget):
        url = self.url_entry.get_text()
        if not url.startswith("http"):
            url = "http://" + url
        print(f"Navigating to: {url}")
        self.webview.load_uri(url)

if __name__ == "__main__":
    print("Starting minimal WebKitGTK test...")
    print("If this crashes loading Mainsail, it's a WebKitGTK bug")
    print("If this works, the issue is OrcaSlicer-specific")
    print("-" * 50)

    win = WebKitTest()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
