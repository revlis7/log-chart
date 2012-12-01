#!/usr/bin/python
import sys

def ip_chart(line):
    global result
    global distinct
    if line.startswith('TRACE'):
        fields = line.split(' ', 8)
        if fields.__len__() >=8:
            if set(fields[5]).issubset(set('1234567890.')):
                key = fields[5]
                query = fields[0] + fields[1] + fields[2] + fields[3] + fields[4] + fields[5] + fields[6]
                if query not in distinct:
                    distinct[query] = 1
                    if key in result:
                        result[key] += 1
                    else:
                        result[key] = 1

def url_chart(line):
    global result
    global distinct
    if line.startswith('TRACE'):
        fields = line.split(' ', 8)
        if fields.__len__() >=8:
            if set(fields[5]).issubset(set('1234567890.')):
                key = fields[6]
                query = fields[0] + fields[1] + fields[2] + fields[3] + fields[4] + fields[5] + fields[6]
                if query not in distinct:
                    distinct[query] = 1
                    if key in result:
                        result[key] += 1
                    else:
                        result[key] = 1

def ip_url_chart(line, ip):
    global result
    global distinct
    if line.startswith('TRACE'):
        fields = line.split(' ', 8)
        if fields.__len__() >=8:
            if set(fields[5]).issubset(set('1234567890.')) and fields[5] == ip:
                key = fields[6]
                query = fields[0] + fields[1] + fields[2] + fields[3] + fields[4] + fields[5] + fields[6]
                if query not in distinct:
                    distinct[query] = 1
                    if key in result:
                        result[key] += 1
                    else:
                        result[key] = 1

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc == 2:
        option = sys.argv[1]
    elif argc == 3:
        option = sys.argv[1]
        ip = sys.argv[2]
    else:
        sys.exit()
    result = {}
    distinct = {}
    file_name = 'log-2012-11-22.log'
    f = open(file_name)
    lines = f.readlines()
    f.close()
    for line in lines:
        if option == '--url-chart':
            url_chart(line)
        elif option == '--ip-chart':
            ip_chart(line)
        elif option == '--ip-url-chart':
            ip_url_chart(line, ip)
    for key in result:
        print key, result[key]