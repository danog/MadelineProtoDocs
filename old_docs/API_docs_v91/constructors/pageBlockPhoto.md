---
title: pageBlockPhoto
description: Page block photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockPhoto  
[Back to constructors index](index.md)



Page block photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo\_id|[long](../types/long.md) | Yes|Photo ID|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|
|url|[string](../types/string.md) | Optional|URL|
|webpage\_id|[long](../types/long.md) | Optional|Webpage ID|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockPhoto = ['_' => 'pageBlockPhoto', 'photo_id' => long, 'caption' => PageCaption, 'url' => 'string', 'webpage_id' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockPhoto", "photo_id": long, "caption": PageCaption, "url": "string", "webpage_id": long}
```


Or, if you're into Lua:

```lua
pageBlockPhoto={_='pageBlockPhoto', photo_id=long, caption=PageCaption, url='string', webpage_id=long}

```


