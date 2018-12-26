---
title: updateChannelTooLong
description: Update channel too long
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelTooLong  
[Back to constructors index](index.md)



Update channel too long

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelTooLong = ['_' => 'updateChannelTooLong', 'channel_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChannelTooLong", "channel_id": int}
```


Or, if you're into Lua:

```lua
updateChannelTooLong={_='updateChannelTooLong', channel_id=int}

```


