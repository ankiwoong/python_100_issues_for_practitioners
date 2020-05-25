from selenium import webdriver
import time

# 100대 통계지표 엑셀 다운로드


def download_bok_statistics():

    driver = webdriver.Chrome("./Selenium/chromedriver")
    driver.implicitly_wait(3)
    driver.get("http://ecos.bok.or.kr/jsp/vis/keystat/#/key")

    excel_download = driver.find_element_by_css_selector('img[alt="download"]')
    driver.implicitly_wait(3)

    excel_download.click()
    time.sleep(5)

    driver.close()
    print("파일 다운로드 실행...")

    return None


# 함수 실행 - 100대 통계지표 엑셀 다운로드
download_bok_statistics()
