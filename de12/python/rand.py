# ゲームのメイン関数

def game_of_life():
 while True: 
    name=input("あなたのお名前は？")
    print(name,"さんですね！")
    print("今から人生ゲームが始まるよ！")
    print(name,"には問題に出てくる二択に答えてね。")
    print("ではゲームスタート！")
    
    
    #最初の問題
    print("問題")
    print(name,"は今幼稚園児。公園で遊んでるよ。アリをつぶす？ つぶさない？")
    user_choice = input("「つぶす」または「つぶさない」を入力してください： ").strip().lower()

    if user_choice == "つぶす":
        print("幼稚園児はみなありを潰します小学校入学です！")
    elif user_choice == "つぶさない":
        print("ありを潰さない子供などいません。")
        print("ゲームオーバー！ミジンコになりました。")
    else:
        print("無効な選択です。正しい選択を入力してください。")
        continue
        

    # 新しい問題
    print("次の問題:")
    print("無事に小学校に入学した"+name,"今日はクラスで休みが出たよ。さて始まるのは牛乳じゃんけん。参加する？しない？")
    user_choice = input("「参加する」または「参加しない」を入力してください： ").strip().lower()

    if user_choice == "参加する":
        print(name,"は牛乳じゃんけんで勝ち続け、学校の人気者に！中学校入学！")
    elif user_choice == "参加しない":
        print("学校になじめず引きこもりからのニート！")
        print("ゲームオーバー！ニートになりました。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        continue #再び問題
    print("次の問題")
    print("無事に中学校に入学した"+name, "。知り合いの女の子がいるよ。最近なぜか流行っているスカートめくり。あなたは彼女のスカートをめくる？めくらない？")
    user_choice=input("「めくる」または「めくらない」を入力してください： ")
    
    if user_choice == "めくる":
        print("これを機に彼女と仲良くなり楽しい学校生活を過ごしました！")
    elif user_choice =="めくらない":
        print("何もない学校生活に嫌気がさした。家に引きこもりニートに")
        print("ゲームオーバー！ニートになりました。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        continue #再び問題
    print("次の問題")
    print("無事に高校に入学した"+name,"。髪型や服装に目覚めるお年頃。周りのみんなは制服を着崩しているよ。あなたも制服を着崩す？着崩さない？")
    user_choice=input("「着崩す」または「着崩さない」を入力してください: ")
    
    if user_choice == "着崩す":
        print("そこから高速を破りまくり！悪い仲間とつるむように")
        print("逮捕され前科持ちにゲームオーバー！")
        return  # ゲーム終了
    elif user_choice =="着崩さない":
        print("髪型も制服も勉強もきっちりこなす学生生活を過ごしました！某有名大学入学することに！")
        
    else:
        print("無効な選択です。正しい選択を入力してください。")
        continue #再び問題
    print("次の問題")
    print("無事に大学に入学した"+name,"！友達から誘われたサークルが飲みサーだった！このサークルに入る？入らない？")
    user_choice=input("「入る」または「入らない」を入力してください: ")
    
    if user_choice == "入る":
        print("先輩や友達がたくさんできた！毎日の生活がたのしい無事４年生になった。")
    elif user_choice =="入らない":
        print("友達ができなく学校に行かなくなっていった。")
        print("思っていた大学生活と違う！ゲームオーバー！ニートになりました。")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        continue #再び問題
    print("次の問題")
    print("大学４年生になった"+name,"卒業後の進路はどうする？")
    user_choice=input("「家を継ぐ」または「旅に出る」: ")
    
    if user_choice == "家を継ぐ":
        print("代々お酒作る実家を継ぎ若手社長になった！")
        print("それなりのお金持ちになった")
        return
    elif user_choice =="旅に出る":
        print("インドに旅に出た"+name,"")
        print("悟りを開き神になった!congratulation!ゲームクリア！")
        return  # ゲーム終了
    else:
        print("無効な選択です。正しい選択を入力してください。")
        continue 
     
if __name__ == "__main__":
    game_of_life()
    import random

