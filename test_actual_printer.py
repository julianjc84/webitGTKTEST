#!/usr/bin/env python3
"""
Test actual printer's web UI (Mainsail/Fluidd) in WebKitGTK.
Enter your printer's IP address in the URL bar and click Go.
"""
import sys
import os
os.environ['G_MESSAGES_DEBUG'] = 'all'
os.environ['WEBKIT_DEBUG'] = 'all'

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.1')
from gi.repository import Gtk, WebKit2

class PrinterTest(Gtk.Window):
    def __init__(self):
        super().__init__(title="WebKitGTK Test - Actual Printer")
        self.set_default_size(1200, 800)

        self.webview = WebKit2.WebView()
        settings = self.webview.get_settings()
        settings.set_enable_developer_extras(True)
        settings.set_enable_write_console_messages_to_stdout(True)

        scrolled = Gtk.ScrolledWindow()
        scrolled.add(self.webview)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Info label
        info = Gtk.Label()
        info.set_markup("<b>Test your printer's web UI in WebKitGTK</b>\nEnter your printer's IP address below and press Go (or Enter)")
        info.set_margin_top(10)
        info.set_margin_bottom(10)

        # URL bar
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.url_entry = Gtk.Entry()
        self.url_entry.set_text("http://")
        self.url_entry.set_placeholder_text("http://your-printer-ip")
        self.url_entry.connect("activate", self.on_navigate)
        go_button = Gtk.Button(label="Go")
        go_button.connect("clicked", self.on_navigate)
        hbox.pack_start(self.url_entry, True, True, 0)
        hbox.pack_start(go_button, False, False, 0)

        vbox.pack_start(info, False, False, 5)
        vbox.pack_start(hbox, False, False, 5)
        vbox.pack_start(scrolled, True, True, 0)

        self.add(vbox)

        # Accept URL from command line argument
        if len(sys.argv) > 1:
            url = sys.argv[1]
            if not url.startswith("http"):
                url = "http://" + url
            self.url_entry.set_text(url)
            print(f"Loading: {url}")
            self.webview.load_uri(url)

    def on_navigate(self, widget):
        url = self.url_entry.get_text()
        if not url.startswith("http"):
            url = "http://" + url
        print(f"Navigating to: {url}")
        self.webview.load_uri(url)

if __name__ == "__main__":
    print("=" * 50)
    print("Printer Web UI Test")
    print("=" * 50)
    print("Enter your printer's IP in the URL bar and click Go.")
    print("Optionally pass URL as argument: python3 test_actual_printer.py 192.168.1.96")
    print("-" * 50)

    win = PrinterTest()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
