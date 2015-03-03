import server
import MySQLdb

"""
@author Blakely Madden
@date 2014-02-24
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
    def __init__(self, host, user, passwd, db):
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
        self.user = user
        self.passwd = passwd
        self.db = db
        self.cursor = None
        self.database = None

    def hook_db(self):
        """
        @author Blakely Madden
        @date 2014-02-24
        @purpose hook up to the db
        @args None
        @return None
        @exceptions Exception
        @can_block False
        """
        self.database = MySQLdb.connect(host=self.host,
                                        user=self.user,
                                        passwd=self.passwd,
                                        db=self.db)
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
