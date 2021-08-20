from flask import Flask, request
import logging.config


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(name)s | %(asctime)s | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },

        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "logfile.log",
            "when": "h",
            "interval": 10,
            "backupCount": 1
        }
    },
    "loggers": {
        "server_logger": {
            "lvl": "DEBUG",
            "handlers": ["file", "console"],
        }
    },
}

logging.config.dictConfig(dict_config)
logger = logging.getLogger('server_logger')
logger.setLevel('DEBUG')


app = Flask(__name__)


@app.route(
    "/logs", methods=["POST"],
)
def _ps():
    message = request.form

    logger.debug(f"from {message['name']} | {message['levelname']} |  {message['msg']}")
    # logger.debug(message) # эта строка если запрос передается через curl http://127.0.0.1:5000/logs --data "123"

    return f"ok"


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
