from abc import ABC,abstractmethod
import math

class Figura(ABC):

    def __repr__(self):
        return f"<{self.__class__.__name__}>"
    
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

class Kolo(Figura):
    def __init__(self,r):
        self.r=r

    def oblicz_pole(self):
        return math.pi*self.r**2

    def oblicz_obwod(self):
        return 2*math.pi*self.r

    def info(self, m):
        return super().info(m) + f" wymiary: r={self.r}"


if __name__ == '__main__':
    pr = Prostokat(6.8,11.2)
    print(pr.oblicz_pole())
    print(pr.oblicz_obwod())
    print(pr.info(10))
    pr.obiekt(pr)

    print("_"*60)
    ko = Kolo(10)
    print(ko.oblicz_pole())
    print(ko.oblicz_obwod())
    print(ko.info(10))
    ko.obiekt(ko)
