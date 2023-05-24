---
title: "auth.sentCodeTypeFragmentSms"
description: "The code was delivered via fragment.com."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeFragmentSms.html
---
# Constructor: auth.sentCodeTypeFragmentSms  
[Back to constructors index](/API_docs/constructors/index.html)



The code was delivered via [fragment.com](https://fragment.com).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|Open the specified URL to log into [fragment.com](https://fragment.com) with the wallet that owns the specified phone number and view the code.|
|length|[int](/API_docs/types/int.html) | Yes|Length of the delivered code.|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeFragmentSms = ['_' => 'auth.sentCodeTypeFragmentSms', 'url' => 'string', 'length' => int];
```  
