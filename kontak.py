import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()

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
        dokumen.menyimpan_kontak(isi=self.kontak)