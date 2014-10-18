"""
call.py - Telemarketing script that displays the next name
          and phone number of a Customer to call.

          This script is used to drive promotions for
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

import sqlite3

DB = None
CONN = None

# Make the database from CSV files

def populate_customers_table(filename):
	f = open(filename)
	#table column names must be specified AND in order!! See .schema
	#I also wasn't supposed to include the id number. Why??
	query = """INSERT INTO customers (email, givenname, surname,
		telephone, called) VALUES (?,?,?,?,?)"""
	for line in f:
		customer_record = line.strip().split(",")
		cid, first, last, email, telephone, called = customer_record
		if len(customer_record[5]) < 1:
			customer_record[5] = "00/00/00"
		print "Row: ", customer_record
		DB.execute(query, (email, first, last, telephone, called))
	CONN.commit()
	f.close()

# # Class definition to store our customer data
# class Customer(object):
# 	def __init__(self, id=None, first=None, last=None, telephone=None):
# 		self.first = ''
# 		self.last = ''
# 		self.telephone = ''
# 		pass

# 	def __str__(self):
# 		output = " Name: %s, %s\n" % (self.last, self.first)
# 		output += "Phone: %s" % self.telephone

# 		return output

# Connect to the Database
def connect_to_db():
	global DB, CONN
	CONN = sqlite3.connect('meloninfo.db')

	DB = CONN.cursor()


# # Retrieve the next uncontacted customer record from the database.
# # Return the data in a Customer class object.
# #
# # Remember: Our telemarketers should only be calling customers
# #           who have placed orders of 20 melons or more.
# def get_next_customer():
# 	c = Customer()

# 	return c


# def display_next_to_call(customer):
# 	print "---------------------"
# 	print "Next Customer to call"
# 	print "---------------------\n"
# 	print customer
# 	print "\n"


# # Update the "last called" column for the customer
# #   in the database.
# def update_customer_called(customer):
# 	pass

def main():
	connect_to_db()
	populate_customers_table("customers.csv")

	# done = False

	# while not done:
	# 	customer = get_next_customer()
	# 	display_next_to_call(customer)

	# 	print "Mark this customer as called?"
	# 	user_answer = raw_input('(y/n) > ')

	# 	if user_answer.lower() == 'y':
	# 		update_customer_called(customer)
	# 	else:
	# 		done = True


if __name__ == '__main__':
	main()