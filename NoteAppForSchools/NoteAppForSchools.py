import sqlite3
con = sqlite3.connect("notes.db")
cr = con.cursor()
def CreateTable():
    cr.execute("CREATE TABLE IF NOT EXISTS infos(name TEXT,sirname TEXT,number INT,note INT)")
def WriteNote():
    name = input("Student's name: ")
    sirname = input("Student's sirname: ")
    schoolnumber = int(input("Student's school number: "))
    note = int(input("Student's grade: "))
    cr.execute("INSERT INTO infos(name,sirname,number,note) VALUES(?,?,?,?)",(name,sirname,schoolnumber,note))
    con.commit()
    print("---------------------------------------")
    print("Transaction Completed Successfully.")
    print("---------------------------------------")
def ReadNote():
    cr.execute("SELECT * FROM infos")
    datas = cr.fetchall()
    for data in datas:
        print("Student's name: {}\nStudent's sirname: {}\nStudent's school number: {}\nStudent's grade: {}".format(data[0],data[1],data[2],data[3]))
        print("---------------------------------------")
CreateTable()
while True:
    print("---------------------------------------")
    action = input("Please select an action:\nPress 1 to enter a student grade\nPress 2 to view student grades\nPress 3 to exit the application\nPress: ")
    print("---------------------------------------")
    if action == "1":
        WriteNote()
        dialog = input("Do you want to return to the menu? Y/N: ")
        if dialog.upper() == "Y":
            continue
        elif dialog.upper() == "N":
            print("Exiting Application...")
            print("---------------------------------------")
            break
    elif action == "2":
        ReadNote()
        dialog = input("Do you want to return to the menu? Y/N: ")
        if dialog.upper() == "Y":
            continue
        elif dialog.upper() == "N":
            print("Exiting Application...")
            print("---------------------------------------")
            break
    elif action == "3":
        print("Exiting Application...")
        print("---------------------------------------")
        break