
import pyautogui
import datetime

def attender(team,driver,t3):
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # driver = webdriver.Chrome(r"H:\msteamsbot\chromedriver_win32\chromedriver.exe")

    driver.get("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6ImFhNzZiYzE1LTg4ZDAtNDlmMi1hMDllLTUwZGNkZjZjNzU2MiIsInRzIjoxNjMzNDQ5NTYyLCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=a2db4be8-ec7b-44fb-a89e-953c6dad8ecf&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=13704c37-bf4c-4fc1-9f99-b55993562eb0&response_mode=fragment&sso_reload=true")
    driver.maximize_window()
    time.sleep(1)
    uname = WebDriverWait(driver,50).until(
        EC.presence_of_element_located((By.ID, 'i0116'))
    )

    time.sleep(2)
    uname.send_keys("257258@student.annauniv.edu")
    nextbutton = WebDriverWait(driver,50).until(
        EC.presence_of_element_located((By.ID, 'idSIButton9'))
    )
    nextbutton.click()

    time.sleep(2)

    passwd =  WebDriverWait(driver,50).until(
        EC.presence_of_element_located((By.ID, 'i0118'))
    )
    passwd.send_keys("Ujesh9112k@")
    loginbutton = WebDriverWait(driver,50).until(
        EC.presence_of_element_located((By.ID, 'idSIButton9'))
    )
    loginbutton.click()
    time.sleep(2)
    no = WebDriverWait(driver,50).until(
        EC.presence_of_element_located((By.ID, 'idBtn_Back'))
    )
    no.click()
    time.sleep(1)
    try:
        finalLogin = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.ID, 'i0116'))
        )
        finalLogin.send_keys("257258@student.annauniv.edu")

        time.sleep(1)
        finalNext = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.ID, 'idSIButton9'))
        )
        finalNext.click()
    except:
        cl = WebDriverWait(driver,50).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'table'))
        )
        cl.click()

    time.sleep(15)
    time.sleep(2)
    dismiss = (driver.find_elements_by_class_name("action-button "))
    for i in range(len(dismiss)):
        val = dismiss[i].get_attribute("Title")
        if(val == "Dismiss"):
            dismiss[i].click()
    
    pyautogui.moveTo(300, 300)
    parentElement1 = driver.find_elements_by_class_name("team-card")
    time.sleep(2)
    pyautogui.scroll(-800)
    parentElement2 = driver.find_elements_by_class_name("team-card")
    time.sleep(2)
    pyautogui.scroll(-800)
    parentElement3 = driver.find_elements_by_class_name("team-card")
    time.sleep(2)
    pyautogui.scroll(-800)
    parentElement4 = driver.find_elements_by_class_name("team-card")
    time.sleep(2)

    parentElement = set()
    parentElement = set.union(set(parentElement1),set(parentElement2),set(parentElement3),set(parentElement4))
    parentElement = list(parentElement)

    for ele in range(len(parentElement)):
        elementList = parentElement[ele].find_element_by_class_name("team-name")
        print(elementList.text)

    for ele in range(len(parentElement)):
        elementList = parentElement[ele].find_element_by_class_name("team-name")
        
        if(elementList.text == team):
            parentElement[ele].click()
            break

    try:        
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\extensionicon.PNG', confidence=0.8)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    except:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\extensionicon.PNG', confidence=0.7)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)

    try:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\Screenshot (46).png', confidence=0.8)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(2)
    except:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\Screenshot (46).png', confidence=0.7)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(2)

    try:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\onlyscreen.PNG', confidence=0.8)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    except:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\onlyscreen.PNG', confidence=0.7)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    
    try:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\system.PNG', confidence=0.8)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    except:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\system.PNG', confidence=0.7)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    
    try:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\startrecording.PNG', confidence=0.8)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    except:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\startrecording.PNG', confidence=0.7)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    
    try:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\chrometab.PNG', confidence=0.8)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    except:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\chrometab.PNG', confidence=0.7)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)

    try:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\microsoft-teams.PNG', confidence=0.7)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    except:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\microsoft-teams.PNG', confidence=0.6)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)

    try:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\share.PNG', confidence=0.8)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    except:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\share.PNG', confidence=0.7)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)

    k = 1
    while(k<30):
        try:
            joinbutton = driver.find_element_by_class_name("ts-calling-join-button")
            joinbutton.click()
            break
        except:
            time.sleep(60)
            driver.refresh()
            k+=1
    
    try:
        img_location = pyautogui.locateOnScreen('H:/msteamsbot/allowbutton.PNG', confidence=0.6)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    except:
        img_location = pyautogui.locateOnScreen('H:/msteamsbot/allowbutton.PNG', confidence=0.5)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    
    time.sleep(5)

    try:
        img_location = pyautogui.locateOnScreen('H:/msteamsbot/vdoff.PNG', confidence=0.9)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    except:
        img_location = pyautogui.locateOnScreen('H:/msteamsbot/vdoff.PNG', confidence=0.8)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)

    time.sleep(2)

    join = driver.find_element_by_class_name("join-btn")
    join.click()
    time.sleep(2)
    while(1):
        now = datetime.datetime.now()
        cur = now.strftime("%H:%M")
        arr1 = cur.split(":")
        arr1 = list(map(int,arr1))
        t1 = (arr1[0]*3600) + (arr1[1]*60)
        print(t3-t1)
        if(t1>=t3):
            #exit class
            pyautogui.moveTo(400, 400, 2)
            time.sleep(1)
            hangup = driver.find_element_by_id("hangup-button")
            hangup.click()
            time.sleep(2)
            break
        else:
            time.sleep(60)
    
    #save the video
    try:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\stopsharing.PNG', confidence=0.6)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(2)
    except:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\stopsharing.PNG', confidence=0.5)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(2)
    
    try:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\continue.PNG', confidence=0.6)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    except:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\continue.PNG', confidence=0.5)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(1)
    try:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\save.PNG', confidence=0.6)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(2)
    except:
        img_location = pyautogui.locateOnScreen('H:\msteamsbot\save.PNG', confidence=0.5)
        image_location_point = pyautogui.center(img_location)
        x, y = image_location_point
        pyautogui.click(x, y)
        time.sleep(2)
    time.sleep(100)
    # try:
    #     img_location = pyautogui.locateOnScreen('H:\msteamsbot\maximize.PNG', confidence=0.8)
    #     image_location_point = pyautogui.center(img_location)
    #     x, y = image_location_point
    #     pyautogui.click(x, y)
    #     time.sleep(2)
    # except:
    #     img_location = pyautogui.locateOnScreen('H:\msteamsbot\maximize.PNG', confidence=0.7)
    #     image_location_point = pyautogui.center(img_location)
    #     x, y = image_location_point
    #     pyautogui.click(x, y)
    #     time.sleep(2)
    # try:
    #     img_location = pyautogui.locateOnScreen('H:\msteamsbot\quit.PNG', confidence=0.8)
    #     image_location_point = pyautogui.center(img_location)
    #     x, y = image_location_point
    #     pyautogui.click(x, y)
    #     time.sleep(1)
    # except:
    #     img_location = pyautogui.locateOnScreen('H:\msteamsbot\quit.PNG', confidence=0.7)
    #     image_location_point = pyautogui.center(img_location)
    #     x, y = image_location_point
    #     pyautogui.click(x, y)
    #     time.sleep(1)
    # time.sleep(1000000)
    profile = driver.find_element_by_id("personDropdown")
    profile.click()
    time.sleep(1)
    signout = driver.find_element_by_id("logout-button")
    signout.click()
    logout = WebDriverWait(driver,50).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'table'))
        )
    logout.click()
    time.sleep(1)
    
    return