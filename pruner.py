import json

with open('baby_names.txt') as json_file:
    data =json.load(json_file)
    check=['Gary', 'Aaron', 'Luke', 'Winston', 'Avery']

    for key in list(data['top'].keys()):
        if key.find('v')!=-1:
            data['top'].pop(key)

    for key in check:
        if key in list(data['top'].keys()):
            data['top'].pop(key)
    
    for key in list(data['top'].keys()):
        if data['top'].get(key) == '28':
            data['top'].pop(key)

    data['top']['Ron']='5'
    formatted_obj = json.dumps(data, indent=4)
    with open('better_names.txt', mode='w') as outfile:
        outfile.write(formatted_obj)


