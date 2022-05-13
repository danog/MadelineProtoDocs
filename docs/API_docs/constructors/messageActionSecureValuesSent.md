---
title: "messageActionSecureValuesSent"
description: "Request for secure telegram passport values was sent"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSecureValuesSent  
[Back to constructors index](/API_docs/constructors/index.html)



Request for secure [telegram passport](https://core.telegram.org/passport) values was sent

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|types|Array of [SecureValueType](/API_docs/types/SecureValueType.html) | Yes|Secure value types|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionSecureValuesSent = ['_' => 'messageActionSecureValuesSent', 'types' => [SecureValueType, SecureValueType]];
```  
