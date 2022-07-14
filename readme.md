## About
Merupakan rest api sederhana untuk aplikasi pendeteksi dan penjualan waste. Untuk pendeteksinya menggunakan pre-trained model.

## Installation

```
git init
git clone git@github.com:chrnicle7/projekakhir-backend.git
cd projekakhir-backend
```
- Kemudian copy model junk91.h5 ke folder cv_model
- Set env production
```
pip install -r requirements.txt
python main.py
```

Gunakan postman/sejenisnya untuk mencoba
## Login
###  http://127.0.0.1:5000/auth/login POST
#### Header
```
Content-Type: application-json
```
#### Body
```
{
    "email": "exusiai@gmail.com",
    "password": "password"
}
```
#### Response
```
{
    "token": "<token>",
}
```
Kemudian lampirkan token pada Authorization header > bearer token.
Kalau token expired, login lagi.


## Mendeteksi image
###  http://127.0.0.1:5000/scan-img POST
#### Header
```
Content-Type: application/json
```
#### Body
```
{
    "img": <file.jpg/jpeg/png>
}
```
#### Response
```
{
    "data": {
        "is_dapat_dijual": true,
        "is_anorganik": false,
        "result": "Kertas",
        "probability": "0.42",
        "message": "Item ini tidak bisa dijual"
    }
}
```

## Dashboard
###  http://127.0.0.1:5000/scan-img GET
#### Header
```
Content-Type: application/json
```
#### Response
```
{
    "total_item": 8,
    "organik": 6,
    "anorganik": 2,
    "terjual": 0
}
```

## List saya
###  http://127.0.0.1:5000/list-saya GET
#### Header
```
Content-Type: application/json
```
#### Response
```
{
    data: [
        {
            "id": 1,
            "nama_item": "Kaca piring",
            "jumlah": "19 pcs",
            "jenis": "anorganik",
            "url_delete": "http://127.0.0.1:5000/list-saya/1"
        },
        {
            "id": 7,
            "nama_item": "Botol plastik",
            "jumlah": "27 pcs",
            "jenis": "anorganik",
            "url_delete": "http://127.0.0.1:5000/list-saya/7"
        },
        ...
    ]
}
```
###  http://127.0.0.1:5000/list-saya/{id} GET
#### Header
```
Content-Type: application/json
```
#### Response
```
{
    data: {
        "id": 1,
        "nama_item": "Kaca piring",
        "jumlah": "19 pcs",
        "jenis": "anorganik",
        "url_delete": "http://127.0.0.1:5000/list-saya/1"
    }
}
```

###  http://127.0.0.1:5000/list-saya/{id} POST

### Untuk menambahkan/mengurangi jumlah item
id adalah id milik item, berupa int
untuk mengganti jumlah item

jumlah: 10 berarti jumlahnya diganti menjadi 10
misal awal 100, kemudian pada request 10, berarti hasil akhirnya 10
#### Header
```
Content-Type: application/json
```
#### Body
```
{
    "jumlah": 10
}
```
#### Response
```
message : {
    "Item berhasil disimpan"
}
```
###  http://127.0.0.1:5000/list-saya/{id} DELETE
### Untuk menghapus 
#### Response
```
message : {
    "Item berhasil dihapus"
}
```

###  http://127.0.0.1:5000/pilih-mitra GET
Pada halaman pilih mitra
#### Header
```
Content-Type: application/json
```
#### Response
```
{
    "data": [
        {
            "id": 4,
            "nama": "D",
            "alamat": "9210 Welch Bridge\nLake Mavis, ND 21670-9743",
            "rating": "5.0",
            "path_foto": "path/to/foto"
        }
        ...
    ]
}
```

Pada saat mengisikan query search
###  http://127.0.0.1:5000/pilih-mitra?search=namamitra GET
#### Header
```
Content-Type: application/json
```
#### Response
```
{
    "data": [
        {
            "id": 4,
            "nama": "D",
            "alamat": "9210 Welch Bridge\nLake Mavis, ND 21670-9743",
            "rating": "5.0",
            "path_foto": null
        }
        ...
    ]
}
```

Pada saat melihat detail mitra, 
akan memberikan estimasi harga
###  http://127.0.0.1:5000/pilih-mitra/{id} POST
id yaitu milik mitra
id berupa integer
#### Header
```
Content-Type: application/json
```
#### Response
```
{
    "data": {
        "mitra": {
            "nama_mitra": "E",
            "alamat_mitra": "71754 Kuvalis Run\nBurdetteview, WY 51212",
            "rating_mitra": "5.0",
            "path_foto_mitra": null
        },
        "items": [
            {
                "nama": "Botol kaca",
                "harga_x_quantity": "Rp. 1000 x 40 pcs",
                "harga_per_item": 40000,
                "path_foto_item": "path/to/photo"
            },
            {
                "nama": "Kertas",
                "harga_x_quantity": "Rp. 2000 x 40 pcs",
                "harga_per_item": 80000,
                "path_foto_item": "path/to/photo"
            }
        ],
        "total_harga": 120000,
        "list_id": "UBFUI5qWAJH9aCiYOONsfH0cJcjn9I4X",
        "mitra_id": 5
    }
}
```

