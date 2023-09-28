import sys
import time
from textwrap import dedent

import function

output = {
    "menu": """\
    Выберите действие:
    ___________________________
    1. Удалить запись.
    2. Добавить запись
    3. Изменить запись.
    4. Вывести данные.
    5. Очистить файл.
    6. Скопировать справочник
    7. Выход.""",
    "change_prompt": """\
    Отлично! Выбери данные, которые Вы хотите поменять:
    1 - Имя,
    2 - Фамилия,
    3 - Телефон,
    4 - Город
    Примечание: Если Вы хотите изменить несколько данных одновременно,\
    \b\b\bто запишите номера через пробел.
    Ввод: """,
    "parameters_prompts": [
        "Введите имя: ",
        "Введите фамилию: ",
        "Введите номер телефона: ",
        "Введите город: ",
        "Введите разделитель(  - . ; ,  ): ",
    ],
    "delete_prompt": """\
    Желаю всего доброго!\
    \b\b\bНе забывай, что все данные, которые ты записал, они сохранились.
    Удалить? (ОТВЕТЬТЕ ДА/НЕТ): """,
    "greeting_msg": [
        "***************************",
        "  Добро пожаловать!  ",
    ],

    "fields": ["Номер", "Имя", "Фамилия", "Телефон", "Город"],
    "farewell_msg": "Всего доброго!",
    "answer_error": "ERROR! Ошибка, скорее всего, Вы указали неправильное число.",
    "action_answer_err": "Введите значение от 1 до 7." "",
    "file_answer_err": "Введите номер файла от 1 до 3: ",
    "underscores": "___________________________",
    "action_prompt": "Введите номер действия: ",
    "file_delete_prompt": "Выберите из какого файла Вы хотите удалить данные: ",
    "file_clear_prompt": "Выберите какой файл Вы хотите очистить: ",
    "file_add_prompt": "Выберите файл, в который Вы хотите добавить строку: ",
    "file_change_prompt": "Выберите в каком файле Вы хотите изменить запись: ",
    "file_copy_prompt_sourse": "Выберите файл откуда копировать данные: ",
    "file_copy_prompt_target": "Выберите файл куда копировать данные: ",
    "file_choice_msg": "Отлично! Будем {action} данные из {file_num}-файла.",
    "line_prompt": "{action} номер строки от 1 до {line_count}: ",
    "success_msg": "Данные успешно {action}!",
    "copy_success_msg": "Данные из файла {source} перенесены в файл {target}!",
    "del_success_msg": "Удаление успешно завершено!",
    "file_clear_msg": "Отлично! Происходит очистка файла, подождите :)",
    "clear_success_msg": "Файл {file_num} успешно очищен!",
    "print_msg": "Вывожу данные из {file_num}-го файла:",
    "empty_file": "Файл пустой!"
}


def interface():
    print_greeting()
    print_menu()

    action = choose_action()

    while action != 7:
        if action == 1:
            get_delete_params()
        elif action == 2:
            get_add_params()
        elif action == 3:
            get_change_params()
        elif action == 4:
            function.print_data()
        elif action == 5:
            get_clear_params()
        elif action == 6:
            get_copy_params()
        print_menu()
        action = choose_action()

    print(output["underscores"])
    action = input(dedent(output["delete_prompt"]))
    print(output["underscores"])

    if action.lower() in ["да", "yes"]:
        function.clear_all_files()
        print(output["success_msg"].format(action="удалены"), end=" ")

    print(output["farewell_msg"])
    exit()


def get_delete_params():
    function.print_data()

    file_num = choose_file(output["file_delete_prompt"], "удалять")
    line = choose_line(file_num)

    if line is not None:
        function.delete_line(file_num, line)

        print(output["underscores"], output["del_success_msg"], sep="\n")


