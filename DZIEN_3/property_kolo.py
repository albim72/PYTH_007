#property jako atrybut wyliczany dynamicznie
import math
class Kolo:
    def __init__(self,r:float):
        self._r=r

    @property
    def pole(self) -> float:
        return math.pi*self._r**2

    @property
    def obwod(self) -> float:
        return 2*math.pi*self._r

if __name__ == '__main__':
    k1 = Kolo(2.1)
    print(k1.pole)
    print(k1.obwod)
    k2 = Kolo(7.32)
    print(k2.pole)
    print(k2.obwod)
