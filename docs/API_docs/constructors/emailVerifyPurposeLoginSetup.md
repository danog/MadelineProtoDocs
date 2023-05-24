---
title: "emailVerifyPurposeLoginSetup"
description: "Email verification purpose: setup login email"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: emailVerifyPurposeLoginSetup  
[Back to constructors index](/API_docs/constructors/index.html)



Email verification purpose: setup login email

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](/API_docs/types/string.html) | Yes|Phone number|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Yes|Phone code hash as specified by the [documentation](https://core.telegram.org/api/auth#email-verification)|



### Type: [EmailVerifyPurpose](/API_docs/types/EmailVerifyPurpose.html)


### Example:

```
$emailVerifyPurposeLoginSetup = ['_' => 'emailVerifyPurposeLoginSetup', 'phone_number' => 'string', 'phone_code_hash' => 'string'];
```  
