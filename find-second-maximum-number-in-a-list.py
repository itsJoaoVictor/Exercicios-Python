#Exercio do site HackerRank link    https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort()
    arr.reverse()
    for i in range(0, n):
        if arr[i] != arr[i + 1]:
            print(arr[i + 1])
            break
                