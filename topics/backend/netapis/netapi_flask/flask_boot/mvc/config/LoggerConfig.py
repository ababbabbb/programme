import logging
import logging.handlers
import os
import re

from frame.conventions import BasicConfig


class Log:
    @staticmethod
    def init(log_path: str):
        """初始化日志模块"""
        logger = logging.getLogger()
        if not logger.handlers:
            logger.setLevel(logging.INFO)

            # 终端输出
            logging_formatter = logging.Formatter(
                '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
            sh = logging.StreamHandler()
            sh.setFormatter(logging_formatter)
            logger.addHandler(sh)

            # 日志文件设置
            os.makedirs(os.path.split(log_path)[0], exist_ok=True)
            file_handler = logging.handlers.TimedRotatingFileHandler(
                filename=log_path, when="MIDNIGHT", interval=1, backupCount=30)
            file_handler.suffix = "%Y-%m-%d.log"
            file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
            file_handler.setFormatter(logging_formatter)  # 定义日志输出格式
            logger.addHandler(file_handler)


class LoggerConfig(BasicConfig):
    sort = 0
    LOG_PATH = None

    def init_app(self, app):
        if self.LOG_PATH:
            Log.init(self.LOG_PATH)
