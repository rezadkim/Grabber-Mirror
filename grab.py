#!/usr/bin/python
import requests, sys, re, os, time, random
from bs4 import BeautifulSoup

#################
#     Warna	#
#################
green = ("\33[0;32m") #Green
greenl = ("\33[32;1m") #GreenLight
blue = ("\33[0;36m") #Blue
bluel = ("\33[36;1m") #BlueLight
red = ("\33[31;1m") #Red
white = ("\33[37;1m") #White
black = ("\33[30;1m") #Black
yellow = ("\33[33;1m") #Yellow
yellowl = ("\33[1;33m") #YellowLight

res = requests.Session();
def sampah():
	if os.path.exists("sampah"):
		pass
	else:
		os.mkdir("sampah")

def file_archive():
	if os.path.exists("sampah/archive.txt"):
		if os.path.getsize("sampah/archive.txt") !=0:
			print(white+"["+red+"!"+white+"] File Exists : "+blue+"sampah/archive.txt")
			cek = raw_input(white+"["+green+"?"+white+"] Append ID ("+green+"y"+white+"/"+green+"n"+white+"): ")
			if cek.lower() !="y":
				print(white+"["+green+">"+white+"] Output : "+blue+"sampah/archive.txt")
				open("sampah/archive.txt","w").close()
			else:
				print(white+"["+green+">"+white+"] Output : "+blue+"sampah/archive.txt")
		else:
			open("sampah/archive.txt","w").close()
	else:
		print(white+"["+green+">"+white+"] Output : "+blue+"sampah/archive.txt")
		open("sampah/archive.txt","w").close()
def file_archive_star():
	if os.path.exists("sampah/archive_star.txt"):
		if os.path.getsize("sampah/archive_star.txt") !=0:
			print(white+"["+red+"!"+white+"] File Exists : "+blue+"sampah/archive_star.txt")
			cek = raw_input(white+"["+green+"?"+white+"] Append ID ("+green+"y"+white+"/"+green+"n"+white+"): ")
			if cek.lower() !="y":
				print(white+"["+green+">"+white+"] Output : "+blue+"sampah/archive_star.txt")
				open("sampah/archive_star.txt","w").close()
			else:
				print(white+"["+green+">"+white+"] Output : "+blue+"sampah/archive_star.txt")
		else:
			open("sampah/archive_star.txt","w").close()
	else:
		print(white+"["+green+">"+white+"] Output : "+blue+"sampah/archive_star.txt")
		open("sampah/archive_star.txt","w").close()
def file_onhold():
	if os.path.exists("sampah/onhold.txt"):
		if os.path.getsize("sampah/onhold.txt") !=0:
			print(white+"["+red+"!"+white+"] File Exists : "+blue+"sampah/onhold.txt")
			cek = raw_input(white+"["+green+"?"+white+"] Append ID ("+green+"y"+white+"/"+green+"n"+white+"): ")
			if cek.lower() !="y":
				print(white+"["+green+">"+white+"] Output : "+blue+"sampah/onhold.txt")
				open("sampah/onhold.txt","w").close()
			else:
				print(white+"["+green+">"+white+"] Output : "+blue+"sampah/onhold.txt")
		else:
			open("sampah/onhold.txt","w").close()
	else:
		print(white+"["+green+">"+white+"] Output : "+blue+"sampah/onhold.txt")
		open("sampah/onhold.txt","w").close()
def file_notifier():
	if os.path.exists("sampah/notifier.txt"):
		if os.path.getsize("sampah/notifier.txt") !=0:
			print(white+"["+red+"!"+white+"] File Exists : "+blue+"sampah/notifier.txt")
			cek = raw_input(white+"["+green+"?"+white+"] Append ID ("+green+"y"+white+"/"+green+"n"+white+"): ")
			if cek.lower() !="y":
				print(white+"["+green+">"+white+"] Output : "+blue+"sampah/notifier.txt")
				open("sampah/notifier.txt","w").close()
			else:
				print(white+"["+green+">"+white+"] Output : "+blue+"sampah/notifier.txt")
		else:
			open("sampah/notifier.txt","w").close()
	else:
		print(white+"["+green+">"+white+"] Output : "+blue+"sampah/notifier.txt")
		open("sampah/notifier.txt","w").close()


#########################################
#		ZONE-H			#
#########################################
def main_zoneh():
	global heder_zoneh
	cookie = raw_input(white+"["+bluel+"+"+white+"] Cookie :"+greenl+"> "+white)
	heder_zoneh = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate','Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Connection': 'keep-alive','Cookie': cookie,'Host': 'zone-h.org','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
	zoneh()

def zoneh():
	os.system("clear")
	print(white+"		[ "+red+"Zone"+white+"-"+red+"H "+white+"]	")
	print(white+"		[ "+green+"https://github.com/rezadkim"+white+"]	")
	print(green+"{"+white+"01"+green+"}"+white+" Archive")
	print(green+"{"+white+"02"+green+"}"+white+" Archive Star")
	print(green+"{"+white+"03"+green+"}"+white+" Onhold")
	print(green+"{"+white+"04"+green+"}"+white+" Notifier")
	print(red+"{"+white+"05"+red+"}"+white+" Exit")
	zoneh_choose = raw_input("\n"+white+"["+green+"+"+white+"] Select From : "+green)
	if zoneh_choose=="1":
		sampah()
		file_archive()
		print(white+"["+bluel+"%"+white+"] Starting ...\n")
		time.sleep(02)
		zoneh_archive()
	elif zoneh_choose=="2":
		sampah()
		file_archive_star()
		print(white+"["+bluel+"%"+white+"] Starting ...\n")
		time.sleep(02)
		zoneh_archive_star()
	elif zoneh_choose=="3":
		sampah()
		file_onhold()
		print(white+"["+bluel+"%"+white+"] Starting ...\n")
		time.sleep(02)
		zoneh_onhold()
	elif zoneh_choose=="4":
		sampah()
		file_notifier()
		notf = raw_input(white+"["+green+"+"+white+"] Attacker : "+green)
		print(white+"["+bluel+"%"+white+"] Starting ...\n")
		time.sleep(02)
		zoneh_notifier(notf)
	else:
		exit()

