import json

#   Data Base Functions - dbf
def read_database():
    with open('domains_data.json', 'r') as file:
        data = file.readlines()
        file.close()
        return data

def write_database(json_data):
    with open('domains_data.json', 'a') as file:
        file.write(str(json.dumps(json_data)) + '\n')
        file.close()
