FROM continuumio/anaconda3:latest

# umaskを設定
RUN echo "umask 000" >> /root/.bashrc

# Pythonの追加パッケージをインストール
RUN pip install termcolor

# エントリポイントスクリプトを追加
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# エントリポイントを設定
ENTRYPOINT ["/entrypoint.sh"]