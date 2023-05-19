# This file contains the function addMovie
# Here we ask the user to enter a unique non-existing
# ID and then we ask about the movie details
# after this we add the details given to us in the
# respective collection.

def addMovie(db):
    genreList = []
    count = 0

    # prompting the user to enter a unique id
    userId = str(input("Please enter a unique ID: "))
    uniqueID = {"tconst": userId}

    # if the id is not unique (already exists)
    while db.title_basics.count_documents(uniqueID) >= 1:
        print("Not a unique ID, please try again.")
        userId = str(input("Please enter a unique ID: "))
        uniqueID = {"tconst": userId}

    # asking for movie details.
    primaryTitle = str(input("Please enter the title of the movie: "))
    originalTitle = primaryTitle
    startYear = str(input("Please enter the start year of the movie: "))
    while not startYear.isnumeric():
        print("The year is not numeric.")
        startYear = str(input("Please enter a valid year: "))
    runtimeMinutes = str(input("Please enter the running time of the movie: "))
    while not runtimeMinutes.isnumeric():
        print("The runtime of the movie is not numeric.")
        runtimeMinutes = str(input("Please enter a valid Running time: "))

    # asking for multiple genres.
    genreName = str(input("Please enter a genre: "))
    genreList.append(genreName)
    userChoice = str(input("Do you want to enter another genre? (y/n)"))
    while userChoice == 'Y' or userChoice == 'y':
        if count == 0:
            genreName = input("Please enter a genre: ")
            genreList.append(genreName)
            userChoice = input("Do you want to enter another genre? (y/n)")
            count += 1
        else:
            genreName = str(input("Please enter a genre: "))
            genreList.append(genreName)
            userChoice = str(input("Do you want to enter another genre? (y/n)"))

    titleType = "movie"
    isAdult = None
    endYear = None
    # final data to be inserted into the collection
    insertDict = {"tconst": userId, "titleType": titleType, "primaryTitle": primaryTitle,
                  "originalTitle": originalTitle, "isAdult": isAdult, "startYear": startYear, "endYear": endYear,
                  "runtimeMinutes": runtimeMinutes, "genres": genreList}
    db.title_basics.insert_one(insertDict)
    print("Movie added succesfully!\n")
