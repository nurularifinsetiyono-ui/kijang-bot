import telebot, threading, time, random, re, os
from datetime import datetime
TOKEN=os.getenv("TOKEN")
MY_ID=8896553858
bot=telebot.TeleBot(TOKEN)
KARYAWAN={1:"Budi",2:"Siti",3:"Joko",4:"Ani",5:"Rudi",6:"Dewi",7:"Agus",8:"Lina",9:"Slamet",10:"Kijang"}
stat={i:"ON DUTY" for i in range(1,11)}
def kirim_aman(text):
    while True:
        try:
            bot.send_message(MY_ID, text)
            break
        except:
            time.sleep(5)
@bot.message_handler(func=lambda m: True)
def all_msg(m):
    if m.chat.id!=MY_ID: return
    t=m.text.lower()
    if "/status" in t:
        s=f"STATUS {datetime.now().strftime('%H:%M')}\n"
        for i in range(1,11): s+=f"{i}.{KARYAWAN[i]}:{stat[i]}\n"
        bot.reply_to(m,s)
    elif "/scan" in t:
        bot.reply_to(m,f"SCAN {random.choice(['BUY','SELL'])}")
    elif "/off" in t:
        n=re.findall(r"\d+",t)
        if n: stat[int(n[0])]="OFF"; bot.reply_to(m,f"OFF {n[0]}")
    elif "/on" in t:
        n=re.findall(r"\d+",t)
        if n: stat[int(n[0])]="ON DUTY"; bot.reply_to(m,f"ON {n[0]}")
def auto_loop():
    while True:
        time.sleep(300)
        kirim_aman(f"AUTO XAU {random.choice(['BUY','SELL'])}")
threading.Thread(target=auto_loop, daemon=True).start()
bot.infinity_polling()
