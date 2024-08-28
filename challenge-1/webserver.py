import http.server
import socketserver
import argparse
import logging

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, Intelygenz!")
        logging.info(f"GET request handled: {self.client_address}")

def run_server(host, port):
    with socketserver.TCPServer((host, port), CustomHandler) as httpd:
        logging.info(f"Server running on http://{host}:{port}")
        httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    run_server(args.host, args.port)