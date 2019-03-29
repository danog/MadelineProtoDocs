---
title: updateChannelPinnedMessage
description: Update channel pinned message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelPinnedMessage  
[Back to constructors index](index.md)



Update channel pinned message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|id|[int](../types/int.md) | Yes|ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelPinnedMessage = ['_' => 'updateChannelPinnedMessage', 'channel_id' => int, 'id' => int];
```  


Or, if you're into Lua:

```lua
updateChannelPinnedMessage={_='updateChannelPinnedMessage', channel_id=int, id=int}

```


