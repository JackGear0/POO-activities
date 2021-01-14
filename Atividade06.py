import csv
import matplotlib.pyplot as plt
with open('Atividade06grafico.csv') as csv_file:
    r = csv.reader(csv_file, delimiter=',')
    person = []
    age = []
    for row in r:
        print(row[0], row[1])
        person.append(row[0])
        age.append(float(row[1]))


    plt.plot(person, age)
    plt.show()
    plt.bar(person, age)
    plt.show()

    fig1, ax1 = plt.subplots(figsize=(6, 6))
    ax1.pie(age, labels=person, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()