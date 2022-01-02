---
title: "messageEntityBankCard"
description: "Indicates a credit card number"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityBankCard  
[Back to constructors index](index.md)



Indicates a credit card number

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityBankCard = ['_' => 'messageEntityBankCard', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityBankCard={_='messageEntityBankCard', offset=int, length=int}

```


