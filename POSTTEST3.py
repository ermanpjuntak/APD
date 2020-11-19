import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')\

def menu():
    print("Selamat datang di toko kue sule\n")
    print("Kue yang tersedia di toko sule: \n")
    print("Cokelat  = Rp3500")
    print("Keju     = Rp6000\n")
    print("Stock kue kami tiap harinya adalah 35 untuk cokelat dan 25 untuk keju\n")
    print("DAPATKAN DISKON HINGGA 15% !!!")
    print("beli kue cokelat 5-20 dapat diskon 7%")
    print("beli kue cokelat 21-35 dapat diskon 12%")
    print("beli kue keju 4-15 dapar diskon 10%")
    print("beli kue keju 16-25 dapat diskon 15%\n")
    

    jumlah_cokelat = int(input("Beli berapa kue cokelat ? "))
    jumlah_keju = int(input("Beli berapa kue keju? "))
    clear_screen()
    if (jumlah_cokelat >= 1 and jumlah_cokelat <= 4):
        biaya_cokelat = 3500*jumlah_cokelat
        total_harga_cokelat = biaya_cokelat
        print("Total pembelian kue cokelat anda: %d" % (jumlah_cokelat))
        print("Total biaya kue cokelat anda: Rp %d" % (biaya_cokelat))
    elif (jumlah_cokelat >= 5 and jumlah_cokelat <= 20):
        biaya_cokelat =  3500*jumlah_cokelat
        diskon_cokelat = biaya_cokelat*7/100
        total_harga_cokelat = biaya_cokelat-diskon_cokelat
        print("Total pembelian kue cokelat:  %d"  % (jumlah_cokelat))
        print("Total biaya kue cokelat: Rp %d" % (biaya_cokelat))
        print("Diskon kue cokelat yang anda dapat: Rp %d" % (diskon_cokelat))
        print("Total kue cokelat yang harus anda bayar: Rp %d" % (total_harga_cokelat))
    elif(jumlah_cokelat >= 21 and jumlah_cokelat <= 35):
        biaya_cokelat = 3500*jumlah_cokelat
        diskon_cokelat = biaya_cokelat*12/100
        total_harga_cokelat = biaya_cokelat-diskon_cokelat
        print("Total pembelian cokelat: %d" % (jumlah_cokelat))
        print("Total biaya kue cokelat : Rp %d" % (biaya_cokelat))
        print("Diskon kue cokelat yang anda dapat: Rp %d" % (diskon_cokelat))
        print("Total kue cokelat yang harus anda bayar: Rp %d" % (total_harga_cokelat))
    elif(jumlah_cokelat == 0):
        total_harga_cokelat = 0
        print("Anda tidak membeli kue cokelat")    
    else:
        total_harga_cokelat = 0
        print("\n*Jumlah kue cokelat yang anda pilih tidak tersedia")
        time.sleep(5)

    if(jumlah_keju >= 1 and jumlah_keju <= 3):
        biaya_keju = 6000*jumlah_keju
        total_harga_keju = biaya_keju
        print("\nTotal pembelian kue cokelat anda: %d" % (jumlah_keju))
        print("Total biaya kue cokelat anda: Rp %d" % (biaya_keju))
    elif(jumlah_keju >= 4 and jumlah_keju <= 15):
        biaya_keju = 6000*jumlah_keju
        diskon_keju = biaya_keju*10/100
        total_harga_keju = biaya_keju-diskon_keju
        print("\nTotal pembelian kue keju: %d" % (jumlah_keju))
        print("Total biaya kue keju: Rp. %d" % (biaya_keju))
        print("Diskon kue keju yang anda dapat: Rp. %d" % (diskon_keju))
        print("Total kue keju yang harus anda bayar: Rp %d" % (total_harga_keju))
    elif(jumlah_keju >= 16 and jumlah_keju <= 25):
        biaya_keju = 6000*jumlah_keju
        diskon_keju = biaya_keju*25/100
        total_harga_keju = biaya_keju-diskon_keju
        print("Total pembelian kue keju: %d" % (jumlah_keju))
        print("Total biaya kue keju: Rp. %d" % (biaya_keju))
        print("Diskon kue keju yang anda dapat: Rp. %d" % (diskon_keju))
        print("Total kue keju yang harus anda bayar: Rp %d" % (total_harga_keju))
    elif(jumlah_keju == 0):
        total_harga_keju = 0
        print("Anda tidak membeli kue keju")
    else:
        total_harga_keju = 0
        print("\n*Jumlah kue keju yang anda pilih tidak tersedia")
        time.sleep(5)

    total_semua = total_harga_cokelat+total_harga_keju
    print("\nJumlah total biaya belanjaan kue anda: Rp %d" % (total_semua)) 
    bayar = float(input("\nMasukkan  nominal uang anda: Rp "))
    angsul = bayar-total_semua
    if(bayar >= total_semua):
        print("Kembalian: Rp %d" % (angsul))
        print("\nTerima kasih sudah berbelanja !!!")
    else:
        print("\nUang anda tidak cukup!!!")
        time.sleep(10)
        clear_screen()
        menu()

menu()
