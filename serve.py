#!/usr/bin/env python3
"""Simple HTTP file server for local TZP-client testing.

Serves the TZP-client directory so the launcher can download mods/configs.
Run: python3 serve.py
"""
import http.server
import functools
from pathlib import Path

PORT = 8580
DIRECTORY = Path(__file__).resolve().parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

    def translate_path(self, path):
        # Strip /files/ prefix if present
        if path.startswith("/files/"):
            path = "/" + path[7:]
        return super().translate_path(path)

if __name__ == "__main__":
    with http.server.HTTPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Serving TZP-client at http://127.0.0.1:{PORT}/files/")
        print(f"Directory: {DIRECTORY}")
        print("Press Ctrl+C to stop")
        httpd.serve_forever()
