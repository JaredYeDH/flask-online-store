DEBUG = True
SECRET_KEY = 'yoursecret'
STRIPE_API_KEY = 'yourapisecret'
BCRYPT_LEVEL = 13
MAIL_FROM_EMAIL = "admin@example.com"
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@server/fos'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SERVER_NAME = 'fos.dev'
DEBUG_TB_INTERCEPT_REDIRECTS=False
UPLOADS_DEFAULT_DEST = "public"
UPLOADS_DEFAULT_URL  = "http://fos.dev/"
