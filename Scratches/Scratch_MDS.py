import getpass


def main():
    user, passwd = ask_user_and_password()
    # input_objects_to_be_checked
    # get_objects_from_mds
    # loop_to_check_if_object_exists
        # if_exists_check_fields
        # if_not_exists_create
    # report



def ask_user_and_password():
    user = input('Username to connect to MDS: ')
    user = user.strip()
    password = input('password: ')
    return user, password


def input_object_to_be_checked():
    pass


def get_objects_from_mds():
    pass


def loop_to_check_if_objects_exists():
    pass


def report():
    pass


if __name__ == '__main__':
    main()
