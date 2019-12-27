---
title: messageActionSecureValuesSent
description: Request for secure [telegram passport](https://core.telegram.org/passport) values was sent
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSecureValuesSent  
[Back to constructors index](index.md)



Request for secure [telegram passport](https://core.telegram.org/passport) values was sent

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|types|Array of [SecureValueType](../types/SecureValueType.md) | Yes|Types|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionSecureValuesSent = ['_' => 'messageActionSecureValuesSent', 'types' => [SecureValueType, SecureValueType]];
```  


Or, if you're into Lua:

```lua
messageActionSecureValuesSent={_='messageActionSecureValuesSent', types={SecureValueType}}

```


