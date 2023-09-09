FROM continuumio/anaconda3:latest

# umaskを設定
RUN echo "umask 000" >> /root/.bashrc

# 必要なパッケージを更新・インストール
RUN apt-get update && apt-get install -y sqlite3

# Pythonの追加パッケージをインストール
RUN pip install termcolor \
    mysql-connector-python==8.0.29 \
    pymysql \
    python-memcached \
    networkx \
    matplotlib \
    pytest-cov \
    pytest-xdist \
    pytest-flake8 \
    pytest-mock \
    pytest-pylint \
    pytest-runner \
    pytest-sugar \
    pytest-timeout \
    pytest-watch \
    pytest-xdist \
    selenium \
    pycryptodome

# エントリポイントスクリプトを追加
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# エントリポイントを設定
ENTRYPOINT ["/entrypoint.sh"]