def get_add_params():
    function.print_data()

    file_num = choose_file(output["file_add_prompt"], "")
    parameters = choose_add_parameters()

    function.add_to_file(file_num, parameters)

    msg = output["success_msg"].format(action="записаны")
    print(output["underscores"], msg, sep="\n")


def get_change_params():
    function.print_data()

    file_num = choose_file(output["file_change_prompt"], "изменять")
    line = choose_line(file_num)

    if line is not None:
        values = choose_new_values()

        function.change_line(file_num, line, values)

        msg = output["success_msg"].format(action="изменены")
        print(output["underscores"], msg, sep="\n")


def get_clear_params():
    function.print_data()
    file_num = choose_file(output["file_clear_prompt"], "")

    print(output["underscores"], output["file_clear_msg"], sep="\n")

    function.clear_file(file_num)

    loading()
    msg = output["clear_success_msg"].format(file_num=file_num)
    print(output["underscores"], msg, sep="\n")

def get_copy_params():
    function.print_data()
    file_num_sourse = choose_file(output["file_copy_prompt_sourse"], "")
    
    file_num_target = choose_file(output["file_copy_prompt_target"], "")
    
    function.copy_data(file_num_sourse, file_num_target)
    loading()
    msg = output["copy_success_msg"].format(source=file_num_sourse, target=file_num_target)
    print(output["underscores"], msg, sep="\n")
    


def choose_action():
    answer = int(input(output["action_prompt"]))
    loading()

    while answer < 1 or answer > 7:
        print(output["answer_error"], output["action_answer_err"], sep="\n")
        print_menu()

        answer = int(input(output["action_prompt"]))

        loading()

    return answer


def choose_file(prompt, action):
    print(output["underscores"])
    answer = int(input(prompt))

    while answer < 1 or answer > 3:
        print(output["underscores"], output["answer_error"], sep="\n")
        answer = int(input(output["file_answer_err"]))
        loading()

    if action != "":
        print(
            output["underscores"],
            output["file_choice_msg"].format(action=action, file_num=answer),
            sep="\n",
        )

    return answer


def choose_line(file_num):
    line_count = len(function.read_file(file_num))

    if line_count:
        prompt = output["line_prompt"].format(action="Выбери", line_count=line_count)

        line = int(input(prompt))

        while line < 1 or line > line_count:
            prompt = output["line_prompt"].format(
                action="Введите", line_count=line_count
            )
            print(output["answer_error"])
            line = int(input(prompt))

        return line
    else:
        print(output["underscores"], output["empty_file"], sep="\n")
        return None


def choose_add_parameters():
    print(output["underscores"], "|", sep="\n")

    answers = list()
    for prompt in output["parameters_prompts"]:
        print("|")
        answers.append(input("| " + prompt))

    return answers



def choose_new_values():
    values = list()
    fields = [0]

    while min(fields) < 1 or max(fields) > 4:
        print(output["underscores"])
        fields = list(map(int, input(dedent(output["change_prompt"])).split()))

    for i in range(4):
        if i + 1 in fields:
            answer = input(output["parameters_prompts"][i])
        else:
            answer = ""
        values.append(answer)

    return values


def loading():
    animation = [
        "■□□□□□□□□□",
        "■■□□□□□□□□",
        "■■■□□□□□□□",
        "■■■■□□□□□□",
        "■■■■■□□□□□",
        "■■■■■■□□□□",
        "■■■■■■■□□□",
        "■■■■■■■■□□",
        "■■■■■■■■■□",
        "■■■■■■■■■■",
    ]

    for i in range(len(animation)):
        sys.stdout.write("\r" + animation[i] + f" {(i + 1) * 10}%")
        sys.stdout.flush()
        time.sleep(0.2)

    print("\n")


def print_menu():
    print(
        dedent(output["menu"]),
        output["underscores"],
        sep="\n",
    )


def print_greeting():
    print(
        output["greeting_msg"][0],
        output["greeting_msg"][1],
        output["greeting_msg"][0],
        sep="",
    )
