---
title: inputNotifyPeer
description: Notify peer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputNotifyPeer  
[Back to constructors index](index.md)



Notify peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|Peer|



### Type: [InputNotifyPeer](../types/InputNotifyPeer.md)


### Example:

```php
$inputNotifyPeer = ['_' => 'inputNotifyPeer', 'peer' => InputPeer];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputNotifyPeer", "peer": InputPeer}
```


Or, if you're into Lua:

```lua
inputNotifyPeer={_='inputNotifyPeer', peer=InputPeer}

```


