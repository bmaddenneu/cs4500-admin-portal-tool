#!/usr/bin/python
from socket import *

"""
@author Blakely Madden
@date 2014-02-24
@group 16
@purpose This is a test which produces invalid output when used on the
 "performance_schema game database
"""

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("127.0.0.1", 10003))
sock.sendall("garbage")
sock.close()
