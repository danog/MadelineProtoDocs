---
title: recentMeUrlChat
description: recentMeUrlChat attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: recentMeUrlChat  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|url|[string](../types/string.md) | Yes|
|chat\_id|[int](../types/int.md) | Yes|



### Type: [RecentMeUrl](../types/RecentMeUrl.md)


### Example:

```php
$recentMeUrlChat = ['_' => 'recentMeUrlChat', 'url' => 'string', 'chat_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "recentMeUrlChat", "url": "string", "chat_id": int}
```


Or, if you're into Lua:

```lua
recentMeUrlChat={_='recentMeUrlChat', url='string', chat_id=int}

```


