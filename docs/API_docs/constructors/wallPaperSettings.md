---
title: wallPaperSettings
description: Wallpaper settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaperSettings  
[Back to constructors index](index.md)



Wallpaper settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blur|[Bool](../types/Bool.md) | Optional|Blur?|
|motion|[Bool](../types/Bool.md) | Optional|Motion?|
|background\_color|[int](../types/int.md) | Optional|Background color|
|intensity|[int](../types/int.md) | Optional|Intensity|



### Type: [WallPaperSettings](../types/WallPaperSettings.md)


### Example:

```php
$wallPaperSettings = ['_' => 'wallPaperSettings', 'blur' => Bool, 'motion' => Bool, 'background_color' => int, 'intensity' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "wallPaperSettings", "blur": Bool, "motion": Bool, "background_color": int, "intensity": int}
```


Or, if you're into Lua:

```lua
wallPaperSettings={_='wallPaperSettings', blur=Bool, motion=Bool, background_color=int, intensity=int}

```


