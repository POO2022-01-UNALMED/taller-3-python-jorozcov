from televisores.tv import TV

class Control:
    def __init__(self):
        self._tv = ""

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canaDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self,canal):
        self._tv.setCanal(canal)

    def enlazar(self,tv):
        self._tv = tv
        self._tv.setControl(self)
    
    def getTv(self):
        return self._tv

    def setTv(self,tv):
        self._tv = tv