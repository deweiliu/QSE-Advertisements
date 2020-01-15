from dynamoDB import *
from read import read
table = get_table('Advertisement')
data = read('Companies.csv')
for each in data:
    print(each)
    table.put_item(Item=each)
