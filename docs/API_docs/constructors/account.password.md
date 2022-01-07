---
title: "account.password"
description: "Configuration for two-factor authorization"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_password.html
---
# Constructor: account.password  
[Back to constructors index](index.md)



Configuration for two-factor authorization

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_recovery|[Bool](../types/Bool.md) | Optional|Whether the user has a recovery method configured|
|has\_secure\_values|[Bool](../types/Bool.md) | Optional|Whether telegram [passport](https://core.telegram.org/passport) is enabled|
|has\_password|[Bool](../types/Bool.md) | Optional|Whether the user has a password|
|current\_algo|[PasswordKdfAlgo](../types/PasswordKdfAlgo.md) | Optional|The [KDF algorithm for SRP two-factor authentication](https://core.telegram.org/api/srp) of the current password|
|srp\_B|[bytes](../types/bytes.md) | Optional|Srp B param for [SRP authorization](https://core.telegram.org/api/srp)|
|srp\_id|[long](../types/long.md) | Optional|Srp ID param for [SRP authorization](https://core.telegram.org/api/srp)|
|hint|[string](../types/string.md) | Optional|Text hint for the password|
|email\_unconfirmed\_pattern|[string](../types/string.md) | Optional|A [password recovery email](https://core.telegram.org/api/srp#email-verification) with the specified [pattern](https://core.telegram.org/api/pattern) is still awaiting verification|
|new\_algo|[PasswordKdfAlgo](../types/PasswordKdfAlgo.md) | Yes|The [KDF algorithm for SRP two-factor authentication](https://core.telegram.org/api/srp) to use when creating new passwords|
|new\_secure\_algo|[SecurePasswordKdfAlgo](../types/SecurePasswordKdfAlgo.md) | Yes|The KDF algorithm for telegram [passport](https://core.telegram.org/passport)|
|secure\_random|[bytes](../types/bytes.md) | Yes|Secure random string|
|pending\_reset\_date|[int](../types/int.md) | Optional|



### Type: [account.Password](../types/account.Password.md)


### Example:

```php
$account_password = ['_' => 'account.password', 'has_recovery' => Bool, 'has_secure_values' => Bool, 'has_password' => Bool, 'current_algo' => PasswordKdfAlgo, 'srp_B' => 'bytes', 'srp_id' => long, 'hint' => 'string', 'email_unconfirmed_pattern' => 'string', 'new_algo' => PasswordKdfAlgo, 'new_secure_algo' => SecurePasswordKdfAlgo, 'secure_random' => 'bytes', 'pending_reset_date' => int];
```  
