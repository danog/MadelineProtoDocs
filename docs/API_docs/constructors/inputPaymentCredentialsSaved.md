---
title: "inputPaymentCredentialsSaved"
description: "Saved payment credentials"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPaymentCredentialsSaved  
[Back to constructors index](/API_docs/constructors/index.html)



Saved payment credentials

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.html) | Yes|Credential ID|
|tmp\_password|[bytes](/API_docs/types/bytes.html) | Yes|Temporary password|



### Type: [InputPaymentCredentials](/API_docs/types/InputPaymentCredentials.html)


### Example:

```
$inputPaymentCredentialsSaved = ['_' => 'inputPaymentCredentialsSaved', 'id' => 'string', 'tmp_password' => 'bytes'];
```  
