---
title: "account.webAuthorizations"
description: "Web authorizations"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_webAuthorizations.html
---
# Constructor: account.webAuthorizations  
[Back to constructors index](/API_docs/constructors/index.html)



Web authorizations

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorizations|Array of [WebAuthorization](/API_docs/types/WebAuthorization.html) | Yes|Web authorization list|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [account.WebAuthorizations](/API_docs/types/account.WebAuthorizations.html)


### Example:

```
$account_webAuthorizations = ['_' => 'account.webAuthorizations', 'authorizations' => [WebAuthorization, WebAuthorization], 'users' => [User, User]];
```  
