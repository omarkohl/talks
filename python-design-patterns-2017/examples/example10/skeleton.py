class AbstractBase:
    def orgMethod(self):
        self.doThis()
        self.doThat()


class Concrete(AbstractBase):
    def doThis(self):
        ...
    def doThat(self):
        ...
