# -*- coding: utf-8 -*-
import string
import os
import csv
import sys
def main():
    print("Stand up")
    print("Welcome to Misflix")
    welcome()

def welcome():

    choice = input("""
                      A: Please Register
                      B: Login
                      Q: Logout

                      Please enter your choice: """)

    if choice == "A" or choice == "a":
        register()
    elif choice == "B" or choice == "b":
        login()
    elif choice == "Q" or choice == "q":
        print("Thank you for visiting us,Please come again")
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        welcome()

def register():
    print('Please register on our website to get free movie')
    global firstname
    firstname = input('Please enter your firstname')
    global lastname
    lastname = input('Please enter your lastname')
    global phonenumber
    phonenumber = input('Please enter your phone number')
    global dob
    dob = input('Enter Date and Birth Format : dd/mm/yy')
    substring=dob[-4:]
    print('your unique username is ' , firstname  + substring)
    global username
    username = firstname + substring
    password = input("Please enter your password -it must contain a capital letter and at least one integer")
    with open('misflix.txt', 'a') as misflix:
        misflixWriter = csv.writer(misflix)
        misflixWriter.writerow([username ,password,firstname, lastname])
        print("Record has been written to file")
        misflix.close()
    welcome()


def login():
    # set a variable (boolean type) to true if the user is NOT logged on
    notloggedin = "true"
    # while the user is not logged on (i.e. while the login credentials provided do not work ...)
    while notloggedin == "true":
        print("***WELCOME - PLEASE LOGIN")

        # open the file we are reading from
        with open("misflix.txt", 'r') as misflix:
            # prompt the user to enter their login details
            username = input("Enter username:-")
            password = input("Enter password:-")
            # call upon our reader (this allows us to work with our file)
            misflixReader = csv.reader(misflix)
            # for each row that is read by the Reader
            for row in misflixReader:
                for field in row:

                    # search for the required matches in user entry against what is stored in the file
                    if field == username and row[1] == password:
                        print("Granted")
                        displayfilms()
                        notloggedin = "false"
def displayfilms():
   print("*******************WELCOME to Misflix **************************")
   print("What would you like to watch today?")
   choice = input("""
                     W:Watch a Movie 
                     V:View your recommendataion 
                     K:Search by Title 
                     R:Search by Rating 
                     L:View your "LIKED" list 
                     Q:Quit Misflix 
                     """)
   if choice == "W" or choice == "w":
       watchmovies()
   elif choice == 'V' or choice == 'v':
       viewrecs()
   elif choice == 'T' or choice =='t':
       searchbyTitle()
   elif choice ==  'R' or choice == 'r':
       searchbyrating()
   elif choice == "L" or choice == "l":
       viewliked()
   elif choice == "Q" or choice == "q":
       sys.exit
   else:
       print("You must only select from the given options")
       print("Please try again")
       displayfilms()


def watchmovies():
    # Open the file for reading
    filmsfile = open("films.txt", "r", encoding="utf8")
    # Create a list called displayfilms into which all the file lines are read into....
    displayfilmslist = filmsfile.read()
    # print the list (that now has the film details in it)
    print("List of all movies title available on our site")
    print(displayfilmslist)
    filmsfile.close()
    print("~What would you like to do?~")
    choice = input("""
                      Select a number(1-4) to watch a movie 
                                         or
                      F: Return to the Misflix Menu
                      Q: Quit Misflix

                      Please enter your choice: """)

    if choice == "F" or choice == "f":
        displayfilms()
    elif choice == "Q" or choice == "q":
        sys.exit
    elif choice == "1":
        viewfilmfunction(1)
    elif choice == "2":
        viewfilmfunction(2)
    elif choice == "3":
        viewfilmfunction(3)
    elif choice == "4":
        viewfilmfunction(4)
    elif choice == "5":
        viewfilmfunction(5)
    elif choice == "6":
        viewfilmfunction(6)
    elif choice == "7":
        viewfilmfunction(7)
    else:
        print("You must only select from the given options")
        print("Please try again")
        print("Please try again")
        displayfilms()


def viewfilmfunction(x):
    # open the file as student file (variable)
    print("You are about to view movie:", x, "Enter the selection ID number of the film again to confirm viewing")
    with open("films.txt", "r") as filmsfile:
        # prompt the user to enter the ID number they require
        idnumber = input("Enter the ID number you require:")
        # call upon our reader (this allows us to work with our file)
        filmsfileReader = csv.reader(filmsfile)
        # for each row that is read by the Reader
        for row in filmsfileReader:
            # and for each field in that row (this does it automatically for us)
            for field in row:
                # if the field is equal to the id number that is being searched for
                if field == idnumber:
                    # print the row fields (genre and title) corresponding to that ID number
                    # create a list which contains the relevant fields in the row.
                    viewedlist = [row[1], row[2]]
                    print("You have viewed:", viewedlist)


main()
