"""Local dev server — serves extensionless URLs by mapping /about -> about.html"""
import http.server
import os
import sys

PORT = 8080
ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?")[0].split("#")[0]

        # Try the path as-is first (handles /styles.css, /images/logo.png, etc.)
        fs_path = os.path.join(ROOT, path.lstrip("/"))

        if os.path.isfile(fs_path):
            return super().do_GET()

        # Directory -> serve index.html inside it
        if os.path.isdir(fs_path):
            index = os.path.join(fs_path, "index.html")
            if os.path.isfile(index):
                self.path = path.rstrip("/") + "/index.html"
                return super().do_GET()

        # Extensionless URL -> try appending .html
        html_path = fs_path + ".html"
        if os.path.isfile(html_path):
            self.path = path + ".html"
            return super().do_GET()

        # Fall through to default (will 404)
        return super().do_GET()

    def log_message(self, fmt, *args):
        print(fmt % args)


if __name__ == "__main__":
    os.chdir(ROOT)
    with http.server.HTTPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
