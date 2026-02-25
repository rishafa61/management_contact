
import kontak

def main():

    kontak_kantor = kontak.Kontak()
    kontak_keluarga = kontak.Kontak()

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
if __name__ == "__main__":
    main()