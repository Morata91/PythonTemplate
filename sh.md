# シェルスクリプト系

## venv
```
python -m venv .env
#.envは仮想環境の名前
```
```
source .env/bin/activate
```
```
pip install -r requirements.txt
```
```
#終了
deactivate
```
# 削除
フォルダを削除するだけ

```
#一覧
pip freeze
```
```
#一覧をファイルに書き込み
pip freeze > requirements.txt
```
```
#仮想環境の削除


```


## conda環境
```
#作成
conda create -n 環境名
```

```
conda activate 環境名
```
```
conda deactivate
```