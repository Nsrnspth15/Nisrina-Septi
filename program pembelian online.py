from itertools import product
from datetime import date

data_product = {
    1:"Laptop",
    2:"Mouse ",
    3:"Mouse Pad",
    4:"Cooling Pad",
    5:"Charger",
}

daftar_harga = {
    1: 5000000,
    2: 50000,
    3: 25000,
    4: 80000,
    5: 170000
}

dict_trx = {}
daftar_metode_pembayaran = {
    1:"Transfer Bank",
    2:"Virtual Account",
    3:"Cash on Delivery",
    4:"Kartu Kredit"
}
print("==========List Product==========")
for i in data_product:
    print("Id Product : ",i,"\t Nama Product : ",data_product[i],"\t Harga Product : ",daftar_harga[i])
pilih_id = int(input("Pilih Id Product : "))
if pilih_id in data_product :
    pilih_beli = input("Ingin Beli? (Y/N): ")
    if pilih_beli == "y" or pilih_beli=="Y":
        nama_penerima    = input("Nama Penerima   : ")
        alamat_penerima  = input("Alamat Penerima : ")
        telepon          = input("No HP           : ")
        kurir_pengiriman = input("Kurir Pengiriman: ")
        
        dict_trx = {
            "nama_penerima": nama_penerima,
            "alamat penerima": alamat_penerima,
            "No HP": telepon,
            "Kurir pengiriman": kurir_pengiriman,
            "product id": data_product,
        }
    else:
        pass
    if len (dict_trx) > 0 :
        print("==========Metode Pembayaran==========")
    for i in daftar_metode_pembayaran:
        print("Id: ", i, "\t Metode Pembayaran: ", daftar_metode_pembayaran[i])
    pilih_metode = int(input("Pilih ID Metode Pembayaran : "))
    if pilih_metode in daftar_metode_pembayaran :
        tanggal = date.today()
        print("Tanggal \t:", tanggal)
        print ("")
        print("Nama Penerma : ", dict_trx["nama_penerima"])
        print("Alamat Penerima : ", dict_trx["alamat penerima"])
        print("No HP : ", dict_trx["No HP"])
        print("Kurir Pengiriman : ", dict_trx["Kurir pengiriman"])
        print("Product : ", data_product[pilih_id])
        print("Harga : ", daftar_harga[pilih_id])
        print("Metode Pembayaran : ", daftar_metode_pembayaran[pilih_metode])
        konfirmasi = input("Apakah Anda Yakin ingin melakukan pembayaran? (Y/N) : ")
        if konfirmasi == "y" or konfirmasi == "Y" :
            print("Anda sudah berhasil melakukan pembayaran")
        else:
            pass
    else:
        print("Id metode pembayaran tidak tersedia")
else:
    print("Id product tidak tersedia")
    
