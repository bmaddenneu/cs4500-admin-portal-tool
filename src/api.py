"""
@author Blakely Madden
@date 2014-02-24
@group 16
@purpose The functions here represent the API as presented to users. Utility
 functions and classes to support these API calls are also present
"""

import db_hooks

import calendar
import datetime
import json
import MySQLdb

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
    # remove whitespace and trailing '/'
    # split fields separated by '/' and make a list of them
    info = data.strip()
    info = info.strip('/')
    info = info.split('/')

    for i in info: # escape all the strings for use with SQL statements
        i = MySQLdb.escape_string(i)

    db = db_hooks.DBHook(api_info.host, api_info.port, api_info.user,
                         api_info.pw, api_info.db) # set up the DB connection
    table = info[0]
    try: # get the column data that we need to make JSON objects
        cols = db.execute_db_command("SHOW COLUMNS FROM %s" % table)
    except Exception as e:
        return invalid_request(table, e)

    col_names = [] # pull out the actual column names
    for item in cols:
        col_names.append(item[0])

    if len(info) == 1:
        return safe_db_query_to_json (table_rows (table), col_names, db)
    if len(info) == 2:
        return safe_db_query_to_json (all_values_in_column (table, info[1]),
                                      [info[1]], db)
    if len(info) == 3:
        return safe_db_query_to_json (rows_matching_table_field_val (table,
                                                                     info[1],
                                                                     info[2]),
                                      col_names, db)

def safe_db_query_to_json (escaped_query, cols, db):
    """
    @author Blakely Madden
    @date 2014-04-08
    @purpose expects an escaped string that is executed as a query to the DB.
     Makes JSON serialized data from the response
    @args escaped_query [string], cols [list], db [MySQLdb.connection]
    @return list of dictionaries
    @exceptions Exception
    @can_block False
    """
    try:
        data = db.execute_db_command(escaped_query)
    except Exception as e:
        return invalid_request (escaped_query, e)

    return make_json_objs (data, cols)

def invalid_request(query, exception):
    """
    @author Blakely Madden
    @date 2014-04-08
    @purpose print an error message based on the exception
    @args query [string], exception [Exception]
    @return empty string
    @exceptions None
    @can_block False
    """
    print "Invalid SQL query request: \"%s\" Ignoring... \nError: "\
        % query + exception.message
    return ""

def make_json_objs (all_data, cols):
    """
    @author Blakely Madden
    @date 2014-04-08
    @purpose make JSON objects and return them in a list
    @args all_data [list], cols [list]
    @return list of dictionaries
    @exceptions Exception
    @can_block False
    """
    data = []
    temp_dict = {}
    for row in all_data:
        for col,item in zip(cols, row):
            temp_dict[col] = item
        data.append(temp_dict)
        temp_dict = {}
    return data

def all_values_in_column (table, field):
    """
    @author Blakely Madden
    @date 2014-04-08
    @purpose get a query string for the values in a specific column
    @args table [string], field [string]
    @return string
    @exceptions None
    @can_block False
    """
    return "SELECT %s from %s" % (field, table)
p
def rows_matching_table_field_val(table, field, val):
    """
    @author Blakely Madden
    @date 2014-04-08
    @purpose get a query string for the rows in a table with the column,
     "field", and the value, "val"
    @args table [string], field [string], val [string]
    @return string
    @exceptions None
    @can_block False
    """
    return "SELECT * FROM %s WHERE %s = %s" % (table, field, val)

def table_rows(table):
    """
    @author Blakely Madden
    @date 2014-02-24
    @updated 2014-03-19
     2014-04-08
    @purpose corresponds to the API call for a column of data from a table
    @args table [string], field [string], val [string]
    @return string
    @exceptions None
    @can_block False
    """
    return "SELECT * FROM %s" % table
