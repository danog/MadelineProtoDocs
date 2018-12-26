---
title: inputPaymentCredentialsApplePay
description: Payment credentials apple pay
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPaymentCredentialsApplePay  
[Back to constructors index](index.md)



Payment credentials apple pay

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|payment\_data|[DataJSON](../types/DataJSON.md) | Yes|Payment data|



### Type: [InputPaymentCredentials](../types/InputPaymentCredentials.md)


### Example:

```php
$inputPaymentCredentialsApplePay = ['_' => 'inputPaymentCredentialsApplePay', 'payment_data' => DataJSON];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputPaymentCredentialsApplePay", "payment_data": DataJSON}
```


Or, if you're into Lua:

```lua
inputPaymentCredentialsApplePay={_='inputPaymentCredentialsApplePay', payment_data=DataJSON}

```


