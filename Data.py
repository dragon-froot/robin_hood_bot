import pymysql 

db = pymysql.connect("127.0.0.1", 'root', 'password', 'DayTradingBot')

cursor = db.cursor()

# Drop table if it already exists in execute() method
# cursor.execute("DROP TABLE IF EXISTS current_holdings")

sql = """
        CREATE TABLE current_holdings (
            symbol CHAR(20) NOT NULL,
            avg_buy_price FLOAT NOT NULL,
            quantity FLOAT,
            profit FLOAT NOT NULL
        )
      """

cursor.execute(sql)