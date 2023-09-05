import os
import subprocess

# os.system('ls') # 非推奨
subprocess.run(['ls', '-al'])
subprocess.run('ls -al', shell=True) # コマンドをシェルに渡す
# subprocess.run('ls -al | grep test', shell=True) # shell=Trueは非推奨。シェルインジェクション

r = subprocess.run('ls hoge', shell=True, check=True) # check=Trueは、エラーが出たら例外を出す
print('###')
print(r.returncode)
print(r)

# |などのパイプラインを使う場合は、Popenを使う
# シェルインジェクションを避ける
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(
    ['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE
)
p1.stdout.close()
output = p2.communicate()[0]
print(output)