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



### Type: [MessageFwdHeader](../types/MessageFwdHeader.md)


### Example:

```php
$messageFwdHeader = ['_' => 'messageFwdHeader', 'from_id' => int, 'date' => int, 'channel_id' => int, 'channel_post' => int, 'post_author' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageFwdHeader", "from_id": int, "date": int, "channel_id": int, "channel_post": int, "post_author": "string"}
```


Or, if you're into Lua:

```lua
messageFwdHeader={_='messageFwdHeader', from_id=int, date=int, channel_id=int, channel_post=int, post_author='string'}

```