def zoneh_archive():
	for jml in range(1, 51):
		page = res.get("http://www.zone-h.org/archive/page="+str(jml), headers=heder_zoneh).text
		if '<html><body>-<script type="text/javascript"' in page:
				print(white+"["+red+"!"+white+"] Ganti Cookie :*")
		elif '<input type="text" name="captcha" value=""><input type="submit">' in page:
				print(white+"["+red+"!"+white+"] Ganti Cookie :*")
		else:
			fix = re.findall('<td>(.*)\n							</td>', page)
			soup = BeautifulSoup((res.get("http://www.zone-h.org/archive/page="+str(jml), headers=heder_zoneh)).text, "html.parser")
			for qwe in soup.find_all('a',href=True):
				for cek in fix:
					hasil = cek
					if "/archive/notifier" in qwe['href']:
						jembod = (qwe['href']).replace("/archive/notifier=","")
						print(white+'Result > '+green+ hasil.split('/')[0] +" = "+blue+jembod)
						with open ("sampah/archive.txt", "a") as sv:
							sv.write(hasil.split('/')[0]+"\n")
					else:
						pass
	print(white+"\n["+greenl+"./"+white+"] Saved : "+blue+"sampah/archive.txt")
	os.sys.exit()

def zoneh_archive_star():
	for jml in range(1, 51):
		page = res.get("http://www.zone-h.org/archive/special=1/page="+str(jml), headers=heder_zoneh).text
		if '<html><body>-<script type="text/javascript"' in page:
				print(white+"["+red+"!"+white+"] Ganti Cookie :*")
		elif '<input type="text" name="captcha" value=""><input type="submit">' in page:
				print(white+"["+red+"!"+white+"] Ganti Cookie :*")
		else:
			fix = re.findall('<td>(.*)\n							</td>', page)
			soup = BeautifulSoup((res.get("http://www.zone-h.org/archive/special=1/page="+str(jml), headers=heder_zoneh)).text, "html.parser")
			for qwe in soup.find_all('a',href=True):
				for cek in fix:
					hasil = cek
					if "/archive/special=1/notifier" in qwe['href']:
						jembod = (qwe['href']).replace("/archive/special=1/notifier=","")
						print(white+'Result > '+green+ hasil.split('/')[0] +" = "+blue+jembod)
						with open ("sampah/archive_star.txt", "a") as sv:
							sv.write(hasil.split('/')[0]+"\n")
					else:
						pass
	print(white+"\n["+greenl+"./"+white+"] Saved : "+blue+"sampah/archive_star.txt")
	os.sys.exit()

def zoneh_onhold():
	for jml in range(1, 51):
		page = res.get("http://www.zone-h.org/archive/published=0/page="+str(jml), headers=heder_zoneh).text
		if '<html><body>-<script type="text/javascript"' in page:
				print(white+"["+red+"!"+white+"] Ganti Cookie :*")
		elif '<input type="text" name="captcha" value=""><input type="submit">' in page:
				print(white+"["+red+"!"+white+"] Ganti Cookie :*")
		else:
			fix = re.findall('<td>(.*)\n							</td>', page)
			soup = BeautifulSoup((res.get("http://www.zone-h.org/archive/published=0/page="+str(jml), headers=heder_zoneh)).text, "html.parser")
			for qwe in soup.find_all('a',href=True):
				for cek in fix:
					hasil = cek
					if "/archive/notifier" in qwe['href']:
						jembod = (qwe['href']).replace("/archive/notifier=","")
						print(white+'Result > '+green+ hasil.split('/')[0] +" = "+blue+jembod)
						with open ("sampah/onhold.txt", "a") as sv:
							sv.write(hasil.split('/')[0]+"\n")
					else:
						pass
	print(white+"\n["+greenl+"./"+white+"] Saved : "+blue+"sampah/onhold.txt")
	os.sys.exit()

def zoneh_notifier(nama):
	for jml in range(1, 51):
		page = res.get("http://www.zone-h.org/archive/notifier="+nama+"/page="+str(jml), headers=heder_zoneh).text
		if '<html><body>-<script type="text/javascript"' in page:
				print(white+"["+red+"!"+white+"] Ganti Cookie :*")
		elif '<input type="text" name="captcha" value=""><input type="submit">' in page:
				print(white+"["+red+"!"+white+"] Ganti Cookie :*")
		else:
			fix = re.findall('<td>(.*)\n							</td>', page)
			if '/mirror/id/' in page:
				for xx in fix:
					qqq = xx.replace('...','')
					print(white+'Result > '+green+qqq.split('/')[0])
					with open('sampah/notifier.txt', 'a') as sv:
						sv.write("http://"+qqq.split('/')[0] + '\n')
			else:
				print(white+"\n["+greenl+"./"+white+"] Saved : "+blue+"sampah/notifier.txt")
				os.sys.exit()
	print(white+"\n["+greenl+"./"+white+"] Saved : "+blue+"sampah/notifier.txt")
	os.sys.exit()

main_zoneh()
