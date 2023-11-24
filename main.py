import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + Fore.GREEN +'토큰 만들기 시작중...'+i)
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()

banner = (Fore.WHITE +Fore.RED +"["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]\n"+ 
Fore.WHITE +Fore.RED +'''\n  








                                 
' \n\n'''+ Fore.RESET + Fore.WHITE +Fore.RED +" ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]\n")

count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
	
print(Fore.WHITE +Fore.RED +"                                                            ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
print(Fore.WHITE +Fore.RED +"-\토큰 생성기에 오신것을"+Fore.BLUE+" 환영합니다! -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-")
print(Fore.WHITE +Fore.RED +"-\ [1] "+Fore.BLUE+"토큰 생성 \-")
print(Fore.WHITE +Fore.RED +"-\ [2] "+Fore.BLUE+"토큰 확인 \-")
print(Fore.WHITE +Fore.RED +"-\ [3] "+Fore.BLUE+"크레딧 \-")
print(Fore.WHITE +Fore.RED +"-\ [4] "+Fore.BLUE+"나가기 \-")
print(Fore.WHITE +Fore.RED +"                                                                                              ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
opcion = input("\n번호 선택: ")
if opcion=='1':
	print(banner)
	cantidad = input("\n토큰 갯수: ")
	while int(count)<int(cantidad):
		Generated = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
		f= open(current_path +"/"+str("Generated")+str("")+".txt","a")
		f.write(Generated+"\n")
		print(Fore.GREEN +"토큰: "+ Fore.RESET + Generated)
		count+=1
		if int(count)==int(cantidad):
			print("\n" + Fore.CYAN +Fore.RED +"토큰 만들기 성공!")
			print(Fore.WHITE +Fore.RED +"Generated.txt에 저장 되었습니다.")
			input(Fore.RED +Fore.RED +"\n엔터키를 눌러 나가기")
			os.system("cls")
			print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
			print(Fore.RED +Fore.RED +"                                                   토큰 만들기 닫기...")
			print(Fore.GREEN +Fore.RED +"                                               륨인 유튜브 구독!")
			print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
			time.sleep(2)
			sys.exit()
			pass
	pass
if opcion=='2':
	os.system("cls")
	print("\n" + banner + "\n")
	with open('Generated.txt', 'r') as f:
	    for line in f:
	        time.sleep(0)
	        token = line.rstrip("\n")
	        headers = {
	            'Authorization': f'{token}'  
	        }
	        src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

	        try:
	            if src.status_code == 200:
	                print(f'{Fore.RED}Invalid token >{Fore.RESET} ' + token)
	            else:
	                print(f'{Fore.LIGHTGREEN_EX}만든 토큰 >{Fore.RESET} ' + token)
	        except Exception:
	            print(f"{Fore.CYAN}E에러, 관리자에게 문의 하세요! {Fore.RESET}")
pass
if opcion=='3':
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.WHITE +Fore.RED +"                                         토큰 생성"+Fore.YELLOW+" Made by "+Fore.RED+"륨인")
	print(Fore.WHITE +Fore.RED +"                                         [디스코드] "+Fore.GREEN+"lumin21#5080")
	print(Fore.BLUE +Fore.RED +"                                         [서버] "+Fore.RED+"https://discord.com/invite/JvuJte6vw5")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	input(Fore.RED +Fore.RED +"\n엔터키를 눌러 나가기")
	os.system("cls")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.RED +Fore.RED +"                                                   닫기...")
	print(Fore.GREEN +Fore.RED +"                                               륨인 유튜브 구독!")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	time.sleep(2)
	sys.exit()
	pass
if opcion=='4':
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	print(Fore.RED +Fore.RED +"                                                   닫기...")
	print(Fore.GREEN +Fore.RED +"                                               륨인 유튜브 구독!")
	print(Fore.WHITE +Fore.RED +"                         ["+Fore.WHITE +Fore.RED +"+"+Fore.WHITE +Fore.RED +"]"+ Fore.WHITE +Fore.RED +"-------------------------------------------------------"+ Fore.WHITE +Fore.RED +"["+ Fore.WHITE +Fore.RED +"+"+ Fore.WHITE +Fore.RED +"]")
	time.sleep(2)
	sys.exit()
	pass


