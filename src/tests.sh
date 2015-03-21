#!/bin/sh

#@author Blakely Madden
#@date 2014-03-19
#@group 16
#@purpose The functions here represent the API as presented to users. Utility
# functions and classes to support these API calls are also present

rm *.pyc

#strings for reuse
START_SERV="./main.py 10009 129.10.76.16 3306 Gamers G@meDB GameLabVPAL"
GET="wget -t 1 localhost:10009/GL_VPAL_"
STAT="stat GL_VPAL_"

$START_SERV &

sleep 5 # make sure we give enough time to the server, since it is
        # running in the background

# these are known existing tables. Currently Attacks and Player_Actions are
# empty, but this is subject to change. The result is that the "stat" tests
# will indicate that these files are very small (two bytes for the "[]"
# default that is the response of an empty DB lookup), and this is expected.
$GET"Attacks" && $GET"Interactions" && $GET"Player_Actions" && \
    $GET"Player_Position" && $GET"User_Details" && \
    echo Requests Succeeded || echo Requests Failed

echo

# grepping for "regular file" verifies that these files contain something.
# if they didn't, that would indicate an error
$STAT"Attacks" | grep "regular file" && $STAT"Interactions" | \
    grep "regular file" && $STAT"Player_Actions" | grep "regular file" \
    && $STAT"Player_Position" | grep "regular file" && $STAT"User_Details" | \
    grep "regular file" && echo Responses Succeeded || echo Responses Failed

echo

# In order to verify the contents of the response files, you can just open the
# files normally. They are located in the directory you ran this test script
# from.

echo Tests Complete

killall python # kill the background process. careful of collateral damage
