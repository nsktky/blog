# 本番環境用設定ファイル

from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ["ayameblog.herokuapp.com"]

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)