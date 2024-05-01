---
title: "inputPaymentCredentials"
description: "Payment credentials"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPaymentCredentials  
[Back to constructors index](/API_docs/constructors/index.html)



Payment credentials

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|save|[Bool](/API_docs/types/Bool.html) | Optional|Save payment credential for future use|
|data|[DataJSON](/API_docs/types/DataJSON.html) | Yes|Payment credentials|



### Type: [InputPaymentCredentials](/API_docs/types/InputPaymentCredentials.html)


### Example:

```
$inputPaymentCredentials = ['_' => 'inputPaymentCredentials', 'save' => Bool, 'data' => DataJSON];
```  
