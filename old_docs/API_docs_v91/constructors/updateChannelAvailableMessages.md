---
title: updateChannelAvailableMessages
description: Update channel available messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelAvailableMessages  
[Back to constructors index](index.md)



Update channel available messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|available\_min\_id|[int](../types/int.md) | Yes|Available min ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelAvailableMessages = ['_' => 'updateChannelAvailableMessages', 'channel_id' => int, 'available_min_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChannelAvailableMessages", "channel_id": int, "available_min_id": int}
```


Or, if you're into Lua:

```lua
updateChannelAvailableMessages={_='updateChannelAvailableMessages', channel_id=int, available_min_id=int}

```


