def extension():
    from selenium import webdriver
    import time
    import pyautogui

    driver = webdriver.Chrome(r"H:\msteamsbot\chromedriver_win32\chromedriver.exe")
    driver.get("https://chrome.google.com/webstore/detail/screen-recorder/hniebljpgcogalllopnjokppmgbhaden?hl=en")
    time.sleep(3)
    driver.maximize_window()
    time.sleep(1)
    add = driver.find_elements_by_tag_name("div")
    for i in range(len(add)):
            try:
                val = add[i].get_attribute("aria-label")
                if(val == "Add to Chrome"):
                    add[i].click()
                    break
            except:
                continue
    time.sleep(2)
    try:
        img_location = pyautogui.locateOnScreen('H:/msteamsbot/addextension.PNG', confidence=0.6)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    except:
        img_location = pyautogui.locateOnScreen('H:/msteamsbot/addextension.PNG', confidence=0.5)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    return driver