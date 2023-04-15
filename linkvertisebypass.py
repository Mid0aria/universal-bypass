#coded by @mid0aria on github
import requests
from os import system

system("cls && title 𝙇𝙄𝙉𝙆𝙑𝙀𝙍𝙏𝙄𝙎𝙀 𝙇𝙄𝙉𝙆 𝘽𝙔𝙋𝘼𝙎𝙎𝙀𝙍")


def purple(text):
    system(""); faded = ""
    red = 35
    for character in text:
        red += 3
        if red > 255:
            red = 255
        faded += (f"\033[38;2;{red};0;220m{character}")
    return faded

def red(text):
    system(""); faded = ""
    green = 250
    for character in text:
        green -= 5
        if green < 0:
            green = 0
        faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
    return faded


link = input(purple(" [>] Linkvertise link : "))

headers = {
	"origin": "https://thebypasser.com",
	"referer": "https://thebypasser.com/"
    }

try:
    data = requests.get(f"https://api.toksaver.com/bypass/" + link, headers=headers)
    link = data.json()["link"]
    print(purple(f" [>] Destination link : {link}"))
except:
    print(red(" [!] An unexpected error occurred"))

system("pause >nul")