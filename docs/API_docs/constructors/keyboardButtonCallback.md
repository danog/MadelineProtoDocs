---
title: "keyboardButtonCallback"
description: "Callback button"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonCallback  
[Back to constructors index](/API_docs/constructors/index.html)



Callback button

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|requires\_password|[Bool](/API_docs/types/Bool.html) | Optional|Whether the user should verify his identity by entering his [2FA SRP parameters](https://core.telegram.org/api/srp) to the [messages.getBotCallbackAnswer](../methods/messages.getBotCallbackAnswer.html) method. NOTE: telegram and the bot WILL NOT have access to the plaintext password, thanks to [SRP](https://core.telegram.org/api/srp). This button is mainly used by the official [@botfather](https://t.me/botfather) bot, for verifying the user's identity before transferring ownership of a bot to another user.|
|text|[string](/API_docs/types/string.html) | Yes|Button text|
|data|[bytes](/API_docs/types/bytes.html) | Yes|Callback data|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.html)


### Example:

```
$keyboardButtonCallback = ['_' => 'keyboardButtonCallback', 'requires_password' => Bool, 'text' => 'string', 'data' => 'bytes'];
```  
