* Pastikan sudah terinstall anaconda
* Jalankan perintah `conda env list` untuk melihat environment yang sudah dibuat

### CARA ONLINE
Membuat environment baru
  * `conda create -n <nama_environment> python=3.6 <package apa yang ingin diinstall, ex: numpy, pandas>`
  * pilih yes (y)
  * cek kembali `conda env list`
  * aktifkan environment `activate <nama_environment>`
  * melihat package apa yang sudah terinstall dengan `conda list`
  * menambah package baru, `conda install <nama_package, ex: scikit-learn>`
  * pilih yes (y)
  * pastikan ada koneksi internet
