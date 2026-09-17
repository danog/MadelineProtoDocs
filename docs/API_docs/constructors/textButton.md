---
title: "textButton"
description: "textButton attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textButton  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[RichText](/API_docs/types/RichText.html) | Yes|
|type|[InlineButtonType](/API_docs/types/InlineButtonType.html) | Yes|
|style|[RichButtonStyle](/API_docs/types/RichButtonStyle.html) | Optional|



### Type: [RichText](/API_docs/types/RichText.html)


### Example:

```
$textButton = ['_' => 'textButton', 'text' => RichText, 'type' => InlineButtonType, 'style' => RichButtonStyle];
```  
