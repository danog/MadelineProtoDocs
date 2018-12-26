---
title: updateMessageID
description: Update message ID
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessageID  
[Back to constructors index](index.md)



Update message ID

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateMessageID = ['_' => 'updateMessageID', 'id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateMessageID", "id": int}
```


Or, if you're into Lua:

```lua
updateMessageID={_='updateMessageID', id=int}

```


