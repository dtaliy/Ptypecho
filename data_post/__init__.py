import requests


data = {'dbAdapter':'Pdo_Mysql',
'dbHost':'',
'dbPort':'3306',
'dbUser':'root',
'dbPassword':'',
'dbDatabase':'typecho',
'dbCharset':'utf8',
'dbCharset':'utf8',
'dbEngine':'MyISAM',
'dbPrefix':'typecho_',
'userUrl':'',
'userName':'',
'userPassword':'',
'userMail':'',
'action':'config'}

header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate',
'Referer':'',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length':'281',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1'}
class imformation():
    def __init__(self,dbhost,userurl,userpassword,dbpassword,username ,usermail):
        self._dbhost = dbhost
        self._dbpassword = dbpassword
        self._userurl = userurl
        self._username = username
        self._userpassword = userpassword
        self._usermail = usermail
        self._dict = {}
        self._header = {}
    def __get_dict(self):
        self._dict = dict
    def __get_hearder(self):
        self._header = header
    def update(self):
        self._dict["dbHost"] = self._dbhost
        self._dict['dbPassword'] = self._dbpassword
        self._dict['usrUrl'] = "http://" + self._userurl
        self._dict['userMail'] = self._usermail
        self._dict['userName'] = self._username
        self._dict['userPassword'] = self._userpassword
    def sent(self):
        url = 'http://'+self._userurl+ '/install.php?config'
        self._header['Referer'] = 'http://' + url + '/install.php?config'
        r = requests.post(url,data=self._dict,headers=self._header)
        if r.status_code == 200 :
            print("安装完毕")
        else:
            print("安装出现了不可描述的错误，请联系作者")