from selenium import webdriver;
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from PIL import Image, ImageDraw
import cv2
import telebot
token = ""
     #Calendar
now = datetime.now()
formatted_date = now.strftime("%d, %m, %Y")  # правильно форматируем строку даты
date_obj = datetime.strptime(formatted_date, "%d, %m, %Y")  # преобразуем строку обратно в объект datetime
today = date_obj.weekday()  # вызываем метод weekday() на объекте datetime, а не на строке
current_time = datetime.now().strftime("%H:%M:%S")
print(current_time)
message_sent = "False"

#Время сейчас
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    # Проверяем, если текущее время равно 20:00:00 и сообщение еще не было отправлено
    if current_time == "08:44:00":
        bot = telebot.TeleBot(token)
        # Замените 'GROUP_ID' на ID вашей группы
        group_id = '-1002017998937'
        MESSAGE_THREAD_ID = '2386'
        photo = open('homework.png', 'rb')
        bot.send_photo(group_id, photo, message_thread_id=MESSAGE_THREAD_ID)
        message_sent = "True"  # Устанавливаем флаг отправки сообщения
        time.sleep(1)  # Чтобы не отправлять фото несколько раз за секунду
        bot.polling(none_stop=True)
    # Сбрасываем флаг отправки сообщения в следующий день
    if current_time == "00:00:00":
        message_sent = False

    if current_time == "19:58:00":
        if today == "5":
            pass
        else:
            # Запускаем браузер
            driver = webdriver.Chrome()

            # Переходим на страницу авторизации
            driver.get('https://ms-edu.tatar.ru/login/')

            # Находим поля для ввода логина и пароля и вводим данные
            username = driver.find_element(By.CSS_SELECTOR,
                                           "#formLogin > div.Auth_Fields__en5Sv > div:nth-child(1) > div > input")
            username.send_keys('')
            password = driver.find_element(By.CSS_SELECTOR, "#formLogin > div.Auth_Fields__en5Sv > div:nth-child(2) > div > input")
            password.send_keys('')

            # Нажимаем кнопку "Войти"
            login_button = driver.find_element(By.CSS_SELECTOR, '#formLogin > div:nth-child(4) > button')
            login_button.click()

            # Ожидание
            time.sleep(10)

            #Переходим на страницу с дз
            driver.get('https://school-edu.tatar.ru/diary/homeworks/homeworks?view=next')

            # Ожидание
            time.sleep(20)

            # Заменяем текст с помощью JavaScript
            script = "document.getElementsByClassName(' _1n9PQ29RiaJqaa2Pr7g07_')[0].textContent = 'HomeworkToday';"
            driver.execute_script(script)
            # Заменяем текст с помощью JavaScript
            script1 = "document.getElementsByClassName(' _1-uphLzJWeofiZ7pM_JDmO')[0].textContent = 'БОТ';"
            driver.execute_script(script1)

            # Заменяем текст с помощью JavaScript
            script2 = "document.getElementsByClassName(' sqhGmZnUHMpOtgx_2Gv48')[0].textContent = '7Л';"
            driver.execute_script(script2)

            #Удаление лишних объектов
            script3 = '''
    const element = document.querySelector('#global-header-wrapper > div._56grJoiM2euP0m-4_cQJ0._2za3MNLbs6QsEgJHttHGQK.DWN--OG6Jrh0WYIMrCT-p > div > div._21jYlx5yq1zRU0a_JLznCt > div._3KodGxO-Ng7-R2ducqYatl._3Mx6fUwA7q_YtgC4hE7p4H._310Rq2MqQstWdmIE3HsZaR > div > div > span');
    element.remove();
    '''
            driver.execute_script(script3)

            script4 = '''
    const element = document.querySelector('#global-header-wrapper > div._56grJoiM2euP0m-4_cQJ0._2za3MNLbs6QsEgJHttHGQK.DWN--OG6Jrh0WYIMrCT-p > div > div._21jYlx5yq1zRU0a_JLznCt > div._2P0BSZ-G3jeQbcahVN-Zv6._2xVfMyiWweLhpqqEr2W2Dp._38GMaLW1298wJ86sPT9H2U > div._2GOM9v4VlxcQSOG51v2juK');
    element.remove();
    '''
            driver.execute_script(script4)

            #Скриншот
            driver.set_window_size(1920, 1080)
            driver.save_screenshot("homework.png")

        #Фотошоп
            # Открываем изображение
            img = Image.open('homework.png')

            # Определяем координаты и размеры области, которую нужно вырезать (левая верхняя x, левая верхняя y, правая нижняя x, правая нижняя y)
            left = 569
            top =  49
            right = 1595
            bottom = 930

            # Обрезаем изображение
            cropped_img = img.crop((left, top, right, bottom))

            # Сохраняем обрезанное изображение
            cropped_img.save('homework.png')

            # Загрузка изображения
            image = cv2.imread('homework.png')

            # Создание изображения с альфа-каналом (прозрачным фоном)
            result = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

            # Наложение прямоугольника белого цвета
            cv2.rectangle(result, (25, 62), (0, 80), (255, 255, 255, 255), -1)
            cv2.rectangle(result, (159, 97), (455, 53), (255, 255, 255, 255), -1)
            cv2.rectangle(result, (1, 35), (634, 7), (255, 255, 255, 255), -1)

            # Сохранение результата
            cv2.imwrite('homework.png', result)
            time.sleep(20)
            driver.quit()
            break
    time.sleep(1)

#Телеграм бот



