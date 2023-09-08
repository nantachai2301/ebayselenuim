from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# สร้าง instance ของเบราว์เซอร์
driver = webdriver.Chrome()  # ต้องมี Chrome WebDriver ใน PATH

# เปิดหน้าเว็บ eBay
driver.get("https://www.ebay.com")

# ขยายหน้าต่างเบราว์เซอร์ให้เต็มจอ
driver.maximize_window()

# ค้นหาคำว่า "car" ในช่องค้นหา
search_box = driver.find_element("name", "_nkw")
search_box.send_keys("car")
search_box.send_keys(Keys.RETURN)

# รอให้ผลการค้นหาปรากฏขึ้น
driver.implicitly_wait(10)  # รอไม่เกิน 10 วินาที

# ตรวจสอบคำว่า "car" ในเนื้อหาของหน้าเว็บ
page_content = driver.page_source
assert "car" in page_content, "Keyword 'car' not found in page content."



# หยุดทำงานเป็นเวลา 60 วินาที (1 นาที)
time.sleep(60)