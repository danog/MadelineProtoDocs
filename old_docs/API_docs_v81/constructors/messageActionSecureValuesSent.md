---
title: messageActionSecureValuesSent
description: messageActionSecureValuesSent attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSecureValuesSent  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|types|Array of [SecureValueType](../types/SecureValueType.md) | Yes|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```
$messageActionSecureValuesSent = ['_' => 'messageActionSecureValuesSent', 'types' => [SecureValueType, SecureValueType]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionSecureValuesSent", "types": [SecureValueType]}
```


Or, if you're into Lua:  


```
messageActionSecureValuesSent={_='messageActionSecureValuesSent', types={SecureValueType}}

```


