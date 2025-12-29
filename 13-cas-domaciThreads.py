import subprocess
import webbrowser
from win10toast import ToastNotifier
import time
import threading

toaster = ToastNotifier()

subprocess.Popen(["C:/Program Files/JetBrains/PyCharm 2025.2.4/bin/pycharm64.exe"])
webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://www.itskola.net")
#pozivamo odredjenu web stranicu

def notification():
    while True:
        toaster.show_toast("Reminder!","Pobednicki", duration=5)
        time.sleep(6)

threadnotificate=threading.Thread(target=notification()) #paralelno radi ovu funkciju notification()
threadnotificate.start() #pocni funkciju notification()
print("Hello")
