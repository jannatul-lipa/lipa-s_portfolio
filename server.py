"""
Python Local Server for Previewing Jannatul Ferdousi Lipa's Portfolio Website
Run this script using: python server.py
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def run_server():
    # Make sure index.html is built
    print("🔨 Checking website build...")
    os.system("python build.py")

    Handler = http.server.SimpleHTTPRequestHandler
    
    print(f"\n=======================================================")
    print(f"🚀 Portfolio Local Server Running At:")
    print(f"👉 http://localhost:{PORT}")
    print(f"=======================================================\n")
    
    # Open browser automatically
    webbrowser.open(f"http://localhost:{PORT}")

    with ReusableTCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Local server stopped.")

if __name__ == "__main__":
    run_server()
