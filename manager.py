# The main program here is intended to be run on cmd/terminal rather than on the IDE

from dbclass import DbClass
from time import sleep
import os

# Clears the command prompt.
clear = lambda: os.system("cls")

# Turns all values in a comma separated line into strings.
def parenthesis(text):
    text = text.split(",")
    tlen = len(text)
    line = ''
    i = 0
    while(i < tlen):
        text[i] = text[i].strip(" ")
        line += '"'+text[i]+'",'
        i += 1

    llen = len(line)
    line = line[:llen-1]
    return line
    
# Meant to take a comma separated line of sqlite table column names and add a TEXT data type specification. 
def columndefault(text):
    parts = text.split(",")
    pcount = len(parts)
    i = 0
    while(i < pcount):
        parts[i] = parts[i].strip(" ")
        parts[i] += " TEXT,"
        i+=1
        
    print(parts)
    line = "".join(parts)
    
    line = line[0:]
    llen = len(line)
    line = line[0:llen-1]
    return line

# Prints the given table list.
def printlist(tlist):
    ntables = len(tlist)
    i = 0
    j = 0
    while(i < ntables):
        # Hidding the extra table created when using auto increment value.
        if tlist[i][0] != "sqlite_sequence":
            print(" "+str(j)+". "+tlist[i][0])
        j += 1
        i += 1
    ntables -= 1
    print("\nThere are "+str(ntables)+" tables in this database.")
    
# The main program, a database manager.
def main():
    # Connecting to a database given by name.
    dbn = input('Name of database : ')
    dbn += ".db"
    dbn = dbn.strip(" ")
    dbase = DbClass(dbn)
    sleep(2)
    clear()
    print("Welcome to "+dbn+".\n")
    
    # The database manager loop.
    while 1:
        print("  1) Create a table")
        print("  2) Edit")
        print("  3) View")
        print("  4) Exit\n")
        user = input("What to do? (Enter a number.) : ")
        clear()
        
# Create a table
        if user == '1':
            try:
                tname = input("Table name : ")
                cnames = input("Column titles (separate with commas) : ")
                cnames = columndefault(cnames)
                DbClass.createtbl(dbase,tname,cnames)
                clear()
                print("Table created.")
            except:
                print("An error occured!")
            proceed = input("Hit enter to continue...")
            clear()

# Edit (tables)
        elif user == '2':
            while 1:
                print("---Edit Menu---\n")
                print("  1) Insert values into a table")
                print("  2) Edit a cell")
                print("  3) Delete a table")
                print("  4) Back\n")
                user = input("Enter a number : ")
                clear()
            # Insert values into a table
                if user == '1':
                    printlist(DbClass.tbllist(dbase))
                    tbl = input("Table to input data into : ")
                    print(DbClass.header(dbase,tbl))
                    cols = input("Column(s) to insert data into. ( Seperate by commas ) : ")
                    data = input("Data to be inserted. ( Seperate by commas ) : ")                    
                    data = parenthesis(data)
                    print(data)
                    try:         
                        DbClass.intotbl(dbase,tbl,cols,data)
                        user = input("Data saved. Hit enter key to continue...")
                    except:
                        user = input("Invalid input! Hit enter key to coninute...")
            # Edit a cell
                elif user == '2':
                    printlist(DbClass.tbllist(dbase))
                    tbl = input("Table : ")
                    DbClass.viewtbl(dbase,tbl)
                    idx = input("Row log number : ")
                    cols = input("Column(s) to edit. ( Seperate by commas ) : ")
                    data = input("Data to be inserted. ( Seperate by commas ) : ")
                    data = parenthesis(data)
                    try:
                        DbClass.editcell(dbase,tbl,cols,data,idx)
                        user = input("Data saved. Hit enter key to continue...")
                    except:
                        user = input("Invalid input! Hit enter key to coninute...")
            # Delete a table
                elif user == '3':
                    printlist(DbClass.tbllist(dbase))
                    tbl = input("Table : ")
                    try:
                        DbClass.deletetbl(dbase, tbl)
                        print("Table "+tbl+" deleted! Hit enter to continue...")
                    except:
                        user = input("Invalid input! Hit enter key to coninute...")
            # Back            
                elif user == '4':
                    break
                else:
                    user = input("Invalid input! Hit enter to continue...")
                clear()
                
# View (tables)
        elif user == '3':
            while 1:
                print("---View Menu---\n")
                print("  1) Existing tables")
                print("  2) Table header") 
                print("  3) View a table")
                print("  4) Back\n")
                user = input("Enter a number : ")
                clear()
            # Existing tables
                if user == '1':
                    print("___Table List___\n")
                    printlist(DbClass.tbllist(dbase))
                    user = input("Hit enter to continue...")
            # Table header
                elif user == '2':
                    printlist(DbClass.tbllist(dbase))
                    tbl = input("Table's header to view : ")
                    head = DbClass.header(dbase,tbl)
                    if (head == "[ ]"):
                        user = input('Table "'+tbl+'" does not exitst. Hit enter...')
                    else:
                        print("\n"+head+"\n")
                        user = input("Hit enter to continue...")
            # View a table
                elif user == '3':
                    printlist(DbClass.tbllist(dbase))
                    tbl = input("Table to view : ")
                    clear()
                    try:
                        DbClass.viewtbl(dbase,tbl)
                        user = input("Hit enter to continue...")
                    except:
                        user = input('Table "'+tbl+'" does not exitst. Hit enter...')
                # Back
                elif user == '4':
                    break
                else:
                    user = input("Invalid input! Hit enter to continue...")
                clear()
                
# Exit
        elif user == '4':
            print("Exiting application...")
            sleep(2)
            break



if __name__ == "__main__":
    main()
