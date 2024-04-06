---
title: "inputBusinessIntro"
description: "inputBusinessIntro attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBusinessIntro  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](/API_docs/types/string.html) | Yes|
|description|[string](/API_docs/types/string.html) | Yes|
|sticker|[MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.html) | Optional|



### Type: [InputBusinessIntro](/API_docs/types/InputBusinessIntro.html)


### Example:

```
$inputBusinessIntro = ['_' => 'inputBusinessIntro', 'title' => 'string', 'description' => 'string', 'sticker' => InputDocument];
```  
