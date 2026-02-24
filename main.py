
def membuka_kontak(path = 'kontak.txt'):
    with open(path, mode='r') as file:
        kontak = file.readlines()
    return kontak

def menyimpan_kontak(path = 'kontak.txt', isi=[]):

    with open(path, mode='w') as file:
        kontak = file.writelines(isi)


class Kontak:
    def __init__(self):
        self.kontak = membuka_kontak()

    def melihat_kontak(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}.' + item)
        else:
            print("Kontak Kosong")
            return 1

    def menambah_kontak(self):
        nama = input("Nama: ")
        no_hp = input("Nomer HP: ")
        email = input("Email: ")

        kontak_baru = f'{nama} ({no_hp}) {email}' + '\n'
        self.kontak.append(kontak_baru)
        print("Berhasil Ditambahkan")

    def menghapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                index_hapus = int(input("Pilih Nomer (1,2,3,4): "))
                del self.kontak[index_hapus - 1]
            except:
                print("Masukkan nomer yang tertera")
    def keluar_kontak(self):
        menyimpan_kontak(isi=self.kontak)

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

while True:
    print("\nMenu Kontak")
    print("1. Melihat Kontak")
    print("2. Menambahkan Kontak")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Pilih Nomer (1,2,3,4): ")

    if pilihan == '1':
        kontak_kantor.melihat_kontak()

    elif pilihan == '2':
        kontak_kantor.menambah_kontak()

    elif pilihan == '3':
        # Menghapus Kontak
        kontak_kantor.menghapus_kontak()

    elif pilihan == '4':
        # Keluar dari
        kontak_kantor.keluar_kontak()
        break
    else:
        print("Masukkan nomer yang tertera")