---
title: secureRequiredTypeOneOf
description: Secure required type one of
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureRequiredTypeOneOf  
[Back to constructors index](index.md)



Secure required type one of

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|types|Array of [SecureRequiredType](../types/SecureRequiredType.md) | Yes|Types|



### Type: [SecureRequiredType](../types/SecureRequiredType.md)


### Example:

```php
$secureRequiredTypeOneOf = ['_' => 'secureRequiredTypeOneOf', 'types' => [SecureRequiredType, SecureRequiredType]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureRequiredTypeOneOf", "types": [SecureRequiredType]}
```


Or, if you're into Lua:

```lua
secureRequiredTypeOneOf={_='secureRequiredTypeOneOf', types={SecureRequiredType}}

```


