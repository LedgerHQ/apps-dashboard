#!/usr/bin/env python3

"""
https://127.0.0.1:4433/docs/index.html
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import ssl

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    certfile = os.path.join(script_dir, "cert.pem")

    # Run the web server from the root directory of the project
    os.chdir(os.path.join(script_dir, ".."))

    httpd = HTTPServer(("localhost", 4433), SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile=certfile)
    print("Serving apps dashboard on https://127.0.0.1:4433/docs/index.html")
    httpd.serve_forever()
