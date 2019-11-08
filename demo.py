from alg.apriori import Apriori

data = [
    [1,2,3,4,1,5,8],
    [7,8,10,5,1,7,3,1],
    [3,1,4,7,8,5],
    [6,7,8,6,7],
    [1,2,5,6,3,8],
    [5,7,9,1,2,3,3,1],
    [6,10],
    [5,3,1,4,2,9,4,1,1,3],
    [7,8,9,10,11,1],
    [1,5,6,8,3,4],
]

print(Apriori.find_associations(data, 0.5))

from helpers.ds_builder import DatasetBuilder

ds = DatasetBuilder.generate_normal_distribution(['a', 'b', 'c', 'd', 'k'], 2, 4, 20)
for el in ds:
    print(el)
print('------------------------')
print(Apriori.find_associations(ds, 0.3))
