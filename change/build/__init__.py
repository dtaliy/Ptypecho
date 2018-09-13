import os
def build():

    command = """
            cd ./php &&
            sudo docker build -t scofieldpeng/php-fpm:7.2.3-fpm . &&
            cd .. &&
            sudo docker-compose up -d
    """
    os.system(command)
