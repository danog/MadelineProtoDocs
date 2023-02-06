---
title: "auth.sentCodeTypeFirebaseSms"
description: "auth.sentCodeTypeFirebaseSms attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeFirebaseSms.html
---
# Constructor: auth.sentCodeTypeFirebaseSms  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|nonce|[bytes](/API_docs/types/bytes.html) | Optional|
|receipt|[string](/API_docs/types/string.html) | Optional|
|push\_timeout|[int](/API_docs/types/int.html) | Optional|
|length|[int](/API_docs/types/int.html) | Yes|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeFirebaseSms = ['_' => 'auth.sentCodeTypeFirebaseSms', 'nonce' => 'bytes', 'receipt' => 'string', 'push_timeout' => int, 'length' => int];
```  
