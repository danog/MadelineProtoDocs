---
title: "account.resetPasswordFailedWait"
description: "account.resetPasswordFailedWait attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_resetPasswordFailedWait.html
---
# Constructor: account.resetPasswordFailedWait  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|retry\_date|[int](../types/int.md) | Yes|



### Type: [account.ResetPasswordResult](../types/account.ResetPasswordResult.md)


### Example:

```php
$account_resetPasswordFailedWait = ['_' => 'account.resetPasswordFailedWait', 'retry_date' => int];
```  


Or, if you're into Lua:

```lua
account_resetPasswordFailedWait={_='account.resetPasswordFailedWait', retry_date=int}

```


