## Installation

```
git init
git clone git@github.com:naomihc/projekakhir-backend.git
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
###  http://127.0.0.1:5000/auth/login (post)
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


## Mendeteksi image (login dulu)
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
    "result": "Kertas",
    "probability": "0.95"
}
```

## Dashboard (login dulu)
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

## List saya (login dulu)
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
untuk mengganti jumlah item
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
            "path_foto": null
        }
        ...
    ]
}
```

Pada saat mengisikan query search
###  http://127.0.0.1:5000/pilih-mitra?search=namamitra GET
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
###  http://127.0.0.1:5000/pilih-mitra/{id} GET
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
                "path_foto_item": "http://localhost:5000/static/uploads/Botol_Kaca_Coca_Cola_Sprite_Fanta.jpg"
            },
            {
                "nama": "Kertas",
                "harga_x_quantity": "Rp. 2000 x 40 pcs",
                "harga_per_item": 80000,
                "path_foto_item": "http://localhost:5000/static/uploads/Timbunan_Sampah_Kertas.jpg"
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
                "path_foto_item": "http://localhost:5000/static/uploads/Botol_Kaca_Coca_Cola_Sprite_Fanta.jpg"
            },
            {
                "nama": "Kertas",
                "harga_x_quantity": "Rp. 2000 x 40 pcs",
                "harga_per_item": 80000,
                "path_foto_item": "http://localhost:5000/static/uploads/Timbunan_Sampah_Kertas.jpg"
            }
        ],
        "total_harga": 120000,
        "list_id": "UBFUI5qWAJH9aCiYOONsfH0cJcjn9I4X",
        "mitra_id": 5
    }
}
```