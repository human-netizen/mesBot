import json
import requests, pickle
from bs4 import BeautifulSoup as Soup
import time
import random
import time
from mega import Mega
import os
mega = Mega()
m = mega.login('proniloy9@gmail.com','#pronot0MA')
folder = m.find('comments')
folder = folder[0]

def write_fun(data, file_name):
    global didtime
    try:
        try:
            f = repo.get_contents(file_name)
            repo.update_file(file_name, 'updated', data, f.sha)
        except:
            repo.create_file(file_name, 'updated', data)
        didtime = 0
    except:
        if (didtime < 3):
            time.sleep(2)
            print('#w#')
            write_fun(data, file_name)
            didtime += 1
        else:
            didtime = 0


def append_fun(data, file_name):
    global didtime
    try:
        f = repo.get_contents(file_name)
        r = repo.get_contents(file_name).decoded_content.decode()
        repo.update_file(file_name, 'updated', r + "\n" + data, f.sha)
    except:
        if (didtime < 3):
            time.sleep(2)
            print('#ax#')
            append_fun(date, file_name)
            didtime += 1
        else:
            didtime = 0


def read_fun_list(file_name):
    temp_list = []
    try:
        f = repo.get_contents(file_name).decoded_content.decode().split('\n')
        temp_list = [x for x in f if x]
    except Exception as e:
        print(e)

    return temp_list


def read_fun_string(file_name):
    temp_string = ""
    try:
        temp_string = repo.get_contents(file_name).decoded_content.decode()

    except Exception as e:
        print(e)

    return temp_string


from_path = 'media.json'  # eta change korte hobe
done = []
from github import Github

github = Github('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')
repo = github.get_repo('human-netizen/mesBot')
done = read_fun_list('done.txt')
big_file = open(from_path)
links = json.load(big_file)
total_file = len(links)


def img_name(url):
    ed = url.find('?')
    st = url.rfind('/', 0, ed) + 1
    return url[st:ed]


for idx, l in enumerate(links):
    if(len(done)%100 == 0):
        done_data = json.dumps(done,ensure_ascii = False,indent = 4)
        done.append('hola')
        append_fun(done_data,'done.txt')
    print(len(done))
    if (not l):
        continue
    l = l.strip()
    image_name = img_name(l)
    if (image_name in done):
        continue

    timeout = 999 if idx >= total_file else 1
    try:
        r = requests.get(l, timeout = timeout)
        done.append(image_name)
        if (r.text == 'URL signature expired'):
            continue
    except:
        links.append(l)
        continue

    with open(image_name, 'wb') as image_file:
        image_file.write(r.content)
    m.upload(image_name,folder)
    os.remove(image_name)
    time.sleep(.1)
