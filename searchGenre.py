# This file contains the function searchGenre
# Here we prompt the user to enter a valid genre and then
# and then prompt for the minimum number of votes to be shown
# We display all the title and the ratings of the movies.

def searchGenre(db):
    # a list of all the genres.
    validGenres = ["Crime", "Horror", "Adventure", "Comedy", "Sci-Fi", "Documentary", "Action", "Mystery", "Biography",
                   "Sport", "Romance", "Drama", "Fantasy", "Thriller", "War", "Family", "Western", "Musical", ""]
    # prompting the user to enter a genre and checking if that exists in the validGenres
    userGenre = str(input("Please enter a Genre: "))
    for i in range(len(validGenres)):
        if userGenre.lower() == validGenres[i].lower():
            userGenre = validGenres[i]
    minVote = int(input("Please enter the minimum vote count: "))

    # Query to find the respective movies with greater votes and ratings

    finalData = db.title_basics.aggregate([
        {
            "$match": {"genres": userGenre}

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
            "$match": {"rating.numVotes": {"$gte": minVote}}
        },
        {
            "$sort": {"rating.averageRating": -1}
        },
        {
            "$project": {
                "primaryTitle": 1, "genres": 1, "rating.averageRating": 1
            }
        }
    ])
    # printing out the final data (results)
    finalData = list(finalData)
    print(f"{'Title':<60}{'Rating':>10}")
    print('-' * 80)
    for i in finalData:
        rating = str(i['rating'][0]['averageRating'])
        print(f"{str(i['primaryTitle']):<60}{rating:>10}")
    print('\n')
