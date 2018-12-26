---
title: inputNotifyGeoChatPeer
description: Notify geo chat peer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputNotifyGeoChatPeer  
[Back to constructors index](index.md)



Notify geo chat peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | Yes|Peer|



### Type: [InputNotifyPeer](../types/InputNotifyPeer.md)


### Example:

```php
$inputNotifyGeoChatPeer = ['_' => 'inputNotifyGeoChatPeer', 'peer' => InputGeoChat];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputNotifyGeoChatPeer", "peer": InputGeoChat}
```


Or, if you're into Lua:

```lua
inputNotifyGeoChatPeer={_='inputNotifyGeoChatPeer', peer=InputGeoChat}

```


