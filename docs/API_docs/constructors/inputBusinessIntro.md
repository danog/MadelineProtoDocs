---
title: "inputBusinessIntro"
description: "Telegram Business introduction »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBusinessIntro  
[Back to constructors index](/API_docs/constructors/index.html)



[Telegram Business introduction »](https://core.telegram.org/api/business#business-introduction).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Title of the introduction message|
|description|[string](/API_docs/types/string.html) | Yes|Profile introduction|
|sticker|[MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.html) | Optional|Optional introduction [sticker](https://core.telegram.org/api/stickers).|



### Type: [InputBusinessIntro](/API_docs/types/InputBusinessIntro.html)


### Example:

```
$inputBusinessIntro = ['_' => 'inputBusinessIntro', 'title' => 'string', 'description' => 'string', 'sticker' => InputDocument];
```  
