---
title: error
description: Error
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: error  
[Back to constructors index](index.md)



Error

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|code|[int](../types/int.md) | Yes|Code|
|text|[string](../types/string.md) | Yes|Text|



### Type: [Error](../types/Error.md)


### Example:

```php
$error = ['_' => 'error', 'code' => int, 'text' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "error", "code": int, "text": "string"}
```


Or, if you're into Lua:

```lua
error={_='error', code=int, text='string'}

```


