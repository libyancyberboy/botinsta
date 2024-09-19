#------------[المكاتب المطلوبه]----------------#

from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
import urllib.request
import requests
import telebot
import os
from telebot import types
import pycountry
from datetime import datetime
uid = uuid4()
csr = token_hex(8) * 2

token = "7501655078:AAFJseSaIx1oo7bbyhTGPoh7j9Xrbczuj74" #توكنك
bot = telebot.TeleBot(token, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):
    buttons = types.InlineKeyboardMarkup(row_width=1)
    but1 = types.InlineKeyboardButton(text='المطور - Developer', url='https://t.me/')
    but2 = types.InlineKeyboardButton(text='قناة المطور - Channel Developer', url='https://t.me/')
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

            patre = {
                "Host": "www.tiktok.com",
                "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": "\"Android\"",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "sec-fetch-site": "none",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5,zh-CN;q=0.4,zh;q=0.3"
            }

            tikinfo = requests.get(f'https://www.tiktok.com/@{fm}', headers=patre).text        

            try:
                getting = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
                try:
                    id = str(getting.split('id":"')[1]).split('",')[0]
                except:
                    id = ""
                try:
                    name = str(getting.split('nickname":"')[1]).split('",')[0]
                except:
                    name = ""
                try:
                    bio = str(getting.split('signature":"')[1]).split('",')[0]
                except:
                    bio = ""
                try:
                    country = str(getting.split('region":"')[1]).split('",')[0]
                except:
                    country = ""
                try:
                    private = str(getting.split('privateAccount":')[1]).split(',"')[0]
                except:
                    private = ""
                try:
                    followers = str(getting.split('followerCount":')[1]).split(',"')[0]
                except:
                    followers = ""
                try:
                    following = str(getting.split('followingCount":')[1]).split(',"')[0]
                except:
                    following = ""
                try:
                    like = str(getting.split('heart":')[1]).split(',"')[0]
                except:
                    like = ""
                try:
                    video = str(getting.split('videoCount":')[1]).split(',"')[0]
                except:
                    video = ""
                try:
                    secid = str(getting.split('secUid":"')[1]).split('"')[0]
                except:
                    secid = ""
                try:
                    countryn = str(pycountry.countries.get(alpha_2=country)).split("name='")[1].split("'")[0]
                except:
                    countryn = ""
                try:
                    countryf = str(pycountry.countries.get(alpha_2=country)).split("flag='")[1].split("'")[0]
                except:
                    countryf = ""
                binary = "{0:b}".format(int(id))
                i = 0
                bits = ""
                while i < 31:
                    bits += binary[i]
                    i += 1
                timestamp = int(bits, 2)
                try:
                    cdt = datetime.fromtimestamp(timestamp)
                except:
                    cdt = ""

                msg = f'''
═════════𝚃𝙸𝙺𝚃𝙾𝙺═══════════
𝐍𝐀𝐌𝐄 ⇾ {name}
𝐈𝐃 ⇾ {id}
𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 ⇾ {fm}
𝐅𝐎𝐋𝐋𝐎𝐖𝐄𝐑𝐒 ⇾ {followers}
𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 ⇾ {following}
𝐋𝐈𝐊𝐄𝐒 ⇾ {like}
𝐕𝐈𝐃𝐄𝐎 ⇾ {video}
𝐂𝐎𝐔𝐍𝐓𝐑𝐘 ⇾ {country}
𝐂𝐎𝐔𝐍𝐓𝐑𝐘_𝐍𝐀𝐌𝐄 ⇾ {countryn}
𝐂𝐎𝐔𝐍𝐓𝐑𝐘_𝐅𝐋𝐀𝐆 ⇾ {countryf}
𝐏𝐑𝐈𝐕𝐓𝐄𝐒 ⇾ {private}
𝐒𝐄𝐂𝐔𝐈𝐃 ⇾ {secid}
𝐁𝐈𝐎 ⇾ {bio}
𝐔𝐑𝐋 ⇾ https://www.tiktok.com/@{fm}
═════════𝚃𝙸𝙺𝚃𝙾𝙺═══════════
𝙳𝙴𝚅: 
'''
                bot.reply_to(message, msg)

            except (KeyError, IndexError):
                msg = f'''Error Username 🚫 ⇾ {fm}\nTry again'''
                bot.reply_to(message, msg)
                
    except Exception as e:
        msg = f'''An error occurred: {str(e)}'''
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
            try:
                email = res['obfuscated_email']
            except:
                email = ""
            try:
                phone = res['obfuscated_phone']
            except:
                phone = ""
            try:
                Private = res['user']['is_private']
            except:
                Private = ""
            try:
                FP = res['fb_login_option']
            except:
                FP = ""
            try:
                WH = res['can_wa_reset']
            except:
                WH = ""
            try:
                Sms = res['can_sms_reset']
            except:
                Sms = ""
            try:
                rest = res['can_email_reset']
            except:
                rest = ""
            try:
                Ph = res['has_valid_phone']
            except:
                Ph = ""
            try:
                Varfid = res['user']['is_verified']
            except:
                Varfid = ""
            try:
                profile_pic_url = res['user']['profile_pic_url']
            except:
                profile_pic_url = ""
                
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
            try:
                Id = rr['data']['user']['id']
            except:
                Id = ""
            try:
                Name = rr['data']['user']['full_name']
            except:
                Name = 'No name'
            try:
                bio = rr['data']['user']['biography']
            except:
                bio = ""
            try:
                flos = rr['data']['user']['edge_followed_by']['count']
            except:
                flos = ""
            try:
                flog = rr['data']['user']['edge_follow']['count']
            except:
                flog = ""               

            try:
                re = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}").json()
                da = re['date']
            except:
                da = 'No Date'

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
𝙳𝙴𝚅: 
            '''

            with open(profile_pic_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=msg, parse_mode='html')                
                os.remove(profile_pic_path)
        
    except Exception as e:
        msg = f'''Error: {str(e)}'''
        bot.reply_to(message, msg)
        
while True:
    try:
        bot.infinity_polling()
    except:
        pass