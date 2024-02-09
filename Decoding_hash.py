import hashlib

input_hashed = input('Введите хэшированный пароль: ')

password_file = open('D:\Рабочий стол\Урок 4. Основы криптографической защиты информации\\passwords.txt', 'r')

try:
    for word in password_file:
        encoding_word = word.encode('utf-8')
        hashed_word = hashlib.sha256(encoding_word.strip())
        digesting = hashed_word.hexdigest()

        if digesting == input_hashed:
            print('Искомый пароль: ', word)
            password_file.close()
            break
except:
    print('Пароль не найден. ')
    password_file.close()
    
