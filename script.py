import ai_modules

PROMPTS = ai_modules.prompt()

def bingLoop() :
    for prompt in PROMPTS:
        for i in range(1, 4):
            try:
                ai_modules.bing(prompt, i)
            except:
                continue

bingLoop()
