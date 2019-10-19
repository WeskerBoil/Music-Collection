import requests
import re
import time
'''
第一步分析网页url

第一页
http://www.htqyy.com/genre/musicList/1?pageIndex=0&pageSize=20
第二页：
http://www.htqyy.com/genre/musicList/1?pageIndex=1&pageSize=20
第三页
http://www.htqyy.com/genre/musicList/1?pageIndex=2&pageSize=20
'''

#歌曲播放url   http://www.htqyy.com/play/33
# 歌曲资源所在网页 http://f2.htqyy.com/play7/33/mp3/10

page=int(input("请输入您要下载的页数:"))
songID=[]
songName=[]

for i in range(0,page):
	url="http://www.htqyy.com/genre/musicList/1?pageIndex="+str(i)+"&pageSize=20"
	#获取网页音乐信息
	html=requests.get(url)
	strr=html.text

	pat1=r'title="(.*?)" sid'
	pat2=r'sid="(.*?)"'
	idlist=re.findall(pat2,strr)
	titlelist=re.findall(pat1,strr)
	songID.extend(idlist)
	songName.extend(titlelist)
	#print(songID)
	#print(songName)
for i in range(0,len(songID)):
	songurl="http://f2.htqyy.com/play7/"+str(songID[i])+"/mp3/10"
	songname=songName[i]
	data=requests.get(songurl).content
	print("正在下载第",i+1,)

	with open('D:\\music\\{}.mp3'.format(songname),"wb") as f:
		f.write(data)
		time.sleep(1)




