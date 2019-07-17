LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'bencoder.log',
            'encoding': 'utf-8',
            'maxBytes': 1024 * 1024,
            'backupCount': 1,
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
    }
}

MEDIAINFO_PATH = 'tools/MediaInfo.exe'

TOOLS = {
    'info': ['tools/MediaInfo.exe', '-f', '--Output=JSON'],
    'subtitle': 'tools/SubtitleEdit.exe',
    'encoder': 'tools/ffmpeg.exe',
    'mkvtool': 'tools/mkvmerge.exe',
}

INPUT_PATH = 'd:/토렌트/모아'
OUTPUT_PATH = 'viki-output'
WHITE_LIST = ('.avi', '.mkv', '.mp4', '.mov', '.3gp', '.wmv', 'webm', 'flv')
BALCK_LIST = ('.jpg', '.png', '.gif', '.jpeg', '.zip', '.alz', '.7z')
SUBTITLE_TYPES = ('.smi', '.sami', '.srt', '.ass', '.sub', '.sbv')
