import hashlib
import random
import string
import mysql.connector

class Block:
	def __init__(self, previous_hash, transaction):
		self.transactions = transaction
		self.previous_hash = previous_hash
		self.connection = mysql.connector.connect(user="root", password="",
												  host="127.0.0.1", database="blockchain")
		string_to_hash = "".join(transaction) + previous_hash
		self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()

		while (self.block_hash[:3] != "000"):
			letters = string.ascii_lowercase
			result_str = "".join(random.choice(letters) for i in range(10))
			string_to_hash = string_to_hash + result_str
			self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()
			print(self.block_hash)
		my_cursor = self.connection.cursor()
		sql = "INSERT INTO blocks (previous_hash, hash) VALUES (%s, %s)"
		val = (self.previous_hash, self.block_hash)
		my_cursor.execute(sql, val)
		self.connection.commit()
		print("\nBlock added successfully!")
		self.connection.close()