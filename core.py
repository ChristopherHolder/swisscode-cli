import hashlib
import json
import pickle
import sqlite3

from tinydb import TinyDB, Query

class Problem:
    def __init__(self):
        self.index = ''
        self.title = ''
        self.desc = ''
        self.solution = ''
        self.difficulty = 0
        self.comments = []
        self.tags = []
        self.author = ''
        self.source = ''
        self.test_id = ''
    def load_from_source(self, filename):
        with open(filename, 'r') as file:
            data = file.read()
'''
Manages on-disk databases interactions.
Implements Toxi solution to add database tagging.
'''
class LocalDB:
    def __init__(self):
      self.problem_db = TinyDB('problems.json')
      self.conn = sqlite3.connect('swiss.db')
      self.c = self.conn.cursor()
      self.c.execute('CREATE TABLE IF NOT EXISTS tags(tid INTEGER PRIMARY KEY, tag STRING)')
      self.c.execute('CREATE TABLE IF NOT EXISTS problems(pid STRING PRIMARY KEY, pindex STRING UNIQUE)')
      self.c.execute('CREATE TABLE IF NOT EXISTS tagmap(tmid INTEGER PRIMARY KEY, tid INTEGER, pid INTEGER, FOREIGN KEY (tid) REFERENCES tags(tid) FOREIGN KEY (pid) REFERENCES problems(pid))')
    def add(self, p):
        pass
    

# Helper methods
##################################################
'''
Input: filename
Output: sha251 hash of file
'''
def file_signature(filename):
    size = 65536
    hasher = hashlib.sha1()
    with open(filename, 'rb') as f:
        buf = f.read(size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(size)
    return hasher.hexdigest()
