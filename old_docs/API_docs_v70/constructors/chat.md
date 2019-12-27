---
title: chat
description: Info about a group
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chat  
[Back to constructors index](index.md)



Info about a group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](../types/Bool.md) | Optional|Whether the current user is the creator of the group|
|kicked|[Bool](../types/Bool.md) | Optional|Whether the current user was kicked from the group|
|left|[Bool](../types/Bool.md) | Optional|Whether the current user has left the group|
|admins\_enabled|[Bool](../types/Bool.md) | Optional|Admins enabled?|
|admin|[Bool](../types/Bool.md) | Optional|Admin?|
|deactivated|[Bool](../types/Bool.md) | Optional|Whether the group was [migrated](https://core.telegram.org/api/channel)|
|id|[int](../types/int.md) | Yes|ID of the group|
|title|[string](../types/string.md) | Yes|Title|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Chat photo|
|participants\_count|[int](../types/int.md) | Yes|Participant count|
|date|[int](../types/int.md) | Yes|Date of creation of the group|
|version|[int](../types/int.md) | Yes|Used in basic groups to reorder updates and make sure that all of them were received.|
|migrated\_to|[InputChannel](../types/InputChannel.md) | Optional|Means this chat was [upgraded](https://core.telegram.org/api/channel) to a supergroup|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$chat = ['_' => 'chat', 'creator' => Bool, 'kicked' => Bool, 'left' => Bool, 'admins_enabled' => Bool, 'admin' => Bool, 'deactivated' => Bool, 'id' => int, 'title' => 'string', 'photo' => ChatPhoto, 'participants_count' => int, 'date' => int, 'version' => int, 'migrated_to' => InputChannel];
```  


Or, if you're into Lua:

```lua
chat={_='chat', creator=Bool, kicked=Bool, left=Bool, admins_enabled=Bool, admin=Bool, deactivated=Bool, id=int, title='string', photo=ChatPhoto, participants_count=int, date=int, version=int, migrated_to=InputChannel}

```


