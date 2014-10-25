import sqlite3



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



def main():


if __name__ == "__main__":
	main()



