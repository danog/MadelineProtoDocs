---
title: channelBannedRights
description: Banned user rights (when true, the user will NOT be able to do that thing)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelBannedRights  
[Back to constructors index](index.md)



Banned user rights (when true, the user will NOT be able to do that thing)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|view\_messages|[Bool](../types/Bool.md) | Optional|Disallow viewing messages|
|send\_messages|[Bool](../types/Bool.md) | Optional|Disallow sending messages|
|send\_media|[Bool](../types/Bool.md) | Optional|Disallow sending media|
|send\_stickers|[Bool](../types/Bool.md) | Optional|Disallow sending stickers|
|send\_gifs|[Bool](../types/Bool.md) | Optional|Disallow sending gifs|
|send\_games|[Bool](../types/Bool.md) | Optional|Disallow sending games|
|send\_inline|[Bool](../types/Bool.md) | Optional|Disallow sending inline keyboards|
|embed\_links|[Bool](../types/Bool.md) | Optional|Disallow embedding links|
|until\_date|[int](../types/int.md) | Yes|Until date|



### Type: [ChannelBannedRights](../types/ChannelBannedRights.md)


### Example:

```php
$channelBannedRights = ['_' => 'channelBannedRights', 'view_messages' => Bool, 'send_messages' => Bool, 'send_media' => Bool, 'send_stickers' => Bool, 'send_gifs' => Bool, 'send_games' => Bool, 'send_inline' => Bool, 'embed_links' => Bool, 'until_date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelBannedRights", "view_messages": Bool, "send_messages": Bool, "send_media": Bool, "send_stickers": Bool, "send_gifs": Bool, "send_games": Bool, "send_inline": Bool, "embed_links": Bool, "until_date": int}
```


Or, if you're into Lua:

```lua
channelBannedRights={_='channelBannedRights', view_messages=Bool, send_messages=Bool, send_media=Bool, send_stickers=Bool, send_gifs=Bool, send_games=Bool, send_inline=Bool, embed_links=Bool, until_date=int}

```


