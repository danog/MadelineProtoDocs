---
title: "inputPaymentCredentials"
description: "Payment credentials"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPaymentCredentials  
[Back to constructors index](index.md)



Payment credentials

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|save|[Bool](../types/Bool.md) | Optional|Save payment credential for future use|
|data|[DataJSON](../types/DataJSON.md) | Yes|Payment credentials|



### Type: [InputPaymentCredentials](../types/InputPaymentCredentials.md)


### Example:

```php
$inputPaymentCredentials = ['_' => 'inputPaymentCredentials', 'save' => Bool, 'data' => DataJSON];
```  
