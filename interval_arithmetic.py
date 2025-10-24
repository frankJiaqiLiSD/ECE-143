# fill out the necessary methods shown below and add others if need be.

class Interval(object):
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        self._a = a
        self._b = b
    def __repr__(self):
        pass
    def __eq__(self,other):
        return isinstance(other,Interval) and self._a==other._a and self._b==other._b
    def __lt__(self,other):
        return isinstance(other,Interval) and self._a<other._a and self._b<other._b
    def __gt__(self,other):
        return isinstance(other,Interval) and self._a>other._a and self._b>other._b
    def __ge__(self,other):
        return isinstance(other,Interval) and self._a>=other._a and self._b>=other._b
    def __le__(self,other):
        return isinstance(other,Interval) and self._a<=other._a and self._b<=other._b
    def __add__(self,other):
        assert isinstance(other,Interval)
        if self._b<=other._a or other._b<=self._a:
            return [self,other]
        else:
            return Interval(min(self._a,other._a),max(self._b,other._b))