import sqlite3, random,json

conn = sqlite3.connect('distanceSensorDataDatabase.db')
print ("Opened database successfully");

ok = random.randint(1, 2001)
ok2 = random.uniform(1, 2001)
ok3 = random.randint(1, 2001)
ok4 = random.randint(1, 2001)

# conn.execute('CREATE TABLE distanceSensorData (ID INT PRIMARY KEY NOT NULL,sensorName TEXT, sensorType TEXT, realData REAL, roundedData INTEGER)')
conn.execute(f"INSERT INTO distanceSensorData (ID, sensorName, sensorType, realData, roundedData) \
    VALUES ({ok3}, 'd boi', 'HC{ok4} whatevver', {ok2}, {ok})")
# print ("Table created successfully");
print ("Table updated");


cursor = conn.execute("SELECT ID, sensorName, sensorType, realData, roundedData from distanceSensorData")
for row in cursor:
   print(json.dumps({"ID":row[0],"sensorName":row[1],"sensorType":row[2], "realData":row[3],"roundedData":row[4] }))
print ("Operation done successfully")
conn.commit()
conn.close()