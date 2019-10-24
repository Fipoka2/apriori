from alg.apriori import Apriori

data = [
    [1, 3, 4],
    [2, 3, 5],
    [5, 2, 1, 2, 3],
    [2, 5, 2],
]

print(Apriori.find_associations(data, 0.75))
