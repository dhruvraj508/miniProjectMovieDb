#---------------CMPUT 291 - MP2-------------------------
# Group Members:
# Dhruvraj Singh (ccid: dhruvraj)
# Mobashhir Khan (ccid: mobashhi)
#--------------------------------------------------------

# This is the main file of our Project
# Here we ask the user to enter a valid port number
# to connect to the port
# Once the connection is established, we then display the main menu
# Then we perform different tasks according to the user input.

import sys
# importing all the different files for different tasks
import searchTitles
import searchGenre
import searchCast
import addMovie
import addCast
#import searchTitleNew

from pymongo import MongoClient


def main():
    # prompting the user to enter a valid port number and making the connection.
    portNumber = str(input("Please enter a valid Port Number: "))
    client = MongoClient("mongodb://localhost:"+portNumber+"/")
    # client = MongoClient("mongodb://localhost:27017/")
    db = client["291db"]

    programQuit = False
    while not programQuit:
        # runs until the user says to exit
        print("Welcome to the Main Menu!")
        userChoice = str(input("Please select an option\n"
                               "1. Search for titles\n"
                               "2. Search for Genres\n"
                               "3. Search for Cast/Crew Members\n"
                               "4. Add a movie\n"
                               "5. Add a Cast/Crew member\n"
                               "6. Exit\n"))
        # calling the respective functions.
        if userChoice == '1':
            searchTitles.searchTitles(db)
        elif userChoice == '2':
            searchGenre.searchGenre(db)
        elif userChoice == '3':
            searchCast.searchCast(db)
        elif userChoice == '4':
            addMovie.addMovie(db)
        elif userChoice == '5':
            addCast.addCast(db)
        elif userChoice == '6':
            print("Thank you for using the program.")
            programQuit = True
            sys.exit()
        else:
            print("Invalid Entry! Please try again!")


main()
