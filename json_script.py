import sqlite3
import json


conn = sqlite3.connect('webapp.db')
cursor = conn.cursor()


cursor.execute('SELECT id, name, category, service_description, promo FROM web_app')
data = cursor.fetchall()


conn.close()

result = []

for row in data:


    id, name, category, service_description, promo = row
    if id == 0:
        continue
    result.append({
        'id': id,
        'name': name,
        'category': category,
        'description': service_description,
        'promo': promo
    })

with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, ensure_ascii=False, indent=4)

