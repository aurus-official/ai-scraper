import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def bing(prompt, count, driver) :
    # Setting up
    login_url = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3fedge_suppress_profile_switch%3d1%26requrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%26sig%3d261241FBE81160430F7052DEE90561AA&wp=MBI_SSL&lc=1033&CSRFToken=c3599dfc-32e9-4468-8d1a-e7ef967bcb4e&aadredir=1"
    ai_url = "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx"
    username = ""
    password = ""

    # Logging in
    driver.webdriver.get(login_url)
    time.sleep(2)
    email_element = driver.webdriver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div[2]/div/input[1]")
    email_element.send_keys(username)
    time.sleep(2)
    next_element = driver.webdriver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[5]/div/div/div/div/input")
    next_element.click()
    time.sleep(2)
    password_element = driver.webdriver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input")
    password_element.send_keys(password)
    time.sleep(2)
    signin_element = driver.webdriver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input")
    signin_element.click()
    time.sleep(2)

    # Switching tabs
    driver.webdriver.execute_script("window.open('');")
    driver.webdriver.switch_to.window(driver.webdriver.window_handles[1])
    driver.webdriver.get(ai_url)
    time.sleep(5)

    # Unshadowing the roots
    parent_shadow_root = driver.webdriver.find_element(By.CLASS_NAME, "cib-serp-main")
    parent_shadow_content = driver.webdriver.execute_script("return arguments[0].shadowRoot", parent_shadow_root)
    child_shadow_root = parent_shadow_content.find_element(By.CSS_SELECTOR, "#cib-action-bar-main")
    child_shadow_content = driver.webdriver.execute_script("return arguments[0].shadowRoot", child_shadow_root)
    child_child_shadow_root = child_shadow_content.find_element(By.CSS_SELECTOR, "div > div.main-container.body-2 > div.input-container.as-ghost-placement > cib-text-input")
    child_child_shadow_content = driver.webdriver.execute_script("return arguments[0].shadowRoot", child_child_shadow_root)

    # Inputting prompt
    input_element = child_child_shadow_content.find_element(By.ID, "searchbox")
    input_element.send_keys(prompt)
    time.sleep(2)
    input_element.send_keys(Keys.RETURN)
    time.sleep(50)
    
    # Unshadowing more roots
    fifth_shadow_root = parent_shadow_content.find_element(By.ID, "cib-conversation-main")
    fifth_shadow_content = driver.webdriver.execute_script("return arguments[0].shadowRoot", fifth_shadow_root)
    fourth_shadow_root = fifth_shadow_content.find_element(By.CSS_SELECTOR, "#cib-chat-main > cib-chat-turn")
    fourth_shadow_content = driver.webdriver.execute_script("return arguments[0].shadowRoot", fourth_shadow_root)
    third_shadow_root = fourth_shadow_content.find_element(By.CLASS_NAME, "response-message-group")
    third_shadow_content = driver.webdriver.execute_script("return arguments[0].shadowRoot", third_shadow_root)
    second_shadow_root = third_shadow_content.find_element(By.CSS_SELECTOR, "cib-message:nth-child(3)")
    second_shadow_content = driver.webdriver.execute_script("return arguments[0].shadowRoot", second_shadow_root)
    first_shadow_root = second_shadow_content.find_element(By.CSS_SELECTOR, "cib-shared")

    # Making a full page screenshot
    time.sleep(2)
    dimension = lambda x : driver.webdriver.execute_script('return document.body.parentNode.scroll'+x)
    driver.webdriver.set_window_size(dimension('Width'), dimension('Height'))
    first_shadow_root.screenshot(f"{count}.png")

    # Notify when done
    print(f"\t{prompt.rstrip()}. Try {count}. Done!")
