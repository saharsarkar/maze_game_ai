
import random
import json


dic = {}
walls = [tuple([random.randint(0, 19), random.randint(0, 19)])
         for i in range(random.randint(10, 100))]

for row in range(1, 21):
    arr = []
    for col in range(20):
        arr.append({'id': col + 1, 'x': 20 - row, 'y': col,
                    'color': 'black' if walls.__contains__((row, col)) else 'white'})
    dic[f'row{row}'] = arr

with open('grid.json', mode='w') as file:
    file.write(json.dumps(dic))
