class Product:

    def __init__(self) -> None:
        self.__id = -1
        self.__name = ""
        self.__price = 0.0
        self.__description = ""
        self.__pic_links = list()
        self.__time = ""

    @property
    def id(self):
        return self.__id;

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name;

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price;

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def description(self):
        return self.__description;

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def pic_links(self):
        return self.__pic_links;

    @pic_links.setter
    def pic_links(self, pic_links):
        self.__pic_links = pic_links

    @property
    def time(self):
        return self.__time;

    @time.setter
    def time(self, time):
        self.__time = time