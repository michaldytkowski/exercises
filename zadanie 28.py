import json

def filter_active_users():
    data =[]
    with open('users.json', 'r') as f:
        json_data = json.loads(f.read())
        for item in json_data:
            #print(item['is_active'])
            if item['is_active'] == True:
                data.append(item)
    json_string = json.dumps(data, indent=2)
    with open('active_users.json', 'w') as f:
        f.write(json_string)




filter_active_users()