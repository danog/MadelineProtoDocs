---
title: payments.paymentForm
description: Payment form
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_paymentForm.html
---
# Constructor: payments.paymentForm  
[Back to constructors index](index.md)



Payment form

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_save\_credentials|[Bool](../types/Bool.md) | Optional|Whether the user can choose to save credentials.|
|password\_missing|[Bool](../types/Bool.md) | Optional|Indicates that the user can save payment credentials, but only after setting up a [2FA password](https://core.telegram.org/api/srp) (currently the account doesn't have a [2FA password](https://core.telegram.org/api/srp))|
|bot\_id|[int](../types/int.md) | Yes|Bot ID|
|invoice|[Invoice](../types/Invoice.md) | Yes|Invoice|
|provider\_id|[int](../types/int.md) | Yes|Payment provider ID.|
|url|[string](../types/string.md) | Yes|Payment form URL|
|native\_provider|[string](../types/string.md) | Optional|Payment provider name.<br>One of the following:<br>\- `stripe`|
|native\_params|[DataJSON](../types/DataJSON.md) | Optional|Contains information about the payment provider, if available, to support it natively without the need for opening the URL.<br>A JSON object that can contain the following fields:<br><br>\- `publishable_key`: Stripe API publishable key<br>\- `apple_pay_merchant_id`: Apple Pay merchant ID<br>\- `android_pay_public_key`: Android Pay public key<br>\- `android_pay_bgcolor`: Android Pay form background color<br>\- `android_pay_inverse`: Whether to use the dark theme in the Android Pay form<br>\- `need_country`: True, if the user country must be provided,<br>\- `need_zip`: True, if the user ZIP/postal code must be provided,<br>\- `need_cardholder_name`: True, if the cardholder name must be provided<br>|
|saved\_info|[PaymentRequestedInfo](../types/PaymentRequestedInfo.md) | Optional|Saved server-side order information|
|saved\_credentials|[PaymentSavedCredentials](../types/PaymentSavedCredentials.md) | Optional|Contains information about saved card credentials|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [payments.PaymentForm](../types/payments.PaymentForm.md)


### Example:

```php
$payments.paymentForm = ['_' => 'payments.paymentForm', 'can_save_credentials' => Bool, 'password_missing' => Bool, 'bot_id' => int, 'invoice' => Invoice, 'provider_id' => int, 'url' => 'string', 'native_provider' => 'string', 'native_params' => DataJSON, 'saved_info' => PaymentRequestedInfo, 'saved_credentials' => PaymentSavedCredentials, 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
payments.paymentForm={_='payments.paymentForm', can_save_credentials=Bool, password_missing=Bool, bot_id=int, invoice=Invoice, provider_id=int, url='string', native_provider='string', native_params=DataJSON, saved_info=PaymentRequestedInfo, saved_credentials=PaymentSavedCredentials, users={User}}

```


