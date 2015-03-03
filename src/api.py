"""
@author Blakely Madden
@date 2014-02-24
@group 16
@purpose The functions here represent the API as presented to users. Utility
 functions and classes to support these API calls are also present
"""

import db_hooks
import sys

class APIInfo(object):
    """
    @author Blakely Madden
    @date 2014-02-24
    @purpose object to hold data essential for database interactions through
     the API
    @params host [string], user [string], pw [string], db [string]
    """
    def __init__ (self, host, user, pw, db):
        self.host = host
        self.user = user
        self.pw = pw
        self.db = db

def api_handler(data, api_info):
    """
    @author Blakely Madden
    @date 2014-02-24
    @purpose take the raw request and sanitize it for use with the DB
    @args data [string]
    @return string
    @exceptions None
    @can_block False
    """
    table = data.strip()
    return grab_column_data_from_table(table, api_info)

def grab_column_data_from_table(table, api_info):
    """
    @author Blakely Madden
    @date 2014-02-24
    @purpose corresponds to the API call for a column of data from a table
    @args None
    @return list [string]
    @exceptions None
    @can_block False
    """
    db = db_hooks.DBHook(api_info.host, api_info.user,
                         api_info.pw, api_info.db) # set up the DB connection
    # get the data for the given table
    try:
        all_data = db.execute_db_command("SELECT * FROM %s" % table)
    except Exception as e: # we received an invalid table request
        print "Invalid table request. Exiting... \nError: " + e.message
        sys.exit(1) # exit with an error 
    data = []
    for row in all_data: # pull out all the rows from this column
        data.append(row)
    print data # prints the data for now
    return data
