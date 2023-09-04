# import lesson_package.utils
from lesson_package import utils
from lesson_package.utils import say_twice # あまり推奨されない

# lesson_package.utils.say_twice('word')
r = utils.say_twice('word')
print(r)

r = say_twice('word')
print(r)