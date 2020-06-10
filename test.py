import pprint
from services.get_all_blood_banks import get_all_blood_banks

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(get_all_blood_banks(page=2))
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
