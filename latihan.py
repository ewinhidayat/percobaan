# Input data dari pengguna
nama_karyawan = input("Masukkan nama karyawan: ")
jumlah_jam_kerja = int(input("Masukkan jumlah jam kerja: "))
jabatan = input("Masukkan jabatan (Kepala/Sekretaris/Staff): ")

if jabatan == "Kepala":
    gaji_pokok = 2000000
    tunjangan = 1000000
    transport = 100000
elif jabatan == "Sekretaris":
    gaji_pokok = 1500000
    tunjangan = 500000
    transport = 50000
else:  # Defaultnya adalah Staff biasa
    gaji_pokok = 700000
    tunjangan = 150000
    transport = 30000

upah = transport * jumlah_jam_kerja

if jumlah_jam_kerja > 45:
    upah_lembur = upah * 0.35
else:
    upah_lembur = 0

total_upah = gaji_pokok + tunjangan + upah + upah_lembur

print("\nSlip Gaji untuk", nama_karyawan)
print("Jabatan:", jabatan)
print("Gaji Pokok: Rp.", gaji_pokok)
print("Tunjangan: Rp.", tunjangan)
print("Upah: Rp.", upah)
print("Upah Lembur: Rp.", upah_lembur)
print("Total Upah Bersih: Rp.", total_upah)
