from pymongo import MongoClient

# client = MongoClient(host=['localhost:27017'])
client = MongoClient("mongodb://admin:password@localhost:27017")

# mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]
print(client)
database= client.User
collection = database.Users


# insert query
def insert_user(user_name_password):
    try:
        query_to_insert_user_in_db = collection.insert_one(user_name_password)
        """here query_to_insert_user_in_db.acknowledged gives
           status which is boolean value.
         """
        if query_to_insert_user_in_db.acknowledged == True:
            return True
        else:
            return False
    except Exception as e:
        return str(e)


test_data = {"username": "Amit", "password": "abc123"}
print(insert_user(test_data))


# read query
def read(a, b, **kwargs):
    # findquery = {"username": username, "password": password}
    # projection = {"username": 1, "age": 1, "_id": 0}
    try:
        cursor = collection.find_one(a, b)
        return cursor
    except Exception as e:
        return {str(e)}

# test_data = {"username": "Amit", "password": "abc123"}
# projection = {"username": 1,"age":1, "_id": 0}
# print(read(test_data,projection))
# delete query
def delete(find):
    try:
        query = collection.delete_one(find)
        return query.deleted_count
    except Exception as e:
        return {str(e)}


# n = {"username":"Controller"}
# # insert(n)
# res =delete(n)
# print(res)

# update query

def updatee(find, update):
    # a represents match{}
    # b represents projection
    # find = {"username": username}
    # update = {"$set": {"age": age}}
    try:
        query = collection.update_one(find, update)
        ack = query.acknowledged
        match = query.modified_count
        return [ack, match]
    except Exception as e:
        return {str(e)}

# n = {"username":"Amit"}
# #insert(n)
# up = {"$set":{"age":24}}
# u = update(n,up)
# print(u)
