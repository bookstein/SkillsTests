import sqlite3

# Connect to the Database
def connect_to_db():
	global DB, CONN
	CONN = sqlite3.connect('meloninfo.db')

	DB = CONN.cursor()

# Make the database from CSV files

def populate_customers_table(filename):
	f = open(filename)
	#table column names must be specified AND in order!! See .schema
	#I also wasn't supposed to include the id number. Why??
	query = """INSERT INTO customers (email, givenname, surname,
		telephone, called) VALUES (?,?,?,?,?)"""

	# gets first row of file -- headers
	header = f.readline().rstrip().split(",")

	for line in f:
		customer_record = line.strip().split(",")
		cid, first, last, email, telephone, called = customer_record
		if len(customer_record[5]) < 1:
			customer_record[5] = "00/00/00"
		print "Added row: ", customer_record
		DB.execute(query, (email, first, last, telephone, called))
	CONN.commit()
	f.close()

def populate_orders_table(filename):
	f = open(filename)

	query = """INSERT INTO orders (customer_id, status, shipto_address1, shipto_city,
		shipto_state, shipto_postalcode, subtotal, tax, order_total)
		VALUES (?,?,?,?,?,?,?,?,?)"""

	# gets first row of file -- headers -- this was causing an error in datatype
	header = f.readline().rstrip().split(",")

	for line in f:
		line = line.decode('utf-8')
		order_record = line.strip().split(",")

		#unpack order_record from csv
		order_id, order_date, status, customer_id, email, address, city, state, postalcode, num_watermelons, num_othermelons, subtotal, tax, order_total = order_record
		print order_record
		# execute query for each record
		# columns in table that are not given value will have Null value
		DB.execute(query, (customer_id, status, address, city, state, postalcode, subtotal, tax, order_total))
	CONN.commit()
	f.close()


def main():
	connect_to_db()
	# populate_customers_table("customers.csv")
	populate_orders_table("orders.csv")

if __name__ == "__main__":
	main()



