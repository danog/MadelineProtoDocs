---
title: updateDeleteMessages
description: updateDeleteMessages attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteMessages  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|messages|Array of [int](../types/int.md) | Yes|
|pts|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDeleteMessages = ['_' => 'updateDeleteMessages', 'messages' => [int, int], 'pts' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateDeleteMessages", "messages": [int], "pts": int}
```


Or, if you're into Lua:

```lua
updateDeleteMessages={_='updateDeleteMessages', messages={int}, pts=int}

```


