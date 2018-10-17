---
title: messageFwdHeader
description: messageFwdHeader attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageFwdHeader  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|from\_id|[int](../types/int.md) | Optional|
|date|[int](../types/int.md) | Yes|
|channel\_id|[int](../types/int.md) | Optional|
|channel\_post|[int](../types/int.md) | Optional|
|post\_author|[string](../types/string.md) | Optional|
|saved\_from\_peer|[Peer](../types/Peer.md) | Optional|
|saved\_from\_msg\_id|[int](../types/int.md) | Optional|



### Type: [MessageFwdHeader](../types/MessageFwdHeader.md)


### Example:

```php
$messageFwdHeader = ['_' => 'messageFwdHeader', 'from_id' => int, 'date' => int, 'channel_id' => int, 'channel_post' => int, 'post_author' => 'string', 'saved_from_peer' => Peer, 'saved_from_msg_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageFwdHeader", "from_id": int, "date": int, "channel_id": int, "channel_post": int, "post_author": "string", "saved_from_peer": Peer, "saved_from_msg_id": int}
```


Or, if you're into Lua:

```lua
messageFwdHeader={_='messageFwdHeader', from_id=int, date=int, channel_id=int, channel_post=int, post_author='string', saved_from_peer=Peer, saved_from_msg_id=int}

```


