def read_csv(filename:str):
    data = []
    fields = ["ID","Тип животного", "Имя животного", "Дата рождения", "Команда, которую выполняет животное"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def print_result(data:list):
    print('-'*20)
    for elem in data:
        for key in elem:
            print(f"{key} : {elem[key]}")
        print('-'*20)

def get_search_animal():
    return input('Введите имя животного, которое хотите удалить:')

def find_by_id(data:list, id:str):
    result = []
    for elem in data:
        if elem['ID'] == id:
            result.append(elem)
    return result

def find_by_type(data:list, type: str):
    result = []
    for elem in data:
        if elem['Тип животного'] == type:
            result.append(elem)
    return result



def find_by_date(data:list, date: str):
    result = []
    for elem in data:
        if elem['Дата рождения'] == date:
            result.append(elem)
    return result

def get_new_note():
    fields = ["ID","Тип животного", "Имя животного", "Дата рождения", "Команда, которую выполняет животное"]
    record = dict(zip(fields, input('Введите ID,тип животного, имя животного, дату рождения животного, команду, которую выполняет животное через(,):').strip().split(',')))
    return record
    
def add_note(data:list, note:dict):
    return data.append(note)

def write_csv(filename:str, data:list):
    with open(filename, 'w', encoding='utf-8') as f_out:
        for i in range(len(data)):
            s = ''
            for value in data[i].values():
                s += value + ','
            f_out.write(f'{s[:-1]}\n')

def delete_by_animal(data:list, animal: str):
    for elem in data:
        if elem['Имя животного'] == animal:
            data.remove(elem)
    return data

def show_menu():
    print("\nВыберите нужное действие: \n"
          "1.Отобразить всех животных\n"
          "2.Найти животное по ID номеру\n"
          "3.Найти животное по дате рождения\n"
          "4.Добавить животное\n"
          "5.Удалить животное\n"
          "6.Закончить работу\n")
    choice = int(input())
    return choice
    
def work_with_register():
    choice = show_menu()
    work_with_register = read_csv('ANIMALS.csv')
   
    while(choice!=6):
        if choice == 1:
            print_result(work_with_register)
        elif choice == 2:
            id = input('введите ID и Enter:')                 
            print_result(find_by_id(work_with_register, id))           
        elif choice == 3:
            date = input('введите пробел, дату рождения животного и Enter:')
            print_result(find_by_date(work_with_register, date))
        elif choice == 4:
            new_note = get_new_note()
            add_note(work_with_register, new_note)
            write_csv('ANIMALS.csv', work_with_register)
        elif choice == 5:
            del_animal = get_search_animal()
            delete_by_animal(work_with_register, del_animal)
            write_csv('ANIMALS.csv', work_with_register)
        choice = show_menu()
work_with_register()