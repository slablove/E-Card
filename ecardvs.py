from time import sleep
import random

dic = {"kaiser": "皇帝", "c": "市民", "s": "奴隷"}

print("Eカードをはじめます")
player = input("プレイヤー名を入力してください ")
print("c=市民　s=奴隷　cかsを入力")
user = input('>>>  ')
user = user.lower()

try:
    user_choice = dic[user]

    choice_list = ["kaiser", "c", "s"]
    pc = dic[random.choice(choice_list)]

    draw = '引き分け'
    win = player + 'の勝ちです'
    lose = player +'の負けです'

    if user_choice == pc:
        judge = draw
    else:
        if user_choice == "皇帝":
            if pc == "市民":
                judge = win
            else:
                judge = lose

        elif user_choice == "市民":
            if pc == "奴隷":
                judge = win
            else:
                judge = lose

        elif user_choice == "奴隷":
            if pc == "皇帝":
                judge = win
            else:
                judge = lose

    print(player+"が選んだのは %s" % user_choice)
    sleep(3)
    print("利根川が選んだのは %s" % pc)
    sleep(1)
    print("結果は%s" % judge)
except:
    print("cかsを入力してください。")

