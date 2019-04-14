# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a,b = input().split()
    try:
        print(int(a)//int(b))
    except Exception as e:
        print("Error Code:", e)

""" if only want to specify the following
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
"""
