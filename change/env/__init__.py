import os
import subprocess
def env():
    docker = subprocess.getstatusoutput("sudo docker ps | awk '{print $1}'")
    if docker[1] != 'CONTAINER':
        os.system("sudo curl -sSL https://get.daocloud.io/docker | sh &&")
    command = """
        sudo curl -L https://get.daocloud.io/docker/compose/releases/download/1.22.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose &&
        sudo chmod +x /usr/local/bin/docker-compose
        sudo git clone https://github.com/dtaliy/docker-typecho.git
        sudo git clone https://github.com/typecho/typecho.git
    """
    os.system(command)