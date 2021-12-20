---
title: "messageEntityPhone"
description: "Message entity representing a phone number."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityPhone  
[Back to constructors index](index.md)



Message entity representing a phone number.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityPhone = ['_' => 'messageEntityPhone', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityPhone={_='messageEntityPhone', offset=int, length=int}

```


