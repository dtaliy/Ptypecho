
import subprocess

output = subprocess.getstatusoutput("sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(sudo docker ps | grep 'mysql' | awk '{print $1}')")
key = output[1]