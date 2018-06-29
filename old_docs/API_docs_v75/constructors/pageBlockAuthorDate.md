---
title: pageBlockAuthorDate
description: pageBlockAuthorDate attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockAuthorDate  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|author|[RichText](../types/RichText.md) | Yes|
|published\_date|[int](../types/int.md) | Yes|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```
$pageBlockAuthorDate = ['_' => 'pageBlockAuthorDate', 'author' => RichText, 'published_date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockAuthorDate", "author": RichText, "published_date": int}
```


Or, if you're into Lua:  


```
pageBlockAuthorDate={_='pageBlockAuthorDate', author=RichText, published_date=int}

```


