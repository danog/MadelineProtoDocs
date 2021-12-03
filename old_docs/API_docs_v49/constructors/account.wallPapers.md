---
title: account.wallPapers
description: Installed wallpapers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_wallPapers.html
---
# Constructor: account.wallPapers  
[Back to constructors index](index.md)



Installed wallpapers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|
|wallpapers|Array of [WallPaper](../types/WallPaper.md) | Yes|Wallpapers|



### Type: [account.WallPapers](../types/account.WallPapers.md)


### Example:

```php
$account_wallPapers = ['_' => 'account.wallPapers', 'hash' => int, 'wallpapers' => [WallPaper, WallPaper]];
```  


Or, if you're into Lua:

```lua
account_wallPapers={_='account.wallPapers', hash=int, wallpapers={WallPaper}}

```


