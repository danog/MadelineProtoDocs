---
title: "textEmail"
description: "Rich text email link"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textEmail  
[Back to constructors index](/API_docs/constructors/index.html)



Rich text email link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](/API_docs/types/RichText.html) | Yes|Link text|
|email|[string](/API_docs/types/string.html) | Yes|Email address|



### Type: [RichText](/API_docs/types/RichText.html)


### Example:

```
$textEmail = ['_' => 'textEmail', 'text' => RichText, 'email' => 'string'];
```  
