from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time, random

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 1.네이버 검색창 + 키워드로 드라이버 get
search_query = "여의도 맛집"
serch_link = f"https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={search_query}"
driver.get(serch_link)
time.sleep(2)

# 2.place 더보기 탭을 클릭 (없으면 에러 출력)
try:
    btn_add_select = "#place-main-section-root > div > div.rdX0R > div"
    place_add_element = driver.find_element(By.CSS_SELECTOR, btn_add_select)
    place_add_element.click()
    time.sleep(1)
    btn_add1_select = "a.cf8PL"
    place_add1_element = driver.find_element(By.CSS_SELECTOR, btn_add1_select)
    place_add1_element.click()
except:
    print(f"{search_query}의 업체의 플레이스 순위를 알 수 없습니다.")
    
# 3.찾으려는 업체를 ID 기반으로 찾기
time.sleep(2)
a_id = "1332012839"
a_id_select = f"a[href*='/{a_id}?entry=pll']"
a_elements = driver.find_elements(By.CSS_SELECTOR, a_id_select)

a_element = random.choice(a_elements)
targer_a_element = a_element.find_element(By.XPATH,'./..')

# 3-2.없으면 인피니티 스크롤 5회 시도
# 4.여러 키워드, 여러 업체의 순위를 찾는 프로그램으로 변경
input()
