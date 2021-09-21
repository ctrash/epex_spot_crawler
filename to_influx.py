from influxdb import InfluxDBClient
import json
import datetime, time
import re

#---- Config InfluxDB Connection
host = '167.71.56.97'
port = '8086'
user = 'admin'
password = 'P@ssw0rd'
dbname = 'biogas'
dbuser = 'admin'
dbuser_password = 'P@ssw0rd'
#---- InfluxDB Connection

client = InfluxDBClient(host, port, user, password, dbname)


#readtime = datetime.datetime(2021, 9, 14)
readtime =datetime.datetime.now()

date_f = str(readtime.strftime("%Y-%m-%d"))
# Opening JSON file
f = open('tutorial/data/json/'+date_f+'.json',)

# returns JSON object as
# a dictionary
data = json.loads(f.read())

# Closing file
f.close()

i = 0
while i < len(data):
    #print(i)
  
    #
    #print(len(data))
    hour_read= re.search(r'\d+', data[i]["hours"]).group()
    new_datetime = readtime.replace(hour=int(hour_read), minute=0,second=0,microsecond=0)
    print(new_datetime)
    print(float(data[i]["price"]))
    json_body = [
            {
            "measurement": "epex",
            "tags": {
                "name": "spotprice"
            },
            "time": new_datetime,
            "fields": {
                "Preis": float(data[i]["price"]),
                "buy_volume": float(str(data[i]["buy_volume"]).replace(',','')),
                "sell_volume": float(str(data[i]["sell_volume"]).replace(',','')),
                "volume": float(str(data[i]["volume"]).replace(',','')),
                }
            }
        ]
    client.write_points(json_body)
    #print(json_body)
    
    i += 1
print('InfluxDB done')