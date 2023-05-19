import json
import time

from pymongo import MongoClient

client = None


def load_json(filename,collection_name):
    global client
    db = client["291db"]

    # Drop the collection
    db.drop_collection(collection_name)

    collection = db[collection_name]
    
    with open(filename) as file:
        collection.insert_many(json.load(file))


def main():
    global client
    port_number = int(input("Enter the port number: "))
    client = MongoClient("mongodb://localhost:"+str(port_number)+"/")
    filenames = ["name.basics.json", "title.basics.json","title.principals.json","title.ratings.json"]
    collection_names = ["name_basics", "title_basics", "title_principals", "title_ratings"]

    for f,c in zip(filenames, collection_names):
        load_json(f,c)


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print("Time taken to insert = "+ "%.2f seconds" % (end_time-start_time))
