"""https://contest.yandex.ru/contest/27393/problems/C/"""


def check_number(number, num_from_book):
    correct_number = "".join(number.split('-'))
    if len(correct_number) > 7:
        code_num_check = correct_number[-11:-8] if correct_number[-8] == ")" else correct_number[-10:-7]
        main_num_check = correct_number[-7:]
    else:
        code_num_check = ''
        main_num_check = correct_number
    
    converted_num_book = "".join(num_from_book.split('-'))
    if len(converted_num_book) > 7:
        code_num_book = converted_num_book[-11:-8] if converted_num_book[-8] == ")" else converted_num_book[-10:-7]
        main_num_book = converted_num_book[-7:]
    else:
        code_num_book = ''
        main_num_book = converted_num_book
    

    if main_num_check != main_num_book:
        return "NO"
    if (code_num_book == "" and code_num_check == '495') or (code_num_book == '495' and code_num_check == ''):
        return "YES"
    elif code_num_check == code_num_book:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    added_number = input()
    phone_book = [input() for _ in range(3)]

    for item in phone_book:

        print(check_number(added_number, item))