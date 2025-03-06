import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
import random
from fake_useragent import UserAgent
import pickle
from selenium.common.exceptions import WebDriverException
import chromedriver_autoinstaller

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Tự động cài đặt ChromeDriver
chromedriver_autoinstaller.install()

# Thời gian chạy tối đa (35 phút)
MAX_RUN_TIME = 1730  # 35 phút (tính theo giây)

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
        window_width = driver.execute_script("return window.innerWidth;")
        window_height = driver.execute_script("return window.innerHeight;")
        action = ActionChains(driver)
        x_offset = random.randint(-window_width//2, window_width//2)
        y_offset = random.randint(-window_height//2, window_height//2)
        action.move_by_offset(x_offset, y_offset).perform()
        time.sleep(random.uniform(0.5, 1.5))
    except WebDriverException as e:
        print(f"Error: {e}")
        driver.execute_script("window.scrollBy(0, 250);")
        time.sleep(1)

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

selected_links = random.sample(link_list, 4)

def run_main_selenium():
    start_time = time.time()  # Lưu thời gian bắt đầu

    for link in selected_links:
        for i in ["1", "2", "3"]:
            # Kiểm tra nếu đã chạy quá 35 phút
            if time.time() - start_time >= MAX_RUN_TIME:
                print("Đã chạy đủ 35 phút, dừng ngay!")
                return  # Dừng chương trình

            driver = webdriver.Chrome(options=create_chrome_options())
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

            driver.get("https://www.dailymotion.com/playlist/x9dd5m")
            time.sleep(random.uniform(10, 30))

            driver.get(link)
            time.sleep(random.uniform(3, 5))
            random_mouse_move(driver)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='vplayer']")))

            for i in range(5):
                if time.time() - start_time >= MAX_RUN_TIME:
                    print("Đã chạy đủ 35 phút, dừng ngay!")
                    driver.quit()
                    return
                
                try:
                    play_button_xpath = "//button[@title='Play Video']"
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, play_button_xpath)))
                    play_button = driver.find_element(By.XPATH, play_button_xpath)
                    driver.execute_script("arguments[0].scrollIntoView(true);", play_button)
                    play_button.click()
                    driver.execute_script("""
                        var playButton = document.evaluate("//div[@id='vplayer']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                        if (playButton) {
                            playButton.scrollIntoView({ behavior: 'smooth', block: 'center' });
                            setTimeout(function() { playButton.click(); }, 500);
                        }
                    """)
                    time.sleep(5)
                    random_mouse_move(driver)
                    random_mouse_move(driver)
                except Exception as e:
                    print(f"Error: {e}")

            time.sleep(150)

            # Kiểm tra nếu đã chạy quá 35 phút
            if time.time() - start_time >= MAX_RUN_TIME:
                print("Đã chạy đủ 35 phút, dừng ngay!")
                driver.quit()
                return

            driver.quit()

        download_button_xpath = "//a[@class='btn btn-success btn-lg btn-download btn-download-n']"
        for i in range(5):
            if time.time() - start_time >= MAX_RUN_TIME:
                print("Đã chạy đủ 35 phút, dừng ngay!")
                driver.quit()
                return

            try:
                download_button = driver.find_element(By.XPATH, download_button_xpath)
                download_button.click()
                time.sleep(random.uniform(1, 3))
                random_mouse_move(driver)
            except Exception as e:
                print(f"Error: {e}")

    print("Kết thúc Selenium bot sau 35 phút.")

run_main_selenium()
