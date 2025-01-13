from abc import ABC, abstractmethod
from user import AdminUser, RegularUser, GuestUser

class UserFactory(ABC):
    @abstractmethod
    def create_user(self, username):
        pass


class AdminUserFactory(UserFactory):
    def create_user(self, username):
        return AdminUser(username)


class RegularUserFactory(UserFactory):
    def create_user(self, username):
        return RegularUser(username)


class GuestUserFactory(UserFactory):
    def create_user(self, username):
        return GuestUser(username)
