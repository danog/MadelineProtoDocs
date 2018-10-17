---
title: chatInvite
description: chatInvite attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInvite  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel|[Bool](../types/Bool.md) | Optional|
|broadcast|[Bool](../types/Bool.md) | Optional|
|public|[Bool](../types/Bool.md) | Optional|
|megagroup|[Bool](../types/Bool.md) | Optional|
|title|[string](../types/string.md) | Yes|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|
|participants\_count|[int](../types/int.md) | Yes|
|participants|Array of [User](../types/User.md) | Optional|



### Type: [ChatInvite](../types/ChatInvite.md)


### Example:

```php
$chatInvite = ['_' => 'chatInvite', 'channel' => Bool, 'broadcast' => Bool, 'public' => Bool, 'megagroup' => Bool, 'title' => 'string', 'photo' => ChatPhoto, 'participants_count' => int, 'participants' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatInvite", "channel": Bool, "broadcast": Bool, "public": Bool, "megagroup": Bool, "title": "string", "photo": ChatPhoto, "participants_count": int, "participants": [User]}
```


Or, if you're into Lua:

```lua
chatInvite={_='chatInvite', channel=Bool, broadcast=Bool, public=Bool, megagroup=Bool, title='string', photo=ChatPhoto, participants_count=int, participants={User}}

```


