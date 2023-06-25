from pymongo import MongoClient

client = MongoClient()
mydatebase = client.Users
mycollection = mydatebase.user


#insert query
def insert_user(a):
    try:
        query_to_insert_user_in_db = mycollection.insert_one(a)
        """here query_to_insert_user_in_db.acknowledged gives
           status which is boolean value.
         """
        if query_to_insert_user_in_db.acknowledged == True:
            return True
        else:
            return False
    except Exception as e:
        return str(e)
# test_data = {"username": "Anil", "password":"abc123"}
# print(insert_user(test_data))

#read query
def read(a,b, **kwargs):
    # findquery = {"username": username, "password": password}
    # projection = {"username": 1, "age": 1, "_id": 0}
    try:
        cursor = mycollection.find_one(a, b)
        return cursor
    except Exception as e:
        return {str(e)}

#delete query
def delete(find):
    try:
        query = mycollection.delete_one(find)
        return query.deleted_count
    except Exception as e:
        return {str(e)}

# n = {"username":"Controller"}
# # insert(n)
# res =delete(n)
# print(res)

#update query

def updatee(find,update):
    #a represents match{}
    #b represents projection
    # find = {"username": username}
    # update = {"$set": {"age": age}}
    try:
        query = mycollection.update_one(find, update)
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
