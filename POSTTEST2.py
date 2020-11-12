import os
import time

data_akun = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    clear_screen()
    print("2009106046_Erman Parni Simanjuntak_POST TEST 2\n\n")
    print("==================================================")
    print("               Welcome My Soeltan")
    print("==================================================")
    time.sleep(3)
    game()



def game():
    clear_screen()
    print("Kami menyediakan 2 game tembak-tembakan terbaik")
    print("1. Free Fire")
    print("2. PUBG Mobile")
    print("")
    pilih = int(input("Pilih game yang anda ingin top up: "))
    
    if pilih == int('1'):
        clear_screen()
        for i in range (3):
            username = str(input("Masukkan username anda                     : "))
            data_akun.insert(0,username)
            idg = float(input("Masukkan id anda dengan kode negara .01    : "))
            data_akun.insert(1,idg)
            lvl = int(input("Masukkan angka lvl anda                    : "))
            data_akun.insert(2,lvl)

            print("\nUsername     : ",data_akun[0])
            print("id           : ",data_akun[1])
            print("lvl          : ",data_akun[2])
            input("\ntekan enter untuk pengecekkan...")

            if (username == str('erman')) and (idg == float('666.01')) and (lvl == int('77')):
                clear_screen()
                print("Akun anda ditemukan !!!")
                time.sleep(2)
                ff()
            else:
                clear_screen()
                print("Akun anda tidak ditemukan !!!")
                time.sleep(5)
                clear_screen()
                
        if i == 2:
            print("\nAnda kami kembalikan ke menu awal...")
            time.sleep(5)
        welcome()
    if pilih == int('2'):
        clear_screen()
        for i in range (3):
            username = str(input("Masukkan username anda                    : "))
            data_akun.insert(0,username)
            idg = float(input("Masukkan id anda dengan kode negara .01   : "))
            data_akun.insert(1,idg)
            lvl = int(input("Masukkan angka lvl anda                   : "))
            data_akun.insert(2,lvl)

            print("\nUsername     : ",data_akun[0])
            print("id           : ",data_akun[1])
            print("lvl          : ",data_akun[2])
            input("\ntekan enter untuk pengecekkan...")

            if (username == str('erman')) and (idg == float('666.01')) and (lvl == int('77')):
                clear_screen()
                print("Akun anda ditemukan !!!")
                time.sleep(2)
                pubg()
            else:
                clear_screen()
                print("Akun anda tidak ditemukan !!!")
                time.sleep(5)
                clear_screen()
                
        if i == 2:
            print("\nAnda kami kembalikan ke menu awal...")
            time.sleep(5)
        welcome()

                

def ff():
    clear_screen()
    print("Pilihan diamond yang kami sediakan:")
    print("1. 100  dm    = Rp12000")
    print("2. 200  dm    = Rp20000")
    print("3. 500  dm    = Rp50000")
    print("4. 1000 dm    = Rp100000")

    dm_ff = int(input("\nSilahkan pilih nomor berapa: "))

    if dm_ff == int('1'):
        harga = float(12000 + 2500.25)
        print ("\nTotal semua biaya (termasuk biaya admin): Rp" ,harga,)
        input ("\nTekan enter untuk melanjutkan...")
        metod()
             
    elif dm_ff == int('2'):
        harga = float(20000 + 2500.25)
        print ("\nTotal semua biaya (termasuk biaya admin): Rp" ,harga,)
        input ("\nTekan enter untuk melanjutkan...")
        metod()

    elif dm_ff == int('3'):
        harga = float(50000 + 2500.25)
        print ("\nTotal semua biaya (termasuk biaya admin): Rp" ,harga,)
        input ("\nTekan enter untuk melanjutkan...")
        metod()
            
    elif dm_ff == int('4'):
        harga = float(100000 + 2500.25)
        print ("\nTotal semua biaya (termasuk biaya admin): Rp" ,harga,)
        input ("\nTekan enter untuk melanjutkan...")
        metod()
            
    else:
        clear_screen()
        print("Pilih nomor yang tersedia !")
        time.sleep(3)
        game()
    

def pubg():
    clear_screen()
    print("Pilihan uc yang kami sediakan:")
    print("1. 100  uc    = Rp12000")
    print("2. 200  uc    = Rp20000")
    print("3. 500  uc    = Rp50000")
    print("4. 1000 uc    = Rp100000")

    dm_p = int(input("\nSilahkan pilih nomor berapa: "))

    if dm_p == int('1'):
        harga = float(12000 + 2500.25)
        print ("\nTotal semua biaya (termasuk biaya admin): Rp" ,harga,)
        input ("\nTekan enter untuk melanjutkan...")
        metod()
            
    elif dm_p == int('2'):
        harga = float(20000 + 2500.25)
        print ("\nTotal semua biaya (termasuk biaya admin): Rp" ,harga,)
        input ("\nTekan enter untuk melanjutkan...")
        metod()
            
    elif dm_p == int('3'):
        harga = float(50000 + 2500.25)
        print ("\nTotal semua biaya (termasuk biaya admin): Rp" ,harga,)
        input ("\nTekan enter untuk melanjutkan...")
        metod()
            
    elif dm_p == int('4'):
        harga = float(100000 + 2500.25)
        print ("\nTotal semua biaya (termasuk biaya admin): Rp" ,harga,)
        input ("\nTekan enter untuk melanjutkan...")
        metod()
            
    else:
        clear_screen()
        print("Pilih nomor yang tersedia !")
        time.sleep(3)
        game()
        

            


def metod():
    clear_screen()
    print("Pilih metode pembayaran anda:")
    print("1. E-banking")
    print("2. Toko swalayan")
    mtd = int(input("\nMasukkan nomor pilihan anda: "))
    if mtd == int('1'):
        clear_screen()
        print("Pilihan bank yang tersedia:")
        print("1. BRI")
        print("2. Mandiri")
        ff_mtd = int(input("\nMasukkan nomor pilihan anda: "))
        if ff_mtd == int('1'):
            clear_screen()
            print("Kode pembayaran anda: XY5Z-TY7S-HQW8\n")
            print("Terimakasih sudah berbelanja Sultan")
            time.sleep(10)
            nanya()
        if ff_mtd == int('2'):
            clear_screen()
            print("Kode pembayaran anda: G0FD-TE3S-HUY6\n")
            print("Terimakasih sudah berbelanja Sultan")
            time.sleep(10)
            nanya()

    if mtd == int('2'):
        clear_screen()
        print("Pilihan toko swalayan yang tersedia: ")
        print("1. Indomaret")
        print("2. Alfamart")
        
        ff_mtd = int(input("\nMasukkan nomor pilihan anda: "))
        if ff_mtd == int('1'):
            clear_screen()
            print("Kode pembayaran anda: XYZ-TYS-HQW")
            print("\nTerimakasih sudah berbelanja Sultan")
            time.sleep(10)
            nanya()
        if ff_mtd == int('2'):
            clear_screen()
            print("Kode pembayaran anda: GFD-TES-HUY\n")
            print("Terimakasih sudah berbelanja Sultan")
            time.sleep(10)
            nanya()

def nanya():
    clear_screen()
    jawab = str(input("Mau beli lagi atau udahan? mau/udahan : ")) 
    if jawab == str('mau'):
        clear_screen() 
        welcome()
    if jawab == str('udahan'):
        clear_screen()
        print("See You Later My Soeltan :)")
        time.sleep(5)
        exit()         

welcome()
