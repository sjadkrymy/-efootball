import requests
import os
from pathlib import Path

def download_hacker_images():
    # لینک عکس که شما دادید
    image_url = "https://s6.uupload.ir/files/1581597-مفهومی-برای-هکر-مجرمان-اینترنتی-حمله-سایبری_1eg8.jpg"
    
    # مسیر ذخیره‌سازی
    base_path = "/storage/emulated/0/Download/هک_شد"
    
    try:
        # ایجاد پوشه
        os.makedirs(base_path, exist_ok=True)
        print(f"📁 پوشه ایجاد شد: {base_path}")
        
        print("⏳ در حال دانلود عکس از سرور...")
        
        # هدر برای شبیه‌سازی مرورگر
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # دریافت فایل از سرور
        response = requests.get(image_url, headers=headers, stream=True, timeout=30)
        response.raise_for_status()
        
        # خواندن داده‌های عکس
        image_data = response.content
        file_size = len(image_data) / 1024  # اندازه به کیلوبایت
        
        print(f"✅ عکس اصلی دانلود شد")
        print(f"📊 اندازه فایل: {file_size:.1f} KB")
        print("⏳ در حال ایجاد 50 کپی...")
        
        # ایجاد 50 کپی از عکس
        success_count = 0
        
        for i in range(1, 51):
            filename = f"عکس_هک_{i:02d}.jpg"
            file_path = os.path.join(base_path, filename)
            
            try:
                # ذخیره کپی عکس
                with open(file_path, 'wb') as f:
                    f.write(image_data)
                
                success_count += 1
                
                # نمایش پیشرفت
                if i % 10 == 0:
                    print(f"✅ {i}/50 کپی ایجاد شد...")
                    
            except Exception as e:
                print(f"❌ خطا در ذخیره {filename}: {e}")
        
        # محاسبه فضای استفاده شده
        total_size = (file_size * success_count) / 1024  # به مگابایت
        
        # نتیجه نهایی
        print("\n" + "=" * 40)
        print("🎉 عملیات با موفقیت تکمیل شد!")
        print("=" * 40)
        print(f"📁 پوشه: هک_شد")
        print(f"📸 تعداد عکس‌های ذخیره شده: {success_count}")
        print(f"💾 فضای استفاده شده: {total_size:.2f} MB")
        print(f"📍 مسیر: {base_path}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ خطا در اتصال به اینترنت: {e}")
    except Exception as e:
        print(f"❌ خطای ناشناخته: {e}")

def check_folder_contents():
    """بررسی محتوای پوشه بعد از دانلود"""
    base_path = "/storage/emulated/0/Download/هک_شد"
    
    if os.path.exists(base_path):
        files = os.listdir(base_path)
        print(f"\n📋 لیست فایل‌های در پوشه:")
        print("-" * 30)
        for file in files[:10]:  # نمایش 10 فایل اول
            print(f"📄 {file}")
        if len(files) > 10:
            print(f"... و {len(files) - 10} فایل دیگر")
    else:
        print("❌ پوشه ایجاد نشده است!")

if __name__ == "__main__":
    download_hacker_images()
    print("\n")
    check_folder_contents()
