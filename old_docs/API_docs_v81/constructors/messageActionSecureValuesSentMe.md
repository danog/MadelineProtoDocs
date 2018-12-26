---
title: messageActionSecureValuesSentMe
description: Message action secure values sent me
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSecureValuesSentMe  
[Back to constructors index](index.md)



Message action secure values sent me

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|values|Array of [SecureValue](../types/SecureValue.md) | Yes|Values|
|credentials|[SecureCredentialsEncrypted](../types/SecureCredentialsEncrypted.md) | Yes|Credentials|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionSecureValuesSentMe = ['_' => 'messageActionSecureValuesSentMe', 'values' => [SecureValue, SecureValue], 'credentials' => SecureCredentialsEncrypted];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionSecureValuesSentMe", "values": [SecureValue], "credentials": SecureCredentialsEncrypted}
```


Or, if you're into Lua:

```lua
messageActionSecureValuesSentMe={_='messageActionSecureValuesSentMe', values={SecureValue}, credentials=SecureCredentialsEncrypted}

```


