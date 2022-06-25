---
title: "payments.paymentForm"
description: "Payment form"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_paymentForm.html
---
# Constructor: payments.paymentForm  
[Back to constructors index](/API_docs/constructors/index.html)



Payment form

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_save\_credentials|[Bool](/API_docs/types/Bool.html) | Optional|Whether the user can choose to save credentials.|
|password\_missing|[Bool](/API_docs/types/Bool.html) | Optional|Indicates that the user can save payment credentials, but only after setting up a [2FA password](https://core.telegram.org/api/srp) (currently the account doesn't have a [2FA password](https://core.telegram.org/api/srp))|
|form\_id|[long](/API_docs/types/long.html) | Yes|Form ID|
|bot\_id|[long](/API_docs/types/long.html) | Yes|Bot ID|
|title|[string](/API_docs/types/string.html) | Yes|
|description|[string](/API_docs/types/string.html) | Yes|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|
|invoice|[Invoice](/API_docs/types/Invoice.html) | Yes|Invoice|
|provider\_id|[long](/API_docs/types/long.html) | Yes|Payment provider ID.|
|url|[string](/API_docs/types/string.html) | Yes|Payment form URL|
|native\_provider|[string](/API_docs/types/string.html) | Optional|Payment provider name.<br>One of the following:<br>\- `stripe`|
|native\_params|[DataJSON](/API_docs/types/DataJSON.html) | Optional|Contains information about the payment provider, if available, to support it natively without the need for opening the URL.<br>A JSON object that can contain the following fields:<br><br>\- `apple_pay_merchant_id`: Apple Pay merchant ID<br>\- `google_pay_public_key`: Google Pay public key<br>\- `need_country`: True, if the user country must be provided,<br>\- `need_zip`: True, if the user ZIP/postal code must be provided,<br>\- `need_cardholder_name`: True, if the cardholder name must be provided<br>|
|saved\_info|[PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html) | Optional|Saved server-side order information|
|saved\_credentials|[PaymentSavedCredentials](/API_docs/types/PaymentSavedCredentials.html) | Optional|Contains information about saved card credentials|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [payments.PaymentForm](/API_docs/types/payments.PaymentForm.html)


### Example:

```
$payments_paymentForm = ['_' => 'payments.paymentForm', 'can_save_credentials' => Bool, 'password_missing' => Bool, 'form_id' => long, 'bot_id' => long, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'invoice' => Invoice, 'provider_id' => long, 'url' => 'string', 'native_provider' => 'string', 'native_params' => DataJSON, 'saved_info' => PaymentRequestedInfo, 'saved_credentials' => PaymentSavedCredentials, 'users' => [User, User]];
```  
