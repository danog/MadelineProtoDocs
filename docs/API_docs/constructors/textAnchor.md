---
title: "textAnchor"
description: "Text linking to another section of the page"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textAnchor  
[Back to constructors index](/API_docs/constructors/index.html)



Text linking to another section of the page

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](/API_docs/types/RichText.html) | Yes|Text|
|name|[string](/API_docs/types/string.html) | Yes|Section name|



### Type: [RichText](/API_docs/types/RichText.html)


### Example:

```
$textAnchor = ['_' => 'textAnchor', 'text' => RichText, 'name' => 'string'];
```  
