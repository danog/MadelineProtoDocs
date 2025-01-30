---
title: "auth.sentCodeTypeSmsWord"
description: "The code was sent via SMS as a secret word, starting with the letter specified in beginning"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeSmsWord.html
---
# Constructor: auth.sentCodeTypeSmsWord  
[Back to constructors index](/API_docs/constructors/index.html)



The code was sent via SMS as a secret word, starting with the letter specified in `beginning`

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|beginning|[string](/API_docs/types/string.html) | Optional|If set, the secret word in the sent SMS (which may contain multiple words) starts with this letter.|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeSmsWord = ['_' => 'auth.sentCodeTypeSmsWord', 'beginning' => 'string'];
```  
