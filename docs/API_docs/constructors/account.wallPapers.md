---
title: "account.wallPapers"
description: "Installed wallpapers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_wallPapers.html
---
# Constructor: account.wallPapers  
[Back to constructors index](/API_docs/constructors/index.html)



Installed wallpapers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|wallpapers|Array of [WallPaper](/API_docs/types/WallPaper.html) | Yes|Wallpapers|



### Type: [account.WallPapers](/API_docs/types/account.WallPapers.html)


### Example:

```
$account_wallPapers = ['_' => 'account.wallPapers', 'hash' => long, 'wallpapers' => [WallPaper, WallPaper]];
```  
