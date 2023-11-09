---
title: "webPagePending"
description: "A preview of the webpage is currently being generated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webPagePending  
[Back to constructors index](/API_docs/constructors/index.html)



A preview of the webpage is currently being generated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|ID of preview|
|url|[string](/API_docs/types/string.html) | Optional|
|date|[int](/API_docs/types/int.html) | Yes|When was the processing started|



### Type: [WebPage](/API_docs/types/WebPage.html)


### Example:

```
$webPagePending = ['_' => 'webPagePending', 'id' => long, 'url' => 'string', 'date' => int];
```  
