---
title: "textPhone"
description: "Rich text linked to a phone number"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textPhone  
[Back to constructors index](/API_docs/constructors/index.html)



Rich text linked to a phone number

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](/API_docs/types/RichText.html) | Yes|Text|
|phone|[string](/API_docs/types/string.html) | Yes|Phone number|



### Type: [RichText](/API_docs/types/RichText.html)


### Example:

```
$textPhone = ['_' => 'textPhone', 'text' => RichText, 'phone' => 'string'];
```  
