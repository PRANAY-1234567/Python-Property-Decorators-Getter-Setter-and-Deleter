class Bank:
    def __init__(self, TE, Mname, working_hour, dept):
        self.TE = TE
        self.name = Mname
        self._hour = working_hour
        self.__dept = dept

    @property      #----------------> Getter
    def data(self):
        return(getattr(self, "TE", "employee_data"),
                getattr(self,"name", "name_data"),
                getattr(self, "_hour", "Hour_data"),
                getattr(self,"__dept","dept_data"))

    @data.setter
    def data(self, values):
        self.TE,self.name, self._hour, self.__dept = values

    @data.deleter
    def data(self):
        del self.name,self.__dept

b=Bank(250, "Smith", 9, "Finance")
print(b.data)
b.data=(500, "Allen", 8, "Sales")
print(b.data)
del b.data
print(b.data)
