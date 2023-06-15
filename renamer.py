# 将漫画目录下的图片名重命名，添加漫画标题（根目录名）前缀。

import sys
import os

def removeMultiTail(raw, tail):
    while raw.rfind(tail) == len(raw) - len(tail):
        raw = raw[:-len(tail)]
    return raw

def doRename(rootPath):
    print("doRenaming for ", rootPath)
    rootPath = removeMultiTail(rootPath, '\\')
    if rootPath.rfind('\\') == -1:
        print('invalid rootPath, must be full path. now path:', rootPath)
        return
    comicTitle = rootPath[rootPath.rfind('\\')+1:]
    print('comicTitle:', comicTitle)
    for (root, dirs, files) in os.walk(rootPath):
        for name in files:
            if name.find(comicTitle) == 0: # 防止重复运行时重复添加前缀
                continue
            oldName = os.path.join(root, name)
            newName = os.path.join(root, comicTitle + "_" + name)
            os.rename(oldName, newName)
    print('done')

if __name__ == "__main__":
    for a in sys.argv[1:]:
        doRename(a)
    
