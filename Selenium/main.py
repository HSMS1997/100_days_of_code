from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_experimental_option("detach", True)
service = Service("C:/Users/HILAN/Documents/Selenium/ChromeWebDriver/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.amazon.com.br/Cicero-Criativo-Argolado-Cl%C3%A1ssica-8835/dp/B09T3S1KBT/ref=asc_df_B09T3S1KBT/"
           "?tag=googleshopp00-20&linkCode=df0&hvadid=379708145169&hvpos=&hvnetw=g&hvrand=10082331536461897842&hvpone="
           "&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001773&hvtargid=pla-1707630447757&psc=1")


driver.quit()