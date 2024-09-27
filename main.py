#------------[المكاتب المطلوبه]----------------#

from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
import urllib.request
import requests
import telebot
import os
from telebot import types

uid = uuid4()
csr = token_hex(8) * 2

token = "8084485795:AAFPAACdA8gLblPaW07-zihsy12jjpD-mWg" #توكنك
bot = telebot.TeleBot(token, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):
    buttons = types.InlineKeyboardMarkup(row_width=1)
    but1 = types.InlineKeyboardButton(text='المطور - Developer', url='https://t.me/maho_s9')
    but2 = types.InlineKeyboardButton(text='قناة المطور - Channel Developer', url='https://t.me/maho9s')
    buttons.add(but1, but2)
    bot.send_message(message.chat.id, '''<strong>
اهلا بك🎉
في بوت معرفه معلومات تيك توك او انستجرام من يوزر.

There is a bot to find out information about Tik Tok or Instagram from User.


Kullanıcıdan Tik Tok veya Instagram hakkında bilgi almak için bir bot var.

/helpar لكي اعطيك الاوامر بالعربيه
/helpen For Orders in English
/helptr Türkçe sipariş almak için
</strong>''', parse_mode='html', reply_to_message_id=message.message_id, reply_markup=buttons)

@bot.message_handler(commands=['helpar'])
def helpar(message):
    bot.send_message(message.chat.id, '''<strong>
الاوامر: 🔰
1 -⚜️
لمعرفه معلومات حساب الانتسجرام كامله قد يصحب مع ذلك عمل ريست للحساب
                ( /ig اليوزر )
مثال 
/ig mahos 
2 - ✴️
لمعرفه معلومات حساب التيك توك كامله
             ( /tik اليوزر )
مثال 
/tik maho_s9 
</strong>''', parse_mode='html', reply_to_message_id=message.message_id)
@bot.message_handler(commands=['helpen'])
def helpen(message):
    bot.send_message(message.chat.id, '''<strong>
Commands: 🔰
 1 - ⚜️ To know the complete information of the Instagram account, it may be accompanied by a reset of the account 
(/ig user), 
example /ig mahos
 2 - ✴️ To know the complete information of the Tik Tok account
(/tik the user), example
 /tik maho_s9
</strong>''', parse_mode='html', reply_to_message_id=message.message_id)

@bot.message_handler(commands=['helptr'])
def helptr(message):
    bot.send_message(message.chat.id, '''<strong>
Komutlar: 🔰 
1 - ⚜️ Instagram hesabının tüm bilgilerini öğrenmek için, 
buna hesabın sıfırlanması 
(/ig kullanıcısı) 
eşlik edebilir, örnek /ig mahos 
2 - ✴️ Tik Tok hesabının tüm bilgilerini bilmek için 
( /tik kullanıcı), örnek /tik maho_s9 .
</strong>''', parse_mode='html', reply_to_message_id=message.message_id)

