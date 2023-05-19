# This file contains the function addCast
# Here we ask the user to enter a user id which
# already exists in the collection name_basics.
# Then we take in tittle id and check if that
# exists in the respective database.
# Then we get the highest ordering and we add 1 to
# ordering, after this we insert the data in the collection.

def addCast(db):
    title_principals_db = db["title_principals"]
    # prompting the user to enter a valid crew id
    castId = str(input("Please enter a valid Cast/Crew ID: "))
    castDict = {"nconst": castId}
    # checking if the id is valid or not
    # if not valid, prompting the user again
    while not db.name_basics.count_documents(castDict):
        print("The cast id does not exist in the collection.")
        castId = str(input("Please enter a valid Cast/Crew ID: "))
        castDict = {"nconst": castId}
    # prompting the user to enter a valid title id
    titleId = str(input("Please enter a valid Title ID: "))
    titleDict = {"tconst": titleId}
    # checking if the id is valid or not
    # if not valid, prompting the user again
    while not db.title_basics.count_documents(titleDict):
        print("The title id does not exist in the collection.")
        titleId = str(input("Please enter a valid Title ID: "))
        titleDict = {"tconst": titleId}
    category = str(input("Please enter a Category: "))
    # query to get the orderwise ordering
    query = [{"$match": {"tconst": "{}".format(titleId)}},
             {"$sort": {"ordering": -1}}]
    results = title_principals_db.aggregate(query)
    resultList = list(results)
    # the new value of ordering to be inserted.
    highestOrdering = (resultList[0]['ordering']) + 1
    # if the title id exists, we add highest ordering
    # otherwise we just add 1 in ordering
    if db.title_principals.count_documents(titleDict):
        insertDict = {"tconst": titleId, "ordering": highestOrdering, "nconst": castId, "category": category,
                      "job": None, "characters": None}
        db.title_principals.insert_one(insertDict)
        print("Cast added successfully!\n")
    else:
        insertDict = {"tconst": titleId, "ordering": 1, "nconst": castId, "category": category,
                      "job": None, "characters": None}
        db.title_principals.insert_one(insertDict)
        print("Cast added successfully!\n")
