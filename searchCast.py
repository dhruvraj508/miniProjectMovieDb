# This file contains the function searchCast
# Here we prompt the user to enter the name of
# a cast or crew member and then we search for
# all the members with the given name and display
# their details.

import re

def searchCast(db):
    # prompting the user to enter the cast/crew name and finding the name in the collection
    castName = input("Please enter the name of cast/crew member you would like to search for: ")
    castNameList = db.name_basics.find({"primaryName": re.compile(castName, re.IGNORECASE)})
    # printing the details of every person found
    for name in castNameList:
        print('-' * 60)
        print("Member ID: " + str(name['nconst']) + " Member Name: " + str(name['primaryName']))
        print("     The primary profession of this Member is : " + str(name["primaryProfession"]))
        print('')
        # movie details.
        titlePrincipals = db.title_principals.find({"nconst": name["nconst"]})
        for title in titlePrincipals:
            if title['job'] is None and title['characters'] is None:
                pass
            else:
                result = db.title_basics.find({"tconst": title["tconst"]})
                for i in result:
                    print("     Title of the movie : " + str(i["primaryTitle"]))
                print("     The job of the cast/crew member : " + str(title['job']))
                print("     The characters played by cast/crew member : " + str(title['characters'][0]))
                print('')
