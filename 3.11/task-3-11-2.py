import collections

pets = dict()
last = 0

def create():
    last = 0
    if len(pets) > 0:
        last = collections.deque(pets, maxlen=1)[0]
    name = input('Введите кличку питомца ')
    kind = input('Введите вид питомца ')
    age = int(input('Введите возраст питомца '))
    owner = input('Введите имя владельца ')
    pets[last + 1] = dict()
    pets[last + 1][name] = dict()
    pets[last + 1][name]['Вид питомца'] = kind
    pets[last + 1][name]['Возраст питомца'] = age
    pets[last + 1][name]['Имя владельца'] = owner
    return True

def read(id):
    pet = get_pet(id)

    if pet:
        return print_pet(pet)
    else:
        return False

def update(id):
    pet = get_pet(id)
    if pet:
        name = input('Введите кличку питомца ')
        kind = input('Введите вид питомца ')
        age = int(input('Введите возраст питомца '))
        owner = input('Введите имя владельца ')
        newInfoPet = {
            id: {
                name: {
                    'Вид питомца': kind,
                    'Возраст питомца': age,
                    'Имя владельца': owner
                }
            }
        }
        pets.update(newInfoPet)
    else:
        return False

def delete(id):
    pet = get_pet(id)
    if pet:
        del pets[id]
    else:
        return False

def print_pet(pet):
    return print(f'Это {pet[next(iter(pet))]["Вид питомца"]} по кличке "{next(iter(pet))}". Возраст: {pet[next(iter(pet))]["Возраст питомца"]} {get_suffix(pet[next(iter(pet))]["Возраст питомца"])}. Имя владельца: {pet[next(iter(pet))]["Имя владельца"]}')

def get_pet(id):
    return pets[id] if id in pets.keys() else print('Питомец не найден')

def get_suffix(age):
    return {
        age < 0: 'ошибка',
        age % 10 == 0: 'лет',
        age % 10 == 1: 'год',
        age % 10 > 1 and age % 10 < 5: 'года',
        age % 10 > 4: 'лет',
        age % 100 > 10 and age % 100 < 20: 'лет'
    }[True]

def pets_list():
    for key in pets:
        pet = get_pet(key)
        print_pet(pet)

command = ""
while command != 'stop':
    command = input('Введите команду (create, read, update, delete, list, stop) : ')
    match command:
        case 'create':
            create()
        case 'read':
            id = int(input('Введите индентификатор питомца '))
            read(id)
        case 'update':
            id = int(input('Введите индентификатор питомца '))
            update(id)
        case 'delete':
            id = int(input('Введите индентификатор питомца '))
            delete(id)
        case "list":
            pets_list()
        case "stop":
            break
        case _:
            print('Такой команды не существует')