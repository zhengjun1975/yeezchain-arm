
import subprocess
import shlex
import os
import threading
import time


class repeat_timer(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


def run_cmd(cmd):
    assert isinstance(cmd, str)
    ret = subprocess.check_output(shlex.split(cmd))
    return ret.decode('utf-8')


def read_file(filename, rtype):
    assert isinstance(filename, str)
    assert os.path.exists(filename)
    f = open(filename, rtype)
    content = f.read()
    f.close()
    return content


def write_file(filename, content, wtype):
    assert isinstance(filename, str)
    f = open(filename, wtype)
    f.write(content)
    f.close()
