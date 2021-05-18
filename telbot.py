### 날짜/시간 안내
@bot.message_handler(commands = ['현재시간'])
def now_time(message):
    t = "안녕하세요 주인님 현재 %04d년%02d월%02d일 %02d시%02d분 입니다." % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
    bot.reply_to(message, t)

def morning_time():
    bot.reply_to(TOKEN, "주인님 현재 %02d시%02d분 입니다. 일어나세요" % (now.tm_hour, now.tm_min)
                +"\n게으른 사람은 폐가망신 합니다.")
def lunch_time():
    bot.reply_to(TOKEN, "주인님 현재 %02d시%02d분 입니다." % (now.tm_hour, now.tm_min)
                +"\n맛있는 점심을 드시면 좋을 것 같습니다.")
def night_time():
    bot.reply_to(TOKEN, "주인님 현재 %02d시%02d분 입니다." % (now.tm_hour, now.tm_min)
                +"\n즐거운 퇴근시간~ 오늘하루 고생 많으셨습니다.")
schedule.every().day.at("07:00").do(morning_time)
schedule.every().day.at("12:00").do(lunch_time)
schedule.every().day.at("17:00").do(night_time)

def job():
    bot.send_message(chat_id = TOKEN, text = "일중입니다. . .")

@bot.message_handler(commands = ['안녕텔비']) # /start 또는 /help 라는 채팅이 오면 실행 됨
def send_welcome(message):
    time = "%04d년%02d월%02d일 %02d시%02d분 입니다." % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
    bot.reply_to(message, '텔비등장! ' + '현재 ' + time) # 봇이 응답하는 텍스트

## 음식
@bot.message_handler(commands = ['밥'])
def recommendation(message):
    ask = "한식, 중식, 일식, 양식 중 어떤 걸 드시겠습니까? "
    bot.reply_to(message, ask)

@bot.message_handler(commands = ['한식', '중식', '일식', '양식'])
def random_menu(message):
    menu = message.text
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(5)   # 페이지 로딩 완료할 때까지 대기 ( 최대 초 지정 )
    driver.get('http://dogumaster.com/select/menu')
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    meal.click()
    time.sleep(0.5)
    if menu == '/한식':
        korean_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[2]')
        korean_food.click()
    elif menu == '/중식':
        china_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[3]')
        china_food.click()
    elif menu == '/일식':
        japan_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[4]')
        japan_food.click()
    elif menu == '/양식':
        usa_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[5]')
        usa_food.click()
    else:
        retry = (" 메뉴를 정확히 입력해주세요. 잘못 입력하셨습니다.")
        bot.reply_to(message, retry)
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(0.3)
    img = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/img')
    bot.reply_to(message, img.get_attribute('src') + "메뉴 고민중입니다 . . .")
    time.sleep(1.4)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    bot.reply_to(message, "오늘은 " + result + " 을(를) 추천드립니다.")
    driver.quit()

bot.polling() # 주인님의 명령을 기다림

schedule.every(1).second.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)