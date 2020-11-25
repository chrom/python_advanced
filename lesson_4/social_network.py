# Создать подобие социальной сети.
# 1) Создать класс авторизации, в котором описать методы регистрации, аутентификации, добавить
# методы проверки на валидность пароля (содержание символов и цифр), проверка на уникальность
# логина пользователя. В классовых переменных хранить всех пользователей сети.
# (Отдельно объекты этого класса создаваться не будут, такие классы называются миксинами)
import hashlib, binascii, os, datetime


class Authorization:
    users: dict = {}

    def __init__(self):
        _is_authorized: bool = False

    def registration(self):
        user = Authorization.users.get(self.email)
        if user is None:
            if self.password_validate(user.password):
                user.password = self.hash_password()
                Authorization.users[user.email] = user
            else:
                raise Warning('The password does not meet the specified criteria.')
        else:
            raise Warning('User with this email already exist!')

    def authorization(self, email: str, password: str):
        if Authorization.users.get(email) is None:
            raise Warning('User with this email not exist!')

        user = Authorization.users.get(email)
        if self.verify_password(user.password, password):
            user._is_authorized = True
        else:
            raise Warning('Password is wrong!')

    def hash_password(self) -> str:
        password = self.password
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def verify_password(stored_password: str, provided_password: str) -> bool:
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    @staticmethod
    def password_validate(password: str) -> bool:
        """Check if the password is valid.

        This function checks the following conditions
        if its length is greater than 6 and less than 8
        if it has at least one uppercase letter
        if it has at least one lowercase letter
        if it has at least one numeral
        if it has any of the required special symbols
        """
        special_sym = ['$', '@', '#']
        result = True
        if len(password) < 6:
            print('the length of password should be at least 6 char long')
            result = False
        if len(password) > 25:
            print('the length of password should be not be greater than 25')
            result = False
        if not any(char.isdigit() for char in password):
            print('the password should have at least one numeral')
            result = False
        if not any(char.isupper() for char in password):
            print('the password should have at least one uppercase letter')
            result = False
        if not any(char.islower() for char in password):
            print('the password should have at least one lowercase letter')
            result = False
        if not any(char in special_sym for char in password):
            print('the password should have at least one of the symbols $@#')
            result = False
        if result:
            print('Password is Ok!')
            print(result)
        return result


# 2) Создать класс пользователя, наследующий класс авторизации. который будет разделять  роли
# админа и простого пользователя (этот вопрос можно решить с помощью флага is_admin, либо
# создав 2 разных класса для админа и обычного пользователя и наследовать их). Класс
# пользователя должен наследовать класс авторизации. На момент создания каждого объекта этого
# класса, в переменную объекта сохранять время и дату его создания.

class User(Authorization):

    def __init__(self, email: str, password: str, is_admin: bool = False):
        self._is_admin = is_admin
        self._email = email
        self._password = password
        self._created_at = datetime.date.today()
        super().__init__()

    @property
    def is_admin(self) -> bool:
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value: bool):
        self._is_admin = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = value

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        pass


user1 = User('admin@admin.com', 'PasSword123$')
user1.registration()
user1.authorization('admin@admin.com', 'PasSword123$')
print(user1.__dict__)

user2 = User('1admin@admin.com', 'PasSword123$')
user2.registration()
user2.authorization('1admin@admin.com', 'PasSword123$')
print(user2.__dict__)

user3 = User('2admin@admin.com', 'PasSword123$')
user3.registration()
user3.authorization('1admin@admin.com', 'PasSword123$')
print(user3.__dict__)

# 3) Создать класс поста, который имеет дату публикации и её содержимое.
