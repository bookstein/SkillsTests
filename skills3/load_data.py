import sqlite3 as sq3
from datetime import date, datetime

CONN = None
DB = None

def connect_to_db():
	global CONN, DB
	CONN = sq3.connect("meloninfo.db")
	DB = CONN.cursor()


def make_customer_table():

	DB.execute("""CREATE TABLE customers (
		id INTEGER NOT NULL,
		email VARCHAR(120) NOT NULL,
		givenname VARCHAR(30),
		surname VARCHAR(30),
		password VARCHAR(200),
		telephone VARCHAR(20),
		called VARCHAR(10),
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
		CHECK (gender IN ('Not Specified', 'Male', 'Female', 'Other'))
		);
		""")
	CONN.commit()

def populate_customer_table():
	f = open("customers.csv")

	for line in f:
		customer_id, first, last, email, telephone, called = line.strip().split(",")
		#CSV data: customer_id,first,last,email,telephone,called

		if called == "":
			called = "00/00/0000"
		# if len(called) == 10:
		# 	called = datetime.strptime(called, "%m/%d/%Y")
		# else:
		# 	called = date(1970, 01, 01)

		print customer_id, first, last, email, telephone, called

		query = """INSERT INTO customers (email, givenname, surname, telephone,
			called) VALUES (?, ?, ?, ?, ?)"""
		DB.execute(query, (email, first, last, telephone, called))

	CONN.commit()
	f.close()

def make_orders_table():
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
		order_total NUMERIC(10, 2),
		delivered_at INTEGER,
		PRIMARY KEY (id),
		CHECK (status IN ('New', 'Processing', 'Out for Delivery', 'Delivered', 'Canceled'))
		);
		""")
	CONN.commit()

def populate_orders_table():
	f = open("orders.csv")

	# gets first row of file -- headers -- this was causing an error in datatype
	header = f.readline().rstrip().split(",")

	for line in f:
#order_id,order_date,status,customer_id,email,address,city,state,postalcode,num_watermelons,num_othermelons,subtotal,tax,order_total
		data = line.strip().split(",")
		(order_id,order_date,status,customer_id,email,address,city,state,postalcode,
			num_watermelons,num_othermelons,subtotal,tax,order_total) = data

		query = """INSERT INTO orders (customer_id, status, shipto_postalcode,
			num_watermelons, num_othermelons,
			subtotal, order_total)
			VALUES (?,?,?,?,?,?,?)"""

		DB.execute(query, (customer_id, status, postalcode,
			num_watermelons, num_othermelons, subtotal, order_total))

	CONN.commit()
	f.close()

def main():
	connect_to_db()
	# make_customer_table()
	# populate_customer_table()
	# make_orders_table()
	populate_orders_table()
	CONN.close()


if __name__ == "__main__":
	main()



