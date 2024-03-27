# Я бы тебе советовал все равно делать на классах ибо это нормально блеать
class Repository:
    def __init__(self):
        self._employee: dict = {}

    def get_repos(self):
        return self._employee

    def update_repos(self, **kwargs):
        update = {kwargs['id']: {"fio": kwargs['fio'], "position": kwargs['position']}}
        # Если записи с таким id нет, то добавляем
        self._employee.update(update)

    def get_attr(self, id, attr: str):
        return self._employee[id][attr]

    def set_attr(self, id, attr: str, value):
        self._employee[id][attr] = value
