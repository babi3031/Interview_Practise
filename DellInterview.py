# a = {
#     "_id": "D9023",
#     "hashVersion": 2,
#     "isOnline": False,
#     "name": "KUNTAL-WES-LAPT",
#     "missingQFEUpdates": [
#         {
#             "categories": "Updates, Windows 10 Feature On Demand, ",
#             "hotfixID": "3180030",
#             "urls": [
#                 "http://support.microsoft.com/kb/3180030"
#             ]
#         }
#     ]
# }
#
# # New URL to replace the existing one
# new_url = "http://example.com/newurl"
#
# a["missingQFEUpdates"][0]["urls"].append(new_url)
#
# # Update the URL in the dictionary
# if a.get("missingQFEUpdates"):
#     for update in a["missingQFEUpdates"]:
#         if "urls" in update:
#             update["urls"].append(new_url)
#
# print(a)

import json

# JSON string
json_string = '{"name": "John", "age": 30, "isStudent": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zip": "10001"}}'
print(json_string)
print(type(json_string))
# Convert JSON string to Python dictionary
data = json.loads(json_string)
print(data)
print(type(data))

# Convert Python dictionary to JSON string
json_data = json.dumps(data)
print(json_data)
print(type(json_data))
