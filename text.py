from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ระบุพาธของ ChromeDriver
chrome_driver_path = "C:/Users/jay/chromedriver.exe"

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")

try:
    # ค้นหา element ของชื่อโรงพยาบาล
    result = driver.find_element(By.CLASS_NAME, "logo-title").text

    # ใช้ assert เพื่อตรวจสอบข้อความ
    assert result == "โรงพยาบาลสมเด็จพระสังฆราช องค์ที่ ๑๗", "Fail"

    print("Success")
except Exception as e:
    print("Fail")
    print(str(e))

time.sleep(2)
