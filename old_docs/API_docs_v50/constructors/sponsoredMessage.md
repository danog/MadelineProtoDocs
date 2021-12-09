---
title: sponsoredMessage
description: sponsoredMessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sponsoredMessage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|from\_id|[Peer](../types/Peer.md) | Yes|
|start\_param|[string](../types/string.md) | Optional|
|message|[string](../types/string.md) | Yes|
|entities|Array of [MessageEntity](../types/MessageEntity.md) | Optional|



### Type: [SponsoredMessage](../types/SponsoredMessage.md)


### Example:

```php
$sponsoredMessage = ['_' => 'sponsoredMessage', 'from_id' => Peer, 'start_param' => 'string', 'message' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  


Or, if you're into Lua:

```lua
sponsoredMessage={_='sponsoredMessage', from_id=Peer, start_param='string', message='string', entities={MessageEntity}}

```


