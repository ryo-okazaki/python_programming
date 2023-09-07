import logging.config

# logging.config.fileConfig('logging.ini') #どちらか
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'sampleFormatter': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        }
    },
    'handlers': {
        'sampleHandlers': {
            'class': 'logging.StreamHandler',
            'formatter': 'sampleFormatter',
            'level': logging.DEBUG
        }
    },
    'root': {
        'handlers': ['sampleHandlers'],
        'level': logging.DEBUG
    },
    'loggers': {
        'simpleExample': {
            'handlers': ['sampleHandlers'],
            'level': logging.DEBUG,
            'propagate': 0
        }
    }
})

# logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleExample')

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')