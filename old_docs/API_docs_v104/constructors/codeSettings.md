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
|allow\_app\_hash|[Bool](../types/Bool.md) | Optional||



### Type: [CodeSettings](../types/CodeSettings.md)


### Example:

```php
$codeSettings = ['_' => 'codeSettings', 'allow_flashcall' => Bool, 'current_number' => Bool, 'allow_app_hash' => Bool];
```  


Or, if you're into Lua:

```lua
codeSettings={_='codeSettings', allow_flashcall=Bool, current_number=Bool, allow_app_hash=Bool}

```


