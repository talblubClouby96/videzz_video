import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium.common.exceptions import WebDriverException

import chromedriver_autoinstaller

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chromedriver_autoinstaller.install()

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

def random_mouse_move(driver):
    """Di chuyển chuột ngẫu nhiên trong cửa sổ trình duyệt."""
    try:
        window_width = driver.execute_script("return window.innerWidth;")
        window_height = driver.execute_script("return window.innerHeight;")
        action = ActionChains(driver)
        x_offset = random.randint(-window_width // 2, window_width // 2)
        y_offset = random.randint(-window_height // 2, window_height // 2)
        action.move_by_offset(x_offset, y_offset).perform()
        time.sleep(random.uniform(0.5, 1.5))
    except WebDriverException as e:
        print(f"Error in mouse move: {e}")
        driver.execute_script("window.scrollBy(0, 250);")
        time.sleep(1)

# Danh sách link mẫu
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

# Lấy ngẫu nhiên 2 link (có thể nhân đôi nếu cần)
selected_links = random.sample(link_list, 2)
# Nếu cần nhân đôi danh sách: selected_links = selected_links + selected_links
print("So link dc chon:", len(selected_links))

def run_main_selenium():
    # Lặp qua từng link được chọn
    for link in selected_links:
        # Khởi tạo driver cho mỗi link
        driver = webdriver.Chrome(options=create_chrome_options())
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # Truy cập trang dailymotion trước (có thể là bước khởi tạo session)
        driver.get("https://www.dailymotion.com/playlist/x9dd5m")
        time.sleep(random.uniform(10, 30))

        # Mở link cần tương tác
        driver.get(link)
        time.sleep(random.uniform(3, 5))
        random_mouse_move(driver)

        # Chờ phần tử player xuất hiện
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='vplayer']")))
        except Exception as e:
            print(f"Khong tim thay: {e}")

        play_button_xpath = "//button[@title='Play Video']"

        # Thực hiện thao tác click Play với 2 vòng lặp (nếu cần)
        for iteration in range(2):
            for attempt in range(2):
                try:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, play_button_xpath)))
                    play_button = driver.find_element(By.XPATH, play_button_xpath)
                    driver.execute_script("arguments[0].scrollIntoView(true);", play_button)
                    play_button.click()

                    # Dùng JS click bổ sung nếu cần
                    driver.execute_script("""
                        var playButton = document.evaluate("//button[@title='Play Video']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                        if (playButton) {
                            playButton.scrollIntoView({ behavior: 'smooth', block: 'center' });
                            setTimeout(function() { playButton.click(); }, 500);
                        }""")

                    time.sleep(5)
                    driver.save_screenshot(f"screenshot_{iteration}_{attempt}.png")
                    random_mouse_move(driver)
                    random_mouse_move(driver)
                    break  # Thoát vòng attempt nếu thành công
                except Exception as e:
                    print(f"Loi khi click play button (lan {attempt}): {e}")
                    try:
                        # Fallback: click bằng JavaScript thay cho ActionChains
                        fallback_element = driver.find_element(By.XPATH, play_button_xpath)
                        driver.execute_script("arguments[0].click();", fallback_element)
                        time.sleep(5)
                        driver.save_screenshot(f"screenshot_fallback_{iteration}_{attempt}.png")
                    except Exception as fallback_error:
                        print(f"Fallback click thay bai: {fallback_error}")
            time.sleep(5)
            driver.save_screenshot("screenshot_final.png")

        # Phần tải video
        download_button_xpath = "//a[contains(@class, 'btn-download')]"
        for attempt in range(5):
            time.sleep(2)
            try:
                download_button = driver.find_element(By.XPATH, download_button_xpath)
                driver.execute_script("arguments[0].scrollIntoView(true);", download_button)
                download_button.click()
                time.sleep(random.uniform(1, 3))
                random_mouse_move(driver)
                driver.save_screenshot(f"download_screenshot_{attempt}.png")

                # Xử lý captcha nếu có
                try:
                    captcha_iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
                    ActionChains(driver).move_to_element(captcha_iframe).click().perform()
                    captcha_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'g-recaptcha-response')))
                    driver.execute_script("arguments[0].click();", captcha_box)
                    time.sleep(5)
                except Exception:
                    print("Khong co capcha.")
                break  # Thoát nếu click download thành công
            except Exception as e:
                print(f"loi khi click download button (lan {attempt}): {e}")
        driver.quit()

run_main_selenium()
