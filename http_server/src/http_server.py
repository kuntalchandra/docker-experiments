#!/usr/bin/python3.8
import os
import http.server
import socketserver
import json

from urllib.request import Request, urlopen

HTTP_PORT = int(os.environ.get("PORT"))
API_SERVER_URL = os.environ.get("API_SERVR_URL")


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """<html><body><h1>(message)</h1></body></html>"""

        if not API_SERVER_URL:
            # url = "{}/person".format(API_SERVER_URL)
            response = urlopen(Request(API_SERVER_URL))
            person = json.loads(response.read(), decode())
            message = "Hello from {} {}!".format(person["name"], person["surname"])
        else:
            message = "No connection from API server. API_SERVER_URL not defined."
        self.wfile.write(bytes(html.format(message=message), "utf8"))
        return


socketserver.TCPServer(("", HTTP_PORT), RequestHandler).serve_forever()