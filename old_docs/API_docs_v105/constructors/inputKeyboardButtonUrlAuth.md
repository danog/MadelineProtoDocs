---
title: inputKeyboardButtonUrlAuth
description: Request authorization
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputKeyboardButtonUrlAuth  
[Back to constructors index](index.md)



Request authorization

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|request\_write\_access|[Bool](../types/Bool.md) | Optional|Request write access?|
|text|[string](../types/string.md) | Yes|Text|
|fwd\_text|[string](../types/string.md) | Optional|Forward text|
|url|[string](../types/string.md) | Yes|URL|
|bot|[InputUser](../types/InputUser.md) | Optional|Bot|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$inputKeyboardButtonUrlAuth = ['_' => 'inputKeyboardButtonUrlAuth', 'request_write_access' => Bool, 'text' => 'string', 'fwd_text' => 'string', 'url' => 'string', 'bot' => InputUser];
```  


Or, if you're into Lua:

```lua
inputKeyboardButtonUrlAuth={_='inputKeyboardButtonUrlAuth', request_write_access=Bool, text='string', fwd_text='string', url='string', bot=InputUser}

```


