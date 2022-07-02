import os

DATA_PATH = "data/data.json"
COMMENTS_PATH = "data/comments.json"
DATA_PATH_BOOKMARKS = "data/bookmarks.json"

LOGGER_API_PATH = os.path.join("logs", "api.log")
LOGGER_FORMAT = f"%(asctime)s - %(levelname)s - %(name)s -(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
