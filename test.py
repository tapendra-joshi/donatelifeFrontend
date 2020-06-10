import pprint
from services.login_service import login_user

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(get_all_blood_banks())
data = {
	"email":"tapendra2497@gmail.com",
	"password":"QWERTY"
}
# 	"first_name":"Tapendra",
# 	"last_name":"Joshi",
# 	"sex":"MALE",
# 	"blood_group":"A+",
# 	"city":"Narnaul",
# 	"state":"Haryana",
# 	"birth_date":"1997-04-24"
# }
resp = login_user(data)
print(resp)
# if resp["data"]:
#     print("decoded")
# else:
#     print("123456ytrewq")