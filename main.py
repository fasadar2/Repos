from repository import Repository
#Инициализируем репозиторий с пиздосиком
repo = Repository()
id = 1
fio = "булььбазавр бульбазаврович"
position = "пиздосик"
repo.update_repos(id=id,fio=fio,position=position)
idIn =int(input("введите id: "))
print(repo.get_repos())
print(repo.get_attr(id=idIn,attr='fio'))
repo.set_attr(id=idIn,attr='position',value='Мажажаер')
print(repo.get_repos())