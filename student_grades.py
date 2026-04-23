class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.scores[index]
        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"

    def find(self, pocet_bodu):
        i_bodu = []
        for i in range(len(self.scores)):
            if self.scores[i] == pocet_bodu:
                i_bodu.append(i)
        return i_bodu

    def get_sorted(self):
        scores = list(self.scores)
        for i in range(len(scores)):
            for j in range(len(scores) - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j+1] = scores[j+1], scores[j]
        return scores

    def main(self):
        pocet_studentu = results.count()
        print(f"{pocet_studentu} studentů psalo test.")
        for i in range(pocet_studentu):
            body = results.get_by_index(i)
            znamka = results.get_grade(i)
            print(f"Student {i}: {body} points - {znamka}")



        random_results = StudentsGrades(random_numbers(30, 0, 100))
        print(random_results.count())
        print(random_results.get_sorted())
if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    # print(results.count())  # 9
    # print(results.get_by_index(2))  # 91
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    # print(results.get_grade(5))
    # print(results.find(38))
    print(results.get_sorted())
    print(results.scores)