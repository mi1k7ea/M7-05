# coding=utf-8

from lib.conf import DEFAULT_RESULT_FILE

def write_result(content):
    with open(DEFAULT_RESULT_FILE, "a+") as f:
        f.write(content + "\n")
