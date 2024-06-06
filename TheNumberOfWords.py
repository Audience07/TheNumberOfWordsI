from pathlib import Path


FileNames = ["这里填入文件名,用逗号隔开"]
Unexisits = []


#如果打开文件返回文件的单词个数
#如果打开文件失败返回None

def Content_Words(path):
        try:
            contents = path.read_text()
        except FileNotFoundError:
            return None
        else:
            return len(contents)


    
for FileName in FileNames:
    path = Path(FileName)
    if not Content_Words(path):
        Unexisits.append(path.name)
    else:
         print(f"文件{path.name}的单词数量为{Content_Words(path)}")

    
print(f"不存在的文件:{Unexisits}")
    