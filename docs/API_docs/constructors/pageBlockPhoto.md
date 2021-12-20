---
title: "pageBlockPhoto"
description: "A photo"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockPhoto  
[Back to constructors index](index.md)



A photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo\_id|[long](../types/long.md) | Yes|Photo ID|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|
|url|[string](../types/string.md) | Optional|HTTP URL of page the photo leads to when clicked|
|webpage\_id|[long](../types/long.md) | Optional|ID of preview of the page the photo leads to when clicked|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockPhoto = ['_' => 'pageBlockPhoto', 'photo_id' => long, 'caption' => PageCaption, 'url' => 'string', 'webpage_id' => long];
```  


Or, if you're into Lua:

```lua
pageBlockPhoto={_='pageBlockPhoto', photo_id=long, caption=PageCaption, url='string', webpage_id=long}

```


