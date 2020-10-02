# import only system from os
from os import system, name
import random as r

# Clear screen
def clear ():
  if name == 'nt': 
    _ = system('cls') # jika os windows
  else:
    _ = system('clear') # jika os linux, mac , and other
#  END FUNCTION

# @dj = data jawaban
# @ttl = total
# Penilaian jawaban user
def penilaian (dj_soal, dj_user):
  # inisialisasi variabel total benar, salah, dan nilai
  ttl_benar = 0
  ttl_salah = 0
  ttl_nilai = 0
  i = 0

  # loop data jawaban user dan soal,
  # jika jawaban user benar, increment total benar.
  # jika jawaban user salah, increment total salah.
  while (i < len(dj_soal)):
    if dj_user[i] == dj_soal[i]:
      ttl_benar += 1
      i += 1
      continue

    ttl_salah += 1
    i += 1
  
  # menghitung total nilai
  ttl_nilai = int((ttl_benar / len(dj_soal)) * 100)

  # jika jawaban benar dan salah == 0, beri pesan khusus
  if ttl_salah == 0:
    print("Jawaban benar semua")
  elif ttl_benar == 0:
    print("Jawaban salah semua")   
  else:
    print(F"{ttl_benar} jawaban benar")
    print(F"{ttl_salah} jawaban salah")

  print(F"Anda mendapatkan nilai {ttl_nilai}")
  input("Tekan ENTER ...")
#  END FUNCTION

# @jw = jawaban
# @rand = random integer
# @op = operator
# Membuat soal dan jawaban 
def soal (first_rand, second_rand, op_arithmetic):
  if op_arithmetic == '+':
    jw_soal = first_rand + second_rand
  elif op_arithmetic == '-':
    jw_soal = first_rand - second_rand
  elif op_arithmetic == '*':
    jw_soal = first_rand * second_rand

  return {'jw':jw_soal, 'first':first_rand, 'second':second_rand}
#  END FUNCTION

# @dj = data jawaban
# @jw = jawaban
# @min|max = minimum dan maximum range random
# @jml = jumlah
# @op = operator
# Mengisi soal 
def mengisi_soal (min, max, op_arithmetic):
  # inisialisasi data jawaban user dan soal
  dj_soal = []; dj_user = [];

  # input user
  try:
    jml_soal = int(input("Jumlah soal: "))
  except:
    return

  # loop soal dan jawaban sampai jumlah soal,
  # lalu masukan jawaban soal dan user ke data jawaban
  for i in range(jml_soal):
    # membuat soal dan jawaban
    result = soal(r.randint(min,max), r.randint(min,max), op_arithmetic)
    dj_soal.append(result['jw'])
    try:
      angka_soal1 = result['first']
      angka_soal2 = result['second']
      jw_user = int(input(F"{i+1}. {angka_soal1} {op_arithmetic} {angka_soal2} = "))
      dj_user.append(jw_user)
    except:
      return

  # cek jawaban
  penilaian(dj_soal,dj_user)
#  END FUNCTION

# @jml = jumlah
# Menu pilihan
def menu ():
  while True:
    # clear screen
    clear()

    print("""
      ---- Soal ----
      1. Perkalian
      2. Penjumlahan
      3. Pengurangan
      4. keluar
    """)

    # input user
    try:
      pilihan = int(input("Pilih soal: "))
    except:
      continue
    
    if pilihan == 4:
      return
    elif pilihan == 1:
      mengisi_soal(3, 15, '*')
    elif pilihan == 2:
      mengisi_soal(50, 100, '+')
    elif pilihan == 3:
      mengisi_soal(1, 100, '-')
    else:
      continue
#  END FUNCTION

# Run program
menu()
