from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create a new database
db = client["mydatabase"]

# Create a new collection
collection = db["mycollection"]

# Insert a document into the collection
document = {"name": "John", "age": 30}
collection.insert_one(document)

# Find all documents in the collection
results = collection.find()
for result in results:
    print(result)

# Find a specific document in the collection
result = collection.find_one({"name": "John"})
print(result)

# Update a document in the collection
collection.update_one({"name": "John"}, {"$set": {"age": 31}})

# Delete a document from the collection
collection.delete_one({"name": "John"})

client.close()