@bot.message_handler(commands=['tik'])
def tiktok(message):
    try:
        if "/tik" in message.text:
            card_info = message.text.replace("/tik", "").strip()
            fm = card_info

            url = 'http://tik.report.ilebo.cc/users/login'
            headers = {
                'X-IG-Capabilities': '3brTvw==',
                'User-Agent': 'TikTok 85.0.0.21.100 Android (33/13; 480dpidpi; 1080x2298; HONOR; ANY-LX2; ANY-LX2;)',
                'Accept-Language': 'en-US',
                'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': '73',
                'Host': 'tik.report.ilebo.cc',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip'
            }
            data = {
                'unique_id': fm,
                'purchaseTokens': []
            }
            response = requests.post(url, headers=headers, json=data).json()
            if 'data' in response:
                user_data = response['data']['user']['user']
                stats = response['data']['user']['stats']
                a_user_data = response['data']['aUser']

                Id = user_data['id']
                user = user_data['uniqueId']
                name = user_data['nickname']
                folon = stats['followingCount']
                folos = stats['followerCount']
                lik = stats['heartCount']
                vid = stats['videoCount']
                age = user_data['underAge18']
                priv = user_data['privateAccount']
                sec_uid = user_data.get('secUid', '')
                bio = user_data.get('signature', '')

                msg = f'''
═════════𝚃𝙸𝙺𝚃𝙾𝙺═══════════
𝐍𝐀𝐌𝐄 ⇾ {name}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ⇾ {fm}
𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ⇾ {folos}
𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 ⇾ {folon}
𝐋𝐈𝐊𝐄𝐒 ⇾ {lik}
𝐕𝐈𝐃𝐄𝐎 ⇾ {vid}
𝐀𝐆𝐄 ⇾ {age}
𝐏𝐑𝐈𝐕𝐓𝐄𝐒 ⇾ {priv}
𝐒𝐄𝐂𝐔𝐈𝐃 ⇾ {sec_uid}
𝐁𝐈𝐎 ⇾{bio}
𝐔𝐑𝐋 ⇾ https://www.tiktok.com/@{fm}
═════════𝚃𝙸𝙺𝚃𝙾𝙺═══════════
𝙳𝙴𝚅: @maho_s9 | @maho9s
'''
                bot.reply_to(message, msg)
            
                
    except Exception as e:
        msg = f'''Erorr Username 🚫 ⇾ {user}\nTry again'''
        bot.reply_to(message, msg)

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
                "Cookie2": "$Version=1",
                "Accept-Language": "en-US",
                "X-IG-Capabilities": "AQ==",
                "Accept-Encoding": "gzip",
            }

            datai = {
                "q": user,
                "device_id": f"android{uid}",
                "guid": uid,
                "_csrftoken": csr
            }

            res = requests.post('https://i.instagram.com/api/v1/users/lookup/', headers=heada, data=datai).json()
            email = res.get('obfuscated_email')
            phone = res.get('obfuscated_phone')
            Private = res['user'].get('is_private')
            FP = res.get('fb_login_option')
            WH = res.get('can_wa_reset')
            Sms = res.get('can_sms_reset')
            rest = res.get('can_email_reset')
            Ph = res.get('has_valid_phone')
            Varfid = res['user'].get('is_verified')
            profile_pic_url = res['user'].get('profile_pic_url')            
            profile_pic_path = f"{user}.jpg"
            urllib.request.urlretrieve(profile_pic_url, profile_pic_path)

            he = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en;q=0.9',
                'cookie': f'ig_did={uuid4()}; datr=8J8TZD9P4GjWjawQJMcnRdV_; mid=ZBOf_gALAAGhvjQbR29aVENHIE4Z; ig_nrcb=1; csrftoken=5DoPPeHPd4nUej9JiwCdkvwwmbmkDWpy; ds_user_id=56985317140; dpr=1.25',
                'referer': f'https://www.instagram.com/{user}/?hl=ar',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"10.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': generate_user_agent(),
                'viewport-width': '1051',
                'x-asbd-id': '198387',
                'x-csrftoken': '5DoPPeHPd4nUej9JiwCdkvwwmbmkDWpy',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': '0',
                'x-requested-with': 'XMLHttpRequest',
            }

            rr = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}', headers=he).json()
            Id = rr['data']['user']['id']
            Name = rr['data']['user']['full_name']
            bio = rr['data']['user']['biography']
            flos = rr['data']['user']['edge_followed_by']['count']
            flog = rr['data']['user']['edge_follow']['count']
            re = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}").json()
            da = re["date"]

            msg = f'''
⋘─────━*??𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝙽𝙵𝙾*━─────⋙
𝐍𝐀𝐌𝐄 ⇾ {Name}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ⇾ @{user}         
𝐈𝐃 ⇾ {Id}
𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ⇾ {flos}
𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 ⇾ {flog}
𝐁𝐈𝐎 ⇾ {bio}
𝐃𝐀𝐓𝐄 ⇾ {da}
𝐔𝐑𝐋 ⇾  https://www.instagram.com/{user}
𝐄𝐌𝐀𝐈𝐋 ⇾ {email}
𝐏𝐇𝐎𝐍𝐄 ⇾ {phone}
𝐏𝐑𝐈𝐕𝐓𝐄𝐒 ⇾ {Private}
𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐋𝐎𝐆𝐈𝐍 ⇾ {FP}
𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐑𝐄𝐒𝐄𝐓 ⇾ {WH}
𝐒𝐌𝐒 𝐑𝐄𝐒𝐄𝐓 ⇾ {Sms}
𝐄𝐌𝐀𝐈𝐋 𝐑𝐄𝐒𝐄𝐓 ⇾ {rest}
𝐕𝐀𝐋𝐈𝐃 𝐏𝐇𝐎𝐍𝐄 ⇾ {Ph}
𝐕𝐄𝐑𝐈𝐅𝐈𝐄𝐃 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 ⇾ {Varfid}
⋘─────━*𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝙽𝙵𝙾*━─────⋙
𝙳𝙴𝚅: @maho_s9 | @maho9s
            '''

            with open(profile_pic_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=msg, parse_mode='html')                
                
        
            
            
    except Exception as e:
        msg = f'''Erorr Username 🚫 ⇾ {user}\nTry again'''
        bot.reply_to(message, msg)

bot.infinity_polling()
