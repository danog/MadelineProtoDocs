---
title: codeSettings
description: Settings used by telegram servers for sending the confirm code.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: codeSettings  
[Back to constructors index](index.md)



Settings used by telegram servers for sending the confirm code.

Example implementations: [telegram for android](https://github.com/DrKLO/Telegram/blob/master/TMessagesProj/src/main/java/org/telegram/ui/LoginActivity.java), [tdlib](https://github.com/tdlib/td/tree/master/td/telegram/SendCodeHelper.cpp).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|allow\_flashcall|[Bool](../types/Bool.md) | Optional|Whether to allow phone verification via [phone calls](https://core.telegram.org/api/auth).|
|current\_number|[Bool](../types/Bool.md) | Optional|Pass true if the phone number is used on the current device. Ignored if allow\_flashcall is not set.|
|app\_hash\_persistent|[Bool](../types/Bool.md) | Optional|
|app\_hash|[string](../types/string.md) | Optional|



### Type: [CodeSettings](../types/CodeSettings.md)


### Example:

```php
$codeSettings = ['_' => 'codeSettings', 'allow_flashcall' => Bool, 'current_number' => Bool, 'app_hash_persistent' => Bool, 'app_hash' => 'string'];
```  


Or, if you're into Lua:

```lua
codeSettings={_='codeSettings', allow_flashcall=Bool, current_number=Bool, app_hash_persistent=Bool, app_hash='string'}

```


