# Import modules dan packages
from splinter import Browser
import pyautogui as p
import time as t

# Inisialisai Class
# dilakukan untuk berinteraksi dengan webpage
browser = Browser()

# FUNGSI WEB NGETIK MAYA #
# Fungsi ngetik_maya
# membuka web Ngetik Maya
def ngetik_maya(link):
	# Mengunjungi Link
	# link yang diberikan dari argument=user
	# memberi pesan mulai mengetik
	browser.visit(link)
	iUser = input('Mulai mengetik ? (y/n)')
	if iUser == 'y':
		# Jeda
		# Pesan mulai mengetik
		# Click element input
		t.sleep(5)
		print('mulai mengetik')
		browser.find_by_xpath('//*[@id="input"]').click()
		# Looping
		# melakukan proses waktu dan mengetik kata
		while True:
			# Kata
			# jika element id cocok dengan yang dicari
			# rubah element tersebut menjadi teks
			# lalu masukkan value elemen ke variabel kata
			# ketik teks dengan kata sebagai parameter
			# lalu tekan space
			# ulangi sampai waktu habis
			kata = browser.find_by_id('currentword').text
			p.typewrite(kata)
			p.press('space')


			# Waktu 
			# jika waktu = '0', lakukan looping
			# looping bertujuan memproses pertanyaan yang diberikan
			# jika pada pertanyaan tekan 'y', keluar
			# namun jika tekan 'n', ketik kembali
			# selain syarat diatas, beri pesan error
			# lalu keluar browser dan program
			waktu = browser.find_by_id('timer').text
			if waktu == '0':
				# while True:
				print('selesai mengetik')
				iUser2 = input('Keluar? (y/n): ')
				if iUser2 is 'y':
					print('keluar')
					t.sleep(5)
					browser.quit()
					exit()
				elif iUser2 is 'n':
					iUser3 = input('Ketik lagi? (y): ')
					if iUser3 is 'y':
						browser.reload()
						t.sleep(5)
						print('mulai mengetik')
					else:
						print('ERROR: input tidak cocok')
						browser.quit()
						exit()
	else:
		print('keluar')
		browser.quit()
		exit()