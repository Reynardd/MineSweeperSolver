from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from chromedriver_autoinstaller import install as webdriver_install
class MineSweeperInterface:
    def __init__(self):
        webdriver_service = webdriver.ChromeService(webdriver_install(no_ssl=True))
        webdriver_options = webdriver.ChromeOptions()
        webdriver_options.add_argument('--ignore-ssl-errors=yes')
        webdriver_options.add_argument('--ignore-certificate-errors')
        webdriver_options.set_capability('pageLoadStrategy','eager')
        self.driver = webdriver.Chrome(service=webdriver_service,options=webdriver_options)
        self.driver.get('https://minesweeperonline.com/#beginner')
        self.cell_elements = []
        self.load_elements()
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
                cell_class = self.cell_elements[i][j].get_attribute('class')
                if cell_class == 'square blank':row.append('-')
                elif cell_class.startswith('square open'):
                    clue = int(cell_class.removeprefix('square open'))
                    row.append(clue)
            result.append(row)
        return result
