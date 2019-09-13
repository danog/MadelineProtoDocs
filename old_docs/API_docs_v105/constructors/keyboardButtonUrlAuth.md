---
title: keyboardButtonUrlAuth
description: Url authorization request
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonUrlAuth  
[Back to constructors index](index.md)



Url authorization request

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](../types/string.md) | Yes|Text|
|fwd\_text|[string](../types/string.md) | Optional|Forward text|
|url|[string](../types/string.md) | Yes|URL|
|button\_id|[int](../types/int.md) | Yes|Button ID|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$keyboardButtonUrlAuth = ['_' => 'keyboardButtonUrlAuth', 'text' => 'string', 'fwd_text' => 'string', 'url' => 'string', 'button_id' => int];
```  


Or, if you're into Lua:

```lua
keyboardButtonUrlAuth={_='keyboardButtonUrlAuth', text='string', fwd_text='string', url='string', button_id=int}

```


