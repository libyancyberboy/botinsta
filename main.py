from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
import requests
import telebot
import os
from telebot import types
from flask import Flask, request

# إعدادات المستخدم
uid = uuid4()
csr = token_hex(8) * 2

# توكن البوت الخاص بك
token = "7501655078:AAFJseSaIx1oo7bbyhTGPoh7j9Xrbczuj74"
bot = telebot.TeleBot(token, parse_mode="HTML")

# إعداد Flask
app = Flask(__name__)

@app.route('/' + token, methods=['POST'])
def receive_update():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

@app.route('/')
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your-vercel-app-url.vercel.app/' + token)  # ضع رابط Vercel هنا
    return 'Webhook set', 200

@bot.message_handler(commands=['start'])
def start(message):
    buttons = types.InlineKeyboardMarkup(row_width=1)
    bot.send_message(message.chat.id, '''<strong>
اهلا بك🎉
في بوت معرفه معلومات انستجرام من يوزر.

/helpar لكي اعطيك الاوامر بالعربيه
/helpen For Orders in English
/helptr Türkçe sipariş almak için
</strong>''', parse_mode='html', reply_to_message_id=message.message_id, reply_markup=buttons)

@bot.message_handler(commands=['helpar'])
def helpar(message):
    bot.send_message(message.chat.id, '''<strong>
الاوامر: 🔰
1 -⚜️
لمعرفه معلومات حساب الانتسجرام كاملة
                ( /ig اليوزر )
مثال 
/ig mahos 
</strong>''', parse_mode='html', reply_to_message_id=message.message_id)

@bot.message_handler(commands=['helpen'])
def helpen(message):
    bot.send_message(message.chat.id, '''<strong>
Commands: 🔰
1 - ⚜️ To know the complete information of the Instagram account 
(/ig user), 
example /ig mahos
</strong>''', parse_mode='html', reply_to_message_id=message.message_id)

@bot.message_handler(commands=['helptr'])
def helptr(message):
    bot.send_message(message.chat.id, '''<strong>
Komutlar: 🔰 
1 - ⚜️ Instagram hesabının tüm bilgilerini öğrenmek için 
(/ig kullanıcı), örnek /ig mahos 
</strong>''', parse_mode='html', reply_to_message_id=message.message_id)

@bot.message_handler(commands=['ig'])
def instagram(message):
    try:
        if "/ig" in message.text:
            card_info = message.text.replace("/ig", "").strip()
            user = card_info

            heada = {
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "i.instagram.com",
                "Connection": "Keep-Alive",
                "User-Agent": generate_user_agent(),
                "Cookie": f"mid=YwvCRAABAAEsZcmT0OGJdPu3iLUs; csrftoken={csr}",
                "Accept-Language": "en-US",
                "X-IG-Capabilities": "AQ==",
            }

            datai = {
                "q": user,
                "device_id": f"android{uid}",
                "guid": uid,
                "_csrftoken": csr
            }

            res = requests.post('https://i.instagram.com/api/v1/users/lookup/', headers=heada, data=datai).json()
            profile_pic_url = res['user']['profile_pic_url']

            rr = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}', headers=heada).json()
            Id = rr['data']['user']['id']
            Name = rr['data']['user']['full_name']
            bio = rr['data']['user']['biography']
            flos = rr['data']['user']['edge_followed_by']['count']
            flog = rr['data']['user']['edge_follow']['count']
            email = res.get('obfuscated_email', 'N/A')
            phone = res.get('obfuscated_phone', 'N/A')
            is_private = res['user']['is_private']
            is_verified = res['user']['is_verified']

            msg = f'''
⋘─────━*𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝙽𝙵𝙾*━─────⋙
𝐍𝐀𝐌𝐄 ⇾ {Name}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ⇾ @{user}         
𝐈𝐃 ⇾ {Id}
𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ⇾ {flos}
𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 ⇾ {flog}
𝐁𝐈𝐎 ⇾ {bio}
𝐔𝐑𝐋 ⇾ https://www.instagram.com/{user}
𝐄𝐌𝐀𝐈𝐋 ⇾ {email}
𝐏𝐇𝐎𝐍𝐄 ⇾ {phone}
𝐏𝐑𝐈𝐕𝐀𝐓𝐄 ⇾ {is_private}
𝐕𝐄𝐑𝐈𝐅𝐈𝐄𝐃 ⇾ {is_verified}
⋘─────━*𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝙽𝙵𝙾*━─────⋙
            '''

            bot.send_photo(message.chat.id, profile_pic_url, caption=msg, parse_mode='html')
        
    except Exception as e:
        msg = f'''Error: {str(e)}'''
        bot.reply_to(message, msg)

# تشغيل التطبيق على Vercel
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    except:
        pass
