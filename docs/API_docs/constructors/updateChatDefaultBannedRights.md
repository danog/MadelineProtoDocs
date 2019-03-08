---
title: updateChatDefaultBannedRights
description: updateChatDefaultBannedRights attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatDefaultBannedRights  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](../types/Peer.md) | Yes|
|default\_banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Yes|
|version|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatDefaultBannedRights = ['_' => 'updateChatDefaultBannedRights', 'peer' => Peer, 'default_banned_rights' => ChatBannedRights, 'version' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChatDefaultBannedRights", "peer": Peer, "default_banned_rights": ChatBannedRights, "version": int}
```


Or, if you're into Lua:

```lua
updateChatDefaultBannedRights={_='updateChatDefaultBannedRights', peer=Peer, default_banned_rights=ChatBannedRights, version=int}

```


