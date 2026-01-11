users = {}           # ユーザ情報
current_user = None  # ログイン中ユーザ

def is_valid_password(password):
    if len(password) < 8:
        return False

    has_letter = False
    has_digit = False

    for char in password:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_digit = True

    return has_letter and has_digit

# def register():
#     username = input("ユーザ名を入力してください: ")
#     password = input("パスワードを入力してください: ")

#     if username in users:
#         print("そのユーザ名は既に使われています")
#     else:
#         users[username] = password
#         print("ユーザ登録が完了しました")

# def type():
#     username = input("ユーザ名を入力してください: ")
#     password = input("パスワードを入力してください: ")

def register():
    while True:
        username = input("ユーザ名を入力してください: ")
        password = input("パスワードを入力してください: ")

        if username in users:
            print("そのユーザ名は既に使われています")
            continue  # もう一度最初から

        if not is_valid_password(password):
            print("パスワードは8文字以上で、英字と数字を含めてください")
            continue  # 入力し直し

        users[username] = password
        print("ユーザ登録が完了しました")
        break  # 登録成功 → ループ脱出




def login():
    global current_user

    if current_user is not None:
        print("すでにログインしています:", current_user)
        return

    username = input("ユーザ名: ")

    if username not in users:
        print("そのユーザ名は登録されていません、登録から始めてください")
        return

    password = input("パスワード: ")

    if users[username] != password:
        print("パスワードが違います")
        return

    current_user = username
    print("ログイン成功！")



def logout():
    global current_user

    if current_user is None:
        print("ログインしていません")
    else:
        print(current_user, "をログアウトしました")
        current_user = None


def menu():
    print("==== メニュー ====")
    print("1: ユーザ登録")
    print("2: ログイン")
    print("3: ログアウト")
    print("4: 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
       logout()
    elif choice == "4":
        print("終了します")
        exit()
    else:
        print("無効な選択です")


while True:
    menu()

