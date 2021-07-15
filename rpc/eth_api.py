
import argparse
import json
import string
from datetime import datetime
import time

import util


class eth_api:

    def __init__(self, host, port):
        self.header_get = 'Accept: application/json'
        self.header_post = 'Content-Type: application/json'
        self.host = '%s:%s' % (host, port)


    def eth_sendTransaction(self, source, target, value, data):
        assert isinstance(source, str)
        assert isinstance(target, str)
        assert isinstance(value, str)
        assert isinstance(data, str)
        assert all(ch in string.hexdigits for ch in data)
        method = 'eth_sendTransaction'
        d = {
                'method': method,
                'params': [{
                    'from': source,
                    'to': target,
                    'value': value,
                    'gas': '0xfffff',
                    'data': data
                    }],
                'id': 1,
                'jsonrpc': '2.0'
                }
        cmd = '''curl -s --data '%s' -H %s -X POST %s''' % (json.dumps(d), self.header_post, self.host)
        ret = util.run_cmd(cmd)
        return ret


def parse_args():
    parser = argparse.ArgumentParser(description='eth rpc api',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--method', type=str, default='eth_blockNumber', help='eth rpc method')
    parser.add_argument('--source', type=str, help='transaction address send from')
    parser.add_argument('--target', type=str, help='transaction address send to')
    parser.add_argument('--value', type=str, help='transaction value')
    parser.add_argument('--data', type=str, help='transaction payload')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    op_code = {
            'eth_sendTransaction': 'eth_api().eth_sendTransaction(args.source, args.target, args.value, args.data)'
            }
    ret = eval(op_code[args.method])
    print(ret)


if __name__ == '__main__':
    main()
