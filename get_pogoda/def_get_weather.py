from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefoxOptions
import time

def get_year_weather(year, city_code, mon_st=1, mon_fin=12):
    with open(f'E:/PyCharmProjects/PogodaGis/pogodas/{year}.csv', 'w', encoding='utf-8') as file:
        link = "https://www.gismeteo.ru/diary/"
        file.write(
            f'Число,Температура(день),Давление(день),Ветер(день),Температура(вечер),Давление(вечер),Ветер(вечер)\n')
        month_start = mon_st
        while month_start <= mon_fin:
            options = firefoxOptions()
            options.add_argument('--headless')
            browser = webdriver.Firefox(options=options)

            browser.get(f'{link}{city_code}/{year}/{month_start}')
            time.sleep(0.2)

            day = browser.find_elements(By.CSS_SELECTOR, "tr")
            for i in day:
                temstr = i.text
                temstr = temstr.replace("\n", "").split()
                temstr[1] = temstr[1].strip('+')

                if not temstr[0].isalpha() is True and len(temstr) == 7:
                    if len(temstr[2]) > 3:
                        temstr[2], temstr[3] = temstr[2][:3], f'{temstr[2][3:]} {temstr[3]}'
                    if len(temstr[5]) > 3:
                        temstr[5], temstr[6] = temstr[5][:3], f'{temstr[5][3:]} {temstr[6]}'
                    temstr = (',').join(temstr)
                    if month_start < 10:
                        ms = f'0{month_start}'
                    else:
                        ms = month_start
                    if not temstr[:2].isdigit() == True:
                        temstr = f'0{temstr}'
                    file.write(f'{year}-{ms}-{temstr}\n')

            month_start += 1
            browser.quit()

        file.close()
        print(f'finish write {year}')


get_year_weather(2023, 4394, 1, 7)
