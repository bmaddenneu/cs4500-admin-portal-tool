"""
@author Blakely Madden
@date 2014-03-19
@group 16
@purpose Contains the web server and related services
"""

import BaseHTTPServer
import api

class HTTPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
    @author Blakely Madden
    @date 2014-03-19
    @purpose special handler for get requests to the BaseHTTPServer
    @params api_info [APIInfo] (static member)
    @notes this is not thread safe code. shouldn't matter unless
           some... interesting changes are made to this program
    """
    api_info = None
    def do_GET(s):
        """
        @author Blakely Madden
        @date 2014-03-19
        @purpose calback function upon receipt of a GET request
        @args s [HTTPHandler]
        @return None
        @exceptions None
        @can_block False
        """
        print "Requesting content..."
        response = api.api_handler_json(s.path, HTTPHandler.api_info)
        s.send_response(200)
        s.send_header('Content-type', 'text/json')
        s.end_headers()
        s.wfile.write(response)

# Starts the server
def run(port, api_info):
    """
    @author Blakely Madden
    @date 2014-03-19
    @purpose starts the server and tells it to receive requests forever
    @args port [int], api_info [APIInfo]
    @return None
    @exceptions None
    @can_block True
    """
    HTTPHandler.api_info = api_info
    httpd = BaseHTTPServer.HTTPServer(('', port), HTTPHandler)
    print "Server running..."
    httpd.serve_forever()
