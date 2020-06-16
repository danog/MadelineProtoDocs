---
title: account.noPassword
description: account.noPassword attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_noPassword.html
---
# Constructor: account.noPassword  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|new\_salt|[bytes](../types/bytes.md) | Yes|



### Type: [account.Password](../types/account.Password.md)


### Example:

```php
$account.noPassword = ['_' => 'account.noPassword', 'new_salt' => 'bytes'];
```  


Or, if you're into Lua:

```lua
account.noPassword={_='account.noPassword', new_salt='bytes'}

```


