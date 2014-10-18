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

#Class definition to store our customer data
class Customer(object):
	def __init__(self, id=None, first=None, last=None, telephone=None):
		self.first = ''
		self.last = ''
		self.telephone = ''
		pass

	def __str__(self):
		output = " Name: %s, %s\n" % (self.last, self.first)
		output += "Phone: %s" % self.telephone

		return output

# Connect to the Database
def connect_to_db():
	global DB, CONN
	CONN = sqlite3.connect('meloninfo.db')

	DB = CONN.cursor()


#Retrieve the next uncontacted customer record from the database.
#Return the data in a Customer class object.

# Remember: Our telemarketers should only be calling customers
#           who have placed orders of 20 melons or more.
def get_next_customer(c_id):
	c = Customer(id=c_id)
	query = """SELECT * FROM customers WHERE id = ?"""
	DB.execute(query, (c_id, ))
	row = DB.fetchone()
	c.first = row[2]
	c.last = row[3]
	c.telephone = row[5]

	print c


def display_next_to_call(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print customer
	print "\n"


# Update the "last called" column for the customer
#   in the database.
def update_customer_called(customer):
	pass

def main():
	connect_to_db()

	done = False

	# while not done:
	c_id = 1
	customer = get_next_customer(c_id)
		# display_next_to_call(customer)

		# print "Mark this customer as called?"
		# user_answer = raw_input('(y/n) > ')

		# if user_answer.lower() == 'y':
		# 	update_customer_called(customer)
		# else:
		# 	done = True


if __name__ == '__main__':
	main()