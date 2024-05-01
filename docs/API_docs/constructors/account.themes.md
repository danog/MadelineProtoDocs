---
title: "account.themes"
description: "Installed themes"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_themes.html
---
# Constructor: account.themes  
[Back to constructors index](/API_docs/constructors/index.html)



Installed themes

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|themes|Array of [Theme](/API_docs/types/Theme.html) | Yes|Themes|



### Type: [account.Themes](/API_docs/types/account.Themes.html)


### Example:

```
$account_themes = ['_' => 'account.themes', 'hash' => long, 'themes' => [Theme, Theme]];
```  
