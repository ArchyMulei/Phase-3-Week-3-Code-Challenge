import sqlite3

CONN = sqlite3.connect('kula.db')
CURSOR = CONN.cursor()