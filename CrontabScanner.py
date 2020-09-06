# coding=utf-8

import os

from lib.result_writer import write_result

class CrontabScanner:
    def __init__(self, high_privilege_user, low_privilege_user):
        self.high_privilege_user = high_privilege_user
        self.low_privilege_user = low_privilege_user

    def scan(self):
        print("[*]Loading CrontabScanner to scan crontab...")
        cmd1 = "crontab -l"
        print("[*]Running command: " + cmd1)
        result1 = os.popen(cmd1).read()
        lines = result1.split("\n")

        script_name = []
        for line in lines:
            if not line.startswith("#") and ".sh" in line:
                for content in line.split():
                    if content.endswith(".sh"):
                        name = os.path.basename(content)
                        cmd2 = "find / -name " + name + " -user " + self.low_privilege_user + " 2>/dev/null"
                        print("[*]Running command: " + cmd2)
                        result2 = os.popen(cmd2).read()
                        if result2.find(name) != -1:
                            script_name.append(name)

        if len(script_name) > 0:
            print("[!]Found in crontab!")
            write_result("[!]Found in crontab!")
            for script in script_name:
                print("[+]Low privilege user's shell script in crontab: " + script)
                write_result("[+]Low privilege user's shell script in crontab: " + script)
