import pwn
import json
import re

timeout_default = 1e7
ignore_empty = False
delay_time = 0
conn = None

def extract_json(data):
    if isinstance(data, str):
        data = data.encode()
    return re.findall(rb'\{.*\}', data)

def extract_list(data):
    if isinstance(data, str):
        data = data.encode()
    return re.findall(rb'\[.*\]', data)

def extract_int(data):
    if isinstance(data, str):
        data = data.encode()
    return re.findall(rb'\d+', data)

def extract_hex(data):
    if isinstance(data, str):
        data = data.encode()
    return re.findall(rb'[0-9a-f]+', data)

def extract_base64(data):
    if isinstance(data, str):
        data = data.encode()
    return re.findall(rb'[A-Za-z0-9+/]+=', data)

def connect(host, port):
    global conn
    conn = pwn.remote(host, port)

def recvall(out = True, timeout = None):
    global conn
    if timeout is None:
        timeout = timeout_default
    data = conn.recv(timeout=timeout)
    while conn.can_recv(delay_time):
        data += conn.recv(timeout=timeout)
    if out:
        print(data.decode(), end='')
    if ignore_empty:
        return recvall(out, timeout)
    return data

def recvjson(out = True, timeout = None, n = 0):
    if timeout is None:
        timeout = timeout_default
    data = recvall(out, timeout)
    data = extract_json(data)[n]
    data = json.loads(data)
    return data

def recvlist(out = True, timeout = None, n = 0):
    if timeout is None:
        timeout = timeout_default
    data = recvall(out, timeout)
    data = extract_list(data)[n]
    data = eval(data)
    return data

def recvline(out = True, timeout = None):
    global conn
    if timeout is None:
        timeout = timeout_default
    data = conn.recvline(timeout=timeout)
    if out:
        print(data.decode(), end='')
    if ignore_empty:
        return recvline(out, timeout)
    return data

def sendjson(data, out = True):
    global conn
    data = json.dumps(data).encode()
    if out:
        print(data)
    conn.sendline(data)

def sendline(data, out = True):
    global conn
    if not isinstance(data, bytes) and not isinstance(data, bytearray):
        data = str(data).encode()
    if out:
        print(data)
    conn.sendline(data)

def recvsend(data, out = True):
    res = recvall(out)
    sendline(data, out)
    return res

def recvsendlist(list_data, out = True, recv_first = False):
    res = []
    if not conn.can_recv(1) and not recv_first:
        sendline(list_data.pop(0), out)
    for data in list_data:
        res.append(recvsend(data, out))
    return res

rj  = lambda out = True: recvjson(out)
rln = lambda out = True: recvline(out)
rl  = lambda out = True: recvlist(out)
ra  = lambda out = True: recvall(out)
rs  = lambda data, out = True: recvsend(data, out)
sj  = lambda data, out = True: sendjson(data, out)
sl  = lambda data, out = True: sendline(data, out)
xj  = lambda data: extract_json(data)
xl  = lambda data: extract_list(data)
xi  = lambda data: extract_int(data)
xh  = lambda data: extract_hex(data)
xb  = lambda data: extract_base64(data)
rsl = lambda list_data, out = True, recv_first = False: recvsendlist(list_data, out, recv_first)

def recvdelay(recvfunc, *args, t = 1):
    global delay_time
    delay_time = t
    res = recvfunc(*args)
    delay_time = 0
    return res

rd = lambda recvfunc, *args, t = 1: recvdelay(recvfunc, *args, t = t)

__all__ = ['conn', 'connect', 'recvall', 'recvjson', 'recvlist', 'recvline', 'sendjson', 'sendline', 'recvsend', 'recvsendlist', 'recvdelay', 'rj', 'rl', 'ra', 'rs', 'sj', 'sl', 'xj', 'xl', 'xi', 'xh', 'xb', 'rsl', 'rd']