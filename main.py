import telebot
import requests
from user_agent import generate_user_agent

# ضع هنا التوكن الخاص بالبوت الخاص بك
TOKEN = '8084485795:AAFPAACdA8gLblPaW07-zihsy12jjpD-mWg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['s'])
def instagram(message):
    try:
        if "/s" in message.text:
            card_info = message.text.replace("/s", "").strip()
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

            he = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en;q=0.9',
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
⋘─────━*𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝙽𝙵𝙾*━─────⋙
𝐍𝐀𝐌𝐄 ⇾ {Name}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ⇾ @{user}         
𝐈𝐃 ⇾ {Id}
𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ⇾ {flos}
𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 ⇾ {flog}
𝐁𝐈𝐎 ⇾ {bio}
𝐃𝐀𝐓𝐄 ⇾ {da}
𝐄𝐌𝐀𝐈𝐋 ⇾ {email}
𝐏𝐇𝐎𝐍𝐄 ⇾ {phone}
𝐏𝐑𝐈𝐕𝐀𝐓𝐄 ⇾ {Private}
𝐅𝐁 𝐎𝐏𝐓𝐈𝐎𝐍 ⇾ {FP}
𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐑𝐄𝐒𝐄𝐓 ⇾ {WH}
𝐒𝐌𝐒 𝐑𝐄𝐒𝐄𝐓 ⇾ {Sms}
𝐄𝐌𝐀𝐈𝐋 𝐑𝐄𝐒𝐄𝐓 ⇾ {rest}
𝐕𝐀𝐋𝐈𝐃 𝐏𝐇𝐎𝐍𝐄 ⇾ {Ph}
𝐕𝐄𝐑𝐈𝐅𝐈𝐄𝐃 ⇾ {Varfid}
𝐔𝐑𝐋 ⇾  https://www.instagram.com/{user}
⋘─────━*𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝙽𝙵𝙊*━─────⋙
            '''

            bot.reply_to(message, msg)
            
    except Exception as e:
        msg = f'''Error Username 🚫 ⇾ {user}\nTry again'''
        bot.reply_to(message, msg)

bot.polling()
