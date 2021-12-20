---
title: "wallPaper"
description: "Wallpaper settings."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaper  
[Back to constructors index](index.md)



Wallpaper settings.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Identifier|
|creator|[Bool](../types/Bool.md) | Optional|Creator of the wallpaper|
|default|[Bool](../types/Bool.md) | Optional|Whether this is the default wallpaper|
|pattern|[Bool](../types/Bool.md) | Optional|Pattern|
|dark|[Bool](../types/Bool.md) | Optional|Dark mode|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|slug|[string](../types/string.md) | Yes|Unique wallpaper ID|
|document|[Document](../types/Document.md) | Optional|The actual wallpaper|
|settings|[WallPaperSettings](../types/WallPaperSettings.md) | Optional|Wallpaper settings|



### Type: [WallPaper](../types/WallPaper.md)


### Example:

```php
$wallPaper = ['_' => 'wallPaper', 'id' => long, 'creator' => Bool, 'default' => Bool, 'pattern' => Bool, 'dark' => Bool, 'access_hash' => long, 'slug' => 'string', 'document' => Document, 'settings' => WallPaperSettings];
```  


Or, if you're into Lua:

```lua
wallPaper={_='wallPaper', id=long, creator=Bool, default=Bool, pattern=Bool, dark=Bool, access_hash=long, slug='string', document=Document, settings=WallPaperSettings}

```


