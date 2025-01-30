---
title: "businessIntro"
description: "Telegram Business introduction »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessIntro  
[Back to constructors index](/API_docs/constructors/index.html)



[Telegram Business introduction »](https://core.telegram.org/api/business#business-introduction).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Title of the introduction message (max [intro\_title\_length\_limit »](https://core.telegram.org/api/config#intro-title-length-limit) UTF-8 characters).|
|description|[string](/API_docs/types/string.html) | Yes|Profile introduction (max [intro\_description\_length\_limit »](https://core.telegram.org/api/config#intro-description-length-limit) UTF-8 characters).|
|sticker|[Document](/API_docs/types/Document.html) | Optional|Optional introduction [sticker](https://core.telegram.org/api/stickers).|



### Type: [BusinessIntro](/API_docs/types/BusinessIntro.html)


### Example:

```
$businessIntro = ['_' => 'businessIntro', 'title' => 'string', 'description' => 'string', 'sticker' => Document];
```  
