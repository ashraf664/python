def duplicate_num(A):
    n = len(A)
    expected_sum = (n - 1) * n // 2
    num = sum(A)
    return num - expected_sum

A = list(map(int, input("Enter the numbers from 1 to 4 + space =").split()))

print("The repeated number =", duplicate_num(A))
