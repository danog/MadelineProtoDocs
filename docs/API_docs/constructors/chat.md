---
title: chat
description: Chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chat  
[Back to constructors index](index.md)



Chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](../types/Bool.md) | Optional|Creator?|
|kicked|[Bool](../types/Bool.md) | Optional|Kicked?|
|left|[Bool](../types/Bool.md) | Optional|Left?|
|deactivated|[Bool](../types/Bool.md) | Optional|Deactivated?|
|id|[int](../types/int.md) | Yes|ID|
|title|[string](../types/string.md) | Yes|Title|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Photo|
|participants\_count|[int](../types/int.md) | Yes|Participants count|
|date|[int](../types/int.md) | Yes|Date|
|version|[int](../types/int.md) | Yes|Version|
|migrated\_to|[InputChannel](../types/InputChannel.md) | Optional|Migrated to|
|admin\_rights|[ChatAdminRights](../types/ChatAdminRights.md) | Optional||
|default\_banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Optional||



### Type: [Chat](../types/Chat.md)


### Example:

```php
$chat = ['_' => 'chat', 'creator' => Bool, 'kicked' => Bool, 'left' => Bool, 'deactivated' => Bool, 'id' => int, 'title' => 'string', 'photo' => ChatPhoto, 'participants_count' => int, 'date' => int, 'version' => int, 'migrated_to' => InputChannel, 'admin_rights' => ChatAdminRights, 'default_banned_rights' => ChatBannedRights];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chat", "creator": Bool, "kicked": Bool, "left": Bool, "deactivated": Bool, "id": int, "title": "string", "photo": ChatPhoto, "participants_count": int, "date": int, "version": int, "migrated_to": InputChannel, "admin_rights": ChatAdminRights, "default_banned_rights": ChatBannedRights}
```


Or, if you're into Lua:

```lua
chat={_='chat', creator=Bool, kicked=Bool, left=Bool, deactivated=Bool, id=int, title='string', photo=ChatPhoto, participants_count=int, date=int, version=int, migrated_to=InputChannel, admin_rights=ChatAdminRights, default_banned_rights=ChatBannedRights}

```


