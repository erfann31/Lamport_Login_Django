# Lamport_Login_Django

<div dir="rtl">
این یک پروژه لاگین از طریق پروتوکل لمپورت و استفاده از زنجیره ی چکیده ها است.
</div>
<div dir="rtl">

## مراحل اجرا:

</div>

### Clone project

```
git clone https://github.com/erfann31/Lamport_Login_Django
```

### Run Project

Go to project root and execute the following command in console to run the Project:

```
python manage.py makemigrations customuser
python manage.py migrate
python manage.py runserver
```

<div dir="rtl">

### وارد شدن به واسط گرافیکی:

برای وارد شدن به واسط گرافیکی آدرس زیر را در مرورگر خود(ترجیحا فایرفاکس) وارد کنید:
</div>

```
http://localhost:8000/
```
<div dir="rtl">

## طریق کار:

### ثبت نام:

ابتدا کاربر در صفحه ی register عمل ثبت نام را ازطریق form های جنگو و با استفاده از توکن csrf انجام می‌دهد. با استفاده از فرم های جنگو یوزر نیم و پسورد به صورت امن به سرور فرستاده شده و متغیر iterations که نشان دهنده ی تعداد دفعات ورود است به صورت خودکار برابر 100 قرار میگیرد.<br>
سپس رمز ارسال شده توسط فرم به تعداد iterations بار چکیده سازی شده و در دیتابیس ذخیره می‌شود.
![image](https://github.com/erfann31/Lamport_Login_Django/assets/75057732/5347d6bf-6422-4423-8b09-614d2f1e497c)
### نمونه دیتای ذخیره شده در دیتابیس:
![image](https://github.com/erfann31/Lamport_Login_Django/assets/75057732/02c07dc8-ded4-4c39-a75f-7a17ba45929e)

<br>برای اطلاعات بیشتر به داکیومنت جنگو به آدرس زیر مراجعه فرمایید:
</div>

```
https://docs.djangoproject.com/en/5.0/ref/csrf/
```
<div dir="rtl">

### ورود:

کاربر در هنگام ورود با وارد کردن یوزر نیم و پسورد وارد می‌شود. <br>
عملی که در کلاینت انجام می‌شود به شرح زیر است:<br>
ابتدا با استفاده از یوزرنیم وارد شده توسط کاربر متغیر iterations از سرور دریافت می‌شود. <br>
سپس رمز وارد شده توسط کاربر به مقدار iterations-1 مرتبه چکیده سازی شده و به سرور ارسال می‌شود. سرور پس از دریافت رمز ارسالی توسط کلاینت آنرا یکبار چکیده کرده و با رمز ذخیره شده در دیتابیس مقایسه می‌کند. اگر 2 مقدار برابر بود اجازه ورود داده و مقدار رمز ارسال شده توسط کاربر در دیتابیس بجای رمز قبلی
ذخیره شده و از مقدار iterations یکی کم می‌شود. در غیر اینصورت پیغام خطا را برای کلاینت میفرستد.<br>
برای اطلاعات بیشتر به مقادیر چاپ شده در ترمینال سرور و کنسول مرورگر دقت کنید.
### تست با پسورد اشتباه:
![image](https://github.com/erfann31/Lamport_Login_Django/assets/75057732/21d432b3-70ae-45df-957e-65abee9ab412)
![image](https://github.com/erfann31/Lamport_Login_Django/assets/75057732/4903d7f8-d7e4-414c-b6c4-d6cdf0624e44)
![image](https://github.com/erfann31/Lamport_Login_Django/assets/75057732/104ef1b3-160b-4406-a0fd-98a3c5efa4d2)
### تست با پسورد درست:
![image](https://github.com/erfann31/Lamport_Login_Django/assets/75057732/4baab7da-4928-4e6e-8eb4-fdfec5f758db)
![image](https://github.com/erfann31/Lamport_Login_Django/assets/75057732/6222f7af-00ac-4068-9cf3-28e666ce7097)
![image](https://github.com/erfann31/Lamport_Login_Django/assets/75057732/b775ce66-93bc-4a6f-b42f-5d8ba5b02dc9)


</div>
