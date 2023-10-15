class InvalidTokenError(Exception):
    pass


class AuthenticationError(Exception):
    def __init__(self, message="Invalid username or password"):
        self.message = message
        super().__init__(self.message)


class InvalidPasswordError(Exception):
    def __init__(self, message="Invalid password"):
        self.message = message
        super().__init__(self.message)


class InvalidUsernameError(Exception):
    def __init__(self, message="Invalid username"):
        self.message = message
        super().__init__(self.message)


class UsernameExistsError(Exception):
    def __init__(self, message="A user with that name already exists"):
        self.message = message
        super().__init__(self.message)


class EmailExistsError(Exception):
    def __init__(self, message="A user with that email already exists"):
        self.message = message
        super().__init__(self.message)
