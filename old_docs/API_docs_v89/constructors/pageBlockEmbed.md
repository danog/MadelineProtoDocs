---
title: pageBlockEmbed
description: Page block embed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockEmbed  
[Back to constructors index](index.md)



Page block embed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|full\_width|[Bool](../types/Bool.md) | Optional|Full width?|
|allow\_scrolling|[Bool](../types/Bool.md) | Optional|Allow scrolling?|
|url|[string](../types/string.md) | Optional|URL|
|html|[string](../types/string.md) | Optional|Html|
|poster\_photo\_id|[long](../types/long.md) | Optional|Poster photo ID|
|w|[int](../types/int.md) | Optional|Width|
|h|[int](../types/int.md) | Optional|Height|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockEmbed = ['_' => 'pageBlockEmbed', 'full_width' => Bool, 'allow_scrolling' => Bool, 'url' => 'string', 'html' => 'string', 'poster_photo_id' => long, 'w' => int, 'h' => int, 'caption' => PageCaption];
```  


Or, if you're into Lua:

```lua
pageBlockEmbed={_='pageBlockEmbed', full_width=Bool, allow_scrolling=Bool, url='string', html='string', poster_photo_id=long, w=int, h=int, caption=PageCaption}

```


