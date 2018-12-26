---
title: updateReadChannelInbox
description: Update read channel inbox
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelInbox  
[Back to constructors index](index.md)



Update read channel inbox

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|max\_id|[int](../types/int.md) | Yes|Max ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelInbox = ['_' => 'updateReadChannelInbox', 'channel_id' => int, 'max_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateReadChannelInbox", "channel_id": int, "max_id": int}
```


Or, if you're into Lua:

```lua
updateReadChannelInbox={_='updateReadChannelInbox', channel_id=int, max_id=int}

```


