{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d967afba-0da6-4a80-b47e-5a705c252536",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 149\u001b[0m\n\u001b[0;32m    144\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124msubsidy_data.json\u001b[39m\u001b[38;5;124m'\u001b[39m \u001b[38;5;66;03m# (2)\u001b[39;00m\n\u001b[0;32m    148\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m--> 149\u001b[0m     \u001b[43mcrawling_subsidy\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "Cell \u001b[1;32mIn[2], line 67\u001b[0m, in \u001b[0;36mcrawling_subsidy\u001b[1;34m()\u001b[0m\n\u001b[0;32m     65\u001b[0m WebDriverWait(driver, \u001b[38;5;241m10\u001b[39m)\u001b[38;5;241m.\u001b[39muntil(\u001b[38;5;28;01mlambda\u001b[39;00m driver: \u001b[38;5;28mlen\u001b[39m(driver\u001b[38;5;241m.\u001b[39mwindow_handles) \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m1\u001b[39m)\n\u001b[0;32m     66\u001b[0m driver\u001b[38;5;241m.\u001b[39mswitch_to\u001b[38;5;241m.\u001b[39mwindow(driver\u001b[38;5;241m.\u001b[39mwindow_handles[\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m])\n\u001b[1;32m---> 67\u001b[0m \u001b[43mtime\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43msleep\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m2\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m     69\u001b[0m \u001b[38;5;66;03m# CSS 셀렉터 설정\u001b[39;00m\n\u001b[0;32m     70\u001b[0m car_type_selector \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mbody > form > div > table > tbody > tr > td:nth-child(1)\u001b[39m\u001b[38;5;124m\"\u001b[39m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "import time\n",
    "import json\n",
    "import os\n",
    "\n",
    "def crawling_subsidy():\n",
    "    # 드라이버 설정 및 URL 이동\n",
    "    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))\n",
    "    url = 'https://ev.or.kr/nportal/buySupprt/initSubsidyPaymentCheckAction.do'\n",
    "    driver.get(url)\n",
    "    driver.maximize_window()\n",
    "\n",
    "    # 페이지 로드 대기\n",
    "    wait = WebDriverWait(driver, 10)\n",
    "\n",
    "    try:\n",
    "        # 'btnLocalCarPrc' 버튼 찾기\n",
    "        button = wait.until(EC.element_to_be_clickable((By.ID, 'btnLocalCarPrc')))\n",
    "\n",
    "        # 해당 요소가 보이도록 스크롤\n",
    "        driver.execute_script(\"arguments[0].scrollIntoView(true);\", button)\n",
    "        time.sleep(1)  # 잠시 대기하여 스크롤 후 안정화\n",
    "\n",
    "        # JavaScript로 클릭\n",
    "        driver.execute_script(\"arguments[0].click();\", button)\n",
    "\n",
    "        # 새 창으로 전환\n",
    "        WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)\n",
    "        driver.switch_to.window(driver.window_handles[-1])\n",
    "        time.sleep(2)\n",
    "\n",
    "        # 시/도, 지역구분 CSS 셀렉터 설정\n",
    "        state_selector = \"body > form > div > table > tbody > tr > td:nth-child(1)\"\n",
    "        city_selector = \"body > form > div > table > tbody > tr > td:nth-child(2)\"\n",
    "\n",
    "        # 시도 및 지역구분 정보 크롤링\n",
    "        states = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, state_selector)))\n",
    "        cities = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, city_selector)))\n",
    "\n",
    "        # 시도와 지역구분 텍스트 저장\n",
    "        state_list = [state.text for state in states]\n",
    "        city_list = [city.text for city in cities]\n",
    "\n",
    "        # 수집한 정보를 저장할 리스트\n",
    "        all_data = []\n",
    "\n",
    "        # 모든 지역에 대해 조회 버튼 클릭\n",
    "        for i in range(len(state_list)):\n",
    "            # 각 지역의 조회 버튼 클릭\n",
    "            button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'body > form > div > table > tbody > tr:nth-child({i + 1}) > td.tr_car_btn > a')))\n",
    "\n",
    "            # 해당 요소가 보이도록 스크롤\n",
    "            driver.execute_script(\"arguments[0].scrollIntoView(true);\", button)\n",
    "            time.sleep(1)  # 잠시 대기하여 스크롤 후 안정화\n",
    "\n",
    "            # JavaScript로 클릭\n",
    "            driver.execute_script(\"arguments[0].click();\", button)\n",
    "\n",
    "            # 새 창으로 전환\n",
    "            WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)\n",
    "            driver.switch_to.window(driver.window_handles[-1])\n",
    "            time.sleep(2)\n",
    "\n",
    "            # CSS 셀렉터 설정\n",
    "            car_type_selector = \"body > form > div > table > tbody > tr > td:nth-child(1)\"\n",
    "            maker_selector = \"body > form > div > table > tbody > tr > td:nth-child(2)\"\n",
    "            model_selector = \"body > form > div > table > tbody > tr > td:nth-child(3)\"\n",
    "            subN_selector = \"body > form > div > table > tbody > tr > td:nth-child(4)\"\n",
    "            subC_selector = \"body > form > div > table > tbody > tr > td:nth-child(5)\"\n",
    "            subALL_selector = \"body > form > div > table > tbody > tr > td:nth-child(6)\"\n",
    "\n",
    "            # 크롤링 함수 정의\n",
    "            def crawling():\n",
    "                car_type, maker, model, subN, subC, subALL = [], [], [], [], [], []\n",
    "                last_height = driver.execute_script(\"return document.body.scrollHeight\")\n",
    "\n",
    "                while True:\n",
    "                    # 차종, 제조사, 모델명, 보조금 정보 수집\n",
    "                    car_types = driver.find_elements(By.CSS_SELECTOR, car_type_selector)\n",
    "                    makers = driver.find_elements(By.CSS_SELECTOR, maker_selector)\n",
    "                    models = driver.find_elements(By.CSS_SELECTOR, model_selector)\n",
    "                    subNs = driver.find_elements(By.CSS_SELECTOR, subN_selector)\n",
    "                    subCs = driver.find_elements(By.CSS_SELECTOR, subC_selector)\n",
    "                    subALLs = driver.find_elements(By.CSS_SELECTOR, subALL_selector)\n",
    "\n",
    "                    # 리스트에 추가\n",
    "                    car_type.extend([i.text for i in car_types])\n",
    "                    maker.extend([i.text for i in makers])\n",
    "                    model.extend([i.text for i in models])\n",
    "                    subN.extend([i.text for i in subNs])\n",
    "                    subC.extend([i.text for i in subCs])\n",
    "                    subALL.extend([i.text for i in subALLs])\n",
    "\n",
    "                    # 페이지 끝까지 스크롤\n",
    "                    driver.execute_script(\"window.scrollTo(0, document.body.scrollHeight);\")\n",
    "                    time.sleep(3)  # 스크롤 후 데이터를 로드할 시간을 충분히 줍니다\n",
    "\n",
    "                    # 새로운 높이를 가져와 비교, 더 이상 데이터가 없을 때 탈출\n",
    "                    new_height = driver.execute_script(\"return document.body.scrollHeight\")\n",
    "                    if new_height == last_height:\n",
    "                        break\n",
    "                    last_height = new_height\n",
    "\n",
    "                return car_type, maker, model, subN, subC, subALL\n",
    "\n",
    "            # 크롤링 실행\n",
    "            car_type, maker, model, subN, subC, subALL = crawling()\n",
    "\n",
    "            # 수집한 정보를 저장\n",
    "            for ct, mk, mdl, sn, sc, sa in zip(car_type, maker, model, subN, subC, subALL):\n",
    "                all_data.append({\n",
    "                    'car_type': ct,\n",
    "                    'maker': mk,\n",
    "                    'car_name': mdl,\n",
    "                    'national_subsidy': sn,\n",
    "                    'city_subsidy': sc,\n",
    "                    'state': state_list[i],\n",
    "                    'city_name': city_list[i]\n",
    "                })\n",
    "\n",
    "            # 현재 창 닫기\n",
    "            driver.close()\n",
    "            time.sleep(1)  # 창을 닫고 나서 약간의 시간 대기\n",
    "            # 이전 창으로 전환\n",
    "            driver.switch_to.window(driver.window_handles[-1])\n",
    "\n",
    "\n",
    "        # 수집한 정보를 JSON 파일로 저장\n",
    "        os.makedirs('server/crawling/data', exist_ok=True)\n",
    "        with open('server/crawling/data/car_subsidy.json', 'w', encoding='utf-8') as file: # (2)\n",
    "            json.dump(all_data, file, ensure_ascii=False, indent=4)\n",
    "        \n",
    "    except Exception as e:\n",
    "        print(f\"오류 발생: {e}\")\n",
    "\n",
    "    finally:\n",
    "        # 드라이버 종료\n",
    "        driver.quit()\n",
    "    return 'subsidy_data.json' # (2)\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    crawling_subsidy()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6278af9a-1021-45dd-8633-453b4543c4c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "streamlit run "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86302f85-081b-42ba-b260-857b2a1e64cf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b2464a5-1f38-4f02-b3a7-522fd5031538",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
