# 読み込み
with open('requirements.txt') as reader:
    content = reader.read()
# 置換
print(type(content))
print(content)
e = content.split('\n')
print(e)
e.pop()
print(e)
body = ''
for i in e:
    print(i)
    body += '\t- ' + i + '\n'
header = 'name: env1\nchannels:\n\t- defaults\ndependencies:\n'
bottom = 'prefix: ~/anaconda3/envs/murata_GE1'
print(header)
print(body)
print(bottom)


# 書き出し
with open('requirements.yaml', 'w') as writer:
    writer.write(header+body+bottom)