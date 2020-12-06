import random, string
import webbrowser
import time
import requests

print("""/ vicious#1337
""")
time.sleep(0.2)

num=input('Amount of Nitro codes to generate: ')

f=open("codes.txt","w", encoding='utf-8')

print("[Generating]")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24))
   f.write('discord.gift/')
   f.write(y)
   f.write("\n")

f.close()

with open("codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid: {} ".format(line.strip("\n")))
            break
        else:
        	print(" Invalid: {} ".format(line.strip("\n")))
input("Press enter 5 times to exit")
input("4")
input("3")
input("2")
input("1")
