"""
call.py - Telemarketing script that displays the next name
          and phone number of a Customer to call.

          This script is used to drive promotions for
          specific customers based on their order history.
          We only want to call customers that have placed
          an order of over 20 Watermelons.

"""


#Class definition to store our customer data
class Customer(object):


# Connect to the Database
def connect_to_db():


#Retrieve the next uncontacted customer record from the database.
#Return the data in a Customer class object.

# Remember: Our telemarketers should only be calling customers
#           who have placed orders of 20 melons or more.


def get_next_customer():

		# sample row
		# 1|julia@roomm.gov|Linda|Garrett||8-(184)172-2138|10/19/2014||||||||||2354|1|Canceled||89 Cody Court||Woodland|FL|29208|58|0|136|8.16|||156.42|




def display_next_to_call(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print customer
	print "\n"


# Update the "last called" column for the customer
#   in the database.
def update_customer_called(customer):


def main():



if __name__ == '__main__':
	main()