---
title: inputPaymentCredentialsAndroidPay
description: Payment credentials android pay
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPaymentCredentialsAndroidPay  
[Back to constructors index](index.md)



Payment credentials android pay

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|payment\_token|[DataJSON](../types/DataJSON.md) | Yes|Payment token|



### Type: [InputPaymentCredentials](../types/InputPaymentCredentials.md)


### Example:

```php
$inputPaymentCredentialsAndroidPay = ['_' => 'inputPaymentCredentialsAndroidPay', 'payment_token' => DataJSON];
```  


Or, if you're into Lua:

```lua
inputPaymentCredentialsAndroidPay={_='inputPaymentCredentialsAndroidPay', payment_token=DataJSON}

```