### Mengkonfirmasi list dan masuk ke transaksi
list akan dikosongkan
###  http://127.0.0.1:5000/konfirmasi-list GET
#### Header
```
Content-Type: application/json
```
### Body
```
{
    "mitra_id": <int>
}
```
#### Response
```
{
    "data": {
        "mitra": {
            "nama_mitra": "E",
            "alamat_mitra": "71754 Kuvalis Run\nBurdetteview, WY 51212",
            "rating_mitra": "5.0",
            "path_foto_mitra": null
        },
        "items": [
            {
                "nama": "Botol kaca",
                "harga_x_quantity": "Rp. 1000 x 40 pcs",
                "harga_per_item": 40000,
                "path_foto_item": "path/to/photo"
            },
            {
                "nama": "Kertas",
                "harga_x_quantity": "Rp. 2000 x 40 pcs",
                "harga_per_item": 80000,
                "path_foto_item": "path/to/photo"
            }
        ],
        "total_harga": 120000,
        "list_id": "UBFUI5qWAJH9aCiYOONsfH0cJcjn9I4X",
        "mitra_id": 5
    }
}
```

### Daftar Transaksi
###  http://127.0.0.1:5000/transaksi?status={status_id} GET
status_id boleh diisi boleh tidak
Keterangan status
1	"Mengunggu konfirmasi"
2	"Terkonfirmasi"
3	"Dijemput kurir"
4	"Transaksi selesai" 
#### Header
```
Content-Type: application/json
```
#### Response
```
{
    "data": [
        {
            "nama_mitra": "D",
            "path_foto_mitra": "path/to/photo",
            "total_harga_transaksi": 29500,
            "status_transaksi": "Mengunggu konfirmasi",
            "transaksi_url": "http://127.0.0.1:5000/transaksi/{id}"
        }
        ...
    ]
}
```

### Detail transaksi
###  http://127.0.0.1:5000/transaksi/{id} GET
id berupa string
#### Header
```
Content-Type: application/json
```
#### Response
```
{
    "data": {
        "mitra": {
            "nama_mitra": "D",
            "alamat_mitra": "2774 Kshlerin Field Suite 608\nEllisbury, RI 06678-2293",
            "rating_mitra": "5.0",
            "path_foto_mitra": "path/to/photo"
        },
        "items": [
            {
                "nama_item": "Botol kaca",
                "harga_x_quantity": "Rp. 500 19 pcs",
                "harga_per_item": 9500,
                "path_foto": "http://localhost:5000/path"
            },
            {
                "nama_item": "Plastik",
                "harga_x_quantity": "Rp. 2000 10 pcs",
                "harga_per_item": 20000,
                "path_foto": "http://localhost:5000/path"
            }
        ],
        "status": "Mengunggu konfirmasi"
    }
}
```

### Item saya
###  http://127.0.0.1:5000/transaksi/{id} GET
id berupa string
#### Header
```
Content-Type: application/json
```
#### Response
```
{
    "data": {
        "mitra": {
            "nama_mitra": "D",
            "alamat_mitra": "2774 Kshlerin Field Suite 608\nEllisbury, RI 06678-2293",
            "rating_mitra": "5.0",
            "path_foto_mitra": "path/to/photo"
        },
        "items": [
            {
                "nama_item": "Botol kaca",
                "harga_x_quantity": "Rp. 500 19 pcs",
                "harga_per_item": 9500,
                "path_foto": "http://localhost:5000/path"
            },
            {
                "nama_item": "Plastik",
                "harga_x_quantity": "Rp. 2000 10 pcs",
                "harga_per_item": 20000,
                "path_foto": "http://localhost:5000/path"
            }
        ],
        "status": "Mengunggu konfirmasi"
    }
}
```

### Daftar mitra
###  http://127.0.0.1:5000/daftar-mitra?search=<nama_mitra> GET
<nama_mitra> boleh kosong
#### Header
```
Content-Type: application/json
```
#### Response
```
{
    "data": [
        {
            "id_mitra": 4,
            "nama_mitra": "D",
            "alamat_mitra": "2774 Kshlerin Field Suite 608\nEllisbury, RI 06678-2293",
            "rating_mitra": "5.0",
            "path_foto_mitra": null,
            "url_mitra": "http://127.0.0.1:5000/daftar-mitra/4"
        }
        ...
    ]
}
```

### Detail mitra
###  http://127.0.0.1:5000/daftar-mitra/{id}
id adalah id mitra berupa int
#### Header
```
Content-Type: application/json
```
#### Response
```
{
    "data": {
        "mitra": {
            "nama_mitra": "D",
            "alamat_mitra": "2774 Kshlerin Field Suite 608\nEllisbury, RI 06678-2293",
            "rating_mitra": "5.0",
            "path_foto_mitra": null
        },
        "items": [
            {
                "nama": "Plastik",
                "harga_satuan": "Rp.2000/pcs"
            },
            {
                "nama": "Botol kaca",
                "harga_satuan": "Rp.500/pcs"
            },
            {
                "nama": "Kertas",
                "harga_satuan": "Rp.500/pcs"
            },
            {
                "nama": "Plastik",
                "harga_satuan": "Rp.2000/pcs"
            },
            {
                "nama": "Kardus",
                "harga_satuan": "Rp.500/pcs"
            }
        ]
    }
}
```
