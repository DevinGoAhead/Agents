import logging.config
import os

# 确保日志目录存在
os.makedirs("logs", exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        "simple": {"format": "%(levelname)s: %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",  # 滚动日志，防止单文件过大
            "level": "INFO",
            "formatter": "standard",
            "filename": "logs/app.log",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 3,  # 最多保留 3 个备份文件
            "encoding": "utf-8",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
    "loggers": {
        "httpx": {
            "level": "WARNING",
        },
        "httpcore": {
            "level": "WARNING",
        },
        "openai": {
            "level": "WARNING",
        },
        "urllib3": {
            "level": "WARNING",
        },
    },
}


def setup_logging():
    """初始化日志配置"""
    logging.config.dictConfig(LOGGING_CONFIG)
