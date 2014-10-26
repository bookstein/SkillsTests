"""
call.py - Telemarketing script that displays the next name
          and phone number of a Customer to call.

          This script is used to drive promotions for
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""
import sqlite3 as sq3
from datetime import date, datetime
from load_data import connect_to_db
CONN = None
DB = None

def connect_to_db():
	global CONN, DB
	CONN = sq3.connect("meloninfo.db")
	DB = CONN.cursor()
# how would I only use connect_to_db in ONE file, not 2? Or do I need
# it in both?

#Class definition to store our customer data
class Customer(object):
	def __init__(self, id, first, last, email, telephone, called):
		self.id = id
		self.first = first
		self.last = last
		self.email = email
		self.telephone = telephone
		self.called = called


	def __str__(self):
		return "Name: %s %s\n Telephone: %s\n Last called: %s" % (self.first, self.last,
			 self.telephone, self.called)


#Retrieve the next uncontacted customer record from the database.
#Return the data in a Customer class object.

# Remember: Our telemarketers should only be calling customers
#           who have placed orders of 20 melons or more.


def get_next_customer():
	# sample row
	# 1|julia@roomm.gov|Linda|Garrett||8-(184)172-2138|10/19/2014||||||||||2354|1|Canceled||89 Cody Court||Woodland|FL|29208|58|0|136|8.16|||156.42|
	query = """SELECT id, email, givenname, surname, telephone, called
				FROM customers
				WHERE called = ?"""
	DB.execute(query, ("00/00/0000",))
	row = DB.fetchone()
	c = Customer(row[0], row[2], row[3], row[1], row[4], row[5])
	return c
	# display_next_to_call(c) << do this in main()



def display_next_to_call(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print customer
	print "\n"


# Update the "last called" column for the customer
#   in the database.
def update_customer_called(customer):
	# using UTC time for consistency
	today = datetime.utcnow()
	query = """UPDATE customers
		SET called = ?
		WHERE id = ?"""
	DB.execute(query, (today, customer.id))
	CONN.commit()

def main():
	done = False
	connect_to_db()

	while not done:
		customer = get_next_customer()
		display_next_to_call(customer)

		print "Mark as called?"
		answer = raw_input("> ")
		if answer.lower() == "y":
			update_customer_called(customer)
			continue
		else:
			done = True




if __name__ == '__main__':
	main()