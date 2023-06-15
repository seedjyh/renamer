# renamer

## 概述

对于一个文件夹「A」，可以将其子文件夹里的每一个文件都添加前缀「A」。

```bat
G:\Entertainment\Comic\down\超能力美空
├─第01卷
    ├─第01卷_000001.jpg
    ├─第01卷_000002.jpg
    ├─第01卷_000003.jpg
├─第02卷
    ├─第02卷_000001.jpg
    ├─第02卷_000002.jpg
    ├─第02卷_000003.jpg
```

重命名为

```bat
G:\Entertainment\Comic\down\超能力美空
├─第01卷
    ├─超能力美空_第01卷_000001.jpg
    ├─超能力美空_第01卷_000002.jpg
    ├─超能力美空_第01卷_000003.jpg
├─第02卷
    ├─超能力美空_第02卷_000001.jpg
    ├─超能力美空_第02卷_000002.jpg
    ├─超能力美空_第02卷_000003.jpg
```

## how to use

```bat
C:\Users\jyh>H:

H:\>cd renamer

H:\renamer>renamer.py G:\Entertainment\Comic\down\超能力美空
doRenaming for  G:\Entertainment\Comic\down\超能力美空
comicTitle: 超能力美空
done

H:\renamer>

```
