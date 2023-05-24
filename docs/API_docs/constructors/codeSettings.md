---
title: "codeSettings"
description: "Settings used by telegram servers for sending the confirm code."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: codeSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Settings used by telegram servers for sending the confirm code.

Example implementations: [telegram for android](https://github.com/DrKLO/Telegram/blob/master/TMessagesProj/src/main/java/org/telegram/ui/LoginActivity.java), [tdlib](https://github.com/tdlib/td/tree/master/td/telegram/SendCodeHelper.cpp).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|allow\_flashcall|[Bool](/API_docs/types/Bool.html) | Optional|Whether to allow phone verification via [phone calls](https://core.telegram.org/api/auth).|
|current\_number|[Bool](/API_docs/types/Bool.html) | Optional|Pass true if the phone number is used on the current device. Ignored if allow\_flashcall is not set.|
|allow\_app\_hash|[Bool](/API_docs/types/Bool.html) | Optional|If a token that will be included in eventually sent SMSs is required: required in newer versions of android, to use the [android SMS receiver APIs](https://developers.google.com/identity/sms-retriever/overview)|
|allow\_missed\_call|[Bool](/API_docs/types/Bool.html) | Optional|Whether this device supports receiving the code using the [auth.codeTypeMissedCall](../constructors/auth.codeTypeMissedCall.html) method|
|allow\_firebase|[Bool](/API_docs/types/Bool.html) | Optional|Whether Firebase auth is supported|
|logout\_tokens|Array of [bytes](/API_docs/types/bytes.html) | Optional|Previously stored future auth tokens, see [the documentation for more info »](https://core.telegram.org/api/auth#future-auth-tokens)|
|token|[string](/API_docs/types/string.html) | Optional|Used only by official iOS apps for Firebase auth: device token for apple push.|
|app\_sandbox|[Bool](/API_docs/types/Bool.html) | Optional|Used only by official iOS apps for firebase auth: whether a sandbox-certificate will be used during transmission of the push notification.|



### Type: [CodeSettings](/API_docs/types/CodeSettings.html)


### Example:

```
$codeSettings = ['_' => 'codeSettings', 'allow_flashcall' => Bool, 'current_number' => Bool, 'allow_app_hash' => Bool, 'allow_missed_call' => Bool, 'allow_firebase' => Bool, 'logout_tokens' => ['bytes', 'bytes'], 'token' => 'string', 'app_sandbox' => Bool];
```  
