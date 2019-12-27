---
title: account.password
description: Configuration for two-factor authorization
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.password  
[Back to constructors index](index.md)



Configuration for two-factor authorization

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|current\_salt|[bytes](../types/bytes.md) | Yes|Current salt|
|new\_salt|[bytes](../types/bytes.md) | Yes|New salt|
|hint|[string](../types/string.md) | Yes|Text hint for the password|



### Type: [account\_Password](../types/account_Password.md)


### Example:

```php
$account_password = ['_' => 'account.password', 'current_salt' => 'bytes', 'new_salt' => 'bytes', 'hint' => 'string'];
```  


Or, if you're into Lua:

```lua
account_password={_='account.password', current_salt='bytes', new_salt='bytes', hint='string'}

```


