#!/bin/sh

# @author Blakely Madden
# @date 2014-04-15
# @group 16
# @purpose wrapper for the main.py script. basically a config file for the arguments
#  that are passed to the main program

PROG_PATH="./main.py" # full program path, relative or absolute
CLIENT_PORT="10009"
DB_HOST="129.10.76.16"
DB_HOST_PORT="3306"
DB_USER="Gamers"
DB_PASSWORD="G@meDB"
DB_NAME="GameLabVPAL"

$PROG_PATH $CLIENT_PORT $DB_HOST $DB_HOST_PORT $DB_USER $DB_PASSWORD $DB_NAME
