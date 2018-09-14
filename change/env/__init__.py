import os
import subprocess
def env():
    docker = subprocess.getstatusoutput("sudo docker ps | awk '{print $1}'")
    if docker[1] != "CONTAINER":
        os.system("sudo curl -sSL https://get.daocloud.io/docker | sh")
    docker_compose = subprocess.getstatusoutput("ls /usr/local/bin | grep 'docker-compose'")

    command_env = """
        sudo curl -L https://get.daocloud.io/docker/compose/releases/download/1.22.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose &&
        sudo chmod +x /usr/local/bin/docker-compose
        """
    if docker_compose[1] != "docker-compose":
        os.system(command_env)


    command_file = """
        sudo git clone https://github.com/dtaliy/docker-typecho.git
        cd docker-typecho
        sudo git clone https://github.com/typecho/typecho.git
    """
    os.system(command_file)
