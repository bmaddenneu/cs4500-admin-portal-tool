import MySQLdb
import MySQLdb.converters

"""
@author Blakely Madden
@date 2014-02-24
@updated 2014-03-19
@group 16
@purpose Handles hooking the database via calls to the public API
"""

class DBHook(object):
    """
    @author Blakely Madden
    @date 2014-02-24
    @purpose this is the database management object
    @params None
    """
    def __init__(self, host, port, user, passwd, db):
        """
        @author Blakely Madden
        @date 2014-02-24
        @purpose Initialize a DBHook object
        @args host [string], user [string], passwd [string], db [string]
        @return None
        @exceptions None
        @can_block False
        """
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.cursor = None
        self.database = None

    def hook_db(self):
        """
        @author Blakely Madden
        @date 2014-02-24
        @updated 2014-03-19
        @purpose hook up to the db
        @args None
        @return None
        @exceptions Exception
        @can_block False
        """
        # get dates as strings from the database so that we can serialize to
        # json this is not working for some reason. another solution has been
        # reached, but this would be a better one, so I'm leaving it here.
        #conv = MySQLdb.converters.conversions.copy()
        #conv[10] = str
        self.database = MySQLdb.connect(host=self.host,
                                        port=self.port,
                                        user=self.user,
                                        passwd=self.passwd,
                                        db=self.db)
                                        #conv=conv)
        self.cursor = self.database.cursor()

    def close_connection(self):
        """
        @author Blakely Madden
        @date 2014-02-24
        @purpose close any open DB connections
        @args None
        @return None
        @exceptions None
        @can_block False
        """
        if self.cursor is None and self.database is None:
            # if we don't have an open connection, do nothing
            return
        self.cursor.close()
        self.database.close()

    def execute_db_command(self, command):
        """
        @author Blakely Madden
        @date 2014-02-24
        @purpose execute a command to the hooked DB
        @args None
        @return None
        @exceptions Exception
        @can_block False
        """
        self.hook_db()
        self.cursor.execute(command)
        return self.cursor.fetchall()
