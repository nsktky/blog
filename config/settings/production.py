# 本番環境用設定ファイル

from .base import *

# SECRET_KEYはherokuの環境変数として設定
SECRET_KEY = os.environ.get('SECRET_KEY')

# 本番環境なのでDEBUGはFALSEにする
DEBUG = False

# herokuにデプロイするためALLOWED_HOSTSに記載
ALLOWED_HOSTS = [".herokuapp.com"]

# heroku環境でPostgresを使用するためdj_database_urlを使用
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# 画像のアップロードや表示のためcloudinaryを使用。INSTALLED_APPSに追加。
INSTALLED_APPS.append('cloudinary')
INSTALLED_APPS.append('cloudinary_storage',)

# 各変数は環境変数として設定
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
    'API_KEY': os.environ.get('API_KEY'),
    'API_SECRET': os.environ.get('API_SECRET')
}

# modelsのimagefieldをcloudinaryに対応させるため必要
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'