#設計書

class FortuneBase:
    def __init__(self,name,birthday,score,meal):
        self.name=name
        self.birthday=birthday
        self.score=score
        self.meal=meal
    
    def announcement(self):
        return (f"{self.name}さん、あなたの運勢レベルは{self.score}です。\n"
                f"そしてあなたの今日のラッキー飯は{self.meal}\n"
                f"ラッキー飯を食べた分だけ今日の運勢をあげることができます！")
               
class Daikichi(FortuneBase):
    def announcement(self):
        return (f"{super().announcement()}\n"
                f"そして気になるあなたの今年の運勢は\n"
                f"\n"
                f"【大吉】です!!!!!\n"
                f"\n"
                f"好きなものをたくさんたべて最高の1年にしてください。")

class Kichi(FortuneBase):
    def announcement(self):
        return (f"{super().announcement()}\n"
                f"そして気になるあなたの今年の運勢は\n"
                f"\n"
                f"【吉】です!!\n"
                f"\n"
                f"かなりいい運勢ですねラッキー飯である{self.meal}を食べると最高の一日になります!!")
    
class Chukichi(FortuneBase):
    def announcement(self):
        return (f"{super().announcement()}\n"
                f"そして気になるあなたの今年の運勢は\n"
                f"\n"
                f"【中吉】です\n"
                f"\n"
                f"まずまずの運勢ですねラッキー飯である{self.meal}を一日に2回食べると最高の一日になります!!")
    
class Kyo(FortuneBase):
    def announcement(self):
        return (f"{super().announcement()}\n"
                f"そして気になるあなたの今年の運勢は\n"
                f"\n"
                f"【凶】です、、、\n"
                f"\n"
                f"あまり良くない1年になりそうです。ラッキー飯である{self.meal}を一日に3回食べると最高の一日になります!!")
    