---
title: messageEntityUnderline
description: Message entity representing underlined text.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityUnderline  
[Back to constructors index](index.md)



Message entity representing underlined text.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityUnderline = ['_' => 'messageEntityUnderline', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityUnderline={_='messageEntityUnderline', offset=int, length=int}

```


