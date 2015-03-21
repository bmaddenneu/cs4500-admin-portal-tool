###### DEPRECATED 2014-03-19
# this file is deprecated and should not be used. it is kept in the current
# version in case it is needed again
"""
@author Blakely Madden
@date 2014-02-24
@group 16
@purpose Server implementation for interacting with the DB API
"""
import socket
import sys

class Server(object):
    """
    @author Blakely Madden
    @date 2014-02-24
    @purpose this is the Server object that accepts incoming connections
    @params port [int]
    """
    def __init__(self, port):
        """
        @author Blakely Madden
        @date 2014-02-24
        @purpose initialize the Server object
        @args port [int]
        @return string
        @exceptions None
        @can_block False
        """
        self.port = port

    def accept_message(self):
        """
        @author Blakely Madden
        @date 2014-02-24
        @purpose accept_message starts a socket listening on the port passed in
        on the command line and accepts the first message it receives
        @args None
        @return string
        @exceptions None
        @can_block True
        """
        MAX_PACKET_SIZE = 8096 # really safe number for our max packet size
        received = "Did not receive packet"
        try: # catching errors from system calls
            # make a new IP/TCP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("127.0.0.1", self.port)) # bind it to localhost
            sock.listen(5) # start the socket listening with 5 failure tolerance
            recv_sock, _  = sock.accept() # blocks until a connection is made
                                          # to the given port
            received = recv_sock.recv(MAX_PACKET_SIZE) # return the message
        except Exception as e:
            sys.stderr.write(e.message)
        return received
