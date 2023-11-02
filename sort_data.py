items_from_DynamoDB = [
    {'updated_at': {'S': '2021-03-27T17:33:14.071Z'}, 'created_at': {'S': '2021-03-27T17:33:14.071Z'}, 'id': {'N': '3'},
    'url': {'S': 'https://wind-reliability-server.animal-hospital.mkrs.link/hospitals/3.json'}, 'name': {'S': "Jim's Hospital"}},
    {'updated_at': {'S': '2021-03-27T17:33:14.066Z'}, 'created_at': {'S': '2021-03-27T17:33:14.066Z'}, 'id': {'N': '2'},
    'url': {'S': 'https://wind-reliability-server.animal-hospital.mkrs.link/hospitals/2.json'}, 'name': {'S': 'Colchester General'}},
    {'updated_at': {'S': '2023-10-17T08:51:00.113Z'}, 'created_at': {'S': '2023-10-17T08:51:00.113Z'}, 'id': {'N': '9'},
    'url': {'S': 'https://wind-reliability-server.animal-hospital.mkrs.link/hospitals/9.json'}, 'name': {'S': 'Nice Hospital'}},
    {'updated_at': {'S': '2021-03-27T17:33:14.075Z'}, 'created_at': {'S': '2021-03-27T17:33:14.075Z'}, 'id': {'N': '4'},
    'url': {'S': 'https://wind-reliability-server.animal-hospital.mkrs.link/hospitals/4.json'}, 'name': {'S': 'Third Avenue'}},
    {'updated_at': {'S': '2023-10-18T09:09:20.706Z'}, 'created_at': {'S': '2023-10-16T20:34:58.223Z'}, 'id': {'N': '6'},
    'url': {'S': 'https://wind-reliability-server.animal-hospital.mkrs.link/hospitals/6.json'}, 'name': {'S': "Denise's Hospital"}},
    {'updated_at': {'S': '2021-03-27T17:33:14.049Z'}, 'created_at': {'S': '2021-03-27T17:33:14.049Z'}, 'id': {'N': '1'},
    'url': {'S': 'https://wind-reliability-server.animal-hospital.mkrs.link/hospitals/1.json'}, 'name': {'S': 'Root'}},
    {'updated_at': {'S': '2023-10-16T19:57:41.109Z'}, 'created_at': {'S': '2023-10-16T18:34:56.042Z'}, 'id': {'N': '5'},
    'url': {'S': 'https://wind-reliability-server.animal-hospital.mkrs.link/hospitals/5.json'}, 'name': {'S': 'Updated Hospital'}}
]


def format_data(dynamo_list):
    return [{
        'id':item['id']['N'],
        'name':item['name']['S'],
        'created_at':item['created_at']['S'],
        'updated_at':item['updated_at']['S'],
        'url':item['url']['S']
    } for item in dynamo_list]


formatted_data = format_data(items_from_DynamoDB)
for item in formatted_data:
    print(item)
