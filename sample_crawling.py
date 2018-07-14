#!/usr/bin/env python
# -*- coding:utf-8

from urllib.request import urlopen

f = urlopen("http://google.co.jp/")

# エンコーディング種類の取得(デフォルトutf-8)
enc_type = f.info().get_content_charset(failobj="utf-8")
print(enc_type)

# 型の取得
print(type(f))

# HTTPヘッダの取得
print(f.getheader("Content-Type"))

# ステータスコード
print(f.status)

# HTTPレスポンス
print(f.read().decode(enc_type))
