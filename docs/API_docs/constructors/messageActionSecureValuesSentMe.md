---
title: messageActionSecureValuesSentMe
description: messageActionSecureValuesSentMe attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSecureValuesSentMe  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|values|Array of [SecureValue](../types/SecureValue.md) | Yes|
|credentials|[SecureCredentialsEncrypted](../types/SecureCredentialsEncrypted.md) | Yes|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```
$messageActionSecureValuesSentMe = ['_' => 'messageActionSecureValuesSentMe', 'values' => [SecureValue, SecureValue], 'credentials' => SecureCredentialsEncrypted];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionSecureValuesSentMe", "values": [SecureValue], "credentials": SecureCredentialsEncrypted}
```


Or, if you're into Lua:  


```
messageActionSecureValuesSentMe={_='messageActionSecureValuesSentMe', values={SecureValue}, credentials=SecureCredentialsEncrypted}

```


