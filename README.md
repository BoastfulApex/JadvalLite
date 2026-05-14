# 📅 Dars Jadvali — Info Kiosk + Admin Panel

## O'rnatish va ishga tushirish

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # yoki: admin / admin123 tayyor
python manage.py runserver
```

## Sahifalar

| URL | Tavsif |
|-----|--------|
| `/` | Kiosk — guruhlar + haftalik jadval |
| `/admin-panel/` | Admin panel |
| `/admin-panel/login/` | Admin kirish |

## Admin login (standart)
- Login: `admin`
- Parol: `admin123`

## Excel yuklash tartibi
1. Admin panel → "Yangi Guruh" → nom/rang/ikonka tanlang
2. "Excel Yuklash" → Excel faylni drag-drop yoki tanlab yuklang
3. Kiosk sahifasida guruh paydo bo'ladi

## Excel fayl formati
Har bir varaq bir guruh jadvali. Ustunlar tartibi:
`sana | hafta_kuni | para | vaqt | modul | tur | o'qituvchi | xona`
