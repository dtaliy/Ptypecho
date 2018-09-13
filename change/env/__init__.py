import os
def env():
    command = """
        sudo curl -sSL https://get.daocloud.io/docker | sh &&
        sudo curl -L https://get.daocloud.io/docker/compose/releases/download/1.22.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose &&
        sudo chmod +x /usr/local/bin/docker-compose
        sudo git cone https://github.com/scofieldpeng/docker-typecho.git
        sudo git cone https://github.com/typecho/typecho.git
    """
    os.system(command)