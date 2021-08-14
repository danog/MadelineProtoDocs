---
title: wallPaperNoFile
description: No file wallpaper
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaperNoFile  
[Back to constructors index](index.md)



No file wallpaper

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|
|default|[Bool](../types/Bool.md) | Optional|Whether this is the default wallpaper|
|dark|[Bool](../types/Bool.md) | Optional|Dark mode|
|settings|[WallPaperSettings](../types/WallPaperSettings.md) | Optional|Wallpaper settings|



### Type: [WallPaper](../types/WallPaper.md)


### Example:

```php
$wallPaperNoFile = ['_' => 'wallPaperNoFile', 'id' => long, 'default' => Bool, 'dark' => Bool, 'settings' => WallPaperSettings];
```  


Or, if you're into Lua:

```lua
wallPaperNoFile={_='wallPaperNoFile', id=long, default=Bool, dark=Bool, settings=WallPaperSettings}

```


