---
title: "auth.sentCodeTypeApp"
description: "The code was sent through the telegram app"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeApp.html
---
# Constructor: auth.sentCodeTypeApp  
[Back to constructors index](/API_docs/constructors/index.html)



The code was sent through the telegram app

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|length|[int](/API_docs/types/int.html) | Yes|Length of the code in bytes|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeApp = ['_' => 'auth.sentCodeTypeApp', 'length' => int];
```  
