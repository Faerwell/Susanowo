'''
Main module for Susanowo
awesome print speed CLI checker
'''
import time

def main():
    username = get_to_know()
    typing_test_speed(username)

def get_to_know():
    print('***Susanowo greets you!***\n')
    name = input("What's your name?")
    answer = input('Would you like to take a typing speed test? (y/n)')
    if answer == 'y':
        return name
    else:
        print('Bye!')
        quit()

def typing_test_speed(name):
    print(name, "Let's start! Type the text below:\n")
    text = "///text to type///"
    print(text)
    start_time = time.time()
    name_text = input()
    finish_time = time.time() - start_time
    print(name, 'did it in', finish_time, 'seconds')


if __name__ == '__main__':
    main()
