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
###  http://127.0.0.1:5000/scan-img
#### Header
```
Content-Type: application-json
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