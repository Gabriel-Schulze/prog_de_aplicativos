def get_num():
    return int(input("digite um numero: "))

def contador(num):
    for i in range(1,num +1):
        print(i)


def main():
    num = get_num()
    contador(num)

main()
