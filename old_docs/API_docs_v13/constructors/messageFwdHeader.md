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
|from\_id|[int](../types/int.md) | Optional|The ID of the user that originally sent the message|
|date|[int](../types/int.md) | Yes|When was the message originally sent|
|channel\_id|[int](../types/int.md) | Optional|ID of the channel from which the message was forwarded|
|channel\_post|[int](../types/int.md) | Optional|ID of the channel message that was forwarded|



### Type: [MessageFwdHeader](../types/MessageFwdHeader.md)


### Example:

```php
$messageFwdHeader = ['_' => 'messageFwdHeader', 'from_id' => int, 'date' => int, 'channel_id' => int, 'channel_post' => int];
```  


Or, if you're into Lua:

```lua
messageFwdHeader={_='messageFwdHeader', from_id=int, date=int, channel_id=int, channel_post=int}

```


