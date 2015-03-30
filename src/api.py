"""
@author Blakely Madden
@date 2014-02-24
@group 16
@purpose The functions here represent the API as presented to users. Utility
 functions and classes to support these API calls are also present
"""

import db_hooks
import sys
import json
import datetime
import calendar

def default_json_serializer(item):
    """
    @author Blakely Madden
    @date 2014-03-19
    @purpose lets us serialize datetime.datetime objects from the DB
    @args item [anything]
    @return number (type decided by python)
    @exceptions None
    @can_block False
    """
    if isinstance(item, datetime.datetime):
        if item.utcoffset() is not None:
            item = item - item.utcoffset()
    millisecs = int(
        calendar.timegm(item.timetuple()) * 1000 +
        item.microsecond / 1000
    )
    return millisecs

class APIInfo(object):
    """
    @author Blakely Madden
    @date 2014-02-24
    @updated 2014-03-19
    @purpose object to hold data essential for database interactions through
     the API
    @params host [string], port [int or string], user [string], pw [string],
            db [string]
    """
    def __init__ (self, host, port, user, pw, db):
        self.host = host
        self.port = port
        self.user = user
        self.pw = pw
        self.db = db

def api_handler_json(data, api_info):
    """
    @author Blakely Madden
    @date 2014-03-19
    @purpose output json instead of list format
    @args data [string], api_info [APIInfo]
    @return json serialized data
    @exceptions None
    @can_block False
    """
    response = api_handler(data, api_info)
    return json.dumps(response, default=default_json_serializer)

def api_handler(data, api_info):
    """
    @author Blakely Madden
    @date 2014-02-24
    @updated 2014-03-19
    @purpose take the raw request and sanitize it for use with the DB
    @args data [string], api_info [APIInfo]
    @return dictionary
    @exceptions None
    @can_block False
    """
    table = data.strip()
    table = data.strip('/')
    return grab_column_data_from_table(table, api_info)

def grab_column_data_from_table(table, api_info):
    """
    @author Blakely Madden
    @date 2014-02-24
    @updated 2014-03-19
    @purpose corresponds to the API call for a column of data from a table
    @args table [string], api_info [APIInfo]
    @return list [string]
    @exceptions None
    @can_block False
    """
    db = db_hooks.DBHook(api_info.host, api_info.port, api_info.user,
                         api_info.pw, api_info.db) # set up the DB connection
    # get the data for the given table
    try:
        cols = db.execute_db_command("SHOW COLUMNS FROM %s" % table)
        all_data = db.execute_db_command("SELECT * FROM %s" % table)
    except Exception as e: # we received an invalid table request
        print "Invalid table request: \"%s\" Ignoring... \nError: "\
            % table + e.message
        return ""

    col_names = []
    for item in cols:
        col_names.append(item[0])

    data = []
    temp_dict = {}
    for row in all_data:
        for col,item in zip(col_names,row):
            temp_dict[col] = item
        data.append(temp_dict)
        temp_dict = {}
    return data
