---
title: updateReadChannelInbox
description: Incoming messages in a [channel/supergroup](https://core.telegram.org/api/channel) were read
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelInbox  
[Back to constructors index](index.md)



Incoming messages in a [channel/supergroup](https://core.telegram.org/api/channel) were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|folder\_id|[int](../types/int.md) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|channel\_id|[int](../types/int.md) | Yes|Channel/supergroup ID|
|max\_id|[int](../types/int.md) | Yes|Position up to which all incoming messages are read.|
|still\_unread\_count|[int](../types/int.md) | Yes|Count of messages weren't read yet|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelInbox = ['_' => 'updateReadChannelInbox', 'folder_id' => int, 'channel_id' => int, 'max_id' => int, 'still_unread_count' => int, 'pts' => int];
```  


Or, if you're into Lua:

```lua
updateReadChannelInbox={_='updateReadChannelInbox', folder_id=int, channel_id=int, max_id=int, still_unread_count=int, pts=int}

```


