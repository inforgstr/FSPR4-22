import json
import csv

# 2 модуля для сериализации объектов в питоне

compromised_users = []

with open("passwords.csv", encoding="utf-8") as passwords:
    reader = csv.DictReader(passwords)

    for row in reader:
        compromised_users.append(row)

with open("file.txt", "w") as file_txt:
    for user in compromised_users:
        name = user["Username"]
        password = user["Password"]
        s = f"Name - {name}, Password - {password}\n"
        file_txt.write(s)


with open("boss_message.json", encoding="utf-8", mode="w") as boss_message_json:
    message = {
        "recipient": "The Boss",
        "message": "Mission Success",
    }
    json.dump(message, boss_message_json, indent=4)


hacked_text = r"""
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

with open("new_passwords.txt", "w", encoding="utf-8") as new_passwords:
    new_passwords.write(hacked_text)
