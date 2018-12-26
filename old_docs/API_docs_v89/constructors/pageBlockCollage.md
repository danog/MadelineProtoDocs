---
title: pageBlockCollage
description: Page block collage
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockCollage  
[Back to constructors index](index.md)



Page block collage

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|items|Array of [PageBlock](../types/PageBlock.md) | Yes|Items|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockCollage = ['_' => 'pageBlockCollage', 'items' => [PageBlock, PageBlock], 'caption' => PageCaption];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockCollage", "items": [PageBlock], "caption": PageCaption}
```


Or, if you're into Lua:

```lua
pageBlockCollage={_='pageBlockCollage', items={PageBlock}, caption=PageCaption}

```


