# コマンドライン引数
import sys
print(sys.argv)

for i in sys.argv:
    print(i)

# ターミナル上で
# python lesson.py 1 2 3

# terminal
# docker-compose run --rm anaconda python /app/lessons3/lesson.py [option引数]

# PyCharm
# ファイルを右クリック
# さらに実行/デバッグ → 実行構成の変更
# スクリプトパラメータに引数を入力
# 適用