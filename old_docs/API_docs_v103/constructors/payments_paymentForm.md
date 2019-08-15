---
title: payments.paymentForm
description: Payment form
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: payments.paymentForm  
[Back to constructors index](index.md)



Payment form

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_save\_credentials|[Bool](../types/Bool.md) | Optional|Can save credentials?|
|password\_missing|[Bool](../types/Bool.md) | Optional|Password missing?|
|bot\_id|[int](../types/int.md) | Yes|Bot ID|
|invoice|[Invoice](../types/Invoice.md) | Yes|Invoice|
|provider\_id|[int](../types/int.md) | Yes|Provider ID|
|url|[string](../types/string.md) | Yes|URL|
|native\_provider|[string](../types/string.md) | Optional|Native provider|
|native\_params|[DataJSON](../types/DataJSON.md) | Optional|Native params|
|saved\_info|[PaymentRequestedInfo](../types/PaymentRequestedInfo.md) | Optional|Saved info|
|saved\_credentials|[PaymentSavedCredentials](../types/PaymentSavedCredentials.md) | Optional|Saved credentials|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [payments\_PaymentForm](../types/payments_PaymentForm.md)


### Example:

```php
$payments_paymentForm = ['_' => 'payments.paymentForm', 'can_save_credentials' => Bool, 'password_missing' => Bool, 'bot_id' => int, 'invoice' => Invoice, 'provider_id' => int, 'url' => 'string', 'native_provider' => 'string', 'native_params' => DataJSON, 'saved_info' => PaymentRequestedInfo, 'saved_credentials' => PaymentSavedCredentials, 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
payments_paymentForm={_='payments.paymentForm', can_save_credentials=Bool, password_missing=Bool, bot_id=int, invoice=Invoice, provider_id=int, url='string', native_provider='string', native_params=DataJSON, saved_info=PaymentRequestedInfo, saved_credentials=PaymentSavedCredentials, users={User}}

```


