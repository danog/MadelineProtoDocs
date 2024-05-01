---
title: "auth.sentCodeSuccess"
description: "The user successfully authorized using future auth tokens"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeSuccess.html
---
# Constructor: auth.sentCodeSuccess  
[Back to constructors index](/API_docs/constructors/index.html)



The user successfully authorized using [future auth tokens](https://core.telegram.org/api/auth#future-auth-tokens)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorization|[auth.Authorization](/API_docs/constructors/auth.Authorization.html) | Yes|Authorization info|



### Type: [auth.SentCode](/API_docs/types/auth.SentCode.html)


### Example:

```
$auth_sentCodeSuccess = ['_' => 'auth.sentCodeSuccess', 'authorization' => auth.Authorization];
```  
