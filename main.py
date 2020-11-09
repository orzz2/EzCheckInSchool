import time
import json
import requests
import random
import datetime
# sectets字段录入
areaStr = input()
customerid = input()
deptid = input()
emergencyContact = input()
mergencyPeoplePhone = input()
ownPhone = input()
phonenum = input()
reportdate = input()
sckey = input()
stuNo = input()
TEXT = input()
token = input()
userid = input()
username = input()
#时间设置
a=time.time()
bbb=int(round(a*1000)+28800000)

sign_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"

jsons = {
		"businessType": "epmpics",
	"method": "submitUpInfo",
	"jsonData": {
		"add": false,
		"areaStr":areaStr,
		"cardNo": null,
		"customerid": customerid,
		"deptStr": {
			"deptid": deptid,
			"text": TEXT
		},
		"phonenum": phonenum,
		"stuNo": stuNo,
		"templateid": "pneumonia",
		"upTime": null,
		"userid": userid,
		"username":username,
		"deptid": deptid,
		"updatainfo": [
			{
				"propertyname": "wendu",
				"value": "36.4"
			},
			{
				"propertyname": "symptom",
				"value": "无症状"
			},
			{
				"propertyname": "jkzks",
				"value": "正常"
			},
			{
				"propertyname": "jtcy",
				"value": "否"
			},
			{
				"propertyname": "SFJCQZHYS",
				"value": "否"
			},
			{
				"propertyname": "sfddgr",
				"value": "否"
			},
			{
				"propertyname": "isTouch",
				"value": "否"
			},
			{
				"propertyname": "是否途径或逗留过疫情中，高风险地区？",
				"value": ""
			},
			{
				"propertyname": "isAlreadyInSchool",
				"value": "没有"
			},
			{
				"propertyname": "hsjc0511",
				"value": "否"
			},
			{
				"propertyname": "ownPhone",
				"value": ownPhone
			},
			{
				"propertyname": "emergencyContact",
				"value": emergencyContact
			},
			{
				"propertyname": "mergencyPeoplePhone",
				"value": mergencyPeoplePhone
			}
		],
		"source": "app",
		"reportdate": bbb,
		"gpsType": 0,
		"token": token
	},
}
# 提交打卡
response = requests.post(sign_url, json=jsons)
utcTime = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
cstTime = utcTime.strftime("%H时%M分%S秒")
print(response.text)
# 结果判定
if response.json()["msg"] == '成功':
    msg = cstTime + "打卡成功"
else:
    msg = cstTime + "打卡异常"
print(msg)
# 微信通知

title = msg
result = json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
content = f"""
```
{result}
```

"""
data = {
    "text": title,
    "desp": content
}
req = requests.post(sckey, data=data)
