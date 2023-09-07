FROM continuumio/anaconda3:latest

# umaskを設定
RUN echo "umask 000" >> /root/.bashrc

# 必要なパッケージを更新・インストール
RUN apt-get update && apt-get install -y sqlite3

# Pythonの追加パッケージをインストール
RUN pip install mysql-connector-python==8.0.29
RUN pip install termcolor

# エントリポイントスクリプトを追加
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# エントリポイントを設定
ENTRYPOINT ["/entrypoint.sh"]