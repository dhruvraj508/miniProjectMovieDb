# This file contains the function searchTitles.
# User is prompted to enter one or more keywords,
# All the movies with matching keywords are then
# printed on the screen using AND semantics.
# The user then can select any title to see it's rating,
# votes and the characters of the respective movie.

def searchTitles(db):
    userKwList = []
    nameList = []
    userKeyword = str(input("Please enter a keyword: "))
    userKwList.append(userKeyword)
    userChoice = str(input("Do you want to enter another keyword? (Y/N): "))
    while userChoice == 'y' or userChoice == 'Y':
        userKeyword = str(input("Please enter a keyword: "))
        userKwList.append(userKeyword)
        userChoice = str(input("Do you want to enter another keyword? (Y/N): "))

    yearList = []
    titleList = []
    for key in userKwList:
        key = key.strip()
        if key.isnumeric():
            key = int(key)
            yearList.append(key)
        else:
            titleList.append(key)

    results = []
    queries = []

    if len(titleList) == 0:
        output1 = db.title_basics.find({'startYear': {"$in": yearList}})
        for i in output1:
            results.append(i)

    elif len(yearList) == 0:
        for k in titleList:
            output2 = db.title_basics.find({'primaryTitle': {"$regex": str(k), '$options': 'i'}})
            for i in output2:
                 results.append(i)
    else:
        for k in titleList:
            queries.append(({"$and": [{'primaryTitle': {"$regex": str(k), '$options': 'i'}}, {'startYear': {"$in": yearList}}]}))
        query = {'$and': queries}
        result = db.title_basics.find(query)

        for i in result:
            results.append(i)

    print(f"{'tconst':<10}{'titleType':^10}{'primaryTitle':^60}{'originalTitle':^60}{'isAdult':^10}{'startYear':^10}{'endYear':^10}{'runtimeMinutes':^20}{'genres':>20}")
    for ele in results:
        print(f"{str(ele['tconst']):<10}{str(ele['titleType']):^10}{str(ele['primaryTitle']):^60}{str(ele['originalTitle']):^60}{str(ele['isAdult']):^10}{str(ele['startYear']):^10}{str(ele['endYear']):^10}{str(ele['runtimeMinutes']):^20}{str(ele['genres']):>20}")

    movieChoice = int(input("Select an option: "))
    movieChoice -= 1

    selectData = db.title_basics.aggregate([
        {
            "$match": {
                "primaryTitle": results[movieChoice]["primaryTitle"]
            }
        },
        {
            "$lookup": {
                "from": "title_ratings",
                "localField": "tconst",
                "foreignField": "tconst",
                "as": "rating"
            }
        },
        {
            "$lookup": {
                "from": "title_principals",
                "localField": "tconst",
                "foreignField": "tconst",
                "as": "principals"
            }
        },
        {
            "$lookup": {
                "from": "name_basics",
                "localField": "principals.nconst",
                "foreignField": "nconst",
                "as": "names"
            }
        },
        {
            "$project": {
                'primaryTitle': 1, 'rating.averageRating': 1, 'rating.numVotes': 1, 'names.primaryName': 1, '_id': 0
            }
        }
    ])
    print('\n')
    for i in selectData:
        rating = str(i['rating'][0]['averageRating'])
        votes = str(i['rating'][0]['numVotes'])

        for name in i['names']:
            nameList.append(name['primaryName'])
        print(f"{'Rating':<10}{'Votes':<10}")
        print(f"{rating:<10}{votes:<10}")
        print("The name of the Cast/Crew is:")
        for crewName in nameList:
            print(crewName)
        print('\n')
