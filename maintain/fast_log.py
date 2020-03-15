import logging
import logging.config
import sys

def set_log(path,level='DEBUG'):
    config = {
        'version': 1,
        'formatters': {
            'standard': {
                #'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                #'format': '%(levelname)s %(asctime)s %(message)s',
                'format': '%(levelname)s %(asctime)s %(process)d-%(thread)d %(message)s'
            },
            # 其他的 formatter
        },
        'handlers': {
            'console': {
                'level':'DEBUG',
                'class': 'logging.StreamHandler',
                'stream': sys.stdout
                }, 
            'rotfile':{
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                 #'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
                'maxBytes': 1024*1024*5,
                'backupCount':3,
                'formatter':'standard',
                'filename': path,   
            },  
        },
        'loggers':{
            '':{
                'handlers': ['console','rotfile' ],
                'level': level,
                'propagate': True,  
            },
            'general_log':{
                #'propagate': True,  
            }
            
            # 其他的 Logger
        }
    }
    
    logging.config.dictConfig(config)
