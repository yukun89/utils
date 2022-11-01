def print_red(content):
    content="\033[31m"+content+"\033[0m"
    print(content, *params)
def print_green(content, *params):
    content="\033[32m"+content+"\033[0m"
def print_blue(content, *params):
    content="\033[34m"+content+"\033[0m"

def display():
    print("\033[31m这是红色字体\033[0m")
    print("\033[32m这是绿色字体\033[0m")
    print("\033[33m这是黄色字体\033[0m")
    print("\033[34m这是蓝色字体\033[0m")
    print("\033[38m这是默认字体\033[0m")

