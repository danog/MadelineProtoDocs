---
title: account.noPassword
description: account_noPassword attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.noPassword  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|new\_salt|[bytes](../types/bytes.md) | Yes|



### Type: [account\_Password](../types/account_Password.md)


### Example:

```
$account_noPassword = ['_' => 'account.noPassword', 'new_salt' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.noPassword", "new_salt": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:  


```
account_noPassword={_='account.noPassword', new_salt='bytes'}

```


