---
title: "account.tmpPassword"
description: "Temporary payment password"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_tmpPassword.html
---
# Constructor: account.tmpPassword  
[Back to constructors index](/API_docs/constructors/index.html)



Temporary payment password

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|tmp\_password|[bytes](/API_docs/types/bytes.html) | Yes|Temporary password|
|valid\_until|[int](/API_docs/types/int.html) | Yes|Validity period|



### Type: [account.TmpPassword](/API_docs/types/account.TmpPassword.html)


### Example:

```
$account_tmpPassword = ['_' => 'account.tmpPassword', 'tmp_password' => 'bytes', 'valid_until' => int];
```  
