while True:
    first_name = input('What is your first name? ')
    if first_name.isalpha() and len(first_name) > 1:
        break
    else:
        print('Invalid input!')


while True:
    last_name = input('What is your last name? ')
    if last_name.isalpha() and len(last_name) > 1 and (len(last_name) <= 10):
        break
    else:
        print('Invalid input!')


while True:
    age = int(input('What is your age: '))
    if age > 0 and age < 120:
        break
    else:
        print('Invalid input!')

        
while True:
    post_code = input('What is your postal code? ')
    if len(post_code) == 6 and post_code[:4].isnumeric() and post_code[4:].isalnum():
        break
    else:
        print('Invalid input!')