import random
import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(seznam):
    seznam = seznam[:]

    for i in range(len(seznam)):
        nejmensi_i = i
        for j in range(i + 1, len(seznam)):
            if seznam[j] < seznam[nejmensi_i]:
                nejmensi_i = j
        seznam[i], seznam[nejmensi_i] = seznam[nejmensi_i], seznam[i]
    return seznam



if __name__ == "__main__":

    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    # print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

    cisla_na_sarazeni = [5, 6, 11, 4, 15]
    random = random_numbers(15)

    print(selection_sort(random))
    print(selection_sort(cisla_na_sarazeni))

