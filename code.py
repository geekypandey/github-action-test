import os
import json

import requests

def read_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename) as f:
        data = json.load(f)['data']
    return data

def get_unprocessed(cur_data, indices):
    for index in indices:
        if not any(d['id'] == index for d in cur_data):
            yield index

if __name__ == '__main__':
    indices = [1, 2]
    cur_data = read_file('data.json')
    url = "https://my-json-server.typicode.com/typicode/demo/comments/"
    data = []
    for index in get_unprocessed(cur_data, indices):
        endp = url + str(index)
        res = requests.get(endp)
        res = res.json()
        data.append(res)
        print(index, 'Done')

    data = cur_data + data
    json_data = {
        "data": data
    }
    with open('data.json', 'w') as f:
        json.dump(json_data, f)

