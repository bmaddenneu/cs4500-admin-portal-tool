#!/usr/bin/env python

"""
@author Blakely Madden
@date 2014-02-24
@group 16
@purpose This is the entry point for the server application
"""

import server
import api
import sys # argv

def parse_args():
    """
    @author Blakely Madden
    @date 2014-02-24
    @purpose parse_args parses the command line arguments to the program and
    determines if they are satisfactory inputs
    @args None
    @return (int, string, string, string, string)
    @exceptions TypeError
    @implemented True
    """
    if len(sys.argv) != 6: # if there isn't exactly one argument passed in
        # print a usage message
        sys.stderr.write("usage: %s [port] [host] [user] [pw] [db]"
                         % sys.argv[0])
        sys.exit(0)
    # return a tuple containing the command line argument formatted for use
    return (int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4],
            sys.argv[5])

def start_server(args):
    """
    @author Blakely Madden
    @date 2014-02-24
    @purpose starts the server and delegates any received call to the api
     handler
    @args port [int]
    @return None
    @exceptions Exception
    @can_block False
    """
    port, host, user, pw, db = args # unwrap the tuple
    serv = server.Server(port) # server object
    api_info = api.APIInfo(host, user, pw, db) # APIInfo data object
    call = serv.accept_message() # get a message from our server
    api.api_handler(call, api_info) # reform the API call and execute

# main guard 
if __name__ == "__main__":
    args = parse_args() # get the formatted args from the command line
    start_server(args)
