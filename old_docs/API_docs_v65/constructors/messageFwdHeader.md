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
|date|[int](../types/int.md) | Yes|Date|
|channel\_id|[int](../types/int.md) | Optional|Channel ID|
|channel\_post|[int](../types/int.md) | Optional|Channel post|



### Type: [MessageFwdHeader](../types/MessageFwdHeader.md)


### Example:

```php
$messageFwdHeader = ['_' => 'messageFwdHeader', 'from_id' => int, 'date' => int, 'channel_id' => int, 'channel_post' => int];
```  


Or, if you're into Lua:

```lua
messageFwdHeader={_='messageFwdHeader', from_id=int, date=int, channel_id=int, channel_post=int}

```


