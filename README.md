## پروژه تماس تصویری با Django Channels, WebRTC و Redis

این پروژه یک اپ ساده تماس تصویری مبتنی بر Django Channels، WebRTC و Redis می‌باشد.

## امکانات

- **تماس تصویری:** امکان برقراری تماس تصویری بین دو کاربر (caller و callee).
- **سیگنالینگ Real-time:** استفاده از Django Channels برای مدیریت ارتباطات Real-time.
- **مدیریت وضعیت تماس:** ذخیره و مدیریت وضعیت‌های مختلف تماس تصویری از قبیل تماس در حال برقراری، عدم در دسترس بودن، قبول یا رد تماس و غیره.


## ساختار پروژه

```
django_video_call/
├── django_video_call
│   ├── core
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── routing.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── templates
│   │   ├── account
│   │   │   ├── login.html
│   │   │   ├── logout.html
│   │   │   └── register.html
│   │   ├── base.html
│   │   └── videos
│   │       └── video_chat.html
│   └── video
│       ├── admin.py
│       ├── apps.py
│       ├── consumers.py
│       ├── forms.py
│       ├── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── routing.py
│       ├── tests.py
│       └── views.py
├── LICENSE
├── README.md
└── requirments.txt
```

## پیش نیازها

برای اجرای این پروژه به موارد زیر نیاز دارید:

- **Python**
- **Django**
- **Django Channels**
- **Redis Server**
- **Daphne** 

### نصب و راه‌اندازی

#### 1. کلون کردن مخزن

```bash
git clone https://github.com/eric-py/DjangoVideoCall.git
cd DjangoVideoCall
```

#### 2. ایجاد محیط مجازی و نصب وابستگی‌ها

```bash
python -m venv .venv
source .venv/bin/activate  # در ویندوز: venv\Scripts\activate
pip install -r requirments.txt
```

#### 3. راه‌اندازی Redis

اطمینان حاصل کنید که Redis بر روی سیستم شما نصب و در حال اجرا است.

#### 4. اجرای Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. اجرای اپ

```bash
python manage.py runserver
```

### استفاده

1. پس از اجرای سرور، مرورگر خود را باز کنید و به آدرس `http://127.0.0.1:8000/` مراجعه نمایید.
2. با استفاده از فرم‌های موجود در بخش حساب کاربری (login/register) وارد سیستم شوید.
3. پس از ورود، وارد بخش تماس‌های تصویری میشوید و با وارد کردن آیدی کاربر در بخش تماس، یک تماس تصویری برقرار کنید.