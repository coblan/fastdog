import re
import datetime

def decode_utf8(lines):
    for line in lines:
        line['message'] = line['message'].decode('utf-8')
    return lines

def strip_word(field,lines):
    'INFO 2020-03-12 15:32:29,803 推送拨打记录给app后台,返回状态码200,返回结果{"code":1,"message":"success","data":null}'
    for line in lines:
        message = line.get('message').lstrip()
        word = re.search('\w+',message).group()
        line[field] = word
        line['message'] = message[len(word):]
    return lines

def strip_span(field,span,lines):
    for line in lines:
        message = line.get('message').lstrip()
        word = message[:span]
        line[field] = word
        line['message'] = message[len(word):].strip()
    return lines

def datetime_timestamp(lines):
    beijin = datetime.timezone(datetime.timedelta(hours=8))
    for line in lines:
        line['@timestamp'] = datetime.datetime.strptime(line['@timestamp'],'%Y-%m-%d %H:%M:%S,%f').replace(tzinfo = beijin)
    return lines