---
title: codeSettings
description: codeSettings attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: codeSettings  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|allow\_flashcall|[Bool](../types/Bool.md) | Optional|
|current\_number|[Bool](../types/Bool.md) | Optional|
|app\_hash\_persistent|[Bool](../types/Bool.md) | Optional|
|app\_hash|[string](../types/string.md) | Optional|



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


