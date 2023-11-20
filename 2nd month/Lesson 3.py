# инкапсуляция, git clone
#уровни защиты
# публичная 0,  защищенная(protected _, скрытая __)



class Bank:
    def __init__(self, fullname, money, key):
        self.fullname = fullname
        self.__money = money
        self._password = key

    def __mon(self):
        money = int(input('введите счет: '))
        self.__money+=money

    def mon1(self):
        self.__mon()

    def __str__(self):
        return f'{self.fullname,self.__money,self._password}'

    def getpass(self):
        print(self._password)
    def setpass(self, p):
        self._password=p

    @property
    def nameis(self, name):
        self._password = name
#
beka = Bank('Beka', 0, '2525')
beka.mon1()
# print(bake.nameis)
# # beka.getpass()
# # beka.setpass()
# print(beka.mon1)
# beka.password='1111'
# beka._Bank__money=100000
# print(dir(beka))
# print(beka.password)
# print(beka)


# class Tea:
#     def __init__(self, name):
#         self.name = name
#
#     def start(self):
#         print('поставил чай')
#
#     def __start2(self):
#         print('нагрев воды')
#
#     def __cup(self):
#         print('чай кипит')
#
#     def _stop(self):
#         print('выкл')
#
# beko = Tea('beko')
# beko.start()
# beko._stop()
