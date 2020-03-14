import datetime
from functools import partial
from . share import strip_span,strip_word,decode_utf8,datetime_timestamp

def join_line(lines):
    '整理文件格式，拼接多行，整理不符合普通django格式的日志'
    out_lines = []
    last_line =None
    for line in lines:
        message = line['message']
        if message .startswith(('ERROR','DEBUG','INFO','WARNING')):
            last_line = {'path':line['path'],'message':message }
            out_lines.append(last_line)
        elif not last_line:
            now = datetime.datetime.now()
            last_line ={'path':line['path'],'message':'FORMAT %s %s'%(now.strftime('%Y-%m-%d %H:%M:%S,%f'),message)}
        else:
            last_line['message'] += '\n%s'%line['message']
    return out_lines





django_log_parsers =[
                       decode_utf8,
                       join_line,
                       partial(strip_word,'level'),
                       partial(strip_span,'@timestamp',23), datetime_timestamp,
                       
                    ]