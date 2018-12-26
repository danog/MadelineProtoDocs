---
title: pageBlockSlideshow
description: Page block slideshow
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockSlideshow  
[Back to constructors index](index.md)



Page block slideshow

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|items|Array of [PageBlock](../types/PageBlock.md) | Yes|Items|
|caption|[RichText](../types/RichText.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockSlideshow = ['_' => 'pageBlockSlideshow', 'items' => [PageBlock, PageBlock], 'caption' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockSlideshow", "items": [PageBlock], "caption": RichText}
```


Or, if you're into Lua:

```lua
pageBlockSlideshow={_='pageBlockSlideshow', items={PageBlock}, caption=RichText}

```


