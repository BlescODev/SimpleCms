import sqlite3

class SqliteSettingsRepository(object):
	_table = "settings"
	_key = "key"
	_value = "value"

	_create = "CREATE TABLE IF NOT EXISTS " + _table + "(" + _key + " TEXT PRIMARY KEY NOT NULL UNIQUE, " + _value + " TEXT NOT NULL) WITHOUT ROWID;"
	_set = "INSERT OR REPLACE INTO " + _table + "(" + _key + ", " + _value + ") VALUES(?, ?);"
	_get = "SELECT " + _value + " FROM " + _table + " WHERE " + _key + " = ?;"

	def __init__(self, dbPath):
		self.dbPath = dbPath
		con = self.__getConnection()
		with con:
			cursor = con.cursor()
			cursor.execute(self._create)

	def getSetting(self, key):
		con = self.__getConnection()
		with con:
			cursor = con.cursor()
			cursor.execute(self._get,(key,))
			return cursor.fetchone()

	def setSetting(self, key, value):
		con = self.__getConnection()
		with con:
			cursor = con.cursor()
			cursor.execute(self._set,(key, value))
	
	def __getConnection(self):
		return sqlite3.connect(self.dbPath)