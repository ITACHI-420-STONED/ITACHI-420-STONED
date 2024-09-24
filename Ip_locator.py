# copy paste and edit does not make u the coder😂
import json
import requests
from colorama import Fore


banner = """
     ███████╗██╗███╗░░██╗██████╗░
     ██╔════╝██║████╗░██║██╔══██╗
     █████╗░░██║██╔██╗██║██║░░██║
     ██╔══╝░░██║██║╚████║██║░░██║
     ██║░░░░░██║██║░╚███║██████╔╝
     ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░

        ██╗░░██╗██╗███╗░░░███╗
        ██║░░██║██║████╗░████║
        ███████║██║██╔████╔██║
        ██╔══██║██║██║╚██╔╝██║
        ██║░░██║██║██║░╚═╝░██║
        ╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝
"""


FOOTER_TEXT = "got this mf🤣"
FOOTER_ICON = "https://media.discordapp.net/attachments/1284586063347847342/1287598512640626758/IMG_2546.png?ex=66f2210f&is=66f0cf8f&hm=d47caf319413d7308516b14544297e4631ad139c8346377bd8f993a99d575897&=&width=810&height=810"
IMAGE_URL = "https://media.discordapp.net/attachments/1284586063347847342/1287598512640626758/IMG_2546.png?ex=66f2210f&is=66f0cf8f&hm=d47caf319413d7308516b14544297e4631ad139c8346377bd8f993a99d575897&=&width=810&height=810"  # Change this to your desired image URL
WEBHOOK_NAME = "ITACHIS IP LOCATOR"
WEBHOOK_AVATAR = "https://media.discordapp.net/attachments/1284586063347847342/1287598512640626758/IMG_2546.png?ex=66f2210f&is=66f0cf8f&hm=d47caf319413d7308516b14544297e4631ad139c8346377bd8f993a99d575897&=&width=810&height=810"  # Custom webhook avatar image URL

class whois:
    def __init__(self):
        print(f"{Fore.LIGHTWHITE_EX}{banner}")
        print(f"{Fore.LIGHTGREEN_EX}Enter someone's IP and press enter")
        self.ipadd = input(Fore.WHITE + "Input IP ~# ").strip()


        if self.ipadd.startswith("127") or self.ipadd.startswith("192"):
            print(
                f"{Fore.RED} The Input Address is a local host",
                f"\n{Fore.RED} This is not a Valid IP Address",
            )
            exit()


        self.webhook_url = input(Fore.WHITE + "Enter Webhook URL ~# ").strip()

    def send_to_webhook(self):
        response = requests.get(f"http://ipwhois.app/json/{self.ipadd}")
        json_response = json.loads(response.text)
        
        fields = []
        for key, value in json_response.items():
            if value:
                fields.append(f"**{key.title()}**: {str(value).strip()}")

        
        embed_content = "\n".join(fields)
        data = {
            "content": "@everyone",
            "username": WEBHOOK_NAME,
            "avatar_url": WEBHOOK_AVATAR,
            "embeds": [{
                "title": f"IP Lookup for {self.ipadd}",
                "description": embed_content,
                "color": 16711680,
                "footer": {
                    "text": FOOTER_TEXT,
                    "icon_url": FOOTER_ICON
                },
                "image": {
                    "url": IMAGE_URL
                }
            }]
        }
        response = requests.post(self.webhook_url, json=data, headers={"Content-Type": "application/json"})
        
        if response.status_code == 204:
            print(Fore.GREEN + "IP info sent to webhook successfully!")
        else:
            print(Fore.RED + "Failed to send data to the webhook.")


obj = whois()
obj.send_to_webhook()
