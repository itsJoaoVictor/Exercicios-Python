#Exercicio do site: https://www.hackerrank.com/challenges/nested-list/problem
#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dicio = {name: score}
        
    dicio_ordenado = sorted(dicio.items(), key=lambda x: x[1])
    second_lowest = dicio_ordenado[1]
    if second_lowest == dicio_ordenado[2]:
        print(dicio_ordenado[1])
        print(dicio_ordenado[2])
    else:
        print(dicio_ordenado[1])
    
            