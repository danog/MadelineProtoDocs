---
title: messageFwdHeader
description: Forwarded message info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageFwdHeader  
[Back to constructors index](index.md)



Forwarded message info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|from\_id|[int](../types/int.md) | Optional|From ID|
|from\_name|[string](../types/string.md) | Optional|Author of the original message|
|date|[int](../types/int.md) | Yes|Date|
|channel\_id|[int](../types/int.md) | Optional|Channel ID|
|channel\_post|[int](../types/int.md) | Optional|Channel post|
|post\_author|[string](../types/string.md) | Optional|Post author|
|saved\_from\_peer|[Peer](../types/Peer.md) | Optional|Saved from peer|
|saved\_from\_msg\_id|[int](../types/int.md) | Optional|Saved from msg ID|



### Type: [MessageFwdHeader](../types/MessageFwdHeader.md)


### Example:

```php
$messageFwdHeader = ['_' => 'messageFwdHeader', 'from_id' => int, 'from_name' => 'string', 'date' => int, 'channel_id' => int, 'channel_post' => int, 'post_author' => 'string', 'saved_from_peer' => Peer, 'saved_from_msg_id' => int];
```  


Or, if you're into Lua:

```lua
messageFwdHeader={_='messageFwdHeader', from_id=int, from_name='string', date=int, channel_id=int, channel_post=int, post_author='string', saved_from_peer=Peer, saved_from_msg_id=int}

```


