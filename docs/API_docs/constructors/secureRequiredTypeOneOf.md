---
title: "secureRequiredTypeOneOf"
description: "One of"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureRequiredTypeOneOf  
[Back to constructors index](index.md)



One of

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|types|Array of [SecureRequiredType](../types/SecureRequiredType.md) | Yes|Secure required value types|



### Type: [SecureRequiredType](../types/SecureRequiredType.md)


### Example:

```php
$secureRequiredTypeOneOf = ['_' => 'secureRequiredTypeOneOf', 'types' => [SecureRequiredType, SecureRequiredType]];
```  


Or, if you're into Lua:

```lua
secureRequiredTypeOneOf={_='secureRequiredTypeOneOf', types={SecureRequiredType}}

```


