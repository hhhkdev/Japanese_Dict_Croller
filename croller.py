from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# 버전 114.0.5735.199(공식 빌드) (64비트)
driver = webdriver.Chrome()

LEVEL = 5
S_NUM, L_NUM = 1, 75

j_arr, p_arr, m_arr = [], [], []

for p in range(S_NUM, L_NUM+1):
    driver.get(f"https://ja.dict.naver.com/#/jlpt/list?level={LEVEL}&part=allClass&page={p}")
    sleep(1)
    COUNT = len(driver.find_elements(By.CLASS_NAME, "mean_list"))
    # 단어
    for i in range(1, COUNT+1):
        japanese = driver.find_element(By.CSS_SELECTOR, f"#my_jlpt_list_template > li:nth-child({i}) > div > a")
        j_arr.append(japanese.text)
    # 발음
        try:
            pronunciation = driver.find_element(By.CSS_SELECTOR, f"#my_jlpt_list_template > li:nth-child({i}) > div > span.pronunciation")
            p_arr.append(pronunciation.text)
        except:
            p_arr.append('[]')
    # 뜻
        mean = driver.find_element(By.CSS_SELECTOR, f"#my_jlpt_list_template > li:nth-child({i}) > ul > li > p")
        m_arr.append(mean.text)
        
for i in range(0, len(j_arr)):
    out = [i+1, j_arr[i], p_arr[i], m_arr[i]]
    print(*out)