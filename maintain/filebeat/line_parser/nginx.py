import re
from functools import partial
from . share import decode_utf8,strip_word,strip_span
import re
import datetime

def get_ip(lines):
    pattern = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    for line in lines:
        messge = line['message']
        messge = messge.lstrip()
        mt = re.search(pattern,messge)
        if mt :
            line['ip'] = mt.group()
            line['message'] = messge[len(line['ip']):]
    return lines

def nginx_datetime(lines):
    "[13/Mar/2020:07:25:00 +0800] GET ...."
    pattern = r'\[(\d{2}\/[A-Za-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2}) (\+|\-)\d{4}\]'
    beijin = datetime.timezone(datetime.timedelta(hours=8))
    for line in lines:
        messge = line['message']
        mt = re.search(pattern,messge)
        if mt :
            timestamp_str = mt.group(1)
            line['@timestamp'] = datetime.datetime.strptime(timestamp_str,'%d/%b/%Y:%H:%M:%S').replace(tzinfo = beijin)
            line['message'] = messge[:mt.start(0)] + messge[mt.end(0): ]
    return lines
    
def nginx_path(lines):
    pattern = r'[^\s]+'
    for line in lines:
        messge = line['message']
        mt = re.search(pattern,messge)
        if mt :
            url = mt.group()
            line['url'] = url
            line['message'] = messge[:mt.start(0)] + messge[mt.end(0): ]
    return lines


nginx_log_parser = [
    decode_utf8,
    #get_ip,
    #partial(strip_span,'_no_use',5),
    nginx_datetime
]

nginx_log_full_parser = [
    decode_utf8,
    get_ip,
    partial(strip_span,'_no_use',4),
    nginx_datetime,
    partial(strip_span,'_no_use',1),
    partial(strip_word,'method'),
    nginx_path,

]