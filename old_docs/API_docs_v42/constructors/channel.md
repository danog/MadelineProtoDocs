---
title: channel
description: Channel/supergroup info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channel  
[Back to constructors index](index.md)



Channel/supergroup info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](../types/Bool.md) | Optional|Whether the current user is the creator of this channel|
|kicked|[Bool](../types/Bool.md) | Optional|Kicked?|
|left|[Bool](../types/Bool.md) | Optional|Whether the current user has left this channel|
|editor|[Bool](../types/Bool.md) | Optional|Editor?|
|moderator|[Bool](../types/Bool.md) | Optional|Moderator?|
|broadcast|[Bool](../types/Bool.md) | Optional|Is this a channel?|
|verified|[Bool](../types/Bool.md) | Optional|Is this channel verified by telegram?|
|megagroup|[Bool](../types/Bool.md) | Optional|Is this a supergroup?|
|id|[int](../types/int.md) | Yes|ID of the channel|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|title|[string](../types/string.md) | Yes|Title|
|username|[string](../types/string.md) | Optional|Username|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Profile photo|
|date|[int](../types/int.md) | Yes|Creation date|
|version|[int](../types/int.md) | Yes|Version of the channel (always `0`)|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$channel = ['_' => 'channel', 'creator' => Bool, 'kicked' => Bool, 'left' => Bool, 'editor' => Bool, 'moderator' => Bool, 'broadcast' => Bool, 'verified' => Bool, 'megagroup' => Bool, 'id' => int, 'access_hash' => long, 'title' => 'string', 'username' => 'string', 'photo' => ChatPhoto, 'date' => int, 'version' => int];
```  


Or, if you're into Lua:

```lua
channel={_='channel', creator=Bool, kicked=Bool, left=Bool, editor=Bool, moderator=Bool, broadcast=Bool, verified=Bool, megagroup=Bool, id=int, access_hash=long, title='string', username='string', photo=ChatPhoto, date=int, version=int}

```


