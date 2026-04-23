import random
import random
import matplotlib.pyplot as plt

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


def bubble_sort(seznam2):
    seznam2 = seznam2[:]
    plt.ion()
    plt.show()
    for i in range(len(seznam2)):
        for j in range(len(seznam2)-1):
            if seznam2[j] > seznam2[j+1]:
                seznam2[j], seznam2[j+1] = seznam2[j+1], seznam2[j]
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(seznam2)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(seznam2)), seznam2, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
    plt.ioff()
    plt.show()
    return seznam2





if __name__ == "__main__":

    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    # print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

    cisla_na_sarazeni = [5, 6, 11, 4, 15]
    random = random_numbers(20)

    # print(selection_sort(random))
    # print(selection_sort(cisla_na_sarazeni))
    print(bubble_sort(random))
    # print(bubble_sort(cisla_na_sarazeni))

