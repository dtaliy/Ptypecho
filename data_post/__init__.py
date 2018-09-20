import requests
import time


header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
class imformation():
    def __init__(self,dbhost,userurl,userpassword,dbpassword,username ,usermail):
        self._dbhost = dbhost
        if dbpassword == '':
            self._dbpassword = '123456'
        else:
            self._dbpassword = dbpassword
        self._userurl = userurl
        self._username = username
        self._userpassword = userpassword
        self._usermail = usermail
        self._dict = {
'dbAdapter':'Pdo_Mysql',
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


    def update(self):
        self._dict["dbHost"] = self._dbhost
        self._dict['dbPassword'] = self._dbpassword
        self._dict['userUrl'] = "http://" + self._userurl
        self._dict['userMail'] = self._usermail
        self._dict['userName'] = self._username
        self._dict['userPassword'] = self._userpassword
    def sent(self):

        url = 'http://'+self._userurl+ '/install.php?config'
        self.update()
        print(url)
        print(self._dict)
        r = requests.post(url,data=self._dict,headers=header)
        print(r.status_code)
        print(r.text)
    def write_conf(self):
        configphp = """<?php
/**
 * Typecho Blog Platform
 *
 * @copyright  Copyright (c) 2008 Typecho team (http://www.typecho.org)
 * @license    GNU General Public License 2.0
 * @version    $Id$
 */

/** 定义根目录 */
define('__TYPECHO_ROOT_DIR__', dirname(__FILE__));

/** 定义插件目录(相对路径) */
define('__TYPECHO_PLUGIN_DIR__', '/usr/plugins');

/** 定义模板目录(相对路径) */
define('__TYPECHO_THEME_DIR__', '/usr/themes');

/** 后台路径(相对路径) */
define('__TYPECHO_ADMIN_DIR__', '/admin/');

/** 设置包含路径 */
@set_include_path(get_include_path() . PATH_SEPARATOR .
__TYPECHO_ROOT_DIR__ . '/var' . PATH_SEPARATOR .
__TYPECHO_ROOT_DIR__ . __TYPECHO_PLUGIN_DIR__);

/** 载入API支持 */
require_once 'Typecho/Common.php';

/** 程序初始化 */
Typecho_Common::init();

/** 定义数据库参数 */
$db = new Typecho_Db('Pdo_Mysql', 'typecho_');
$db->addServer(array (
  'host' => '192.168.64.2',
  'user' => 'root',
  'password' => '123456',
  'charset' => 'utf8',
  'port' => '3306',
  'database' => 'typecho',
  'engine' => 'MyISAM',
), Typecho_Db::READ | Typecho_Db::WRITE);
Typecho_Db::set($db);

"""
        configphp = configphp.replace('192.168.64.2',self._dbhost)
        configphp = configphp.replace('123456',self._dbpassword)

        with open("typecho/config.inc.php",'w') as f:
            f.write(configphp)