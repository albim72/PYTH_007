from abc import ABC,abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def oblicz_pole(self):
        pass

    @abstractmethod
    def oblicz_obwod(self):
        pass

    @abstractmethod
    def info(self,m):
        return f"widomość: {m}"

    def obiekt(self,ob):
        print(ob)

class Prostokat(Figura):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def oblicz_pole(self):
        return self.a*self.b

    def oblicz_obwod(self):
        return 2*(self.a+self.b)

    def info(self, m):
        return super().info(m) + f" wymiary: a={self.a}, b={self.b}"

if __name__ == '__main__':
    pr = Prostokat(6.8,11.2)
    print(pr.oblicz_pole())
    print(pr.oblicz_obwod())
    print(pr.info(10))
    pr.obiekt(pr)
