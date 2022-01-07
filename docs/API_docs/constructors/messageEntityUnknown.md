---
title: "messageEntityUnknown"
description: "Unknown message entity"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityUnknown  
[Back to constructors index](index.md)



Unknown message entity

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityUnknown = ['_' => 'messageEntityUnknown', 'offset' => int, 'length' => int];
```  
