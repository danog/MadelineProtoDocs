---
title: messageRange
description: messageRange attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageRange  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|min\_id|[int](../types/int.md) | Yes|
|max\_id|[int](../types/int.md) | Yes|



### Type: [MessageRange](../types/MessageRange.md)


### Example:

```php
$messageRange = ['_' => 'messageRange', 'min_id' => int, 'max_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageRange", "min_id": int, "max_id": int}
```


Or, if you're into Lua:

```lua
messageRange={_='messageRange', min_id=int, max_id=int}

```


