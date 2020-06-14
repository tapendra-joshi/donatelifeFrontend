import pprint
from services.get_all_blood_banks import blood_bank_by_city

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(blood_bank_by_city('Anantapur'))
# data = {
# 	"email":"tapendra2497@gmail.com",
# 	"password":"QWERTY"
# }
# 	"first_name":"Tapendra",
# 	"last_name":"Joshi",
# 	"sex":"MALE",
# 	"blood_group":"A+",
# 	"city":"Narnaul",
# 	"state":"Haryana",
# 	"birth_date":"1997-04-24"
# }
# resp = login_user(data)
# print(resp)
# if resp["data"]:
#     print("decoded")
# else:
#     print("123456ytrewq")
