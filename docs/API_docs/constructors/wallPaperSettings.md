---
title: wallPaperSettings
description: wallPaperSettings attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaperSettings  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|blur|[Bool](../types/Bool.md) | Optional|
|motion|[Bool](../types/Bool.md) | Optional|
|background\_color|[int](../types/int.md) | Optional|
|intensity|[int](../types/int.md) | Optional|



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


