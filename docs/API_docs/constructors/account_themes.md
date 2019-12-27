---
title: account.themes
description: Installed themes
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.themes  
[Back to constructors index](index.md)



Installed themes

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|themes|Array of [Theme](../types/Theme.md) | Yes|Themes|



### Type: [account\_Themes](../types/account_Themes.md)


### Example:

```php
$account_themes = ['_' => 'account.themes', 'hash' => int, 'themes' => [Theme, Theme]];
```  


Or, if you're into Lua:

```lua
account_themes={_='account.themes', hash=int, themes={Theme}}

```


