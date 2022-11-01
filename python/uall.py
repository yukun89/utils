def print_red(content):
    content="\033[31m"+content+"\033[0m"
    print(content, *params)
def print_green(content, *params):
    content="\033[32m"+content+"\033[0m"
def print_blue(content, *params):
    content="\033[34m"+content+"\033[0m"

def display():
    print("\033[31m RED \033[0m")
    print("\033[32m GREEN \033[0m")
    print("\033[33m YELLOW \033[0m")
    print("\033[34m BLUE \033[0m")
    print("\033[38m DEFAULT \033[0m")

display()
