class SmileChecker:
    def __init__(self):
        self.stack = []
    def append_smile(self, a):
        self.stack.append(a)
    def check_correct(self):
        left = [':-(', ':-[', ':-{', ':-<']
        right = [':-)',':-]',':-}',':->']
        pair = dict(zip(right, left))
        A = []
        for bracket in self.stack:
            if bracket in left:
                A.append(bracket)
            elif bracket in right:
                if A == []:
                    return False
                if A[-1] != pair[bracket]:
                    return False
                else:
                    A.pop()
        if A == []:
            return True
        else:
            return False


