---
title: secureRequiredType
description: Secure required type
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureRequiredType  
[Back to constructors index](index.md)



Secure required type

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|native\_names|[Bool](../types/Bool.md) | Optional|Native names?|
|selfie\_required|[Bool](../types/Bool.md) | Optional|Selfie required?|
|translation\_required|[Bool](../types/Bool.md) | Optional|Translation required?|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Type|



### Type: [SecureRequiredType](../types/SecureRequiredType.md)


### Example:

```php
$secureRequiredType = ['_' => 'secureRequiredType', 'native_names' => Bool, 'selfie_required' => Bool, 'translation_required' => Bool, 'type' => SecureValueType];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureRequiredType", "native_names": Bool, "selfie_required": Bool, "translation_required": Bool, "type": SecureValueType}
```


Or, if you're into Lua:

```lua
secureRequiredType={_='secureRequiredType', native_names=Bool, selfie_required=Bool, translation_required=Bool, type=SecureValueType}

```


