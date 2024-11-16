# Random Password Generator
# Written by Azim Hatami


import random
import string
import os
from time import sleep


settings = {
    'lower_case': True,
    'upper_case': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8,
}

PASSWORD_MIN_LENGTH = 4
PASSWORD_MAX_LENGTH = 30


def clear_screen():
    os.system('clear')


def show_welcome_message():
    print('Welcome to the Random Password Generatore.')
    print('\n', '-' * 18, '\n')

def get_user_password_length(option,
                             defult,
                             pw_min_length=PASSWORD_MIN_LENGTH,
                             pw_max_length=PASSWORD_MAX_LENGTH):
    while True:
        user_input = input('Enter password length: '
                           f'(Defult is {defult}) (enter: defult): ')

        if user_input == '':
            return defult

        if user_input.isdigit():
            user_password_length = int(user_input)
            if pw_min_length <= user_password_length < pw_max_length:
                return int(user_input)
            print('Invalid input.')
            print('password length should be '
                  f'between {pw_min_length} and {pw_max_length}.')
        else:
            print('Invalid input, Yor should enter a number.')

        print('Please try again.')


def get_yes_or_no_for_settings(option, defult):
    while True:
        user_input = input(f'Include {option}? (Defult is {defult} '
                           '(y: yes, n: no, enter: defult): ')

        if user_input == '':
            return defult

        if user_input in ['y', 'n']:
            return user_input == 'y'

        print('Invalid input. Please try again.')


def get_settings_from_users(settings):
    for option, defult in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no_for_settings(option, defult)
            settings[option] = user_choice
        else:
            user_password_length = get_user_password_length(option, defult)
            settings[option] = user_password_length


def ask_if_change_settings(settings):
    while True:
        user_answer = input('Do you want to change defult settings? '
                            '(y: yes, n: no, enter: yes): ')
        if user_answer in ['y', 'n', '']:
            if user_answer in ['y', '']:
                print('\n', '-' * 5, 'Change Settings', '-' * 5, '\n', sep='')
                get_settings_from_users(settings)
            break
        else:
            print('Invalid input')
            print('Please try again.')


def get_random_upper_case():
    return random.choice(string.ascii_uppercase)


def get_random_lower_case():
    return random.choice(string.ascii_lowercase)


def get_random_number():
    return random.choice('0123456789')


def get_random_symbol():
    return random.choice("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")


def generate_random_char(choices):
    choice = random.choice(choices)

    if choice == 'upper_case':
        return get_random_upper_case()
    if choice == 'lower_case':
        return get_random_lower_case()
    if choice == 'symbol':
        return get_random_symbol()
    if choice == 'number':
        return get_random_number()
    if choice == 'space':
        return ' '


def password_generator(settings):
    final_password = ''
    password_length = settings['length']

    choices = list(filter(lambda x: settings[x], ['upper_case',
                                                  'lower_case',
                                                  'symbol',
                                                  'number',
                                                  'space',
                                                  ]))


    for i in range(password_length):
        final_password += generate_random_char(choices)

    return final_password


def ask_user_to_generate_another_password():
    while True:
        user_answer = input('Regenerate: (y: yes, n: no): ')
        if user_answer in ['y', 'n', '']:
            if user_answer == 'n':
                return False
            return True
        else:
            print('Invalid input')
            print('please try again.')


def password_generator_loop(settings):
    while True:
        print('-' * 20)
        print(f'Generated Password: {password_generator(settings)}')

        if ask_user_to_generate_another_password() == False:
            break


if __name__ == '__main__':
    clear_screen()
    show_welcome_message()
    ask_if_change_settings(settings)
    password_generator_loop(settings)
    print('Thank you for chooosing us.')

