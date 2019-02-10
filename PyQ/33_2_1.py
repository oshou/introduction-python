from string import ascii_uppercase

ALLOW_CHARS = ' ' + ascii_uppercase  # ' ABCD...XYZ'


def encrypt(value):
    nums = []
    for c in value:
        n = ALLOW_CHARS.index(c.upper())
        nums.append(n)
    return nums


def input_loop():
    while True:
        value = input('文章を入力してください[A-Z,Space]:')
        try:
            nums = encrypt(value)
        except ValueError:
            print(value, 'はローマ字またはスペースではありません')
        else:
            print(*nums)
        finally:
            print('終了するにはCtrl-Cを入力して下さい')


def main():
    try:
        input_loop()
    except KeyboardInterrupt:
        print('\nbye bye')


if __name__ == '__main__':
    main()
