import hashlib
import json
import pickle
import sqlite3
import subprocess

from tinydb import TinyDB, Query

class Problem:
    def __init__(self):
        self.pindex = ''
        self.title = ''
        self.desc = ''
        self.difficulty = 0
        self.comments = []
        self.tags = []
        self.author = ''
        self.source_path = ''
        self.file_hash = ''
        self.test_path = ''

'''
Manages on-disk databases interactions.
Implements Toxi solution to add database tagging.
'''
class LocalDB:
    def __init__(self):
      self.problem_db = TinyDB('problems.json')
      self.conn = sqlite3.connect('swiss.db')
      self.c = self.conn.cursor()
      self.c.execute('CREATE TABLE IF NOT EXISTS tags(tag_name STRING PRIMARY KEY)')
      self.c.execute('CREATE TABLE IF NOT EXISTS problems(pindex STRING PRIMARY KEY)')
      self.c.execute('CREATE TABLE IF NOT EXISTS tagmap(tmid INTEGER PRIMARY KEY AUTOINCREMENT, tag_name INTEGER, pindex STRING)')

    def add(self, p):
        doc_id = self.problem_db.insert(p.__dict__)
        self.c.execute("INSERT OR IGNORE INTO problems(pindex) VALUES(?)", (p.pindex, ))
        self.tag(p.pindex, p.tags)

    def remove(self, pindex):
        q = Query()
        self.problem_db.remove(q.pindex == pindex)
        self.c.execute("DELETE FROM problems WHERE pindex = ?", (pindex,))
        self.c.execute("DELETE FROM tagmap WHERE pindex = ? ", (pindex,))

    def tag(self, pindex, tags):
        for tag in tags:
            c.execute("INSERT OR IGNORE INTO tags(tag_name) VALUES(?)", (tag.lower(),))
            c.execute("INSERT INTO tagmap(tag_name , pindex) VALUES (?,?)", (tag.lower(), pindex))

    '''
    Returns list of problems
    '''
    def query(self, text):
        words = text.split()
        q = '''SELECT problems.pindex
                    FROM tagmap, problems, tags
                    WHERE tags.tag_name = tagmap.tag_name
                    AND tagmap.pindex = problems.pindex '''
        attrs = ""
        for i, word in enumerate(words):
            if i == len(words) - 1:
                attrs += "'" + word + "'"
            else:
                attrs += "'" + word + "',"
        q2 = '''AND (tags.tag_name IN ({}))
                    GROUP BY tags.tag_name
                    HAVING COUNT( b.id ) = {}'''.format(attrs, str(len(words)) )
        q += q2
        self.c.execute(q)
        data = self.c.fetchall()
        print(data)
        return data

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

def load_from_source(self, filename):
    with open(filename, 'r') as file:
        data = file.read()
        return data
