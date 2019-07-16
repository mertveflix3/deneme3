import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
print ("Baslatiliyor")
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options,executable_path="/root/geckodriver")

driver.set_window_size(1024, 768) # optional
driver.get('https://www.youtube.com/watch?v=o4z-tJ2K9gE')
time.sleep(5)
driver.execute_script('document.getElementsByClassName("ytp-large-play-button ytp-button")[0].click()')
time.sleep(30)
driver.save_screenshot('screen2.png') # save a screenshot to disk
print("Screen Shot Alindi")
driver.close()
exit(1)
