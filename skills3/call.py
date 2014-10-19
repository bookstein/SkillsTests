"""
call.py - Telemarketing script that displays the next name
          and phone number of a Customer to call.

          This script is used to drive promotions for
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""

import sqlite3
from datetime import date, timedelta

DB = None
CONN = None

#Class definition to store our customer data
class Customer(object):
	def __init__(self, id=None, first=None, last=None, telephone=None,
		called=None, melons=None):
		self.id = ''
		self.first = ''
		self.last = ''
		self.telephone = ''
		self.called = ''
		self.melons = ''

	def __str__(self):
		output = " Name: %s, %s\n" % (self.last, self.first)
		output += "Phone: %s\n" % self.telephone
		output += "ID: %s\n" % self.id
		output += "Last called: %s\n" % self.called
		output += "Melons purchased: %s" % self.melons

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


def get_next_customer(time):
	c = Customer()

	not_called = ""

	query = """SELECT * FROM customers
		LEFT JOIN orders
		ON (customers.id = orders.customer_id)
		WHERE (called = ? OR called < ?)
		AND (num_watermelons + num_othermelons >= 20)"""

		# sample row
		# 1|julia@roomm.gov|Linda|Garrett||8-(184)172-2138|10/19/2014||||||||||2354|1|Canceled||89 Cody Court||Woodland|FL|29208|58|0|136|8.16|||156.42|

	DB.execute(query, (not_called, time))
	row = DB.fetchone()
	c.id = row[0]
	c.first = row[2]
	c.last = row[3]
	c.telephone = row[5]
	c.called = row[6]
	c.melons = int(row[25]) + int(row[26])
	return c


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

	today = date.today()
	# .strftime("%m/%d/%Y")
		# mimic 04/01/2014
	thirty_days_ago = today + timedelta(-30)

	done = False

	while not done:
		customer = get_next_customer(thirty_days_ago)
		display_next_to_call(customer)

		print "Mark this customer as called?"
		user_answer = raw_input('(y/n) > ')

		if user_answer.lower() == 'y':
			update_customer_called(today, customer)
		else:
			done = True


if __name__ == '__main__':
	main()