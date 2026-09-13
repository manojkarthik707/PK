import http.server
import socketserver
import os
import json

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class WeddingRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == '/api/save':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body.decode('utf-8'))
                html_content = data.get('html')
                if html_content:
                    index_path = os.path.join(DIRECTORY, 'index.html')
                    with open(index_path, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    
                    # Also save JSON data for easy backup
                    if 'formData' in data:
                        with open(os.path.join(DIRECTORY, 'invitation-data.json'), 'w', encoding='utf-8') as f:
                            json.dump(data['formData'], f, indent=2)
                    
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"status": "success", "message": "Saved directly to index.html"}).encode('utf-8'))
                    return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
                return

        self.send_response(404)
        self.end_headers()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), WeddingRequestHandler) as httpd:
        print(f"Serving wedding invitation studio at http://localhost:{PORT}")
        httpd.serve_forever()
