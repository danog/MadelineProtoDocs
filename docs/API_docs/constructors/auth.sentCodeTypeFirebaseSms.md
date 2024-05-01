---
title: "auth.sentCodeTypeFirebaseSms"
description: "An authentication code should be delivered via SMS after Firebase attestation, as described in the auth documentation »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeFirebaseSms.html
---
# Constructor: auth.sentCodeTypeFirebaseSms  
[Back to constructors index](/API_docs/constructors/index.html)



An authentication code should be delivered via SMS after Firebase attestation, as described in the [auth documentation »](https://core.telegram.org/api/auth).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|nonce|[bytes](/API_docs/types/bytes.html) | Optional|On Android, the nonce to be used as described in the [auth documentation »](https://core.telegram.org/api/auth)|
|receipt|[string](/API_docs/types/string.html) | Optional|On iOS, must be compared with the `receipt` extracted from the received push notification.|
|push\_timeout|[int](/API_docs/types/int.html) | Optional|On iOS: if a push notification with the `ios_push_secret` isn't received within `push_timeout` seconds, the `next_type` authentication method must be used, with [auth.resendCode](../methods/auth.resendCode.html).|
|length|[int](/API_docs/types/int.html) | Yes|Length of the code that will be delivered.|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeFirebaseSms = ['_' => 'auth.sentCodeTypeFirebaseSms', 'nonce' => 'bytes', 'receipt' => 'string', 'push_timeout' => int, 'length' => int];
```  
