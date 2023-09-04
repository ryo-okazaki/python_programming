import lesson_package.talk.animal

import config

print('lesson', __name__)


# 上記のようにローカルにimportすると予期しない動作をする
# 必ず以下のように書く
def main():
    lesson_package.talk.animal.sing()

if __name__ == '__main__':
    main()