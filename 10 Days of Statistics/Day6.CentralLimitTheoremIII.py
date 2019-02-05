# Enter your code here. Read input from STDIN. Print output to STDOUT
n, pop_mean, pop_std, p, z = [float(input()) for i in range(5)]
sample_mean = pop_mean
sample_std  = pop_std/(n**0.5)

A = sample_mean - sample_std*z
B = sample_mean + sample_std*z
print('%0.2f' %A)
print('%0.2f' %B)
