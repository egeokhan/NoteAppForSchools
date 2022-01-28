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
def ChangeNote():
    print("---------------------------------------")
    schoolnumb = int(input("Student's school number: "))
    newnote = int(input("Student's new grade: "))
    print("---------------------------------------")
    print("Old information:")
    cr.execute("SELECT * FROM infos WHERE number = {}".format(schoolnumb))
    datastudent = cr.fetchall()
    print("---------------------------------------")
    for i in datastudent:
        print("Name: {}\nSirname: {}\nSchool Number: {}\nNote: {}".format(i[0],i[1],i[2],i[3]))
        break
    print("---------------------------------------")
    cr.execute("UPDATE infos SET note = {} WHERE number = {}".format(newnote,schoolnumb))
    cr.execute("SELECT * FROM infos WHERE number = {}".format(schoolnumb))
    newdata = cr.fetchall()
    print("New information:")
    print("---------------------------------------")
    for j in newdata:
        print("Name: {}\nSirname: {}\nSchool Number: {}\nNote: {}".format(j[0],j[1],j[2],j[3]))
        break
    print("---------------------------------------")
    sure = input("Changes will be saved, are you sure? Y/N: ")
    if(sure.upper() == "Y"):
        con.commit()
        print("Transaction completed successfully")
        print("---------------------------------------")
    else:
        print("The transaction has been cancelled.")
        print("---------------------------------------")
def DeleteStudent():
    schoolnumber = int(input("Student's school number: "))
    yesno = input("Changes will be saved, are you sure? Y/N: ")
    if yesno.upper() == "Y":
        cr.execute("DELETE FROM infos WHERE number = {}".format(schoolnumber))
        con.commit()
        print("---------------------------------------")
        print("Student deleted...")
    else:
        print("The transaction has been cancelled.")
        print("---------------------------------------")

CreateTable()
while True:
    print("---------------------------------------")
    action = input("Please select an action:\nPress 1 to enter a student grade\nPress 2 to view student grades\nPress 3 to change note\nPress 4 to delete a student\nPress 5 to exit the application\nPress: ")
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
        ChangeNote()
        dialog = input("Do you want to return to the menu? Y/N: ")
        if dialog.upper() == "Y":
            continue
        elif dialog.upper() == "N":
            print("Exiting Application...")
            print("---------------------------------------")
            break
    elif action == "4":
        DeleteStudent()
        dialog = input("Do you want to return to the menu? Y/N: ")
        if dialog.upper() == "Y":
            continue
        elif dialog.upper() == "N":
            print("Exiting Application...")
            print("---------------------------------------")
            break
    elif action == "5":
        print("Exiting Application...")
        print("---------------------------------------")
        break