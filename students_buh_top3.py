import csv
from operator import itemgetter

students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923,
                       'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973,
                       'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936,
                       'Zoi': 4.937}


def make_report_about_top3(students_avg_scores):
    res = dict(
        sorted(students_avg_scores.items(), key=itemgetter(1), reverse=True)[
        :3])

    with open('./result.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Sudent', 'Average rating'])
        for key, value in res.items():
            writer.writerow([key, value])


make_report_about_top3(students_avg_scores)
