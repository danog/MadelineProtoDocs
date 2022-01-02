---
title: "messageRange"
description: "Indicates a range of chat messages"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageRange  
[Back to constructors index](index.md)



Indicates a range of chat messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|min\_id|[int](../types/int.md) | Yes|Start of range (message ID)|
|max\_id|[int](../types/int.md) | Yes|End of range (message ID)|



### Type: [MessageRange](../types/MessageRange.md)


### Example:

```php
$messageRange = ['_' => 'messageRange', 'min_id' => int, 'max_id' => int];
```  


Or, if you're into Lua:

```lua
messageRange={_='messageRange', min_id=int, max_id=int}

```


