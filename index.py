from main import Cymon
import json
import csv
api = Cymon('8d839c293762a7fe740d39decd0c86688f56489e')
blacklist = [
	'malware',
	'botnet',
	'c2',
	'zombie',
	'phishing',
	'malvertising',
	'ek',
	'scan',
	'bruteforce',
	'proxy',
	'tor',
	'vpn',
	'malicious activity',
	'blacklist',
	'dnsbl'
	]
'''
start=0
end=1000
'''
start=310
end=start+20
for count in range(start,end,10):
	startnumber=str(count)
	print('\tATTACK:RANSOMWARE')
	#'ransomware',
	#reading the previous ips
	txtfile=open('TXT/ransomware.txt','r')
	text=txtfile.read()
	olditems=text.split()
	newitems=[]
	txtfile.close()



	z=api.ip_blacklist('ransomware',startnumber)


	#json writer
	'''
	jsonfile=open('JSON/ransomware.json','a')
	jsonfile.write(str(z))
	jsonfile.close()'''


	#finding the new ips
	for i in range(len(z['hits'])):
		if 'ip' in z['hits'][i]['ioc'].keys():
			ip=str(z['hits'][i]['ioc']['ip'])
			if ip not in olditems:
				print("\t\t"+str(ip))
				newitems.append(ip)#only when not present in the old items
	#only if new items were added
	if(len(newitems)>0):
		txtfile=open('TXT/ransomware.txt','a')
		for i in newitems:
			txtfile.write(str(i)+"\n")
		txtfile.close()
	#----------------------------------------
	#for the entire list
	for attack in blacklist:

		
		print("\tATTACK:"+attack.upper())
			
		#reading the previous ips
		txtfile=open('TXT/'+attack+'.txt','r')
		text=txtfile.read()
		olditems=[]
		olditems=text.split()
		newitems=[]
		txtfile.close()

		
		z = api.ip_blacklist(attack,startnumber)

		#JSON Writer
		'''
		jsonfile=open('JSON/'+attack+'.json','a')
		jsonfile.write(str(z))
		jsonfile.close()
		'''

		
		#finding the new ips
		for j in range(len(z['hits'])):
			if 'ip' in z['hits'][j]['ioc'].keys():
				ip=str(z['hits'][j]['ioc']['ip'])
				if ip not in olditems:
					print("\t\t"+str(ip))
					newitems.append(ip)
			
		
		# only if new items were added
		if(len(newitems)>0):
			txtfile = open('TXT/'+attack+'.txt','a')
			for i in newitems:
				txtfile.write(str(i)+"\n")
			txtfile.close()

print("You are done Boss\n");




