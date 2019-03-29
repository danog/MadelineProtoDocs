---
title: updateDeleteMessages
description: Update delete messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteMessages  
[Back to constructors index](index.md)



Update delete messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [int](../types/int.md) | Yes|Messages|
|pts|[int](../types/int.md) | Yes|Pts|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDeleteMessages = ['_' => 'updateDeleteMessages', 'messages' => [int, int], 'pts' => int];
```  


Or, if you're into Lua:

```lua
updateDeleteMessages={_='updateDeleteMessages', messages={int}, pts=int}

```


