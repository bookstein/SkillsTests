import sqlite3

# Connect to the Database
def connect_to_db():
	global DB, CONN
	CONN = sqlite3.connect('meloninfo.db')

	DB = CONN.cursor()

# drop existing database tables
# DOES NOT WORK!?
# def delete_table(tablename):
# 	query = """DROP TABLE ?"""
# 	DB.execute(query, (tablename, ))

# Make the database from CSV files

def populate_customers_table(filename):
	f = open(filename)

	DB.execute("""
		CREATE TABLE customers (id INTEGER NOT NULL,
		email VARCHAR(120) NOT NULL,
		givenname VARCHAR(30),
		surname VARCHAR(30),
		password VARCHAR(200),
		telephone VARCHAR(20),
		called DATE,
		tos_agree INTEGER,
		gender VARCHAR(13),
		dob DATE,
		billto_address1 VARCHAR(40),
		shipto_address2 VARCHAR(40),
		shipto_city VARCHAR(35),
		shipto_state VARCHAR(35),
		shipto_postalcode VARCHAR(10),
		region VARCHAR(20),
		PRIMARY KEY (id),
		CHECK (gender IN ('Not Specified', 'Male', 'Female', 'Other')));
		""")
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
			customer_record[5] = "00/00/00" # did this not work??
		print "Added row: ", customer_record
		DB.execute(query, (email, first, last, telephone, called))
	CONN.commit()
	f.close()

def populate_orders_table(filename):
	f = open(filename)

	DB.execute("""
		CREATE TABLE orders (
		id INTEGER NOT NULL,
		customer_id INTEGER NOT NULL,
		status VARCHAR(16),
		salesperson_id INTEGER,
		shipto_address1 VARCHAR(40),
		shipto_address2 VARCHAR(40),
		shipto_city VARCHAR(35),
		shipto_state VARCHAR(35),
		shipto_postalcode VARCHAR(10),
		num_watermelons INTEGER,
		num_othermelons INTEGER,
		subtotal NUMERIC(10, 2),
		tax NUMERIC(10, 2),
		delivery_method VARCHAR(20),
		delivery_amount NUMERIC(10, 2),
		order_total NUMERIC(10, 2), delivered_at INTEGER,
		PRIMARY KEY (id),
		CHECK (status IN ('New', 'Processing', 'Out for Delivery', 'Delivered', 'Canceled'))
		);
		""")

	query = """INSERT INTO orders (customer_id, status, shipto_address1, shipto_city,
		shipto_state, shipto_postalcode, num_watermelons, num_othermelons,
		subtotal, tax, order_total) VALUES (?,?,?,?,?,?,?,?,?,?,?)"""

	# gets first row of file -- headers -- this was causing an error in datatype
	header = f.readline().rstrip().split(",")

	for line in f:
		line = line.decode('utf-8')
		order_record = line.strip().split(",")

		#unpack order_record from csv
		(order_id, order_date, status, customer_id, email, address, city, state,
		 postalcode, num_watermelons, num_othermelons,
		 subtotal, tax, order_total) = order_record
		print order_record
		# execute query for each record
		# columns in table that are not given value will have Null value
		DB.execute(query, (customer_id, status, address, city, state,
			postalcode, num_watermelons, num_othermelons, subtotal,
			tax, order_total))
	CONN.commit()
	f.close()

def make_top_customers_view():
	"""Create new view that defines top customers.
	In this case, top customers made purchases of more than
	20 melons of any type."""
	query = """
		DROP VIEW top_customers;
		CREATE VIEW top_customers AS
		SELECT * FROM customers LEFT JOIN orders
		ON (orders.customer_id = customers.id)
		WHERE (num_watermelons + num_othermelons >= 20)
		"""
	DB.execute(query)
	print "Dropped old top customers view/Added top customers view."
	CONN.commit()

def main():
	connect_to_db()
	# populate_customers_table("customers.csv")
	make_top_customers_view()
	populate_orders_table("orders.csv")

if __name__ == "__main__":
	main()



