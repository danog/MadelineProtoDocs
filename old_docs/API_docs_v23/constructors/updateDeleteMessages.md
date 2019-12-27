---
title: updateDeleteMessages
description: Messages were deleted.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteMessages  
[Back to constructors index](index.md)



Messages were deleted.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [int](../types/int.md) | Yes|Messages|
|pts|[int](../types/int.md) | Yes|New quality of actions in a message box|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDeleteMessages = ['_' => 'updateDeleteMessages', 'messages' => [int, int], 'pts' => int];
```  


Or, if you're into Lua:

```lua
updateDeleteMessages={_='updateDeleteMessages', messages={int}, pts=int}

```


