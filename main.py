import telepot
import requests
import json

def s(a, b, c):
    u = 'https://ws.messaggisms.com/messages/'
    h = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer 67a684d65fc3100a8d0ca426',
    }
    d = {
        "test": False,
        "sender": a,
        "body": b,
        "recipients": c
    }
    r = requests.post(u, headers=h, json=d)
    return r.json()

def f(r):
    if "-" in r:
        return r
    else:
        return r[:3] + "-" + r[3:]

def h(m):
    c = m['chat']['id']
    t = m['text']
    s_c = u_s.get(c, None)

    if t.startswith('/start'):
        b.sendMessage(c, "/spoof - for SID spoofing")
    elif t.startswith('/spoof'):
        u_s[c] = 'w_s'
        b.sendMessage(c, "enter the sender id")
    elif s_c == 'w_s':
        a = t
        u_s[c] = 'w_b'
        u_d[c] = {'sender': a}
        b.sendMessage(c, "enter the body message")
    elif s_c == 'w_b':
        b_m = t
        u_d[c]['body'] = b_m
        u_s[c] = 'w_r'
        b.sendMessage(c, "enter the sender, format: +39-3333333333.")
    elif s_c == 'w_r':
        r_m = t
        fr = f(r_m)
        a = u_d[c]['sender']
        b_m = u_d[c]['body']
        r = s(a, b_m, fr)
        # Risposta con il formato "codice"
        b.sendMessage(c, f"done, API response 👇\n```\n{json.dumps(r, indent=4)}\n```", parse_mode='MarkdownV2')
        u_s[c] = None

u_s = {}
u_d = {}
T = '7067666430:AAFrtDCBWSLrKfI_K_od65Kd9OMeXk_kqlg'
b = telepot.Bot(T)
b.message_loop(h)

print('hosted..')

import time
while True:
    time.sleep(10)
