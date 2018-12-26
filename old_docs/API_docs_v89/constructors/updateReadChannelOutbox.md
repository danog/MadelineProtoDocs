---
title: updateReadChannelOutbox
description: Update read channel outbox
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelOutbox  
[Back to constructors index](index.md)



Update read channel outbox

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|max\_id|[int](../types/int.md) | Yes|Max ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelOutbox = ['_' => 'updateReadChannelOutbox', 'channel_id' => int, 'max_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateReadChannelOutbox", "channel_id": int, "max_id": int}
```


Or, if you're into Lua:

```lua
updateReadChannelOutbox={_='updateReadChannelOutbox', channel_id=int, max_id=int}

```


