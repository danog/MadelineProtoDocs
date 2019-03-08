---
title: chatBannedRights
description: Banned rights (when true, the user will NOT be able to do that thing)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatBannedRights  
[Back to constructors index](index.md)



Banned rights (when true, the user will NOT be able to do that thing)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|view\_messages|[Bool](../types/Bool.md) | Optional|Can view messages?|
|send\_messages|[Bool](../types/Bool.md) | Optional|Can send messages?|
|send\_media|[Bool](../types/Bool.md) | Optional|Can send media?|
|send\_stickers|[Bool](../types/Bool.md) | Optional|Can send stickers?|
|send\_gifs|[Bool](../types/Bool.md) | Optional|Can send gifs?|
|send\_games|[Bool](../types/Bool.md) | Optional|Can send games?|
|send\_inline|[Bool](../types/Bool.md) | Optional|Can use inline bots?|
|embed\_links|[Bool](../types/Bool.md) | Optional|Can embed links?|
|send\_polls|[Bool](../types/Bool.md) | Optional|Can send polls?|
|change\_info|[Bool](../types/Bool.md) | Optional|Can change info?|
|invite\_users|[Bool](../types/Bool.md) | Optional|Can invite users?|
|pin\_messages|[Bool](../types/Bool.md) | Optional|Can pin messages?|
|until\_date|[int](../types/int.md) | Yes|Until date (0 = forever)|



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


