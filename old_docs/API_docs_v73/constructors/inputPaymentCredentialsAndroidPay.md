---
title: inputPaymentCredentialsAndroidPay
description: inputPaymentCredentialsAndroidPay attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: inputPaymentCredentialsAndroidPay  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|payment\_token|[DataJSON](../types/DataJSON.md) | Yes|



### Type: [InputPaymentCredentials](../types/InputPaymentCredentials.md)


### Example:

```
$inputPaymentCredentialsAndroidPay = ['_' => 'inputPaymentCredentialsAndroidPay', 'payment_token' => DataJSON];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputPaymentCredentialsAndroidPay", "payment_token": DataJSON}
```


Or, if you're into Lua:  


```
inputPaymentCredentialsAndroidPay={_='inputPaymentCredentialsAndroidPay', payment_token=DataJSON}

```


