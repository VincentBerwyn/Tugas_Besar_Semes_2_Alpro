# %%
def jumlah_hari(bulan, tahun):
    if bulan in ['januari', 'maret', 'mei', 'juli', 'agustus', 'oktober', 'desember']:
        return 31
    elif bulan in ['april', 'juni', 'september', 'november']:
        return 30
    elif bulan == 'februari':
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 0

def prediksi_mens(hari_pertama_mens, lama_mens, jumlah_hari_bulan, lama_siklus=28):
    tanggal_haid_berikutnya = hari_pertama_mens + lama_siklus

    if tanggal_haid_berikutnya <= jumlah_hari_bulan:
        bulan_haid_berikutnya = "bulan ini"
    else:
        tanggal_haid_berikutnya -= jumlah_hari_bulan
        bulan_haid_berikutnya = "bulan depan"

    tanggal_masa_subur = tanggal_haid_berikutnya - 14
    if tanggal_masa_subur > 0:
        bulan_masa_subur = bulan_haid_berikutnya
    else:
        tanggal_masa_subur += jumlah_hari_bulan
        bulan_masa_subur = "bulan ini" if bulan_haid_berikutnya == "bulan depan" else "bulan sebelumnya"

    print(f"\n--- HASIL PREDIKSI ---")
    print(f"Prediksi haid berikutnya : {tanggal_haid_berikutnya} ({bulan_haid_berikutnya})")
    print(f"Prediksi masa subur      : {tanggal_masa_subur} ({bulan_masa_subur})\n")

def cari_bulan(data_list, target_bulan):
    print(f"\n--- PENCARIAN DATA BULAN: {target_bulan} ---")
    nomor = 1
    for data in data_list:
        if data['bulan'].lower() == target_bulan.lower():
            print(f"{nomor}. {data['hari1']} {data['bulan']} {data['tahun']} - {data['lama']} hari")
            nomor += 1
    else:
        if nomor == 1:
            print("Data untuk bulan tersebut tidak ditemukan.")


def urutkan_lama_mens(data_list):
    n = len(data_list)
    for i in range(n):
        for j in range(i + 1, n):
            if data_list[j]['lama'] < data_list[i]['lama']:
                data_list[i], data_list[j] = data_list[j], data_list[i]
    
    print("\n--- DATA SETELAH DIURUTKAN BERDASARKAN LAMA MENS ---")
    nomor = 1
    for data in data_list:
        print(f"{nomor}. {data['hari1']} {data['bulan']} {data['tahun']} - {data['lama']} hari")
        nomor += 1

def main():
    data_mens = []

    print ("Tugas Besar Alpro (Vincent, Gracella, Novena)")
    while True:
        print("\n=== APLIKASI MENSTRUASI ===")
        print("======= MENU UTAMA =======")
        print("1. Input mens")
        print("2. Prediksi mens (berdasarkan input terakhir)")
        print("3. Lihat semua data")
        print("4. Urutkan riwayat (berdasarkan lama mens)")
        print("5. Cari riwayat berdasarkan bulan")
        print("6. Keluar")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            tahun = int(input("Masukkan tahun: "))
            bulan = input("Masukkan nama bulan dalam huruf kecil: ")
            hari1_mens = int(input("Masukkan tanggal mulai menstruasi: "))
            lama_mens = int(input("Masukkan lama menstruasi (hari): "))
            
            data = {
                "tahun": tahun,
                "bulan": bulan,
                "hari1": hari1_mens,
                "lama": lama_mens
            }
            data_mens.append(data)
            print("Data berhasil disimpan.")

        elif pilihan == "2":
            if not data_mens:
                print("Belum ada data. Silakan input terlebih dahulu di menu 1.")
            else:
                data_terakhir = data_mens[-1]
                jumlah_hari_bln = jumlah_hari(data_terakhir["bulan"], data_terakhir["tahun"])
                if jumlah_hari_bln == 0:
                    print("Nama bulan tidak valid.")
                else:
                    prediksi_mens(
                        data_terakhir["hari1"],
                        data_terakhir["lama"],
                        jumlah_hari_bln
                    )

        elif pilihan == "3":
            if data_mens==[]:
                print("Belum ada data.")
            else:
                print("\n--- SEMUA DATA MENSTRUASI ---")
                nomor = 1
                for data in data_mens:
                    print(f"{nomor}. {data['hari1']} {data['bulan']} {data['tahun']} - {data['lama']} hari")
                    nomor += 1

        elif pilihan == "4":
            if data_mens==[]:
                print("Belum ada data untuk diurutkan.")
            else:
                urutkan_lama_mens(data_mens)

        elif pilihan == "5":
            if data_mens==[]:
                print("Belum ada data.")
            else:
                target_bulan = input("Masukkan nama bulan yang ingin dicari: ")
                cari_bulan(data_mens, target_bulan)

        elif pilihan == "6":
            print("Program berakhir, Selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 sampai 6.")

main()


# %%



