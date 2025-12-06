---
title: "inputPasskeyResponseLogin"
description: "inputPasskeyResponseLogin attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPasskeyResponseLogin  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|client\_data|[DataJSON](/API_docs/types/DataJSON.html) | Yes|
|authenticator\_data|[bytes](/API_docs/types/bytes.html) | Yes|
|signature|[bytes](/API_docs/types/bytes.html) | Yes|
|user\_handle|[string](/API_docs/types/string.html) | Yes|



### Type: [InputPasskeyResponse](/API_docs/types/InputPasskeyResponse.html)


### Example:

```
$inputPasskeyResponseLogin = ['_' => 'inputPasskeyResponseLogin', 'client_data' => DataJSON, 'authenticator_data' => 'bytes', 'signature' => 'bytes', 'user_handle' => 'string'];
```  
