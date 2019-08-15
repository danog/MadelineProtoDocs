---
title: account.wallPapers
description: Wallpapers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.wallPapers  
[Back to constructors index](index.md)



Wallpapers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|Hash|
|wallpapers|Array of [WallPaper](../types/WallPaper.md) | Yes|Wallpapers|



### Type: [account\_WallPapers](../types/account_WallPapers.md)


### Example:

```php
$account_wallPapers = ['_' => 'account.wallPapers', 'hash' => int, 'wallpapers' => [WallPaper, WallPaper]];
```  


Or, if you're into Lua:

```lua
account_wallPapers={_='account.wallPapers', hash=int, wallpapers={WallPaper}}

```


