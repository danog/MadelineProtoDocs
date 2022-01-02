---
title: "keyboardButtonCallback"
description: "Callback button"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonCallback  
[Back to constructors index](index.md)



Callback button

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|requires\_password|[Bool](../types/Bool.md) | Optional|Whether the user should verify his identity by entering his [2FA SRP parameters](https://core.telegram.org/api/srp) to the [messages.getBotCallbackAnswer](../methods/messages.getBotCallbackAnswer.md) method. NOTE: telegram and the bot WILL NOT have access to the plaintext password, thanks to [SRP](https://core.telegram.org/api/srp). This button is mainly used by the official [@botfather](https://t.me/botfather) bot, for verifying the user's identity before transferring ownership of a bot to another user.|
|text|[string](../types/string.md) | Yes|Button text|
|data|[bytes](../types/bytes.md) | Yes|Callback data|



### Type: [KeyboardButton](../types/KeyboardButton.md)


### Example:

```php
$keyboardButtonCallback = ['_' => 'keyboardButtonCallback', 'requires_password' => Bool, 'text' => 'string', 'data' => 'bytes'];
```  


Or, if you're into Lua:

```lua
keyboardButtonCallback={_='keyboardButtonCallback', requires_password=Bool, text='string', data='bytes'}

```


