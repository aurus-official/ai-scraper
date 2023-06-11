import os
import ai_modules

PROMPTS = ai_modules.prompt()

def bingLoop() :
    print("Bing - 3 Prompts, 3 Tries")

    for prompt in PROMPTS:
        if not os.path.exists(f"./BING - {prompt}"):
            os.mkdir(f"BING - {prompt}")

        os.chdir(f"./BING - {prompt}")
        files_currDir = os.listdir(os.getcwd())

        while len(files_currDir) != 3:
            try:
                DRIVER = ai_modules.driver()
                DRIVER.webdriver.maximize_window()
                ai_modules.bing(prompt, len(files_currDir) + 1, DRIVER)
                DRIVER.webdriver.close()
                files_currDir = os.listdir(os.getcwd())

            except:
                continue

        os.chdir("../")

def gptLoop() :
    print("ChatGPT - 3 Prompts, 3 Tries")

    for prompt in PROMPTS:
        if not os.path.exists(f"./CHATGPT - {prompt}"):
            os.mkdir(f"CHATGPT - {prompt}")

        os.chdir(f"./CHATGPT - {prompt}")
        files_currDir = os.listdir(os.getcwd())

        while len(files_currDir) != 3:
            try:
                DRIVER = ai_modules.driver()
                DRIVER.webdriver.maximize_window()
                ai_modules.chatgpt(prompt, len(files_currDir) + 1, DRIVER)
                DRIVER.webdriver.close()
                files_currDir = os.listdir(os.getcwd())

            except:
                continue

        os.chdir("../")

if __name__ == '__main__':
    bingLoop()
    gptLoop()
