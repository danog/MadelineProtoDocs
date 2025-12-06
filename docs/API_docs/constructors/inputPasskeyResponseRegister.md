---
title: "inputPasskeyResponseRegister"
description: "inputPasskeyResponseRegister attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPasskeyResponseRegister  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|client\_data|[DataJSON](/API_docs/types/DataJSON.html) | Yes|
|attestation\_data|[bytes](/API_docs/types/bytes.html) | Yes|



### Type: [InputPasskeyResponse](/API_docs/types/InputPasskeyResponse.html)


### Example:

```
$inputPasskeyResponseRegister = ['_' => 'inputPasskeyResponseRegister', 'client_data' => DataJSON, 'attestation_data' => 'bytes'];
```  
