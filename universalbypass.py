#coded by @mid0aria on github
import requests
from os import system

system("cls && title 𝙇𝙄𝙉𝙆𝙑𝙀𝙍𝙏𝙄𝙎𝙀 𝙇𝙄𝙉𝙆 𝘽𝙔𝙋𝘼𝙎𝙎𝙀𝙍 / Github: @mid0aria")


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

while True:
	link = input(purple("[>] Linkvertise link : "))

	headers = {
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
	    }

	try:
	    data = requests.get(f"https://bypass.pm/bypass2?url=" + link, headers=headers)
	    link = data.json()["destination"]
	    plugin = data.json()["plugin"]
	    print(purple(f"[>] Destination link : {link}"))
	    print(red(f"[>] Plugin: {plugin}"))
	except:
	    print(red("[!] An unexpected error occurred"))

	select = int(input("[1] Bypass\n[99] Exit\n> "))
	if select == 99:
		break
