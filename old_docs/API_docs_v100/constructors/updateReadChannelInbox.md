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
|folder\_id|[int](../types/int.md) | Optional|Folder ID|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|max\_id|[int](../types/int.md) | Yes|Max ID|
|still\_unread\_count|[int](../types/int.md) | Yes|Still unread count|
|pts|[int](../types/int.md) | Yes|PTS|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelInbox = ['_' => 'updateReadChannelInbox', 'folder_id' => int, 'channel_id' => int, 'max_id' => int, 'still_unread_count' => int, 'pts' => int];
```  


Or, if you're into Lua:

```lua
updateReadChannelInbox={_='updateReadChannelInbox', folder_id=int, channel_id=int, max_id=int, still_unread_count=int, pts=int}

```


