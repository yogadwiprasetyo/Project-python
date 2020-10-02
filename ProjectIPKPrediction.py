# TODO: REFACTOR AND DOCUMENTATION

# handle all data and operation on mata kuliah
class MataKuliah:
  # attribute a save all nilai in mata kuliah
  nilai_perilaku = 0
  nilai_tugas1 = 0
  nilai_tugas2 = 0
  nilai_UTS = 0
  nilai_UAS = 0

  # initial attribute mata_kuliah, total_sks, and bobot_nilai.
  def __init__(self):
    print('\n')
    self.mata_kuliah = input('masukkan nama mata kuliah: ')
    self.sks = int(input('masukkan jumlah sks: '))
    self.bobot_nilai = self.setBobotNilai()

  # set bobot_nilai from input users.
  # @return dictionary
  def setBobotNilai(self):
    perilaku = input('bobot nilai perilaku: ')
    tugas = input('bobot nilai tugas: ')
    uts = input('bobot nilai UTS: ')
    uas = input('bobot nilai UAS: ')

    return {
      'perilaku': self.toPercent(perilaku),
      'tugas': self.toPercent(tugas),
      'uts': self.toPercent(uts),
      'uas': self.toPercent(uas),
    }
  
  # convert number to percent
  # @return float
  def toPercent(self, value):
    return float(int(value) / 100)
  
  # set all nilai from input users.
  def inputNilai(self):
    self.nilai_perilaku = int(input('nilai perilaku: '))
    self.nilai_tugas1 = int(input('nilai tugas 1: '))
    self.nilai_tugas2 = int(input('nilai tugas 2: '))
    self.nilai_UTS = int(input('nilai UTS: '))
    self.nilai_UAS = int(input('nilai UAS: '))
  
  # getting the total nilai of all mata kuliah.
  # add attribute nilai with bobot_nilai.
  # total_nilai: nilai_n * bobot_nilai
  # @return float total nilai
  def getTotalNilai(self):
    rata2_tugas = (self.nilai_tugas1 + self.nilai_tugas2) / 2

    total_perilaku = float(self.nilai_perilaku * self.bobot_nilai['perilaku'])
    total_tugas = float(rata2_tugas * self.bobot_nilai['tugas'])
    total_uts = float(self.nilai_UTS * self.bobot_nilai['uts'])
    total_uas = float(self.nilai_UAS * self.bobot_nilai['uas'])

    return float(total_perilaku + total_tugas + total_uts + total_uas)

  # getting the total mutu nilai and mutu huruf.
  # 100 - 80 -> total_sks * 4.0 and A, 
  # 79 - 68 -> total_sks * 3.0 and B,
  # 67 - 56 -> total_sks * 2.0 and C,
  # 55 - 45 -> total_sks * 1.0 and D,
  # else total_sks * 0 and E 
  # @return dictionary: huruf and nilai
  def getTotalMutu(self):
    total_nilai = self.getTotalNilai()

    if total_nilai <= 100 and total_nilai >= 80:
      return { 
        'nilai': self.sks * 4.0, 
        'huruf': 'A' 
      }

    elif total_nilai <= 79.99 and total_nilai >= 68:
      return { 
        'nilai': self.sks * 3.0, 
        'huruf': 'B' 
      }

    elif total_nilai <= 67.99 and total_nilai >= 56:
      return { 
        'nilai': self.sks * 2.0, 
        'huruf': 'C' 
      }

    elif total_nilai <= 55.99 and total_nilai >= 45:
      return { 
        'nilai': self.sks * 1.0, 
        'huruf': 'D' 
      }

    else:
      return { 
        'nilai': self.sks * 0, 
        'huruf': 'E' 
      }

# handle all data and operation on IPK
class IPK:
  # attribute to store hasil IPK, 
  # total sks and total nilai mutu obtained from all MataKuliah.
  list_matakuliah = dict()
  total_sks = 0
  total_mutu = 0

  # input the numbers of obj MataKuliah taken,
  # and set a name, sks, and bobot nilai.
  def inputMataKuliah(self):
    jumlah_matakuliah = int(input('masukkan jumlah mata kuliah: '))

    for x in range(jumlah_matakuliah):
      obj = MataKuliah()
      self.list_matakuliah.update({ obj.mata_kuliah: obj })
  
  # input grades to list obj MataKuliah
  def inputToNilai(self):
    for obj in self.list_matakuliah:
      name = self.list_matakuliah[obj].mata_kuliah
      print("\nMasukkan nilai {Name}\n".format(Name=name))
      self.list_matakuliah[obj].inputNilai()
  
  # add up all sks from list obj MataKuliah,
  # @return integer
  def getTotalSKS(self):
    for obj in self.list_matakuliah:
      self.total_sks += self.list_matakuliah[obj].sks

    return self.total_sks
  
  # add up all nilai mutu from list obj MataKuliah.
  # @return float
  def getTotalMUTU(self):
    for obj in self.list_matakuliah:
      nilai_mutu = self.list_matakuliah[obj].getTotalMutu()
      self.total_mutu += nilai_mutu['nilai']

    return self.total_mutu

  # result divide from total_mutu and total_sks
  # @return float
  def getIPK(self):
    return float(self.getTotalMUTU() / self.getTotalSKS())
  
  # show it nilai and huruf mutu from each in list obj MataKuliah.
  def showNilaiMutu(self):
    print('\n===== Nilai and Huruf Mutu =====\n')

    for obj in self.list_matakuliah:
      name = self.list_matakuliah[obj].mata_kuliah
      mutu = self.list_matakuliah[obj].getTotalMutu()
      print("{Name} = {Nilai} | {Huruf}".format(
        Name=name, 
        Nilai=mutu['nilai'], 
        Huruf=mutu['huruf']
      ))

  # show it total nilai from each in list obj MataKuliah.
  def showNilai(self):
    print('\n===== Total Nilai =====\n')

    for obj in self.list_matakuliah:
      name = self.list_matakuliah[obj].mata_kuliah
      nilai = self.list_matakuliah[obj].getTotalNilai()
      print("{Name} = {Nilai}".format(Name=name, Nilai=nilai))

# OPERATION OBJECTS
# initial object
Predict_IPK = IPK()

# operations 
Predict_IPK.inputMataKuliah()
Predict_IPK.inputToNilai()
Predict_IPK.showNilai()
Predict_IPK.showNilaiMutu()

# results
total_mutu = Predict_IPK.getTotalMUTU()
total_sks = Predict_IPK.getTotalSKS()
ipk = Predict_IPK.getIPK()

print('\nTOTAL MUTU: {Mutu}'.format(Mutu=total_mutu))
print('TOTAL SKS: {Sks}'.format(Sks=total_sks))
print('IPK : {Ipk}'.format(Ipk=ipk))
