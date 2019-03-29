---
title: channel
description: Channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channel  
[Back to constructors index](index.md)



Channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](../types/Bool.md) | Optional|Creator?|
|kicked|[Bool](../types/Bool.md) | Optional|Kicked?|
|left|[Bool](../types/Bool.md) | Optional|Left?|
|editor|[Bool](../types/Bool.md) | Optional|Editor?|
|moderator|[Bool](../types/Bool.md) | Optional|Moderator?|
|broadcast|[Bool](../types/Bool.md) | Optional|Broadcast?|
|verified|[Bool](../types/Bool.md) | Optional|Verified?|
|megagroup|[Bool](../types/Bool.md) | Optional|Megagroup?|
|id|[int](../types/int.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|title|[string](../types/string.md) | Yes|Title|
|username|[string](../types/string.md) | Optional|Username|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Photo|
|date|[int](../types/int.md) | Yes|Date|
|version|[int](../types/int.md) | Yes|Version|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$channel = ['_' => 'channel', 'creator' => Bool, 'kicked' => Bool, 'left' => Bool, 'editor' => Bool, 'moderator' => Bool, 'broadcast' => Bool, 'verified' => Bool, 'megagroup' => Bool, 'id' => int, 'access_hash' => long, 'title' => 'string', 'username' => 'string', 'photo' => ChatPhoto, 'date' => int, 'version' => int];
```  


Or, if you're into Lua:

```lua
channel={_='channel', creator=Bool, kicked=Bool, left=Bool, editor=Bool, moderator=Bool, broadcast=Bool, verified=Bool, megagroup=Bool, id=int, access_hash=long, title='string', username='string', photo=ChatPhoto, date=int, version=int}

```


