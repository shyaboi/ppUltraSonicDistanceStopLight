import sqlite3, random,json
conn = sqlite3.connect('distanceSensorDataDatabase.db')
print ("Opened database successfully");



conn.execute('CREATE TABLE distanceSensorData (ID INT PRIMARY KEY NOT NULL,sensorName TEXT, sensorType TEXT, realData REAL, roundedData INTEGER)')
def insertData(data):
    ok = random.randint(1, 2001)
    ok2 = data
    ok3 = random.randint(1, 2001)
    ok4 = random.randint(1, 2001)
    conn.execute(f"INSERT INTO distanceSensorData (ID, sensorName, sensorType, realData, roundedData) \
        VALUES ({ok3}, 'd boi', 'HC{ok4} whatevver', {data}, {ok})")
# print ("Table created successfully");
print ("Table updated");


cursor = conn.execute("SELECT ID, sensorName, sensorType, realData, roundedData from distanceSensorData")
def thging():
    dumpArr = []
    for row in cursor:
        termp = json.dumps([row].copy())
        dumpArr.insert(len(dumpArr), termp)
        # ok=json.dumps({"ID":row[0],"sensorName":row[1],"sensorType":row[2], "realData":row[3],"roundedData":row[4] })
    return dumpArr
print(thging())
print ("Operation done successfully")
conn.commit()