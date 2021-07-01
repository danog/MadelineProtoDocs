---
title: messageFwdHeader
description: Info about a forwarded message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageFwdHeader  
[Back to constructors index](index.md)



Info about a forwarded message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|from\_id|[int](../types/int.md) | Optional|
|from\_name|[string](../types/string.md) | Optional|The name of the user that originally sent the message|
|date|[int](../types/int.md) | Yes|When was the message originally sent|
|channel\_id|[int](../types/int.md) | Optional|
|channel\_post|[int](../types/int.md) | Optional|ID of the channel message that was forwarded|
|post\_author|[string](../types/string.md) | Optional|For channels and if signatures are enabled, author of the channel message|
|saved\_from\_peer|[Peer](../types/Peer.md) | Optional|Only for messages forwarded to the current user (inputPeerSelf), full info about the user/channel that originally sent the message|
|saved\_from\_msg\_id|[int](../types/int.md) | Optional|Only for messages forwarded to the current user (inputPeerSelf), ID of the message that was forwarded from the original user/channel|



### Type: [MessageFwdHeader](../types/MessageFwdHeader.md)


### Example:

```php
$messageFwdHeader = ['_' => 'messageFwdHeader', 'from_id' => int, 'from_name' => 'string', 'date' => int, 'channel_id' => int, 'channel_post' => int, 'post_author' => 'string', 'saved_from_peer' => Peer, 'saved_from_msg_id' => int];
```  


Or, if you're into Lua:

```lua
messageFwdHeader={_='messageFwdHeader', from_id=int, from_name='string', date=int, channel_id=int, channel_post=int, post_author='string', saved_from_peer=Peer, saved_from_msg_id=int}

```


