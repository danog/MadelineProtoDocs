---
title: "messageEntityHashtag"
description: "#hashtag message entity"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityHashtag  
[Back to constructors index](index.md)



**\#hashtag** message entity

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityHashtag = ['_' => 'messageEntityHashtag', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityHashtag={_='messageEntityHashtag', offset=int, length=int}

```


