def prompt() :
    with open("prompts.txt", "r") as file:
        prompts = file.readlines()
        return prompts
