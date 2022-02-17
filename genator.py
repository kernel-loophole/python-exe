def genator(n):
    for i in range(n):
        if i%2==0:
            yield i
        else:
            continue
def check_gen(gen):
    for i in gen:
        print(i)
check_gen(genator(10))