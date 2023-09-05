import tarfile

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('../test_dir')

with tarfile.open('./test.tar.gz', 'r:gz') as tr:
    # tr.extractall(path='test_tar') # test_tarというディレクトリが作成され、その中に解凍される
    with tr.extractfile('../test_dir/sub_test_dir/test.txt') as f:
        print(f.read())