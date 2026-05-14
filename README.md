# Dars Jadvali — Mobile + Kiosk + Admin Panel

## O'rnatish

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Sahifalar

| URL | Tavsif |
|-----|--------|
| `/` | Mobile versiya — guruh tanlash + haftalik jadval (telefon uchun) |
| `/kiosk/` | Kiosk versiya — katta ekran, chap sidebar, light theme |
| `/display/` | Display versiya — katta ekran, dark theme |
| `/admin-panel/` | Admin panel |
| `/admin-panel/login/` | Admin kirish |

## Admin login (standart)
- Login: `admin`
- Parol: `admin123`

## Serverga deploy (Ubuntu)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

## Excel yuklash tartibi

**Bitta guruh:**
1. Admin panel → "Yangi Guruh" → nom/rang/ikonka tanlang
2. "Excel Yuklash" → faylni yuklang

**Barcha guruhlar bir vaqtda:**
1. Admin panel → "Bulk Upload" → bitta Excel faylni yuklang
2. Har bir varaq alohida guruh sifatida yaratiladi

## Excel fayl formati

Ustunlar tartibi:

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Sana | Hafta kuni | Para | Vaqt | Modul | Tur | O'qituvchi | Xona |
