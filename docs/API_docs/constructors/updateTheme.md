---
title: "updateTheme"
description: "A cloud theme was updated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateTheme  
[Back to constructors index](index.md)



A cloud theme was updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|theme|[Theme](../types/Theme.md) | Yes|Theme|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateTheme = ['_' => 'updateTheme', 'theme' => Theme];
```  


Or, if you're into Lua:

```lua
updateTheme={_='updateTheme', theme=Theme}

```


