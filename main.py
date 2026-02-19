def melihat_kontak():
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f' {num}. {item["nama"]} ({item["No HP"]}, {item["email"]})')
    else:
        print("Kontak Kosong")
        return 1

def menambah_kontak():
    nama = input("Nama: ")
    no_hp = input("Nomer HP: ")
    email = input("Email: ")

    kontak_baru = {'nama': nama, 'No HP': no_hp, 'email': email}
    kontak.append(kontak_baru)
    print("Berhasil Ditambahkan")
def menghapus_kontak():
    if melihat_kontak() == 1:
        return
    else:
        index_hapus = int(input("Pilih Nomer (1,2,3,4): "))
        del kontak[index_hapus - 1]


kontak1 = {'nama' : "a", 'No HP' : "02341234123", 'email' : "a@gmail.com"}
kontak2 = {'nama' : "b", 'No HP' : "02356464445", 'email' : "b@gmail.com"}
kontak3 = {'nama' : "c", 'No HP' : "01231244123", 'email' : "c@gmail.com"}

kontak = [kontak1, kontak2, kontak3]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Kontak")
    print("2. Menambahkan Kontak")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Pilih Nomer (1,2,3,4): ")

    if pilihan == '1':
        melihat_kontak()

    elif pilihan == '2':
        menambah_kontak()

    elif pilihan == '3':
        # Menghapus Kontak
        menghapus_kontak()

    elif pilihan == '4':
        # Keluar dari kontak
        break
    else:
        print("Masukkan nomer yang tertera")