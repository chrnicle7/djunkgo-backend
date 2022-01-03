from decouple import config

"""
    Database configuration
"""
POSTGRES_DEV = {
    "user"          : config('DB_USERNAME'),
    "password"      : config('DB_PASSWORD'),
    "host"          : config('DB_HOST'),
    "port"          : config('DB_PORT'),
    "db"            : config('DB_DATABASE'),
}
DB_URL_DEV = "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s" % POSTGRES_DEV



"""
    JWT configuration
"""
JWT_SECRET_KEY = config('JWT_SECRET_KEY')