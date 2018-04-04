---
title: webPagePending
description: webPagePending attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPagePending  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|



### Type: [WebPage](../types/WebPage.md)


### Example:

```
$webPagePending = ['_' => 'webPagePending', 'id' => long, 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "webPagePending", "id": long, "date": int}
```


Or, if you're into Lua:  


```
webPagePending={_='webPagePending', id=long, date=int}

```


