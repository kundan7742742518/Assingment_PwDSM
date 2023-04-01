# ANS = 1
""""
MongoDB is a popular open-source document-oriented NoSQL database program that uses a 
document data model to store data in a flexible,
semi-structured format

Non-relational databases, also known as NoSQL databases, 
are databases that don't rely on the traditional relational data model used by SQL databases. 
Instead, they use different data models, such as document-based, key-value,
graph-based, or column-family, to store and retrieve data.


Scalability
Flexibility
Real-time analytics
Agile development
"""

# ANS = 2
""""
Flexible data model := MongoDB's document data model allows for a flexible schema design
Scalability:-MongoDB is highly scalable and can handle large amounts of data and high-traffic workloads with ease
Powerful querying:- MongoDB's support for dynamic queries and full-text search makes it easy to query and analyze large volumes of data.
Multi-language support:- MongoDB supports a variety of programming languages, including Java, Python, Node.js, and more, making it easy to integrate with existing applications and development workflows.

"""
# ANS = 3

from pymongo import MongoClient
client = MongoClient()
db = client['mydatabase']
collection = db['mycollection']
post = {"title": "My first post", "content": "This is my first MongoDB post!"}
post_id = collection.insert_one(post).inserted_id
print(post_id)


# ANS = 4


from pymongo import MongoClient
client = MongoClient()
db = client['mydatabase']
collection = db['mycollection']
post = {"title": "My second post", "content": "This is my second MongoDB post!"}
post_id = collection.insert_one(post).inserted_id
print("Inserted record:")
print(collection.find_one({"_id": post_id}))
posts = [
    {"title": "My third post", "content": "This is my third MongoDB post!"},
    {"title": "My fourth post", "content": "This is my fourth MongoDB post!"},
    {"title": "My fifth post", "content": "This is my fifth MongoDB post!"}
]
result = collection.insert_many(posts)
print("Inserted records:")
for post in collection.find():
    print(post)
    
    
# ANS= 5

""""
The find() method in MongoDB is used to retrieve data from a MongoDB collection.
It returns a cursor to the collection that can be iterated to access the documents.

"""
import pymongo


client = pymongo.MongoClient("host")
db = client["mydatabase"]
collection = db["mycollection"]
query = {"name": "John"}
results = collection.find(query)
for result in results:
    print(result)

# ANS= 6
""""
The sort() method in MongoDB is used to sort the documents in a collection based on one
or more fields
db.books.find().sort({ published_date: -1 })
"""

# ANS =- 7
""""
delete_one():- is used to delete a single document that matches a specified filter
delete_many():- is used to delete multiple documents that match a specified filter.
drop():- is used to remove an entire collection from a database. 
"""
