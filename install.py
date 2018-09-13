#/usr/bin/python3

import os
from change.build import *
from change.env import *
from change.choose import *
from buildup import *

sex = choose()
#安装docker与compose
env()

#更改域名
if sex == 1:
    buildup()
else:
    #部署
    build()


