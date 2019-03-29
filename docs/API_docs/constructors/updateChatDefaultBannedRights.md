---
title: updateChatDefaultBannedRights
description: Global chat rights updated
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatDefaultBannedRights  
[Back to constructors index](index.md)



Global chat rights updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|default\_banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Yes|Global chat rights|
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


