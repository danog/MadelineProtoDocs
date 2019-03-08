---
title: chatBannedRights
description: chatBannedRights attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatBannedRights  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|view\_messages|[Bool](../types/Bool.md) | Optional|
|send\_messages|[Bool](../types/Bool.md) | Optional|
|send\_media|[Bool](../types/Bool.md) | Optional|
|send\_stickers|[Bool](../types/Bool.md) | Optional|
|send\_gifs|[Bool](../types/Bool.md) | Optional|
|send\_games|[Bool](../types/Bool.md) | Optional|
|send\_inline|[Bool](../types/Bool.md) | Optional|
|embed\_links|[Bool](../types/Bool.md) | Optional|
|send\_polls|[Bool](../types/Bool.md) | Optional|
|change\_info|[Bool](../types/Bool.md) | Optional|
|invite\_users|[Bool](../types/Bool.md) | Optional|
|pin\_messages|[Bool](../types/Bool.md) | Optional|
|until\_date|[int](../types/int.md) | Yes|



### Type: [ChatBannedRights](../types/ChatBannedRights.md)


### Example:

```php
$chatBannedRights = ['_' => 'chatBannedRights', 'view_messages' => Bool, 'send_messages' => Bool, 'send_media' => Bool, 'send_stickers' => Bool, 'send_gifs' => Bool, 'send_games' => Bool, 'send_inline' => Bool, 'embed_links' => Bool, 'send_polls' => Bool, 'change_info' => Bool, 'invite_users' => Bool, 'pin_messages' => Bool, 'until_date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatBannedRights", "view_messages": Bool, "send_messages": Bool, "send_media": Bool, "send_stickers": Bool, "send_gifs": Bool, "send_games": Bool, "send_inline": Bool, "embed_links": Bool, "send_polls": Bool, "change_info": Bool, "invite_users": Bool, "pin_messages": Bool, "until_date": int}
```


Or, if you're into Lua:

```lua
chatBannedRights={_='chatBannedRights', view_messages=Bool, send_messages=Bool, send_media=Bool, send_stickers=Bool, send_gifs=Bool, send_games=Bool, send_inline=Bool, embed_links=Bool, send_polls=Bool, change_info=Bool, invite_users=Bool, pin_messages=Bool, until_date=int}

```


