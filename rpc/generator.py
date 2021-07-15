
import argparse
import eth_api
import random
from datetime import datetime
import time
import util
import toml


def parse_args():
    parser = argparse.ArgumentParser(description='eth rpc api',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--source', type=str, help='transaction address send from')
    parser.add_argument('--target', type=str, help='transaction address send to')
    args = parser.parse_args()
    return args


def payload_generator(chset, size):
    payload = str()
    while size:
        index = random.random() * len(chset)
        payload = payload + chset[int(index)]
        size = size - 1
    return payload


def main():
    args = parse_args()
    ea = eth_api.eth_api('127.0.0.1', '26660')
    while True:
        payload = payload_generator('0123456789abcdef', 20)
        ret = ea.eth_sendTransaction(args.source, args.target, hex(int(random.random()*10000)), payload)
        print(ret)
        time.sleep(15)

if __name__ == '__main__':
    main()
