from pymongo import MongoClient

client = MongoClient(
	"mongodb+srv://jesco:noksWhSSOjGd88mE@iamjesco.bujsb.mongodb.net/?retryWrites=true&w=majority")
db = client.rawdata


#   ==================================================================================
#                       USER QUERIES
#   ==================================================================================

class Database:

	@staticmethod
	def fetch_all_data():
		query = db.data.find({}, {'_id': 0})
		return [data for data in query]

	@staticmethod
	def add_data(data):
		return db.data.insert_one(data)

	@staticmethod
	def fetch_data(id):
		return db.data.find_one({'id': id}, {'_id': 0})

	@staticmethod
	def update_data(id, data):
		return db.data.update_one({'id': id}, {'$set': data})

	@staticmethod
	def delete_data(id):
		return db.data.delete_one({'id': id})


#   ==================================================================================
#                       USER QUERIES
#   ==================================================================================

class Users:

	@staticmethod
	def fetch_all_users():
		return db.users.find({})

	@staticmethod
	def fetch_user(email):
		return db.users.find_one({'email': email}, {'_id': 0})

	@staticmethod
	def create_user(user):
		return db.users.insert_one(user)

# data = Post('Mi prome poesia', 'Oooga booga mashooga nooga')

# Database.create_post(data.json())

# print(data.json())

# data = Database.fetch_all_data()
# print(data)

# print(data['filename'])


# Database.update_post(8241940, 'Willy Wonka', 'mi kas tambe')

# Database.delete_post(8241940)

# print(Database.fetch_all_posts())

# movies = [movie for movie in Database.fetch_all_movies()]
# print(movies)

# print(Database.fetch_user('saegwsg@hotmail.com'))

# email = 'jesco1979@hotmail.com'
#
# user = Database.fetch_user('jesco1979@hotmail.com')
# if email not in user['email']:
# 	print('ooga')













