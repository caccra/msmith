#!/usr/bin/env python3
import http.server, os, json

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Mock contact.php for local dev — always returns success
        if self.path in ('/contact.php', '/contact.php/'):
            length = int(self.headers.get('Content-Length', 0))
            self.rfile.read(length)  # consume body
            body = json.dumps({'success': True}).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            print('  POST /contact.php -> mock 200 OK')
        else:
            self.send_error(405)

    def do_GET(self):
        p = self.path.split("?")[0]
        if p != "/" and p.endswith("/"):
            candidate = p.rstrip("/").lstrip("/") + ".html"
            if os.path.isfile(candidate):
                self.send_response(301)
                self.send_header("Location", p.rstrip("/"))
                self.end_headers()
                return
        super().do_GET()

    def translate_path(self, path):
        result = super().translate_path(path)
        if not os.path.splitext(result)[1]:
            candidate = result + ".html"
            if os.path.isfile(candidate):
                return candidate
        return result

    def log_message(self, fmt, *args):
        print(f"  {args[0]} {args[1]}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with http.server.HTTPServer(("", 3000), CleanURLHandler) as httpd:
        print("Serving at http://localhost:3000")
        httpd.serve_forever()
