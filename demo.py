from alg.apriori import Apriori

data = [
    [1, 3, 4],
    [2, 3, 5],
    [5, 2, 1, 2, 3],
    [2, 5, 2],
]

print(Apriori.find_associations(data, 0.75))

from helpers.ds_builder import DatasetBuilder

ds = DatasetBuilder.generate_normal_distribution(['a', 'b', 'c', 'd', 'k'], 2, 4, 20)
for el in ds:
    print(el)
print('------------------------')
print(Apriori.find_associations(ds, 0.3))
