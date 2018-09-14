from selenium import webdriver
import time


class imformation():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.elem = None
    def send(self,id,v):
        self.elem = self.driver.find_element_by_id(id).send_keys(v)
    def finsh(self,dbHost,userurl,dbPassword,userName,userPassword,userMail):
        url = 'http://'+self._userurl+ '/install.php?config'
        self.driver.get(url)
        self.send('dbHost',dbHost)
        self.send('dbPassword',dbPassword)
        self.send('userName',userName)
        self.send('userPassword',userPassword)
        self.send('userMail',userMail)
        self.driver.find_element_by_class_name("btn primary").click()
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