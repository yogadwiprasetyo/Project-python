# ALGORITMA 
# tampilkan pilihan tujuan
# ketik pilihan tujuan
# masuk ke link tujuan
# setelah masuk, keluar atau kembali ke menu mode manual?

# KEKURANGAN
# belum bisa melakukan ganti tujuan pada saat program berjalan
# Data Link masih belum lengkap
# penanganan pada link tujuan masih belum semua

# IMPORT MODULE #
from selenium.webdriver import *
from selenium.webdriver.common import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base64 import b64decode
import sys

# decode username
def dec_un():
    f = open("u.txt", "r")
    isiFile = b64decode(f.read())
    un = isiFile.decode()
    f.close()
    return str(un)

# decode password
def dec_pw():
    f = open("p.txt", "r")
    isiFile = b64decode(f.read())
    pw = isiFile.decode()
    f.close()
    return str(pw)

# melakukan proses login
def login(webdriver):
    # masuk ke link yang diberikan
    webdriver.get('http://apps.unas.ac.id:8080/login.do')
    WebDriverWait(webdriver, 10)
    username = dec_un()
    password = dec_pw()
    # pengisian form login
    webdriver.find_element_by_name("username").send_keys(username)
    webdriver.find_element_by_name("password").send_keys(password)
    webdriver.find_element_by_name("Submit").click()
    handling_alert(webdriver)

# menangani alert yang tampil 
def handling_alert(webdriver):
    wait = WebDriverWait(webdriver, 10)
    alert = wait.until(EC.alert_is_present())
    alert.accept()

# pilihan tujuan
def pilihan_tujuan():
    print('''
    ############ ACADEMIC ONLINE SYSTEM ############

        ======= PILIHAN TUJUAN ========
        Data Transkrip     Daftar Wisuda | Pengembangan
        Histori Nilai      Kuesioner Dosen | Pengembangan
        Jadwal Jurusan     Kehadiran Kuliah 
        Jadwal Pribadi     Rencana Pembelajaran | Pengembangan
        Mengisi KRS        Nilai Semester Aktif |Pengembangan
        Jadwal PA          Data Keuangan
        Berita Acara PA    Ubah Password

        ketik DT untuk melihat Data Pribadi

            tekan 'q' keluar

    ############ ACADEMIC ONLINE SYSTEM ############''')

# data pribadi
def data_pribadi(webdriver):
    # ambil data lalu keluar dari browser, kembali ke menu
    xpathData = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table'
    elementData = webdriver.find_element_by_xpath(xpathData).text
    tampilanData = '####### DATA PRIBADI #######\n\n{}\n\n####### DATA PRIBADI #######'.format(elementData)
    print(tampilanData)
    webdriver.quit()
    menu()

# membuat link tujuan user
def tujuan(link,**data): # PROBLEM
    # value diambil untuk akses data tujuan
    user = input('ketik pilihan tujuan: ')
    # exit program
    if user == 'q':
        exit()

    # Cek Operating System
    if sys.platform.startswith('linux'):
        webdriver = Firefox()
        print('OS anda linux')
    elif sys.platform.startswith('win32'):
        webdriver = Chrome()
        print('OS anda Windows')
    elif sys.platform.startswith('darwin'):
        webdriver = Chrome()
        print('OS anda Macos')
    else:
        print('OS not supported')

    # Buka browser
    # webdriver = Firefox()
    # login 
    login(webdriver)

    # jika value input cocok dengan key data link lakukan aksi
    if user in data.keys():
        # membuat link tujuan user
        linkReady = link + data[user]
        # jika sama, lakukan aksi tambahan
        if linkReady == link+'mhsKhsView.do' or linkReady == link+'mhsKehadiranView.do' or linkReady == link+'mhsKeuangan.do': 
            webdriver.get(linkReady)
            # click and browse
            select = '//*[@id="semester"]'
            genap = '#semester > option:nth-child(2)'
            browse = '//*[@id="browse"]'
            webdriver.find_element_by_xpath(select).click()
            webdriver.find_element_by_css_selector(genap).click()
            webdriver.find_element_by_xpath(browse).click()
        else:
            # masuk ke tujuan
            webdriver.get(linkReady)

        # keluar / kembali ke menu manual
        out_manual(webdriver,link)
    elif user == 'DT':
        # ambil data pribadi, lalu keluar
        data_pribadi(webdriver)
    else:
        # warning
        print('samakan penulisan pilihan tujuan')

# menu dan tempat data tujuan
def menu():
    # link default
    linkDefault = 'http://apps.unas.ac.id:8080/'
    # data tujuan
    DataTujuan = {
    'Data Transkrip':'mhsTranskripView.do',
    'Histori Nilai': 'mhsKhsView.do',
    'Jadwal Jurusan': 'mhsJadwalProgdi.do?j=1',
    'Jadwal Pribadi': 'mhsJadwalPribadi.do',
    'Mengisi KRS': 'mhsKrsPa.do',
    'Jadwal PA': 'paJadwalView.do',
    'Berita Acara PA':'paBeritaAcaraMhs.do' ,
    'Daftar Wisuda': '',
    'Kuesioner Dosen': '',
    'Kehadiran Kuliah': 'mhsKehadiranView.do',
    'Nilai Semester Aktif': '',
    'Data Keuangan': 'mhsKeuangan.do',
    'Ubah Password': 'ubahPass.do'
    }

    # menampilkan pilihan tujuan
    while(True):
        pilihan_tujuan()
        # masuk ke tujuan
        tujuan(linkDefault,**DataTujuan)

# logout atau ganti ke mode manual
def out_manual(webdriver,link):
    # input user
    userMenu = input('keluar atau kembali ke menu ? (y = keluar | n = ke menu mode manual): ')

    # jika user tekan 'y' logout, tekan 'n' ke menu dengan mode manual
    if userMenu == 'y' or userMenu == 'Y':
        webdriver.quit()
        exit()
    elif userMenu == 'n' or userMenu == 'N':
        webdriver.get(link + 'menuMhs.do')
        handling_alert(webdriver)
        exit()
    else:
        print('input tidak diketahui, kembali ke menu')
        exit()

