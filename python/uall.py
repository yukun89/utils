from threading import Event

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


##
import time

def process_bar(seconds=10, event=None):
    start = time.perf_counter()
    scale=50#进度条长度
    unit=0.5#进度条刷新频率
    used_time=0
    i = 0#完成的进度条个数
    while i < scale:
        if event is not None and event.is_set():
            i=scale
        passed = "*" * i
        remaining = "." * (scale - i)
        percent = (i / scale) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(percent,passed,remaining,dur),end = "")
        time.sleep(unit)
        used_time+=unit
        expected_percent=min(1.0*used_time/seconds, 0.98)
        i=max(int(expected_percent*50),i)

process_bar(10)
display()
