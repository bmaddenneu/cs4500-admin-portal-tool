#!/usr/bin/env python

"""
@author Blakely Madden
@date 2014-02-24
@updated 2014-03-19
@group 16
@purpose This is the entry point for the server application
"""

import http_server
import api
import sys # argv

def parse_args():
    """
    @author Blakely Madden
    @date 2014-02-24
    @updated 2014-03-19
    @purpose parse_args parses the command line arguments to the program and
    determines if they are satisfactory inputs
    @args None
    @return (int, string, int, string, string, string)
    @exceptions TypeError
    @can_block false
    """
    if len(sys.argv) != 7: # if there aren't exactly 6 arguments passed in
        # print a usage message
        sys.stderr.write("usage: %s [port] [host] [db_port] [user] [pw] [db]"
                         % sys.argv[0])
        sys.exit(0)
    # return a tuple containing the command line argument formatted for use
    return (int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), sys.argv[4],
            sys.argv[5], sys.argv[6])

def start_server(args):
    """
    @author Blakely Madden
    @date 2014-02-24
    @updated 2014-03-19
    @purpose starts the server and delegates any received call to the api
     handler
    @args args [tuple]
    @return None
    @exceptions Exception
    @can_block True
    """
    port, host, api_port, user, pw, db = args # unwrap the tuple
    api_info = api.APIInfo(host, api_port, user, pw, db)
    http_server.run(port, api_info)

# main guard 
if __name__ == "__main__":
    args = parse_args() # get the formatted args from the command line
    start_server(args)
