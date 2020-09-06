# coding=utf-8

import datetime

from lib.banner import show_banner
from lib.input_parser import input_parse
from lib.result_writer import write_result
from ShellScriptScanner import ShellScriptScanner
from CrontabScanner import CrontabScanner

def main():
    show_banner()
    options = input_parse()
    print("[*]Start to scan shell script privilege escalation...")
    write_result("[*]Scan Task at " + str(datetime.datetime.now()))
    write_result("[*]Scan Path: " + options.path)
    write_result("[*]High Privilege User: " + options.high_privilege_user)
    write_result("[*]Low Privilege User: " + options.low_privilege_user)
    shell_script_scanner = ShellScriptScanner(options.path, options.high_privilege_user, options.low_privilege_user)
    shell_script_scanner.scan()
    crontab_scanner = CrontabScanner(options.high_privilege_user, options.low_privilege_user)
    crontab_scanner.scan()
    print("[*]Finished.")
    write_result("[*]Finished.")

if __name__ == '__main__':
    main()
