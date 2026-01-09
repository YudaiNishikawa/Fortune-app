#実行

#ライブラリのインポート
from models_mikuji import Daikichi,Kichi,Chukichi,Kyo
import hashlib
from datetime import date,datetime
#表示
line="="*70

#名前、生年月日の入力
while True:
    user_name=input(f"{line}\n"
                    f"いまからあなたの今年の運勢を占います\n"
                    f"ではまずあなたの名前を入力してください(例：慶應花子)：")
    if user_name:
        break
    print("【Error】名前が入力されていません。")

while True:
    user_birthday=input("生年月日を入力してください(例：20050401)：")
    if len(user_birthday)==8 and user_birthday.isdigit():
        try:
            datetime.strptime(user_birthday,"%Y%m%d")
            break
        except ValueError:
            print("【Error】存在しない日付です。正しい生年月日を入力してください。")
    else:
        print("【Error】8桁の半角数字で入力してください。")

#日付の取得
today=str(date.today())

#スコアの生成
"""Miguel Grinberg氏の"The Flask Mega-Tutorial Part VI: Profile Page and Avatars"を参考にした"""
fortune_seed=(user_name+user_birthday).encode("utf-8")
fortune_hash=hashlib.md5(fortune_seed).hexdigest()
score=int(fortune_hash[:5],16)%100

meal_seed=(user_name+user_birthday+today).encode("utf-8")
meal_hash=hashlib.md5(meal_seed).hexdigest()
meal_index=int(meal_hash[:5],16)%7

#ラッキー飯リスト
meals=["白米","二郎系ラーメン","味噌汁","カレー","ハンバーグ","焼き肉","パン"]
lucky_meal=meals[meal_index]

#運勢
if score>=80:
    result=Daikichi(user_name,user_birthday,score,lucky_meal)
elif score>=50:
    result=Kichi(user_name,user_birthday,score,lucky_meal)
elif score>=20:
    result=Chukichi(user_name,user_birthday,score,lucky_meal)
else:
    result=Kyo(user_name,user_birthday,score,lucky_meal)

print(line)
print(result.announcement())
print(line)