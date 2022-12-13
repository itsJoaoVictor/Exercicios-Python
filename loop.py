'''
Task:
The provided code stub reads and integer n, print n lines. For all non-negative integers i < n, print i^2.
'''
if __name__ == '__main__':
    n = int(input())
    
    for i in range(0, n):
        print(i * i)