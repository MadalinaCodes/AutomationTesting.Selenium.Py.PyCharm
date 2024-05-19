from selenium import webdriver
from selenium.webdriver import ActionChains


class Browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) # asteptam sa se incarce un element timp de 10 secunde
    driver.set_page_load_timeout(10) # asteptam sa se incarce pagina timp de 10 secunde
    driver.maximize_window()

    # # de sters action si importul pentru el
    # def action(self):
    #     action = ActionChains(driver=webdriver.Chrome())
    #     action.context_click()


    # functie care inchide browserul dupa fiecare test automat
    def close(self):
        self.driver.quit()
