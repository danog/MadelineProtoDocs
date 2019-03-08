---
title: messageActionSecureValuesSent
description: Message action secure values sent
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSecureValuesSent  
[Back to constructors index](index.md)



Message action secure values sent

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|types|Array of [SecureValueType](../types/SecureValueType.md) | Yes|Types|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionSecureValuesSent = ['_' => 'messageActionSecureValuesSent', 'types' => [SecureValueType, SecureValueType]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionSecureValuesSent", "types": [SecureValueType]}
```


Or, if you're into Lua:

```lua
messageActionSecureValuesSent={_='messageActionSecureValuesSent', types={SecureValueType}}

```


