---
title: account.wallPapers
description: account_wallPapers attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.wallPapers  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[int](../types/int.md) | Yes|
|wallpapers|Array of [WallPaper](../types/WallPaper.md) | Yes|



### Type: [account\_WallPapers](../types/account_WallPapers.md)


### Example:

```php
$account_wallPapers = ['_' => 'account.wallPapers', 'hash' => int, 'wallpapers' => [WallPaper, WallPaper]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.wallPapers", "hash": int, "wallpapers": [WallPaper]}
```


Or, if you're into Lua:

```lua
account_wallPapers={_='account.wallPapers', hash=int, wallpapers={WallPaper}}

```


