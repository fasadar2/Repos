from repository import Repository

# Инициализируем репозиторий с пиздосиком
repo = Repository()
id = 1
fio = "булььбазавр бульбазаврович"
position = "пиздосик"

# Добавляем сотрудника
repo.update_repos(id=id, fio=fio, position=position)

# Просим id для дальнейшей демонстрации
idIn = int(input("введите id: "))

# демонстрируем работу репозитрия
print(repo.get_repos())

# вывдем по id только fio
print(repo.get_attr(id=idIn, attr='fio'))

# повысим пиздосика до Мажажаера
repo.set_attr(id=idIn, attr='position', value='Мажажаер')

# Убедимся что пиздосик повышен
print(repo.get_repos())
