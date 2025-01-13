from factory import AdminUserFactory, RegularUserFactory, GuestUserFactory

if __name__ == "__main__":
    admin_factory = AdminUserFactory()
    regular_factory = RegularUserFactory()
    guest_factory = GuestUserFactory()

    admin = admin_factory.create_user("admin123")
    regular = regular_factory.create_user("user456")
    guest = guest_factory.create_user("guest789")

    print(admin.get_permissions())  
    print(regular.get_permissions())  
    print(guest.get_permissions())  
