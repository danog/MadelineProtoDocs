---
title: "messageActionSecureValuesSentMe"
description: "Secure telegram passport values were received"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSecureValuesSentMe  
[Back to constructors index](/API_docs/constructors/index.html)



Secure [telegram passport](https://core.telegram.org/passport) values were received

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|values|Array of [SecureValue](/API_docs/types/SecureValue.html) | Yes|Vector with information about documents and other Telegram Passport elements that were shared with the bot|
|credentials|[SecureCredentialsEncrypted](/API_docs/types/SecureCredentialsEncrypted.html) | Yes|Encrypted credentials required to decrypt the data|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionSecureValuesSentMe = ['_' => 'messageActionSecureValuesSentMe', 'values' => [SecureValue, SecureValue], 'credentials' => SecureCredentialsEncrypted];
```  
