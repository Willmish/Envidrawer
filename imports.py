import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
        "[%(asctime)s.%(msecs)03d][TID: %(threadName)-10s : %(log_color)s%(levelname)-8s]%(reset)s %(blue)s%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        reset=True,
        log_colors={
            'DEBUG'     :   'cyan',
            'INFO'      :   'green',
            'WARNING'   :   'yellow',
            'ERROR'     :   'red',
            'CRITICAL'  :   'red,bg_white',
        },
        secondary_log_colors={},
        style='%'))

logger = colorlog.getLogger('logger') # setup one global logger and filter by TID
logger.addHandler(handler)

