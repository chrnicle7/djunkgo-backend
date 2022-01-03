import bcrypt

class PasswordHelper():

    @staticmethod
    def check_password_hash(plain_password, hashed):
        plain_password = plain_password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain_password, salt)

        return bcrypt.checkpw(plain_password, hashed)

    @staticmethod
    def hash_password(plain_password):
        plain_password = plain_password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain_password, salt)

        return hashed