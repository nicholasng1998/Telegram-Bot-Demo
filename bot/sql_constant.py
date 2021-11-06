USER_TABLE = '''
CREATE TABLE IF NOT EXISTS "User" (
"user_id"	INTEGER,
"name"	TEXT,
"address"	TEXT,
PRIMARY KEY("user_id" AUTOINCREMENT)
)
'''

ORDER_TABLE = '''
CREATE TABLE IF NOT EXISTS "Order" (
"order_id"	TEXT,
"item_json"	BLOB,
"user_id"	INTEGER,
PRIMARY KEY("order_id"),
FOREIGN KEY("user_id") REFERENCES "User"("user_id")
)
'''

INSERT_USER = '''
INSERT INTO USER(name, address, chat_id)
VALUES("{}", {}, {});
'''

SELECT_USER = '''
SELECT * from USER
WHERE chat_id = {};
'''
