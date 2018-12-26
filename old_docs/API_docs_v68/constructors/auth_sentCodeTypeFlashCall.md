---
title: auth.sentCodeTypeFlashCall
description: Sent code type flash call
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.sentCodeTypeFlashCall  
[Back to constructors index](index.md)



Sent code type flash call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pattern|[string](../types/string.md) | Yes|Pattern|



### Type: [auth\_SentCodeType](../types/auth_SentCodeType.md)


### Example:

```php
$auth_sentCodeTypeFlashCall = ['_' => 'auth.sentCodeTypeFlashCall', 'pattern' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "auth.sentCodeTypeFlashCall", "pattern": "string"}
```


Or, if you're into Lua:

```lua
auth_sentCodeTypeFlashCall={_='auth.sentCodeTypeFlashCall', pattern='string'}

```


