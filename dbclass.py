# 9/1/2017
# dbportal class placeholder
# Immediately below is an about section that should eventually be separated into its onw document.
'''
ABOUT

TASKS

Comments should be proofread by someone other than me (Jorge) to check for correct use of terms.
Macro idea is to have error catching code outside the scope of methods; think about what you are doing in __init__.
Lacking consistency in variable names.

'''

import sqlite3
'''
The methods in class assume proper input. The error catching is to be done outside the method scopes.
'''
class dbclass(object):
    '''
    Initializes a database named by parameter input.
    Initializes a cursor.
    '''
    def __init__(self, dbase):

        dbase +=".db"
        try:
            self.db = sqlite3.connect(database=dbase)
            self.c = self.db.cursor()
            print("Connection successful.")
        except:
            print("An error has occured!")
            
    '''
    Creates a table in the database.
    '''
    def createtbl(tname, cnames):
        self.c.execute("CREATE TABLE "+tname+" (Log INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"+cnames+")")
        self.db.commit()
        
    '''
    Inserts a row of data into a given table.
    '''
    def intotbl(tbl, tcols, tdata):
        self.c.execute('INSERT INTO '+tbl+' ('+tcols+') VALUES ('+tdata+')')
        self.db.commit()

    '''
    Returns a list of the names of tables in the database.
    '''
    def tbllist():
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.c.fetchall()
        return tables
    
    '''
    Deletes a table from the database.
    '''
    def deletetbl(tbl):
        self.c.execute("DROP TABLE "+tbl)
        self.db.commit()

    '''
    Edit a cell in a table in the database.
    '''
    def editcell(tbl,col,val,idx):
        self.c.execute("UPDATE "+tbl+" SET "+col+"="+val+" WHERE Log="+idx)
        self.db.commit()

