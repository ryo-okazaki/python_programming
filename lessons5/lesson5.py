import os
import pathlib
import glob
import shutil

print(os.path.exists('../README.md')) # ファイルが存在するかどうか
print(os.path.isfile('../README.md')) # ファイルかどうか
print(os.path.isdir('../README.md')) # ディレクトリかどうか

os.rename('test.txt', 'renamed.txt') # ファイル名の変更
os.symlink('renamed.txt', 'symlink.txt') # シンボリックリンクの作成

os.mkdir('test_dir') # ディレクトリの作成
os.rmdir('test_dir') # ディレクトリの削除

pathlib.Path('empty.txt').touch() # 空のファイルを作成
os.remove('empty.txt') # ファイルの削除

os.mkdir('test_dir')
os.mkdir('test_dir/test_dir2')
print(os.listdir('test_dir')) # ディレクトリ内のファイルをリストで表示

pathlib.Path('test_dir/test_dir2/empty.txt').touch()
print(glob.glob('test_dir/test_dir2/*')) # ディレクトリ内のファイルをリストで表示
shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt') # ファイルのコピー

shutil.rmtree('test_dir') # ディレクトリの削除

print(os.getcwd()) # カレントディレクトリの表示