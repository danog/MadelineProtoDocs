---
title: "account.wallPapers"
description: "Installed wallpapers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_wallPapers.html
---
# Constructor: account.wallPapers  
[Back to constructors index](index.md)



Installed wallpapers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](../types/long.md) | Yes|
|wallpapers|Array of [WallPaper](../types/WallPaper.md) | Yes|Wallpapers|



### Type: [account.WallPapers](../types/account.WallPapers.md)


### Example:

```php
$account_wallPapers = ['_' => 'account.wallPapers', 'hash' => long, 'wallpapers' => [WallPaper, WallPaper]];
```  
