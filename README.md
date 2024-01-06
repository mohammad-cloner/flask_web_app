# Flask Web App by google login and share context to Telegram 
##  برنامه فلسک با گوگل لاگین و قابلیت ارسال مطالب در تلگرام

[![Screenshot-2024-01-06-003246.png](https://i.postimg.cc/fRP0GHtk/Screenshot-2024-01-06-003246.png)](https://postimg.cc/3kgRpFZH)


programing and Design by mohammad Reza jamei
طراحی فرانت اند و بک اند توسط محمدرضا جامعی 

- Flask Python 
- HTMl, CSS, JS
- ✨Google and Telegram API ✨
# مقدمه 


<div dir="rtl"> این پروژه یک برنامه وب کارآمد به همراه سیستم احراز هویت و ویژگی‌های امنیتی مدرن را با استفاده از چارچوب Flask در Python ارائه می‌دهد. <br> با استفاده از ماژول‌ها و کتابخانه‌های مختلف در این پروژه، انعطاف‌پذیری و قابلیت توسعه برنامه وب را به نمایش می‌گذاریم. در ابتدا، از `Blueprint` در Flask برای سازمان‌دهی و تفکیک روت‌ها و نگهداری قسمت‌های مختلف برنامه استفاده می‌کنیم، که این به ما اجازه می‌دهد تا برنامه را به بخش‌هایی مستقل و قابل مدیریت تقسیم کنیم. <br>ماژول `Flask-Login` برای مدیریت جلسات کاربران و ارائه مکانیزم‌هایی مانند `login_user` و `logout_user` به کار می‌رود، که تجربه کاربری بهتری را با مدیریت وضعیت ورود در برنامه فراهم می‌آورد. احراز هویت از طریق گوگل با استفاده از ماژول‌های مربوط به Google OAuth2 و Flow انجام می‌گیرد، که کاربران را قادر می‌سازد تا با استفاده از حساب‌های کاربری گوگل خود به سادگی وارد سیستم شوند. <br>بخش `flask_mail` برای ارسال ایمیل‌هایی با محتوای سفارشی به کاربران استفاده می‌شود، مانند ارسال رمز عبور موقت که در صورت ایجاد حساب کاربری جدید یا درخواست تغییر رمز عبور رخ می‌دهد. همچنین، قابلیت‌های امنیتی مانند `csrf`, که محافظت در برابر حملات 'Cross-Site Request Forgery' را فراهم می‌آورد، به طور کامل پیاده‌سازی شده‌اند. سیستم پیام‌رسانی با Telegram از طریق وب‌سرویس API این پلتفرم برای ارسال پیام‌های آنی از درون برنامه به کاربران یا مدیریت سیستم به کار می‌رود. این قابلیت توسط تابع `send_telegram_message` محقق شده و زیرساخت‌های لازم برای برقراری ارتباط با API Telegram را فراهم می‌آورد.<br> دیتابیس و مدل‌های مربوطه با استفاده از SQL Alchemy در Flask مدیریت می‌شوند، که یک لایه انتزاعی برای ساده‌سازی ارتباط با دیتابیس و کار با اطلاعات می‌باشد. <br>در نهایت، این پروژه نمونه‌ای است از چگونگی ایجاد یک برنامه وب کامل و معاصر که شامل فرآیندهای ورود به سیستم، خروج از سیستم، ثبت‌نام، تغییر رمز وب‌ها، و احراز هویت سوم شخص می‌باشد. این سیستم پشتیبانی از خدمات Google و Telegram را یکپارچه کرده و با ارائه یک رابط کاربری واکنش‌گرا به وسیله HTML و CSS، تجربه کاربری جذاب و موثری را ارائه می‌دهد. </div>

# دایرکتوری
<div dir="rtl"> این پروژه شامل دایرکتوری های اصلی به نام های: 

 - Flask-Web-App-Tutorial

<div dir="rtl">دایرکتوری اصلی برنامه که تمامی فایل ها از جمله برنامه اصلی main.py در آن قرار دارد . 
 </div>

 - venv

<div dir="rtl">
virtual environment که در آن کتابخانه ها و ماژول های مورد نیاز برنامه و Scripts ها قرار دارد. 
 </div>
 
 - website
 <div dir="rtl">
 در این دایرکتوری برنامه های پایتون و قالب های HTML و CSS قرار دارد .
<br>فایل های برنامه که شامل init.py ,auth.py , views.py,models.py,client_secret.json  می باشد در این دایرکتوری ذخیره گردیده که در ادامه در مورد کاربرد هرکدام صحبت می کنیم. 
 </div>
 
 - website/templates
 <div dir="rtl">
 در این دایرکتوری فایل های HTML ذخیره شده است. 
 </div>
 
 - website/static
 <div dir="rtl">
فایل های CSS و JS در این دایرکتوری قرار دارند، همچنین تصاویر پروژه نیز در دایرکتوری assest در این پوشه قرار دارد. 
 </div>
 
# توضیحات برنامه نویسی 

 <div dir="rtl">
در این قسمت فایل های برنامه را قرار می دهیم و در مورد هرکدام از فایل ها توضیحات لازم را ارائه می دهیم : 
 </div>
 

 - main.py

```py
from website import create_app  
  
app = create_app()  
  
  
if __name__ == '__main__':  
    app.run(debug=True)
```
 <div dir="rtl">
 این کد ، یک الگوی رایج در اپلیکیشن‌های Flask است و وظیفه‌ای که انجام می‌دهد به شرح زیر است:<br>
 `</div>

`from website import create_app`
 <div dir="rtl">
` این خط کد از ماژول به نام `website` تابعی به نام `create_app` را وارد می‌کند. `website`  یک پکیج یا دایرکتوری در استراکچر پروژه است که حاوی کد اپلیکیشن Flask است.<br> تابع `create_app` این اجازه را به ما می‌دهد که نمونه‌ای از برنامه Flask را ایجاد و پیکربندی کنیم، به این صورت که تمام ماژول‌ها، پیکربندی‌ها، مسیرها، و الحاقات مورد نیاز برنامه را اضافه می‌کنید.
 `</div>
 
`app = create_app()`
 <div dir="rtl">
 این خط کد با فراخوانی تابع `create_app()`، یک نمونه از اپلیکیشن Flask را می‌سازد و در متغیر `app` قرار می‌دهد. این نمونه شامل تمام تنظیمات و تابع‌های درونی اپلیکیشن  می‌شود و آماده اجرا است.
 </div>
 

`if __name__ == '__main__'`
 <div dir="rtl">
 این قطعه کد بررسی می‌کند که آیا این فایل (`__name__` معادل `'__main__'`) به عنوان اسکریپت اصلی اجرا شده است. در Python، اگر یک فایل به صورت مستقیم اجرا شود (نه به عنوان ماژول وارد شود)، متغیر `__name__` مقدار `'__main__'` را به خود می‌گیرد. این بدین معناست که شما می‌توانید قطعاتی از کد را مشخص کنید که فقط هنگام اجرای فایل به عنوان اسکریپت ریشه اجرا شوند. 
 </div>


`app.run(debug=True)`
 <div dir="rtl">
 نهایتاً، اگر فایل به صورت مستقیم اجرا شده باشد، این خط کد سرور توسعه فلسک را با فعال بودن حالت دیباگ اجرا می‌کند. وقتی `debug=True` باشد، سرور در هر زمان که تغییری در کد مشاهده کند، برنامه را به صورت خودکار بازنگری می‌کند و همچنین یک صفحه خطای دیباگر را در مرورگر نمایش می‌دهد که به توسعه‌دهندگان کمک می‌کند تا خطاهای برنامه را راحت‌تر شناسایی و رفع کنند. 
پس، در خلاصه این کد الگوی استانداردی برای راه‌اندازی یک اپلیکیشن Flask برای محیط توسعه است و هدف آن جدا کردن ایجاد اپلیکیشن (که ممکن است شامل پیکربندی‌های متفاوت باشد) از اجرای آن است.
 </div>
  </div>
  
  

 - auth.py
 -  `csrf = CSRFProtect(app)`:  

 <div dir="rtl">
    در این قسمت کد، یک لایه محافظتی به نام Cross-Site Request Forgery (CSRF) برای برنامه اضافه می‌کند تا از فرم‌های وب در برابر حملات CSRF محافظت کند.
 </div>
 
 -  `auth = Blueprint('auth', __name__)`:  
 <div dir="rtl">
    یک Blueprint به نام ‘auth’ ایجاد می‌کند که به عنوان یک کامپوننت قابل استفاده مجدد عمل می‌کند؛ به این صورت که می‌توان شاخه‌های مختلفی از مسیرها (URL routes)، دیدگاه‌ها (views) و فرم‌ها را در اپلیکیشن Flask  سازماندهی کرد.
 </div>
 
 -  `app.secret_key`:  
 <div dir="rtl">
    این خط کلید مخفی برنامه‌ای که برای امضای جلسه کوکی‌ها و دیگر نیازهای امنیتی استفاده می‌شود را تعریف می‌کند.
    
 </div>
 
 -  `os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"`:  
    این تنظیم به برنامه اجازه می‌دهد تا در حین توسعه (و نه در محیط تولید) درخواست‌های HTTP ساده را برای OAuth بپذیرد.
    
 -  `flow = Flow.from_client_secrets_file(...)`:  
 <div dir="rtl">
    این کد بخشی از مکانیزم OAuth 2.0 است که برای احراز هویت کاربران با استفاده از حساب‌های گوگل از آن استفاده می‌شود.
     </div>
     
 -  `send_telegram_message(...)`:  

 <div dir="rtl">
    یک تابع برای ارسال پیام به چت‌بات تلگرام است که از API تلگرام استفاده می‌کند.
     </div>
     
 -  `login_is_required`:  
 <div dir="rtl">
    یک دکوریتور که برای محافظت از دیدگاه‌های اپلیکیشن است که نیاز به اصالت کاربر دارند و کاربر باید لاگین شده باشد.
     </div>
     
 -  `send_email(...)`:  
 <div dir="rtl">
    توسعه‌دهنده می‌تواند با استفاده از این تابع، ایمیل‌هایی با پیام‌های دلخواه بفرستد.
     </div>
     
 -  `@auth.route(...)`:  

  <div dir="rtl">
    این تعریف‌های مسیر (route definitions) برای مدیریت ورود و ثبت‌نام کاربران، احراز هویت گوگل (Google auth)، خروج از حساب و تغییر رمز عبور هستند.
     </div>
     
 -  `login()`, `login_bygoogle()`, `callback()`, `logout()`, `sign_up()`, `Task_note()`, `send_to_telegram()`, `change_password()`:  

  <div dir="rtl">
    این‌ها توابع مختلفی هستند که مسیرهای کنترل کننده ورود کاربر، خروج از سیستم، احراز هویت Google OAuth، ثبت نام، و چند عملکرد دیگر را تعریف می‌کنند.
به طور کلی، این کد بخشی از یک سیستم وب است که شامل ویژگی‌های مدیریت کاربر، احراز هویت OAuth با گوگل و ارتباط با سرویس‌های خارجی مانند Telegram است.
     </div>
     
 - `client_secrets_file`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`: 
  <div dir="rtl">
این‌ها ثابت‌ها و مقادیر پیکربندی هستند که اطلاعات مرتبط با احراز هویت اوت (OAuth) و دسترسی بات تلگرام را نگهداری می‌کنند. این مقادیر برای تنظیم احراز هویت Google و فراخوانی API تلگرام استفاده می‌شوند.
     </div>
     
 - `login_bygoogle()`, `callback()`: 
  <div dir="rtl">
این توابع بخشی از فرآیند ورود به سیستم با استفاده از حساب کاربری گوگل هستند. `login_bygoogle` یک URL برای احراز هویت اوت گوگل ایجاد می‌کند و کاربر را به آن هدایت می‌کند. `callback` جزئی است که پاسخ احراز هویت را دریافت می‌کند و توکن‌ها را جمع‌آوری کرده و تاییدیه کاربر را بررسی می‌کند.
     </div>
     
 - `login_user(user, remember=True)`: 
  <div dir="rtl">
این دستور بخشی از کتابخانه Flask-Login است و برای جلسه کاربری فعلی وارد کاربر می‌شود. اگر `remember` بر روی `True` تنظیم شود، جلسه کاربر برای مدت زمان طولانی‌تری (حتی پس از بستن مرورگر) حفظ می‌شود.
     </div>

 - `redirect(url_for('views.home'))`:
  <div dir="rtl">
 این تابع مرورگر کاربر را به URL دیگری که با استفاده از نام دیدگاه تعریف شده است، هدایت می‌کند. در اینجا، `url_for('views.home')` به صفحه اصلی پس از ورود کاربر اشاره دارد.
     </div>
     
 - `db.session.add(...)`, `db.session.commit()`:
  <div dir="rtl">
 این کدها با استفاده از SQLAlchemy که به عنوان ORM کار می‌کند، اشیاء جدید را به دیتابیس اضافه و تغییرات را ثبت (commit) می‌کنند.
 <br>
 این کد  یک نمونه از یک برنامه پیچیده Flask است که می‌تواند احراز هویت، مدیریت جلسه کاربری، ارسال ایمیل، ارتباط با بات‌های تلگرام و دیگر ویژگی‌های پیشرفته‌ای که برای یک برنامه وب پویا نیاز است را انجام دهد.
     </div>
     

 - views.py

  <div dir="rtl">
این کد  حاوی  چندین مسیر (route) برای نمایش دیدگاه‌ها (views) مختلف در  برنامه وب  که بر پایه Flask نوشته شده است می باشد . برای هر یک از این views یک مسیر مشخص شده و با استفاده از دکوریتورهای مسیر وجود دارد  و به وسیله کنترل دسترسی هدایت می‌شوند.
     </div>

 - __init__.py

<div dir="rtl">
init.py شامل، تنظیمات اولیه برای یک برنامه وب ساخته شده با استفاده از چارچوب کاری Flask در زبان برنامه‌نویسی Python است. این کد شامل موارد زیر است:
</div>

1.  **SQLAlchemy**:

<div dir="rtl">
 یک نمونه از کتابخانه SQLAlchemy ایجاد شده است تا ارتباطات با پایگاه‌داده را مدیریت کند. نام پایگاه‌داده `database.db` تنظیم شده است.
</div>  

2.   **Decorator**:

<div dir="rtl">
 تابع `login_is_required` به عنوان یک decorator ایجاد شده تا بررسی کند که آیا کاربر با استفاده از Google وارد شده است یا خیر. اگر کاربر وارد نشده باشد (یعنی `google_id` در session نباشد)، درخواست با کد خطای 401 متوقف می‌شود.
    
</div>  

 -  **ایجاد نمونه Flask**:
<div dir="rtl">
 تابع `create_app` برنامه Flask را ایجاد می‌کند و پیکربندی‌های اولیه نظیر کلید مخفی و مسیر دیتابیس را تنظیم می‌کند. همچنین برای آزمایش، تنظیماتی را برای اجازه ارتباطات ناامن در OAuth فعال می‌کند (توجه داشته باشید که این تنظیم تنها باید در محیط توسعه و نه در تولید به کار رود).
    
</div>  

 -  **ثبت Blueprint‌**:
<div dir="rtl">
 دو Blueprint با نام‌های `views` و `auth` وارد و به برنامه اضافه می‌شوند که برای تعریف مسیرهای مختلف و جدا کردن بخش‌های احراز هویت و مشاهده صفحات به کار می‌روند.
    </div>  
    
 -  **پیکربندی Login Manager و User Loader**:
<div dir="rtl">
 `LoginManager` از کتابخانه‌ی Flask-Login برای مدیریت جلسه‌های کاربر و تابع `load_user` برای بارگذاری اطلاعات کاربر از پایگاه داده استفاده می‌کند.
    </div>  
    
 -  **ایجاد پایگاه داده**:
<div dir="rtl">
 یک تابع جداگانه به نام `create_database` دیتابیس برنامه را اگر هنوز ایجاد نشده باشد، می‌سازد و پیامی مبنی بر ایجاد پایگاه داده چاپ می‌کند.
    </div>  

 - models.py
  <div dir="rtl">
در این بخش از برنامه کد ها  دو مدل داده‌ای را در چارچوب کاری Flask با استفاده از SQLAlchemy ORM و Flask-Login تعریف می‌کند. `User` و `Note`.
    </div>  

     
## Google Authentication API
  <div dir="rtl">
در وب‌اپلیکیشن‌های مبتنی بر Flask، احراز هویت Google معمولاً با استفاده از پکیج هایی مثل OAuth 2.0 انجام می‌شود. این روند به طور کلی چندین مرحله دارد:
<br>
 مرحله 1: ایجاد پروژه‌ در Google Cloud Platform و تنظیم APIs<br>
اول از همه،  باید به [Google Cloud Console](https://console.cloud.google.com/)
[](https://console.cloud.google.com/)برویم، یک پروژه جدید ایجاد کنید و   Google+ API  را فعال سازیی کنیم.
    </div>  
    
[![Screenshot-2024-01-06-031519.png](https://i.postimg.cc/0N2cn5MD/Screenshot-2024-01-06-031519.png)](https://postimg.cc/BjkTQ0Cn)

  <div dir="rtl">
 مرحله 2: ساختن مشخصات OAuth 2.0<br>
در قسمت ‘Credentials’ در Google Cloud Console، باید یک مشخصه OAuth 2.0 ایجاد کنیم. این شامل ورودی‌هایی مانند راه‌اندازی آدرس های URI واسط برگشتی (redirect URIs) است که Google باید اطلاعات کاربر را به آنها بازگرداند.
<br>
مرحله 3: استفاده از مشخصات در برنامه Flask<br>
مشخصات اخذ شده از Google Cloud Console باید در برنامه‌ی Flask شما وارد شوند. این شامل ثبت شناسه مشتری (Client ID) و راز مشتری (Client Secret) در تنظیمات برنامه یا توسط متغیرهای محیطی است.
<br>
API دریافت شده در فایلی به نام client_secret.json در دایرکتوری website/client_secret.json ذخیره می شود که حاوی توکن ها ، کلایت آیدی و کلاینت سکرت می باشد ذخیره می گردد تا در زمان نیاز برای اعتبار سنجی کاربر توسط google auth فراخوانی گردد . 
</div>

  ```py
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

```

## Telegram API 
  <div dir="rtl">
API تلگرام (Telegram API) به توسعه‌دهندگان اجازه می‌دهد که به صورت برنامه‌ای با سرویس پیام‌رسانی تلگرام تعامل داشته باشند. از این API می‌توان برای ساخت بات‌ها، ارسال و دریافت پیام‌ها، ایجاد و مدیریت گروه‌ها، کانال‌ها و بسیاری کارکردهای دیگر استفاده کرد.
</div>

### Telegram Bot API
[![Screenshot-2024-01-06-095004.jpg](https://i.postimg.cc/QC6hXFXX/Screenshot-2024-01-06-095004.jpg)](https://postimg.cc/N2rWDf9V)

 <div dir="rtl">
 API مخصوص ایجاد و مدیریت بات‌ها است. بات‌های تلگرام می‌توانند به کاربران پاسخ دهند، دستورات را اجرا کنند، کارهای خودکاری را بر عهده بگیرند، و ....<br> برای شروع کار با Bot API،  نیاز به ساخت یک بات با استفاده از BotFather داریم که یک بات .خاص در تلگرام است.<br> BotFather یک token به  می‌دهد که این token به عنوان کلید API  عمل می‌کند و از آن برای تعامل با Bot API استفاده می‌شود.<br>
مثال‌هایی از کاربردهای Bot API عبارتند از:<br>
<ul>
<li>
   ارسال پیام‌های متنی، عکس، ویدئو، فایل‌ها، دکمه‌های inline و…
 </li>
 <li>
  ایجاد webhooks برای دریافت اطلاعیه‌های فوری پس از ارسال پیام به بات
</li>
<li>
   مدیریت پیام‌های رودررو با کاربران یا در گروه‌ها و کانال‌ها
</li>
</div>

```py
def send_telegram_message(chat_id, text):  
    token = '****************************'  
  url = f"https://api.telegram.org/bot{token}/sendMessage"  
  payload = {  
        'chat_id': -1002121162552,  
        'text': text,  
        'parse_mode': 'HTML'  
  }  
    response = requests.post(url, data=payload)  
    return response.ok
```
### Group link 
https://t.me/sendingflasktotelBot

 <div dir="rtl">
پیام های ارسالی برای 'chat_id': -1002121162552,  به آدرس بالا ارسال می شود . 
</div>

## Transport Error 
[![Screenshot-2024-01-06-100825.png](https://i.postimg.cc/Njv9SnPp/Screenshot-2024-01-06-100825.png)](https://postimg.cc/0bZyJVvw)
  <div dir="rtl">
برای استفاده از سرویس Google cloud در شرایط کشور ایران و استفاده از پروتکل های امنیتی مانند csfr محدودیت هایی وجود دارد که برای حل این محدودیت ها از سرویس های تغییر DNS استفاده شده است .<br>
از جمله سرویس های تغییر DNS موثر ، سرویس شکن می باشد .
</div>

[سایت شکن](https://shecan.ir/) 



## Jinja2
  <div dir="rtl">
  در این پروژه از موتور قالب بندی jinja2 برای جایگذاری اسامی و همانطور ارتباط با سمت سرور از طریق کلاینت استفاده شده است . 
  در زیر چند مثال از موتور قالب بندی jinja2  آورده شده است . 
</div>

<div dir="rtl">
  در این مثال با استفاده از موتور jinja2 در برنامه models.py نام کاربر و ایمیل آن گرفته شده و به کاربر نمایش داده می شود. 
  </div>
  <br>
  
```HTML
</div>  
 <div class="user-details hidden">  
 <p class="username">{{ user.first_name }}</p>  
 <p class="user-email">{{ user.email }}</p>  
 </div>
 </div>
```
<br>

  <div dir="rtl">
در اینجا با استفاده از jinja2 دستورات شرطی و حلقه برای تغییر رمز عبور توسط کاربر دریافت شده و توابع و آدرس های لازم برای تغییر رمز عبور فراخوانی شده است. 
  </div>
<br>

```HTML
         <h6 class="title"> Change Password</h6>  
  {% with messages = get_flashed_messages(with_categories=true) %}  
          {% if messages %}  
            {% for category, message in messages %}  
              <div class="alert alert-{{ category }}">{{ message }}</div>  
  {% endfor %}  
          {% endif %}  
        {% endwith %}  
<form class="pasform" method="POST" action="{{ url_for('auth.change_password') }}" >  
 <div class="form-pss" >  
 <label for="new_password">New Password</label>  
 <input type="password" class="form-control" id="new_password" name="new_password" required>  
 </div> <div class="form-pss">  
 <label for="confirm_password">Confirm New Password</label>  
 <input type="password" class="form-control" id="confirm_password" name="confirm_password" required>  
 </div> <button type="submit"> <i class="fa fa-password"></i> Change Password </button>  
  
 </form> 
 </div></div>
```
<br>

  <div dir="rtl">
با استفاده از این دستور در ساختار HTML ما یک صفحه به نام base.html را برای استفاده در صفحات دیگر گسترش می دهیم . 
  </div>
<br>

```HTML
{% extends "base.html" %}  
{% block title %}Task{% endblock %}  
{% block content %}

{% endblock %}
```
<br>

  <div dir="rtl">
مثال های دیگری برای  استفاده از موتور قالب بندی jinja2 نیز درون برنامه وجود دارد که همه آن ها مانند مثال های بالا عمل می کند 
  </div>
<br>

## Project image 
  <div dir="rtl">
عکس های مربوط به پروژه و صفحات آن در ادامه قرار داده می شود : 
  </div>
<br>

### Login page 
[![Screenshot-2024-01-06-105813.png](https://i.postimg.cc/1z0N3G40/Screenshot-2024-01-06-105813.png)](https://postimg.cc/8F5CyrRs)

### SignUp page
[![Screenshot-2024-01-06-105950.png](https://i.postimg.cc/L8pPKQ84/Screenshot-2024-01-06-105950.png)](https://postimg.cc/F7Tz0ZSw)

### Google Auth

[![Screenshot-2024-01-06-110236.png](https://i.postimg.cc/SNrSRgGx/Screenshot-2024-01-06-110236.png)](https://postimg.cc/bsZcFHM7)

<br>

  <div dir="rtl">
این صفحه با فراخوانی callback در auth.py اجرا می شود . 
  </div>
<br>

### Home page
[![Screenshot-2024-01-06-110459.png](https://i.postimg.cc/Y2D87H5r/Screenshot-2024-01-06-110459.png)](https://postimg.cc/6TRCVD6g)

[![Screenshot-2024-01-06-110610.png](https://i.postimg.cc/rwX1yFQk/Screenshot-2024-01-06-110610.png)](https://postimg.cc/Tp0LCxz7)

<br>

  <div dir="rtl">
در طراحی این صفحات از منوی ناوبری پویا استفاده شده است که توسط css و js طراحی گردیده است . 

  </div>
<br>

### Dashboard
[![Screenshot-2024-01-06-111037.png](https://i.postimg.cc/zBCBj8Tn/Screenshot-2024-01-06-111037.png)](https://postimg.cc/CBKSMyP1)

[![Screenshot-2024-01-06-132613.png](https://i.postimg.cc/J0Ssc1Vc/Screenshot-2024-01-06-132613.png)](https://postimg.cc/n9YVnfLC)

### Task
[![Screenshot-2024-01-06-111227.png](https://i.postimg.cc/P5Mn2J7f/Screenshot-2024-01-06-111227.png)](https://postimg.cc/bZd5vy84)

[![Screenshot-2024-01-06-111342.png](https://i.postimg.cc/y6hjJR3N/Screenshot-2024-01-06-111342.png)](https://postimg.cc/8s5M9jH8)

<br>

  <div dir="rtl">
در این صفحه قابلیت اضافه و حذف کردن note ها و ذخیره آن در دیتابیس وجود دارد . 

  </div>
<br>

### Telegram
[![Screenshot-2024-01-06-112313.png](https://i.postimg.cc/BvXL0rHF/Screenshot-2024-01-06-112313.png)](https://postimg.cc/FfXsbnPF)

<br>

  <div dir="rtl">
در این صفحه با استفاده از telegram Bot API پیام های نوشاه شده به آدرس آیدی گروه ارسال می گردد.
<br>
آدرس گروه در زیر قرار داده شده است ، که می توان با اضافه کردن ربات به گروه و دریافت آیدی گروه پیام ها را به هر گروه یا کانال دلخواه ارسال نمود. 
  </div>
<br>

https://t.me/flasktotel


### Setting
[![Screenshot-2024-01-06-132318.png](https://i.postimg.cc/SxBGNhn9/Screenshot-2024-01-06-132318.png)](https://postimg.cc/FYxSDwgF)

  <div dir="rtl">
در این صفحه می توان رمز عبور را تغییر داد 
  </div>
<br>

## Responsive

  <div dir="rtl">
این برنامه وب با کمک کدهای css و media-screen  برای تمامی دستگاه هایی که به وب متصل می شوند مناسب می باشد و رابط کاربری مناسبی دارد. نمونه کد های css در جهت رسپانسیو سازی برنامه وب در پایین آمده است . 
  </div>
<br>

```css
@media (max-device-width: 768px) {

.parent-container {

height: auto;

padding: 5px;

}
.container-task {

padding: 5px;

flex-direction: column;

width: auto;

resize: none;

}

.form-input{
padding: 10px;
}
.blog-content{
margin-left: 70px;
}
}
```

## Final points

 <div dir="rtl">
لازم به ذکر است که فایل client_secret.json بدلیل محرمانگی این فایل در این پروژه قرار نگرفته است و در صورتی که میخواهید برنامه را اجرا کنید این فایل و قسمت های token مربوط به API های تلگرام و گوگل باید توسط اکانت خودتان به صورتی که در قسمت های قبل صحبت کردیم تکمیل گردد . <br>
در صورت وجود هرگونه سوال و مشکل در برنامه می توانید از طریق راه های ارتباطی زیر در تماس باشید : 
  </div>
<br>

mohammadrezajamei2000@gmail.com
https://t.me/Dorrinnab2

 <div dir="rtl">
موفق باشید (محمدرضا جامعی)
  </div>

## Running The App

  

```bash

python  main.py

```

  

## Viewing The App

  

Go to `http://127.0.0.1:5000`
