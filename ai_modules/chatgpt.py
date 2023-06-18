import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def chatgpt(prompt, count, driver) :
    # Setting up
    login_url = "https://platform.openai.com/login?launch"
    username = "aisat.rosales225176@gmail.com"
    password = "41s4tl1f3"

    # Logging in
    driver.webdriver.get(login_url)
    time.sleep(2)
    email_element = driver.webdriver.find_element(By.CSS_SELECTOR, "#username")
    time.sleep(2)
    email_element.send_keys(username)
    time.sleep(2)
    next_element = driver.webdriver.find_element(By.CSS_SELECTOR, "body > div > main > section > div > div > div > div.c8c17eeb0.c451c762a > div > form > div.c7f45701e > button")
    time.sleep(2)
    next_element.click()
    time.sleep(2)
    pass_element = driver.webdriver.find_element(By.CSS_SELECTOR, "#password")
    time.sleep(2)
    pass_element.send_keys(password)
    time.sleep(2)
    pass_element.send_keys(Keys.RETURN)
    time.sleep(5)
    skip_element = driver.webdriver.find_element(By.CLASS_NAME, "launcher-item")
    time.sleep(2)
    skip_element.click()

    # Accepting terms and conditions
    time.sleep(10)
    accept_first_element = driver.webdriver.find_element(By.CSS_SELECTOR, "#radix-\\:r9\\: > div.p-4.sm\\:p-6.sm\\:pt-4 > div.prose.dark\\:prose-invert > div.flex.gap-4.mt-6 > button")
    time.sleep(2)
    accept_first_element.click()
    time.sleep(2)
    accept_second_element = driver.webdriver.find_element(By.CSS_SELECTOR, "#radix-\\:r9\\: > div.p-4.sm\\:p-6.sm\\:pt-4 > div.prose.dark\\:prose-invert > div.flex.gap-4.mt-6 > button.btn.relative.btn-neutral.ml-auto")
    time.sleep(2)
    accept_second_element.click()
    time.sleep(2)
    accept_third_element = driver.webdriver.find_element(By.CSS_SELECTOR, "#radix-\\:r9\\: > div.p-4.sm\\:p-6.sm\\:pt-4 > div.prose.dark\\:prose-invert > div.flex.gap-4.mt-6 > button.btn.relative.btn-primary.ml-auto")
    time.sleep(2)
    accept_third_element.click()

    # Disabling chat history
    time.sleep(2)
    disable_toggle = driver.webdriver.find_element(By.CSS_SELECTOR, "#headlessui-menu-button-\\:r8\\:")
    time.sleep(2)
    disable_toggle.click()
    time.sleep(2)
    setting_element = driver.webdriver.find_element(By.CSS_SELECTOR, "#headlessui-menu-item-\\:r1k\\:")
    time.sleep(2)
    setting_element.click()
    time.sleep(2)
    data_tab = driver.webdriver.find_element(By.CSS_SELECTOR, "#radix-\\:r1p\\:-trigger-DataControls")
    time.sleep(2)
    data_tab.click()
    time.sleep(2)
    turn_off = driver.webdriver.find_element(By.CSS_SELECTOR, "#radix-\\:r1p\\:-content-DataControls > div > div:nth-child(1) > div.flex.items-center.justify-between > button")
    time.sleep(2)
    turn_off.click()
    time.sleep(2)
    close_element = driver.webdriver.find_element(By.CSS_SELECTOR, "#radix-\\:r1m\\: > div.px-4.pb-4.pt-5.sm\\:p-6.flex.items-center.justify-between.border-b.border-black\\/10.dark\\:border-white\\/10 > button")
    time.sleep(2)
    close_element.click()

    # Hiding the sidebar
    time.sleep(2)
    hide_element = driver.webdriver.find_element(By.CSS_SELECTOR, "#__next > div.overflow-hidden.w-full.h-full.relative.flex.z-0 > div.dark.flex-shrink-0.overflow-x-hidden.bg-gray-900 > div > div > div > nav > div.mb-1.flex.flex-row.gap-2 > span > a")
    time.sleep(2)
    hide_element.click()

    # Inputting prompts
    time.sleep(2)
    input_element = driver.webdriver.find_element(By.CSS_SELECTOR, "#prompt-textarea")
    time.sleep(2)
    input_element.send_keys(prompt)
    time.sleep(2)
    input_element.send_keys(Keys.RETURN)

    # Making a full page screenshot
    time.sleep(30)
    capture_element = driver.webdriver.find_element(By.CSS_SELECTOR, "#__next > div.overflow-hidden.w-full.h-full.relative.flex.z-0 > div.relative.flex.h-full.max-w-full.flex-1.overflow-hidden > div > main > div.flex-1.overflow-hidden > div > div > div > div.group.w-full.text-gray-800.dark\\:text-gray-100.border-b.border-black\\/10.dark\\:border-gray-900\\/50.bg-gray-50.dark\\:bg-\\[\\#444654\\]")
    dimension = lambda x : driver.webdriver.execute_script('return document.body.parentNode.scroll'+x)
    driver.webdriver.set_window_size(dimension('Width'), dimension('Height') * 5)
    capture_element.screenshot(f"{count}.png")

    # Notify when done
    print(f"\t{prompt.rstrip()} Try {count}. Done!")

    time.sleep(20)
