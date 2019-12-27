---
title: account.wallPapers
description: Installed wallpapers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.wallPapers  
[Back to constructors index](index.md)



Installed wallpapers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|wallpapers|Array of [WallPaper](../types/WallPaper.md) | Yes|Wallpapers|



### Type: [account.WallPapers](../types/account.WallPapers.md)


### Example:

```php
$account.wallPapers = ['_' => 'account.wallPapers', 'hash' => int, 'wallpapers' => [WallPaper, WallPaper]];
```  


Or, if you're into Lua:

```lua
account.wallPapers={_='account.wallPapers', hash=int, wallpapers={WallPaper}}

```


