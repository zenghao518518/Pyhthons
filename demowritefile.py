import requests

res = requests.get("http://www.10086.cn/support/selfservice/help/sh/5010801_4073_8801.json")
data_dict = res.json()
data_list = data_dict["cData"]['list']
f = open("news.csv", mode='a', encoding='utf-8')
for item in data_list:
    question = item['question']
    up_time = item['up_time']
    id = item['_orderId']
    print(up_time, id, question)
    line = "{},{},{}\n".format(up_time, id, question)
    f.write(line)
f.close()
