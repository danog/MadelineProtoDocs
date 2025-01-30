---
title: "auth.sentCodeTypeSmsPhrase"
description: "The code was sent via SMS as a secret phrase starting with the word specified in beginning"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeSmsPhrase.html
---
# Constructor: auth.sentCodeTypeSmsPhrase  
[Back to constructors index](/API_docs/constructors/index.html)



The code was sent via SMS as a secret phrase starting with the word specified in `beginning`

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|beginning|[string](/API_docs/types/string.html) | Optional|If set, the secret phrase (and the SMS) starts with this word.|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeSmsPhrase = ['_' => 'auth.sentCodeTypeSmsPhrase', 'beginning' => 'string'];
```  
