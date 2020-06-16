---
title: inputPaymentCredentialsAndroidPay
description: Android pay payment credentials
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPaymentCredentialsAndroidPay  
[Back to constructors index](index.md)



Android pay payment credentials

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|payment\_token|[DataJSON](../types/DataJSON.md) | Yes|Android pay payment token|



### Type: [InputPaymentCredentials](../types/InputPaymentCredentials.md)


### Example:

```php
$inputPaymentCredentialsAndroidPay = ['_' => 'inputPaymentCredentialsAndroidPay', 'payment_token' => DataJSON];
```  


Or, if you're into Lua:

```lua
inputPaymentCredentialsAndroidPay={_='inputPaymentCredentialsAndroidPay', payment_token=DataJSON}

```


