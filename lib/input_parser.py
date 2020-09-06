# coding=utf-8

from optparse import OptionParser
import sys
import os

from lib.conf import DEFAULT_PATH, DEFAULT_HIGH_PRIVILEGE_USER

# 解析命令行输入参数
def input_parse():
    parser = OptionParser('python m7-05.py -l <Low Privilege Username> '
                          '[-h <High Privilege Username> -p <Path for Scan>]')
    parser.version = "M7-05 v1.0"
    parser.add_option("-v", "--version", dest="version", action="store_true", help="show scanner's version and exit")
    parser.add_option('--low-privilege-user', dest='low_privilege_user',
                      type='string', help='low privilege username')
    parser.add_option('--high-privilege-user', dest='high_privilege_user', type='string',
                      default=DEFAULT_HIGH_PRIVILEGE_USER, help='[Optional] high privilege username (default "root")')
    parser.add_option('-p', '--path', dest='path', type='string',
                      default=DEFAULT_PATH, help='[Optional] path for scan (default "/")')

    (options, args) = parser.parse_args()

    if options.version:
        print(parser.version, "  --  By Mi1k7ea")
        sys.exit(1)

    if not options.low_privilege_user:
        parser.print_help()
        sys.exit(1)

    if options.path:
        if not os.path.exists(options.path):
            parser.error("[-]Path doesn't exist.")
            sys.exit(1)

    return options
