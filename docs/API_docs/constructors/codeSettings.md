---
title: codeSettings
description: Code settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: codeSettings  
[Back to constructors index](index.md)



Code settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|allow\_flashcall|[Bool](../types/Bool.md) | Optional|Allow flashcal?|
|current\_number|[Bool](../types/Bool.md) | Optional|Current number?|
|app\_hash\_persistent|[Bool](../types/Bool.md) | Optional|Persistent hash?|
|app\_hash|[string](../types/string.md) | Optional|Hash type|



### Type: [CodeSettings](../types/CodeSettings.md)


### Example:

```php
$codeSettings = ['_' => 'codeSettings', 'allow_flashcall' => Bool, 'current_number' => Bool, 'app_hash_persistent' => Bool, 'app_hash' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "codeSettings", "allow_flashcall": Bool, "current_number": Bool, "app_hash_persistent": Bool, "app_hash": "string"}
```


Or, if you're into Lua:

```lua
codeSettings={_='codeSettings', allow_flashcall=Bool, current_number=Bool, app_hash_persistent=Bool, app_hash='string'}

```


