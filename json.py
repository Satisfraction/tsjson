import json

with open('tsjson/accounts.json') as user_file:
  file_contents = user_file.read()
  
print(file_contents)