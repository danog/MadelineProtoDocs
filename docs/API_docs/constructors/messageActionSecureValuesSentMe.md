---
title: "messageActionSecureValuesSentMe"
description: "Secure telegram passport values were received"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSecureValuesSentMe  
[Back to constructors index](index.md)



Secure [telegram passport](https://core.telegram.org/passport) values were received

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|values|Array of [SecureValue](../types/SecureValue.md) | Yes|Vector with information about documents and other Telegram Passport elements that were shared with the bot|
|credentials|[SecureCredentialsEncrypted](../types/SecureCredentialsEncrypted.md) | Yes|Encrypted credentials required to decrypt the data|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionSecureValuesSentMe = ['_' => 'messageActionSecureValuesSentMe', 'values' => [SecureValue, SecureValue], 'credentials' => SecureCredentialsEncrypted];
```  


Or, if you're into Lua:

```lua
messageActionSecureValuesSentMe={_='messageActionSecureValuesSentMe', values={SecureValue}, credentials=SecureCredentialsEncrypted}

```


