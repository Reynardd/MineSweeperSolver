from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from chromedriver_autoinstaller import install as webdriver_install
import var
class MineSweeperInterface:
    def __init__(self):
        webdriver_service = webdriver.ChromeService(webdriver_install(no_ssl=True))
        webdriver_options = webdriver.ChromeOptions()
        webdriver_options.add_argument('--ignore-ssl-errors=yes')
        webdriver_options.add_argument('--ignore-certificate-errors')
        webdriver_options.set_capability('pageLoadStrategy','eager')
        self.driver = webdriver.Chrome(service=webdriver_service,options=webdriver_options)
        self.driver.get(var.WEBSITE_URL)
        self.face_element = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.ID,'face')))
        self.cell_elements = []
        self.cell_elements_cache = [[-1 for _ in range(9)] for _ in range(9)]
        self.load_elements()
    def check_for_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.send_keys('Reynard')
            alert.accept()
        except:pass
    def get_game_state(self):
        self.check_for_alert()
        face = self.face_element.get_attribute('class')
        if face=='facesmile':return 'Playing'
        if face=='facedead':return 'Lost'
        return 'Won'
    def load_elements(self):
        wait = WebDriverWait(self.driver,5)
        for i in range(9):
            row = []
            for j in range(9):
                element = wait.until(EC.presence_of_element_located((By.ID,f'{i+1}_{j+1}')))
                row.append(element)
            self.cell_elements.append(row)
    def parse_elements(self):
        result = []
        for i in range(9):
            row = []
            for j in range(9):
                if self.cell_elements_cache[i][j]!=-1: 
                    row.append(self.cell_elements_cache[i][j])
                    continue
                cell_class = self.cell_elements[i][j].get_attribute('class')
                if cell_class == 'square blank':row.append('-')
                elif cell_class.startswith('square open'):
                    clue = int(cell_class.removeprefix('square open'))
                    self.cell_elements_cache[i][j] = clue
                    row.append(clue)
                else:
                    row.append('X')
            result.append(row)
        return result
    def click_on_cell(self,x,y):
        self.check_for_alert()
        self.cell_elements[y][x].click()
    def rightclick_on_cell(self,x,y):
        self.check_for_alert()
        action_chain = ActionChains(self.driver)
        action_chain.context_click(self.cell_elements[y][x]).perform()

