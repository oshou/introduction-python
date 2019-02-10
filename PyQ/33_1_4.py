def warikan(total, num):
    siharai = 0
    try:
        siharai = total // num
        message = '一人あたり{}円です。'.format(siharai)
        if total % num > 0:
            return message + '{}円の余りが生じています'.format(total % num)
        return message
    except ZeroDivisionError:
        print("ゼロ除算が発生しました。")
        message = '0人で割り勘しないでください！'
        return message
    finally:
        print('finally')


print('---ZeroDivisionErrorが発生する---')
print(warikan(1000, 0))
print('---エラーは発生しない---')
print(warikan(1000, 5))
print(warikan(1000, 3))
