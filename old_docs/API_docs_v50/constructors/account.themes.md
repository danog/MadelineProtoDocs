---
title: account.themes
description: Installed themes
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_themes.html
---
# Constructor: account.themes  
[Back to constructors index](index.md)



Installed themes

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](../types/long.md) | Yes|
|themes|Array of [Theme](../types/Theme.md) | Yes|Themes|



### Type: [account.Themes](../types/account.Themes.md)


### Example:

```php
$account_themes = ['_' => 'account.themes', 'hash' => long, 'themes' => [Theme, Theme]];
```  


Or, if you're into Lua:

```lua
account_themes={_='account.themes', hash=long, themes={Theme}}

```


