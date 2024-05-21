stok = [
    {"nama" : "Beat", "jumlah" : 12},
    {"nama" : "Vario", "jumlah" : 10},
    {"nama" : "Scoopy", "jumlah" : 11},
    {"nama" : "CBR", "jumlah" : 15}

]
def tambah_data ():
    namaBarang = str(input("masukan nama motor : ")).lower()
    jumlah = int(input("masukan stok motor : "))

    stok_baru = {f"nama": namaBarang, "jumlah" : jumlah }
    stok.append(stok_baru)
    print("\n")
    print("data berhasil ditambahkan")
    print("\n")

def edit_data ():
    index = int(input("masukan data index ke : "))
    namaBaru = str(input("masukan nama motor :"))
    jumlahBaru = int(input("masukan stok :"))

    stokBaru = [("nama",namaBaru),("jumlah",jumlahBaru) ]
    stok[index].update(stokBaru)
    print("\n")
    print("data telah diubah")
    print("\n")

def hapus_data():
    hapus = int(input("hapus data index ke : "))
    stok.pop(hapus)
    print("\n")
    print("data berhasil dihapus")
    print("\n")

def tampil_data():
    print("====daftar barang=====")
    for i in stok:
        print(f"{i['nama']} : {i['jumlah']}")
    print("\n")

def cari_data():
    print("========hasil pencarian============")
    items = []
    cari = str(input("data yang akan dicari :")).lower()
    for i in stok :
        if cari in i["nama"] :
            items.append(i)
    if items :
        for item in items :  
            print(f"{item['nama']} : {item['jumlah']}")
    else : 
        print("tidak ada data dengan nama", cari)
    print("\n")

def jumlah_data():
    print("=========jumlah data==========")
    print(f"terdapat {len(stok)} data")
    print("\n")