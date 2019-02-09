def func(x=None):
    if x is None:
        print("引数を指定してください")
    elif x == 0:
        print("0です")
    elif x < 0:
        print("負の数です")
    else:
        print("正の数です")


func()
func(0)
func(-1)
func(99)
