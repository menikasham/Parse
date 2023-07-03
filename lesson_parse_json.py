import requests
import pprint

all_dict = {'watch': 0, 'mobile': 0, 'mouse': 0, 'hdd': 0, 'headphones': 0}
url = 'http://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url).json()


# for key in all_dict.keys():
#     for item in response:
#         if item["categories"] == key:
#             all_dict[key] += int(item["count"])
# print(all_dict)
#
#
# result = {}
# for item in response:
#     result[item['categories']] = result.get(item['categories'],0) + int(item['count'])
# print(result)


result = {}
for item in response:
    result[item['categories']] = result.get(item['categories'],0) + (int(item['price'].split()[0]) * int(item['count']))
print(result)

for key in all_dict.keys():
    for item in response:
        if item["categories"] == key:
            all_dict[key] += int(item['price'].split()[0])
print(all_dict)