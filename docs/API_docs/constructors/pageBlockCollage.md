---
title: "pageBlockCollage"
description: "Collage of media"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockCollage  
[Back to constructors index](index.md)



Collage of media

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|items|Array of [PageBlock](../types/PageBlock.md) | Yes|Media elements|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockCollage = ['_' => 'pageBlockCollage', 'items' => [PageBlock, PageBlock], 'caption' => PageCaption];
```  


Or, if you're into Lua:

```lua
pageBlockCollage={_='pageBlockCollage', items={PageBlock}, caption=PageCaption}

```


