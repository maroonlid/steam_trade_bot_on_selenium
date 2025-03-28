import settings


def update_login():
    with open("stm_login.txt", 'r') as file:
        first_line = file.readline()
    settings.login = first_line


def update_password():
    with open("stm_password.txt", 'r') as file:
        first_line = file.readline()
    settings.password = first_line


def update_skin_link():
    with open("stm_skin_link.txt", 'r') as file:
        first_line = file.readline()
    settings.skin_link = first_line

def update_auth_data():
    update_login()
    update_password()

