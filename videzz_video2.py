import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
import random
from fake_useragent import UserAgent
import pickle
import re

import chromedriver_autoinstaller

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chromedriver_autoinstaller.install()

# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# ua = UserAgent()
# options.add_argument(f"user-agent={ua.random}")
# options.add_argument('--start-maximized')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-gpu')

# driver = uc.Chrome(options=options)

# # Disable WebDriver property in JavaScript
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

def create_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    ua = UserAgent()
    options.add_argument(f"user-agent={ua.random}")
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    return options



# Di chuyển chuột ngẫu nhiên
def random_mouse_move(driver):
    try:
        # Lấy kích thước cửa sổ hiện tại
        window_width = driver.execute_script("return window.innerWidth;")
        window_height = driver.execute_script("return window.innerHeight;")

        # Di chuyển chuột trong phạm vi cửa sổ trình duyệt
        action = ActionChains(driver)
        x_offset = random.randint(-window_width//2, window_width//2)
        y_offset = random.randint(-window_height//2, window_height//2)

        # Di chuyển chuột ngẫu nhiên trong phạm vi này
        action.move_by_offset(x_offset, y_offset).perform()
        time.sleep(random.uniform(0.5, 1.5))  # Đảm bảo thời gian di chuyển không quá nhanh

    except Exception as e:
        # Kiểm tra và xử lý lỗi liên quan đến di chuyển chuột
        print(f"Error: {e}")

        # Cuộn trang để phần tử có thể nằm trong tầm nhìn
        driver.execute_script("window.scrollBy(0, 250);")  # Cuộn trang xuống
        time.sleep(1)  # Thời gian nghỉ ngắn sau khi cuộn


link_list = [
    "https://vidoza.net/ztpgu8by8ikr.html",
    "https://vidoza.net/omaoqnc6mrr6.html",
    "https://vidoza.net/iy1vzopdpztr.html",
    "https://vidoza.net/hybefuiy04fm.html",
    "https://vidoza.net/hwz4y0vkaoq1.html",
    "https://vidoza.net/peigyecqfx1p.html",
    "https://vidoza.net/98bg1sjnusu1.html",
    "https://vidoza.net/pbzkuh20pwnj.html",
    "https://vidoza.net/cjpgc87qip3n.html",
    "https://vidoza.net/dy0rv0p7h3nh.html",
    "https://vidoza.net/3xqk80ieu79e.html",
    "https://vidoza.net/4x20dqp8mj0r.html",
    "https://vidoza.net/pjujya2fuysm.html",
    "https://vidoza.net/w8jecxpis8mm.html",
    "https://vidoza.net/uxh6vhimfl6g.html",
    "https://vidoza.net/fvqpwzxxds2c.html",
]

link_list2 = [
    "https://vidoza.net/f9vlu78gt2vj.html",
    "https://vidoza.net/8u9ti0wv4d6j.html",
    "https://vidoza.net/yra3hrl5rc9q.html",
    "https://vidoza.net/jffzwuq1vqhy.html",
   "https://vidoza.net/y12z7rz8q6nm.html",
   "https://vidoza.net/peuzdqx40851.html",
    "https://vidoza.net/o60h83je6j00.html",
    "https://vidoza.net/rmw582erq23j.html",
    "https://vidoza.net/deu8rmgdc20q.html",
    "https://vidoza.net/pa75dzhugauv.html",
    "https://vidoza.net/lw2o42dajez1.html",
    "https://vidoza.net/k1x9y71oncoh.html"
]

selected_links = random.sample(link_list, 2)
selected_links2 = random.sample(link_list2, 2)
selected_links = selected_links + selected_links2
print(len(selected_links))
def run_main_selenium():

    for link in selected_links:
      for i in ["1", "2", "2"]:
        driver = webdriver.Chrome(options=create_chrome_options())
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        driver.get("https://www.dailymotion.com/playlist/x9dd5m")
        time.sleep(random.uniform(5, 10))

        driver.get(link)
        time.sleep(random.uniform(3, 5))
        random_mouse_move(driver)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='vplayer']")))

        for i in range(5):
            try:
                play_button_xpath = "//button[@title='Play Video']"
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, play_button_xpath)))
                play_button = driver.find_element(By.XPATH, play_button_xpath)
                driver.execute_script("arguments[0].scrollIntoView(true);", play_button)
                # driver.save_screenshot("screenshot_{}.png".format(time.time()))
                play_button.click()

                # Click Play
                driver.execute_script("""
                    var playButton = document.evaluate("//div[@id='vplayer']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    if (playButton) {
                        playButton.scrollIntoView({ behavior: 'smooth', block: 'center' });
                        setTimeout(function() { playButton.click(); }, 500);
                    }""")
                time.sleep(5)
                driver.save_screenshot(f"screenshot_{i}.png")
                random_mouse_move(driver)
                random_mouse_move(driver)

            except Exception as e:
                    print(f"Error: {e}")
                    try:
                        driver.execute_script("""
                                    var element = document.getElementById('vplayer');
                                  var clickEvent = new MouseEvent('click', {
                                    bubbles: true,
                                    cancelable: true,
                                    view: window
                                  });
                                  element.dispatchEvent(clickEvent); """)


                        try:
                                element = driver.find_element(By.XPATH, play_button_xpath)
                                actions = ActionChains(driver)

                                # Click tại tọa độ (x_offset, y_offset) so với phần tử
                                actions.move_to_element_with_offset(element, 5, 5).click().perform()
                                time.sleep(30)
                                driver.save_screenshot("screenshot_{}.png".format(i))
                        except Exception as e:
                                print(f"PyAutoGUI click failed: {e}")

                    except Exception as click_error:
                        print(f"Khong the click toa do: {click_error}")
        time.sleep(150)
        driver.save_screenshot("screenshot_final.png")


      # Tải video
      download_button_xpath = "//a[@class='btn btn-success btn-lg btn-download btn-download-n']"
      for i in range(5):
          try:
                  # Find and click the download button
                  download_button = driver.find_element(By.XPATH, download_button_xpath)
                  download_button.click()
                  time.sleep(random.uniform(1, 3))
                  random_mouse_move()
                  driver.save_screenshot(f"screenshot_{i}.png")

                  # Handle captcha if present
                  try:
                      captcha_iframe = WebDriverWait(driver, 10).until(
                          ec.presence_of_element_located((By.TAG_NAME, 'iframe'))
                      )
                      ActionChains(driver).move_to_element(captcha_iframe).click().perform()

                      captcha_box = WebDriverWait(driver, 10).until(
                          ec.presence_of_element_located((By.ID, 'g-recaptcha-response'))
                      )
                      driver.execute_script("arguments[0].click()", captcha_box)
                      time.sleep(10)
                  except Exception:
                      print("Captcha not found")
          except Exception as e:
                  print(f"Error: {e}")


      # driver.save_screenshot("screenshot_{}.png".format(time.time()))
      # time.sleep(150)
      driver.quit()

run_main_selenium()
