from taosrest import RestClient

db = "power"

client = RestClient(url='http://124.70.89.186:6041',
                             user='root',
                             password='taosdata',
                             database='ht2_data')

result = client.sql(f"SELECT * from {db}.meters")
print(result)

