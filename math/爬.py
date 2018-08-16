import wechatsogou
import time

ws_api =wechatsogou.WechatSogouAPI()
res=ws_api.get_gzh_article_by_history('清华大学学生社团')
count=1
print("公众号：  ",res['gzh']['wechat_name'])
print("公众号简介：  ",res['gzh']['introduction'])
for i in res['article']:
    print("记录",count)
    count+=1
    print("标题:  ",i['title'])
    print('摘要:  ',i['abstract'])
    t=i['datetime']
    time_local = time.localtime(t)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    print('时间:  ',dt,"\n")
    if count>9:
        break

res=ws_api.get_gzh_article_by_history('新清华学堂')

count=1
print("公众号：  ",res['gzh']['wechat_name'])
print("公众号简介：  ",res['gzh']['introduction'])
for i in res['article']:
    print("记录",count)
    count+=1
    print("标题:  ",i['title'])
    print('摘要:  ',i['abstract'])
    t=i['datetime']
    time_local = time.localtime(t)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    print('时间:  ',dt,"\n")
    if count>9:
        break

res=ws_api.get_gzh_article_by_history('清华大学学生会')

count=1
print("公众号：  ",res['gzh']['wechat_name'])
print("公众号简介：  ",res['gzh']['introduction'])
for i in res['article']:
    print("记录",count)
    count+=1
    print("标题:  ",i['title'])
    print('摘要:  ',i['abstract'])
    t=i['datetime']
    time_local = time.localtime(t)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    print('时间:  ',dt,"\n")
    if count>9:
        break