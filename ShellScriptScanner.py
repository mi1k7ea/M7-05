# coding=utf-8

import os

from lib.result_writer import write_result

class ShellScriptScanner:
    def __init__(self, path, high_privilege_user, low_privilege_user):
        self.path = path
        self.high_privilege_user = high_privilege_user
        self.low_privilege_user = low_privilege_user

    def scan(self):
        print("[*]Loading ShellScriptScanner to scan *.sh files...")
        # find /tmp -name "*.sh" -user high_privilege_user 2>/dev/null
        cmd1 = "find " + self.path + " -name \"*.sh\" -user " + self.high_privilege_user + " 2>/dev/null"
        print("[*]Running command: " + cmd1)
        result1 = os.popen(cmd1).read()
        files = result1.split("\n")
        for file in files:
            if not os.path.exists(file):
                continue
            with open(file, "r") as f:
                script_name = []
                for line in f.readlines():
                    content = line.split()
                    for c in content:
                        if c.endswith(".sh"):
                            name = os.path.basename(c)
                            # find / -name a.sh -user low_privilege_user 2>/dev/null
                            cmd2 = "find / -name " + name + " -user " + self.low_privilege_user + " 2>/dev/null"
                            print("[*]Running command: " + cmd2)
                            result2 = os.popen(cmd2).read()
                            if result2.find(name) != -1:
                                script_name.append(name)
                if len(script_name) > 0:
                    print("[!]Found By ShellScriptScanner!")
                    print("[+]High privilege user's shell script: " + file)
                    write_result("[!]Found By ShellScriptScanner!")
                    write_result("[+]High privilege user's shell script: " + file)
                    for script in script_name:
                        print("[+]Low privilege user's shell script: " + script)
                        write_result("[+]Low privilege user's shell script: " + script)
