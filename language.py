class Language:

    def __init__(self, vt: [], vn: [], p: dict, s: str):
        self.vt = vt
        self.vn = vn
        self.p = p
        self.s = s

    def get_kind(self):
        if self.__is_kind_3():
            return 3
        if self.__is_kind_2():
            return 2
        if self.__is_kind_1():
            return 1

        return 0

    def __is_kind_3(self):
        for key in self.p:
            if len(key) != 1:
                return False
            for p in self.p[key]:
                if len(p) > 2:
                    return False
                if len(p) == 1 and p not in self.vt:
                    return False
                if (p[:1] in self.vt and p[1:] in self.vt) or (p[:1] in self.vn and p[1:] in self.vn):
                    return False
        return True

    def __is_kind_2(self):
        for key in self.p:
            if len(key) != 1:
                return False
            for p in self.p[key]:
                for s in p:
                    if s not in self.vt and s not in self.vn and s != 'e':
                        return False
        return True

    def __is_kind_1(self, ):
        for key in self.p:
            if len(key) > len(self.p[key]):
                return False
            for s in key:
                if s not in self.vt and s not in self.vn:
                    return False
            for p in self.p[key]:
                for s in p:
                    if s not in self.vt and s not in self.vn and s != 'e':
                        return False
        return True
