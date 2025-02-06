from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time, random

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 1.네이버 검색창 + 키워드
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
a_id = "1332012839" # 신홍러우 여의도점  ID
a_id_select = f"a[href*='/{a_id}?entry=pll']"

# 3-2.없으면 인피니티 스크롤 5회 시도
a_elements = driver.find_elements(By.CSS_SELECTOR, a_id_select)

a_element = random.choice(a_elements)
for _ in range(5):
    targer_a_element = a_element.find_element(By.XPATH,'./..')
    tagname = targer_a_element.get_attribute("tagName")
    if tagname == "LI":
        print("LI의 태그를 찾았습니다.")
        break
    a_element = targer_a_element
    
all_list_select =  "#_list_scroll_container > div > div > div.place_business_list_wrapper > ul > LI"
all_list_element = driver.find_elements(By.CSS_SELECTOR, all_list_select)
rank = 1
for uni_element in all_list_element:
    if uni_element == targer_a_element:
        break
    rank += 1
print(f"{search_query} // 현재 {rank}등에 노출되고 있습니다.")
# 4.여러 키워드, 여러 업체의 순위를 찾는 프로그램으로 변경
input()
