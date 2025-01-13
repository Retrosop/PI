from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def get_permissions(self):
        pass


class AdminUser(User):
    def __init__(self, username):
        super().__init__(username)
        self.admin_tools = ["Add User", "Delete User", "View Logs"]

    def get_permissions(self):
        return f"Admin permissions for {self.username}: {', '.join(self.admin_tools)}"


class RegularUser(User):
    def __init__(self, username):
        super().__init__(username)
        self.permissions = ["View Content", "Comment"]

    def get_permissions(self):
        return f"Regular user permissions for {self.username}: {', '.join(self.permissions)}"


class GuestUser(User):
    def __init__(self, username):
        super().__init__(username)
        self.permissions = ["View Content"]

    def get_permissions(self):
        return f"Guest user permissions for {self.username}: {', '.join(self.permissions)}"
