from scipy.stats import truncnorm
import numpy as np


class DatasetBuilder:
    def __init__(self):
        pass

    @classmethod
    def generate_normal_distribution(cls, elements: list,
                                     min_size: int, max_size: int, ds_size: int) -> list:
        el_size = len(elements)
        mean_elem = int(el_size / 2)
        mean_size = int((max_size - min_size) / 2)

        size_generator = cls._get_truncated_normal(mean_size, 2, min_size, max_size)
        generated_sizes = np.rint(size_generator.rvs(ds_size)).astype(int)

        ds = []
        for i in range(ds_size):
            sample = []

            elem_generator = cls._get_truncated_normal(mean_elem, 2, 0, el_size)
            for j in range(generated_sizes[i]):

                el = elements[np.floor(elem_generator.rvs()).astype(int)]
                sample.append(el)

            ds.append(sample)
        return ds


    @classmethod
    def _get_truncated_normal(cls, mean=0, sd=1, low=0, upp=10):
        return truncnorm(
            (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
