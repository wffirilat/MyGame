__author__ = 'xwffirilat'


def lin(obj):
    if not obj.components:
        return [obj, ]
    lists = [lin(par) for par in obj.components] + [obj.components]
    return [obj] + merge(*lists)


def merge(*lists):
    lists = [list(l) for l in lists]
    result = []
    while True:

        # Clear out blank lists.
        lists = [l for l in lists if l]
        if not lists:
            return result

        for lst in lists:
            head = lst[0]

            if not any(head in l[1:] for l in lists):
                break
        else:
            raise Exception('Cannot linearize object')

        result.append(head)
        for lst in lists:
            if lst[0] == head:
                del lst[0]


class _Linearizable:
    def __init__(self, name, components, **kwargs):
        self.__dict__.update(**kwargs)
        self.name = name
        self.components = list(components)
        self._mro = lin(self)

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    O = _Linearizable('O', [], moo='cow')

    A = _Linearizable('A', [O])
    B = _Linearizable('B', [O])
    C = _Linearizable('C', [O])
    D = _Linearizable('D', [O])
    E = _Linearizable('E', [O])

    K1 = _Linearizable('K1', [A, B, C])
    K2 = _Linearizable('K2', [D, B, E])
    K3 = _Linearizable('K3', [D, A])

    Z = _Linearizable('Z', [K1, K2, K3])

    print(lin(Z))
