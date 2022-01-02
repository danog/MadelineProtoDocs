---
title: "textImage"
description: "Inline image"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textImage  
[Back to constructors index](index.md)



Inline image

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document\_id|[long](../types/long.md) | Yes|Document ID|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|



### Type: [RichText](../types/RichText.md)


### Example:

```php
$textImage = ['_' => 'textImage', 'document_id' => long, 'w' => int, 'h' => int];
```  


Or, if you're into Lua:

```lua
textImage={_='textImage', document_id=long, w=int, h=int}

```


