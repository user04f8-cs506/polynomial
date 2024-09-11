from abc import ABC, abstractmethod

class Evaluatable(ABC):
    @abstractmethod
    def evaluate(self, x):
        raise NotImplementedError()


class X(Evaluatable):
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, x):
        return x

class Int(Evaluatable):
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add(Evaluatable):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Mul(Evaluatable):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))
