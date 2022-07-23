import os
import json

DIR = "files"
python_data = [{"name": "John", "age": 18},{"name": "John", "age": 25}]

with open(os.path.join(DIR, 'users.json'), 'w', encoding="UTF-8") as f:
   json.dump(python_data, f, ensure_ascii=False)

with open(os.path.join(DIR, 'users.json'), 'r', encoding="UTF-8") as f:
   read_data = json.load(f)

print(read_data[0]['name'])

