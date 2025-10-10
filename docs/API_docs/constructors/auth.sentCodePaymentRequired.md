---
title: "auth.sentCodePaymentRequired"
description: "Official apps may receive this constructor, indicating that due to the high cost of SMS verification codes for the user's country/provider, the user must purchase a Telegram Premium subscription in order to proceed with the login/signup."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodePaymentRequired.html
---
# Constructor: auth.sentCodePaymentRequired  
[Back to constructors index](/API_docs/constructors/index.html)



Official apps may receive this constructor, indicating that due to the high cost of SMS verification codes for the user's country/provider, the user must purchase a [Telegram Premium](https://core.telegram.org/api/premium) subscription in order to proceed with the login/signup.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|store\_product|[string](/API_docs/types/string.html) | Yes|Store identifier of the Telegram Premium subscription.|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Yes|Phone code hash, to be stored and later re-used with [auth.signIn](../methods/auth.signIn.html)|
|support\_email\_address|[string](/API_docs/types/string.html) | Yes|An email address that can be contacted for more information about this request.|
|support\_email\_subject|[string](/API_docs/types/string.html) | Yes|The mandatory subject for the email.|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|



### Type: [auth.SentCode](/API_docs/types/auth.SentCode.html)


### Example:

```
$auth_sentCodePaymentRequired = ['_' => 'auth.sentCodePaymentRequired', 'store_product' => 'string', 'phone_code_hash' => 'string', 'support_email_address' => 'string', 'support_email_subject' => 'string', 'currency' => 'string', 'amount' => long];
```  
