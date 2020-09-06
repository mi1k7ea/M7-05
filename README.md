# M7-05
个人使用的一款Linux shell脚本提权扫描器。

针对的场景是Linux环境下的脚本提权类问题，即高权限用户（默认为root）的脚本中运行了低权限用户的脚本，当低权限用户修改自己的脚本内容就会达到脚本提权的目的。

这里仅仅对两种最常见的场景进行扫描，其他场景可自行补充：

1. 在高权限用户如root的脚本中运行了低权限用户的脚本；
2. 在高权限用户如root的crontab定时任务中运行了低权限用户的脚本；

使用方法：

```powershell
Usage: python m7-05.py -l <Low Privilege Username> [-h <High Privilege Username> -p <Path for Scan>]

Options:
  -h, --help            show this help message and exit
  -v, --version         show scanner's version and exit
  --low-privilege-user=LOW_PRIVILEGE_USER
                        low privilege username
  --high-privilege-user=HIGH_PRIVILEGE_USER
                        [Optional] high privilege username (default "root")
  -p PATH, --path=PATH  [Optional] path for scan (default "/")
```

- --low-privilege-user参数指定低权限用户，即高权限脚本中调用的低权限脚本的属主；
- --high-privilege-user参数指定高权限用户，即高权限脚本的属主，默认为root；
- -p参数指定扫描目录，默认为根目录`/`；
- -u参数指定对目标URL进行Flash CSRF扫描，必须结合`-t csrf`参数进行使用；

example：

```bash
python m7-05.py --low-privilege-user git --high-privilege-user root -p /tmp/test/
```

扫描效果：

```powershell
root@ubuntu:~/M7-05# python m7-05.py --low-privilege-user git --high-privilege-user root -p /tmp/test/


        _|      _|  _|_|_|_|_|                _|    _|_|_|_|
        _|_|  _|_|          _|              _|  _|  _|
        _|  _|  _|        _|    _|_|_|_|_|  _|  _|  _|_|_|
        _|      _|      _|                  _|  _|        _|
        _|      _|    _|                      _|    _|_|_|   v1.0


[*]Start to scan shell script privilege escalation...
[*]Loading ShellScriptScanner to scan *.sh files...
[*]Running command: find /tmp/test/ -name "*.sh" -user root 2>/dev/null
[*]Running command: find / -name b.sh -user git 2>/dev/null
[*]Running command: find / -name c.sh -user git 2>/dev/null
[!]Found By ShellScriptScanner!
[+]High privilege user's shell script: /tmp/test/a.sh
[+]Low privilege user's shell script: b.sh
[+]Low privilege user's shell script: c.sh
[*]Loading CrontabScanner to scan crontab...
[*]Running command: crontab -l
[*]Running command: find / -name crontab_test.sh -user git 2>/dev/null
[!]Found in crontab!
[+]Low privilege user's shell script in crontab: crontab_test.sh
[*]Finished.
root@ubuntu:~/M7-05# cat result/result.txt
[*]Scan Task at 2020-09-06 16:38:53.581886
[*]Scan Path: /tmp/test/
[*]High Privilege User: root
[*]Low Privilege User: git
[!]Found By ShellScriptScanner!
[+]High privilege user's shell script: /tmp/test/a.sh
[+]Low privilege user's shell script: b.sh
[+]Low privilege user's shell script: c.sh
[!]Found in crontab!
[+]Low privilege user's shell script in crontab: crontab_test.sh
[*]Finished.
root@ubuntu:~/M7-05#  
```

