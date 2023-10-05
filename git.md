# gitコマンド集

## 初期化
```
git init
```
## add
```
#特定のファイルのみ
git add [name]
#全てのファイル
git add -A
#カレントディレクトリ配下
git add .
#更新があった全てのファイル
git add -u
```

## commit
```
git commit -m ""
```

## remoteリポジトリの設定
```
git remote add origin https://github.com/XXXX/XXXXXX.git
#originは名前
```

## push
```
git push -u origin master
#origin:remoteリポジトリ名
#master:branch名
```

## クローン
```
git clone https://github.com/hysts/pytorch_mpiigaze.git
```

## pull
```
git pull
```

## fetch
```
git fetch
```

## merge
```
git merge origin/master
```

## remote
```
git remote -v
```