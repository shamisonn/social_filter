# social_filter

[![wercker status](https://app.wercker.com/status/7749870bec9e065bade5b1e4610aca10/s/master "wercker status")](https://app.wercker.com/project/byKey/7749870bec9e065bade5b1e4610aca10)

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">図です <a href="https://t.co/2OFfuLPk2l">pic.twitter.com/2OFfuLPk2l</a></p>&mdash; 4869 (@sh4869sh) <a href="https://twitter.com/sh4869sh/status/767244989503901696">2016年8月21日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

## Requirements

- MeCab
- python3
- `pip install -r requirements.txt`

### Installation of MeCab

To install MeCab, you can use your package manager or manually:

```sh
git clone https://github.com/taku910/mecab.git

# install mecab
cd mecab/mecab
./configure  --enable-utf8-only
make
make check
make install

# install dictionary
cd ../mecab-ipadic
./configure --with-charset=utf8
make
make install
```


# Usage

1. config.iniに鍵を書き込む
2. ↓

![howtouse](howtouse.png "にゃーん")


適当にツイートされるはず。