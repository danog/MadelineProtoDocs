---
title: "auth.sentCodeTypeEmailCode"
description: "The code was sent via the previously configured login email »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeEmailCode.html
---
# Constructor: auth.sentCodeTypeEmailCode  
[Back to constructors index](/API_docs/constructors/index.html)



The code was sent via the [previously configured login email »](https://core.telegram.org/api/auth#email-verification)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|apple\_signin\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|Whether authorization through Apple ID is allowed|
|google\_signin\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|Whether authorization through Google ID is allowed|
|email\_pattern|[string](/API_docs/types/string.html) | Yes|[Pattern](https://core.telegram.org/api/pattern) of the email|
|length|[int](/API_docs/types/int.html) | Yes|Length of the sent verification code|
|reset\_available\_period|[int](/API_docs/types/int.html) | Optional|Clients should wait for the specified amount of seconds before allowing the user to invoke [auth.resetLoginEmail](../methods/auth.resetLoginEmail.html) (will be 0 for [Premium](https://core.telegram.org/api/premium) users).|
|reset\_pending\_date|[int](/API_docs/types/int.html) | Optional|An email reset was already requested, and will occur at the specified date.|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeEmailCode = ['_' => 'auth.sentCodeTypeEmailCode', 'apple_signin_allowed' => Bool, 'google_signin_allowed' => Bool, 'email_pattern' => 'string', 'length' => int, 'reset_available_period' => int, 'reset_pending_date' => int];
```  
