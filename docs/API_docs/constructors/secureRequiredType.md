---
title: "secureRequiredType"
description: "Required type"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureRequiredType  
[Back to constructors index](index.md)



Required type

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|native\_names|[Bool](../types/Bool.md) | Optional|Native names|
|selfie\_required|[Bool](../types/Bool.md) | Optional|Is a selfie required|
|translation\_required|[Bool](../types/Bool.md) | Optional|Is a translation required|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Secure value type|



### Type: [SecureRequiredType](../types/SecureRequiredType.md)


### Example:

```php
$secureRequiredType = ['_' => 'secureRequiredType', 'native_names' => Bool, 'selfie_required' => Bool, 'translation_required' => Bool, 'type' => SecureValueType];
```  


Or, if you're into Lua:

```lua
secureRequiredType={_='secureRequiredType', native_names=Bool, selfie_required=Bool, translation_required=Bool, type=SecureValueType}

```


