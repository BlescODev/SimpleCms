import sqlite3

class SqlitePageRepository:
    _table = "content"
    _route = "route"
    _json = "json"
    
    _create = "CREATE TABLE IF NOT EXISTS " + _table + "(" + _route + " TEXT PRIMARY KEY NOT NULL UNIQUE, " + _json + " TEXT NOT NULL) WITHOUT ROWID;"
    _addOrUpdate = "INSERT OR REPLACE INTO " + _table + "(" + _route + ", " + _json + ") VALUES(?, ?);"
    _get = "SELECT " + _json + " FROM " + _table + " WHERE " + _route + " = ?;"
    _delete = "DELETE FROM " + _table + " WHERE " + _route + " = ?;"
    
    def __init__(self, dbPath):
        self.dbPath = dbPath
        con = self.__getConnection()
        with con:
            cursor = con.cursor()
            cursor.execute(self._create)
             
    def addOrUpdate(self, route, content):        
        con = self.__getConnection()
        with con:
            cursor = con.cursor()
            cursor.execute(self._addOrUpdate,(route, content))
            
    def get(self, route):
        con = self.__getConnection()
        with con:
            cursor = con.cursor()
            cursor.execute(self._get,(route,))
            return cursor.fetchone()
        
    def delete(self, route):
        con = self.__getConnection()
        with con:
            cursor = con.cursor()
            cursor.execute(self._delete,(route,))
        
    def __getConnection(self):
        return sqlite3.connect(self.dbPath)
    
