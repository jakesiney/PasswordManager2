from datetime import datetime

"""
A user can add a password.
A user can update a password.
A user can delete a password.
A user can list passwords for a service.
A user can list services saved with a password.
Lists can be sorted by date added and optionally in reverse order.
Passwords must be unique.
The password must be greater than 8 characters include a special characer.
"""


class PasswordManager2():
    def __init__(self) -> None:
        self.vault = {}
        self.specials = ["!", "@", "$", "%", "&"]

    def pw_length(self, password):
        return len(password) >= 8

    def pw_chars(self, password):
        return any(char in self.specials for char in password)

    def pw_unique(self, password):
        return not any(password in item['password'] for item in self.vault.values())

    def is_valid(self, password):
        return all({
            self.pw_length(password),
            self.pw_chars(password),
            self.pw_unique(password)})

    def add(self, service, password):
        if self.is_valid(password):
            date = datetime.now().date()
            self.vault[service] = {
                'password': password, 'date_added': date
            }
        else:
            print("Password is not valid")

    def remove(self, service):
        del self.vault[service]

    def update(self, service, password):
        if self.is_valid(password):
            self.vault[service].update({'password': password})

    def list_services(self):
        return list(self.vault.keys())

    def sort_services_by(self, sort_by, reverse=False):
        if sort_by == 'service':
            return sorted(self.vault.keys(), reverse=bool(reverse))
        elif sort_by == 'added_on':
            date_sorted = dict(
                sorted(self.vault.items(), key=lambda x: x[1]['date_added']))
            sorted_keys = []
            for key in date_sorted:
                sorted_keys.append(key)
            if reverse:
                sorted_keys.reverse()
            return sorted_keys

    def get_for_service(self, service):
        if service in self.vault:
            return self.vault[service]['password']
        else:
            return None
