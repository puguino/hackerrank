N = int(input())

if (N % 2) != 0:
    print("Weird")
elif N < 6:
    print("Not Weird")
elif N < 21:
    print("Weird")
elif N > 20:
    print("Not Weird")
