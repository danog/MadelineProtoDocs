---
title: "updateChatDefaultBannedRights"
description: "Default banned rights in a normal chat were updated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatDefaultBannedRights  
[Back to constructors index](index.md)



Default banned rights in a [normal chat](https://core.telegram.org/api/channel) were updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|The chat|
|default\_banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Yes|New default banned rights|
|version|[int](../types/int.md) | Yes|Version|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatDefaultBannedRights = ['_' => 'updateChatDefaultBannedRights', 'peer' => Peer, 'default_banned_rights' => ChatBannedRights, 'version' => int];
```  


Or, if you're into Lua:

```lua
updateChatDefaultBannedRights={_='updateChatDefaultBannedRights', peer=Peer, default_banned_rights=ChatBannedRights, version=int}

```


