---
title: "account.password"
description: "Configuration for two-factor authorization"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_password.html
---
# Constructor: account.password  
[Back to constructors index](/API_docs/constructors/index.html)



Configuration for two-factor authorization

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_recovery|[Bool](/API_docs/types/Bool.html) | Optional|Whether the user has a recovery method configured|
|has\_secure\_values|[Bool](/API_docs/types/Bool.html) | Optional|Whether telegram [passport](https://core.telegram.org/passport) is enabled|
|has\_password|[Bool](/API_docs/types/Bool.html) | Optional|Whether the user has a password|
|current\_algo|[PasswordKdfAlgo](/API_docs/types/PasswordKdfAlgo.html) | Optional|The [KDF algorithm for SRP two-factor authentication](https://core.telegram.org/api/srp) of the current password|
|srp\_B|[bytes](/API_docs/types/bytes.html) | Optional|Srp B param for [SRP authorization](https://core.telegram.org/api/srp)|
|srp\_id|[long](/API_docs/types/long.html) | Optional|Srp ID param for [SRP authorization](https://core.telegram.org/api/srp)|
|hint|[string](/API_docs/types/string.html) | Optional|Text hint for the password|
|email\_unconfirmed\_pattern|[string](/API_docs/types/string.html) | Optional|A [password recovery email](https://core.telegram.org/api/srp#email-verification) with the specified [pattern](https://core.telegram.org/api/pattern) is still awaiting verification|
|new\_algo|[PasswordKdfAlgo](/API_docs/types/PasswordKdfAlgo.html) | Yes|The [KDF algorithm for SRP two-factor authentication](https://core.telegram.org/api/srp) to use when creating new passwords|
|new\_secure\_algo|[SecurePasswordKdfAlgo](/API_docs/types/SecurePasswordKdfAlgo.html) | Yes|The KDF algorithm for telegram [passport](https://core.telegram.org/passport)|
|secure\_random|[bytes](/API_docs/types/bytes.html) | Yes|Secure random string|
|pending\_reset\_date|[int](/API_docs/types/int.html) | Optional|The 2FA password will be automatically removed at this date, unless the user cancels the operation|



### Type: [account.Password](/API_docs/types/account.Password.html)


### Example:

```
$account_password = ['_' => 'account.password', 'has_recovery' => Bool, 'has_secure_values' => Bool, 'has_password' => Bool, 'current_algo' => PasswordKdfAlgo, 'srp_B' => 'bytes', 'srp_id' => long, 'hint' => 'string', 'email_unconfirmed_pattern' => 'string', 'new_algo' => PasswordKdfAlgo, 'new_secure_algo' => SecurePasswordKdfAlgo, 'secure_random' => 'bytes', 'pending_reset_date' => int];
```  
