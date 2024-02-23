# завдання 1
# def total_salary(fname):
#     total_salary = 0
#     pracivnuku_count = 0

#     try:
#         with open(fname, 'r',) as file:
#             for line in file:
#                 try:
#                     name, salary = line.strip().split(',')
#                     total_salary += int(salary)
#                     pracivnuku_count += 1
#                 except:
#                     ValueError
                    
#     except FileNotFoundError: # а раптом
#         print("файлу не знайдено")

#     if pracivnuku_count > 0:
#         average_salary = total_salary / pracivnuku_count
#     else:
#         average_salary = 0

#     return total_salary, average_salary


# total, average = total_salary("123(1).txt")
# print(f"загальна сума зарплати: {total}, а cередня: {average}")



# завдання 2 
# def get_cats_info(fname):
#     cats_info = []
    
#     try:
#         with open(fname, 'r',) as file:
#             for line in file:
#                 try:
#                     cat_id, name, age = line.strip().split(',')
#                     cats_info.append({"id": cat_id, "name": name, "age": age})
#                 except ValueError:
#                     print(f"некоректний рядок у файлі: {line.strip()}")
#     except FileNotFoundError: # а раптом
#         print("файлу не знайдено")


#     return cats_info

# cats_info = get_cats_info("123(2).txt")
# print(cats_info)



#завдання 3
def add_contact(phonebook, name, number):
    phonebook[name] = number
    return f"контакт {name} додано до бази ботіка"

def change_contact(phonebook, name, new_number):
    if name in phonebook:
        phonebook[name] = new_number
        return f"контакт {name} оновлен"
    else:
        return "такого контакту немає в базі ботіка"

def show_phone(phonebook, name):
    if name in phonebook:
        return f"номер телефону для контакту {name}: {phonebook[name]}"
    else:
        return "такого контакту немає в базі ботіка"

def show_all(phonebook):
    if phonebook:
        contacts = ""
        for name, number in phonebook.items():
            contacts += f"{name}: {number}\n"
        return contacts
    else:
        return "база ботіка пуста"

def parse_input(command):
    return command.split()

def main():
    phonebook_bot = {}
    while True:
        command = input("введіть команду або 'close'/'exit' для виходу: ").strip()

        parts = parse_input(command)

        if len(parts) == 1:
            action = parts[0]
        elif len(parts) == 2:
            action, arg1 = parts
        elif len(parts) == 3:
            action, arg1, arg2 = parts
        else:
            print("такої команди не існує")
            continue

        if action == "close" or action == "exit":
            print("закриваюсь")
            break
        
        elif action == "hello":
            print("привіт. як я вам можу допомогти ?")
            
        elif action == "add":
            print(add_contact(phonebook_bot, arg1, arg2))
            
        elif action == "change":
            print(change_contact(phonebook_bot, arg1, arg2))
            
        elif action == "phone":
            print(show_phone(phonebook_bot, arg1))
            
        elif action == "all":
            print(f"-------------\n{show_all(phonebook_bot)}\n-------------")
            
        else:
            print("такої команди нема")

if __name__ == "__main__":
    main()


























# невдала спроба(((
# bot_user_data = {}

# def set_name():
#     name = input("введіть ім'я")
#     bot_user_data.append({"name": name})

# def set_age():
#     age = input("введіть вік")
#     bot_user_data.append({"age": age})

# def show_all():
#     print(bot_user_data)

# while True:
#     user_command = input("для выходe введіть 'exit' або ''close): ")
    
#     match user_command:
#         case 'set_name':
#             set_name()
        
#         case 'set_age':
#             set_age()
#         case 'show_all':
#             show_all()
    

    
    
