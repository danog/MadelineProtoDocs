---
title: inputPaymentCredentialsSaved
description: inputPaymentCredentialsSaved attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPaymentCredentialsSaved  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[string](../types/string.md) | Yes|
|tmp\_password|[bytes](../types/bytes.md) | Yes|



### Type: [InputPaymentCredentials](../types/InputPaymentCredentials.md)


### Example:

```php
$inputPaymentCredentialsSaved = ['_' => 'inputPaymentCredentialsSaved', 'id' => 'string', 'tmp_password' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputPaymentCredentialsSaved", "id": "string", "tmp_password": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
inputPaymentCredentialsSaved={_='inputPaymentCredentialsSaved', id='string', tmp_password='bytes'}

```


