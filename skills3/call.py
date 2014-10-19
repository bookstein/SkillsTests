"""
call.py - Telemarketing script that displays the next name
          and phone number of a Customer to call.

          This script is used to drive promotions for
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

import sqlite3
from datetime import date

DB = None
CONN = None

#Class definition to store our customer data
class Customer(object):
	def __init__(self, id=None, first=None, last=None, telephone=None, called=None):
		self.id = ''
		self.first = ''
		self.last = ''
		self.telephone = ''
		self.called = ''

	def __str__(self):
		output = " Name: %s, %s\n" % (self.last, self.first)
		output += "Phone: %s\n" % self.telephone
		output += "ID: %s\n" % self.id
		output += "Last called: %s" % self.called

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
def get_next_customer():
	c = Customer()
	not_called = ""
	query = """SELECT * FROM customers WHERE called = ?"""
	DB.execute(query, (not_called,))
	row = DB.fetchone()
	c.id = row[0]
	c.first = row[2]
	c.last = row[3]
	c.telephone = row[5]
	c.called = row[6]
	print "row ", row
	# return c


def display_next_to_call(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print customer
	print "\n"


# Update the "last called" column for the customer
#   in the database.
def update_customer_called(date, customer):
	query = """UPDATE customers SET called = ? WHERE id = ?"""
	DB.execute(query, (date, customer.id))
	customer.called = date
	print customer
	CONN.commit()

def main():
	connect_to_db()

	done = False
	c_id = 0
	today = date.today().strftime("%m/%d/%Y")
	# mimic 04/01/2014 for date called

	while not done:
		c_id += 1
		customer = get_next_customer()
		display_next_to_call(customer)

		print "Mark this customer as called?"
		user_answer = raw_input('(y/n) > ')

		if user_answer.lower() == 'y':
			update_customer_called(today, customer)
		else:
			done = True


if __name__ == '__main__':
	main()