import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		import src.pilihan
		print("""
1. SMS Gratis
2. OTP Matahari
3. OTP Hallodok
4. OTP Olx
5. OTP Sociolla
0. Tulis exit Untuk Keluar
""")
		pilih=int(input('PILIH :'))
		if pilih == 1:
			import src.payu
		elif pilih == 2:
			import src.matahari
		elif pilih == 3:
			import src.alodok
		elif pilih == 4:
			import src.olx
		elif pilih == 5:
			import src.socil
		else: print("           SALAH KOPLOK !!! BELEGUG SIA MAH")
		print (". . .")
		print (". . .")
		print (". . .")
		input('ENTER untuk ULANGI...')
		self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('cls')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))