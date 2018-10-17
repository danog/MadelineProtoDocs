---
title: msg_copy
description: msg_copy attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: msg\_copy  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|orig\_message|[MTMessage](../types/MTMessage.md) | Yes|



### Type: [MessageCopy](../types/MessageCopy.md)


### Example:

```php
$msg_copy = ['_' => 'msg_copy', 'orig_message' => MTMessage];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "msg_copy", "orig_message": MTMessage}
```


Or, if you're into Lua:

```lua
msg_copy={_='msg_copy', orig_message=MTMessage}

```


