---
title: inputPeerUserFromMessage
description: User from message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerUserFromMessage  
[Back to constructors index](index.md)



User from message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Optional|Chat|
|msg\_id|[int](../types/int.md) | Yes|Message ID|
|user\_id|[int](../types/int.md) | Yes|User ID|



### Type: [InputPeer](../types/InputPeer.md)


### Example:

```php
$inputPeerUserFromMessage = ['_' => 'inputPeerUserFromMessage', 'peer' => InputPeer, 'msg_id' => int, 'user_id' => int];
```  


Or, if you're into Lua:

```lua
inputPeerUserFromMessage={_='inputPeerUserFromMessage', peer=InputPeer, msg_id=int, user_id=int}

```


