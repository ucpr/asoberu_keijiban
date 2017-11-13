# 遊べる掲示板(backend)

KOSENハッカソンで制作した遊べる掲示板というシステムのbackendのコードです.  
heroku上で動いています.  (https://enigmatic-earth-37733.herokuapp.com)

## 使い方
`https://enigmatic-earth-37733.herokuapp.com/comment/<hash_tag>`の `<hash_tag>`のところに検索したいhashtagを書き込んで`GET req`を送ると,tweetの情報がjsonで帰ってきます(今は15件).  
jsonの形式は以下の例の通りです.  

```json
{
  "comment": [
    {
      "date": "Sat Nov 11 14:41:41 +0000 2017", 
      "pic": "", 
      "text": "hoge"
    }, 
    {
      "date": "Sat Nov 11 14:41:31 +0000 2017", 
      "pic": "", 
      "text": "popopopop"
    }, 
    {
      "date": "Sat Nov 11 14:40:00 +0000 2017", 
      "pic": "https://hoge.com/static/hoge.png", 
      "text": "puyo"
    }
  ]
}
```

## example

```bash
$ curl https://enigmatic-earth-37733.herokuapp.com/comment/hogepoyo  
$ curl https://enigmatic-earth-37733.herokuapp.com/comment/banana
```
