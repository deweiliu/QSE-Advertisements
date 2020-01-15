import csv
def get_value(row,index):
    value=row[index]
    if(value==''):
        value='N/A'
    return value

def read(file_name):
    records = list()
    with open(file_name) as f:
        data = csv.reader(f, delimiter=',')
        for row in data:
            record = dict()
            record['Advertiser'] = get_value(row,1)
            record['URL'] = get_value(row,2)
            record['industry'] = get_value(row,3)
            records.append(record)

    return records


