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
|caption|[RichText](../types/RichText.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockPhoto = ['_' => 'pageBlockPhoto', 'photo_id' => long, 'caption' => RichText];
```  


Or, if you're into Lua:

```lua
pageBlockPhoto={_='pageBlockPhoto', photo_id=long, caption=RichText}

```


