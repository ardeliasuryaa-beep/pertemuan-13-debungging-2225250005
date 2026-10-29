
# Pertemuan 13 - Debugging dan Testing

**Nama:** Ardelia Surya Agustin  
**NIM:** 2225250005  
**Kelas:** S1 Pendidikan Matematika

## Tujuan
Mempelajari debugging, tracing, testing, dan test case menggunakan Python di VS Code.

## Kasus
Program awal memiliki tiga bug utama:
1. Fungsi rata-rata selalu membagi dengan 5.
2. Nilai 60 dianggap tidak lulus.
3. Fungsi nilai tertinggi menggunakan operator pembanding yang salah.

## Test Case

| ID | Input | Expected | Actual Awal | Status Awal |
|---|---|---|---|---|
| T1 | [80, 60, 90, 70] | 75.0 | 60.0 | FAIL |
| T2 | [100, 80] | 90.0 | 36.0 | FAIL |
| T3 | status(60) | Lulus | Tidak lulus | FAIL |
| T4 | status(59) | Tidak lulus | Tidak lulus | PASS |
| T5 | [80, 60, 90, 70] | 90 | 0 | FAIL |

## Bug Report

### B01 - Rata-rata
- Gejala: Hasil rata-rata tidak sesuai jumlah data.
- Akar penyebab: Pembagi selalu menggunakan angka 5.
- Perbaikan: Menggunakan len(nilai) dan menangani list kosong.
- Retest: T1 dan T2 PASS.

### B02 - Status kelulusan
- Gejala: Nilai 60 dianggap tidak lulus.
- Akar penyebab: Kondisi menggunakan nilai > 60.
- Perbaikan: Mengubah menjadi nilai >= 60.
- Retest: T3 dan T4 PASS.

### B03 - Nilai tertinggi
- Gejala: Fungsi menghasilkan nilai tertinggi yang salah.
- Akar penyebab: Operator pembanding terbalik dan nilai awal tidak sesuai.
- Perbaikan: Memulai dari elemen pertama dan membandingkan dengan >.
- Retest: T5 PASS.

## Hasil Retest
Seluruh 7 test case pada program versi perbaikan diharapkan PASS, termasuk pengujian data kosong.

## Cara Menjalankan
Jalankan perintah berikut di terminal VS Code:

python praktik/praktik_4_debugging.py

## Refleksi
Tracing dan test case membantu menemukan penyebab bug secara sistematis. Setelah kode diperbaiki, seluruh test harus dijalankan kembali untuk memastikan tidak muncul kesalahan baru.
# pertemuan-13-debungging-2225250005
