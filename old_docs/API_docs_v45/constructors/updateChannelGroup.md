---
title: updateChannelGroup
description: Update channel group
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelGroup  
[Back to constructors index](index.md)



Update channel group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|group|[MessageGroup](../types/MessageGroup.md) | Yes|Group|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelGroup = ['_' => 'updateChannelGroup', 'channel_id' => int, 'group' => MessageGroup];
```  


Or, if you're into Lua:

```lua
updateChannelGroup={_='updateChannelGroup', channel_id=int, group=MessageGroup}

```


