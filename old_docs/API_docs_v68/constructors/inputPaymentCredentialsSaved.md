---
title: inputPaymentCredentialsSaved
description: Payment credentials saved
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPaymentCredentialsSaved  
[Back to constructors index](index.md)



Payment credentials saved

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|ID|
|tmp\_password|[bytes](../types/bytes.md) | Yes|Tmp password|



### Type: [InputPaymentCredentials](../types/InputPaymentCredentials.md)


### Example:

```php
$inputPaymentCredentialsSaved = ['_' => 'inputPaymentCredentialsSaved', 'id' => 'string', 'tmp_password' => 'bytes'];
```  


Or, if you're into Lua:

```lua
inputPaymentCredentialsSaved={_='inputPaymentCredentialsSaved', id='string', tmp_password='bytes'}

```


