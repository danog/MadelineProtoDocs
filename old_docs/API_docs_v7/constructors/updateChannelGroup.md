---
title: updateChannelGroup
description: updateChannelGroup attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelGroup  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel\_id|[int](../types/int.md) | Yes|
|group|[MessageGroup](../types/MessageGroup.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChannelGroup = ['_' => 'updateChannelGroup', 'channel_id' => int, 'group' => MessageGroup];
```  


Or, if you're into Lua:

```lua
updateChannelGroup={_='updateChannelGroup', channel_id=int, group=MessageGroup}

```


