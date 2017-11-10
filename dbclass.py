import sqlite3
# The methods in class assume proper input. The error catching is to be done outside the method scopes.
class dbclass(object):
    # Initializes a database named by parameter input.
    # Initializes a cursor.
    def __init__(self, dbase):

        dbase +=".db"
        try:
            self.db = sqlite3.connect(database=dbase)
            self.c = self.db.cursor()
            print("Connection successful.")
        except:
            print("An error has occured!")
            
    # Creates a table in the database.
    def createtbl(tname, cnames):
        self.c.execute("CREATE TABLE "+tname+" (Log INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"+cnames+")")
        self.db.commit()
        
    # Inserts a row of data into a given table.
    def intotbl(tbl, tcols, tdata):
        self.c.execute('INSERT INTO '+tbl+' ('+tcols+') VALUES ('+tdata+')')
        self.db.commit()

    # Returns a list of the names of tables in the database.
    def tbllist():
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.c.fetchall()
        return tables
    
    # Deletes a table from the database.
    def deletetbl(tbl):
        self.c.execute("DROP TABLE "+tbl)
        self.db.commit()

    # Edit a cell in a table in the database.
    def editcell(tbl,col,val,idx):
        self.c.execute("UPDATE "+tbl+" SET "+col+"="+val+" WHERE Log="+idx)
        self.db.commit()
        
    # Prints a table's header.
    def header(tbl):
        self.c.execute("PRAGMA table_info("+tbl+");")
        rawout = self.c.fetchall()
        rolen = len(rawout)
        i = 1
        refined = "\n[ "
        while(i < rolen):
            #refined += rawout[i][1]+" ("+rawout[i][2]+") "
            # Line above was used for debuging purposes, prints a schema.
            refined += " |"+rawout[i][1]+"| "
            i += 1 
        refined += "]\n"
        print(refined)

    # Prints out a table.
    def viewtbl(tbl):
        # retrieve table/column length
        self.c.execute("PRAGMA table_info("+tbl+");")
        rawout = self.c.fetchall()
        rlen = len(rawout)                  # column length number

        # string with the column names
        colnames = ""
        i = 1
        while(i < rlen):
            colnames += ","+rawout[i][1]
            i += 1 

        # initializing list of max column lengths
        sizes = []
        i = 0
        while i < rlen:
            sizes.append(len(str(rawout[i][1])))
            i += 1

        # Printing the entire table
                    
        # recording max cell space per column
        result = self.c.execute("SELECT Log"+colnames+" FROM "+tbl)
        for row in result:
            idx1 = 0
            while idx1 < rlen:
                if(len(str(row[idx1])) > sizes[idx1]):
                    sizes[idx1] = len(str(row[idx1]))
                idx1 += 1

        # printing table head
        buffer = ""
        self.c.execute("PRAGMA table_info("+tbl+");")
        i = 0
        ref = ""
        while(i < rlen):
            j = 0
            while(j < sizes[i]):
                buffer += " "
                j += 1
            ref += "|  "+rawout[i][1]+buffer[len(str(rawout[i][1])):sizes[i]]+"  "
            i += 1 
        ref += "|"
        print(ref)

        # printing table body
        result = self.c.execute("SELECT Log"+colnames+" FROM "+tbl)             
        for row in result:
            idx2 = 0
            line = ""
            # handling columns (left to right)
            while idx2 < rlen:
                buffer = ""
                i = 0
                while(i < sizes[idx2]):
                    buffer += " "
                    i += 1
                        
                cell = "|  "+str(row[idx2]) + buffer[len(str(row[idx2])):sizes[idx2]] + "  "
                line += cell
                idx2 += 1
            print(line+"|")
    

