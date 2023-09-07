from optparse import OptionParser
from optparse import OptionGroup

def main():
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string',
                      dest='filename', help='File name')
    parser.add_option('-n', '--num', action='store', type='int',
                      dest='num', help='Number (int)')
    parser.set_defaults(verbose=True)
    parser.add_option('-v', action='store_true', # store_false
                      dest='verbose', default=False, help='Verbose flag')

    parser.add_option('-q', '--quiet', action='store_false',
                      dest='verbose', default=False, help='Quiet flag')
    parser.add_option('-r', action='store_const', const='root', dest='user_name') # -rの後に何も指定がないと、user_nameはrootになる

    parser.add_option('-e', dest='env') # -eの後に何も指定がないと、envはNoneになる

    def is_release(option, opt_str, value, parser):
        if parser.values.env == 'prd':
            raise parser.error('Can not release')
        setattr(parser.values, option.dest, True)

    parser.add_option('--release', action='callback', callback=is_release, dest='release')

    group = OptionGroup(parser, 'Dangerous Options')
    group.add_option('-g', action='store_true', help='Group option')
    parser.add_option_group(group)

    options, args = parser.parse_args()
    print(options)
    print(args)

    # python lesson.py --helpでこのファイルのヘルプを表示できる(オプションなどを表示)

    # python lesson.py -f test.txtでファイル名を指定できる
    # python lesson.py -n 100で数値を指定できる
    # python lesson.py -vでverboseをTrueにできる
    # python lesson.py -v -f test.txt -n 100で複数指定できる

    # actionsを書かない場合、typeがデフォルトでstringになる
    #


if __name__ == '__main__':
    main()