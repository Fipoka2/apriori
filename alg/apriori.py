from itertools import combinations
import functools


class Apriori:

    @staticmethod
    def find_associations(transactions: list, supp: float) -> list:
        if supp < 0 or supp > 1:
            raise Exception()
        itemset = set(x for l in transactions for x in l)
        associations = []
        curr = []

        it = 0
        while True:
            if it == 0:
                for item in itemset:
                    if Apriori._check_supp(transactions,supp,[item]):
                        curr.append([item])
                associations.append(curr.copy())
                it += 1
                continue

            curr = []
            comb = combinations(associations[-1], 2)
            for pair in list(comb):
                if Apriori._validate(*pair):
                    union = Apriori._unite(*pair)
                    if Apriori._check_supp(transactions, supp, union):
                        curr.append(union)

            if len(curr) == 0:
                break
            associations.append(curr)
            it += 1

        return associations

    @staticmethod
    def _validate(a: list, b: list) -> bool:
        if len(a) != len(b):
            return False
        if functools.reduce(lambda i, j: i and j, map(lambda m, k: m == k, a[:-1], b[:-1]), True):
            return True
        else:
            return False

    @staticmethod
    def _check_supp(transactions: list, supp: float, arr: list) -> bool:
        size = len(transactions)
        curr = 0
        for t in transactions:
            if (set(arr)).issubset(t):
                curr += 1
        if curr / size >= supp:
            return True
        else:
            return False

    @staticmethod
    def _unite(a: list, b: list) -> list:
        if a[-1] > b[-1]:
            union = b.copy()
            union.append(a[-1])
        else:
            union = a.copy()
            union.append(b[-1])
        return union
