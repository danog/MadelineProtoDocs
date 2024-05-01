---
title: "updateWebPage"
description: "An instant view webpage preview was generated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateWebPage  
[Back to constructors index](/API_docs/constructors/index.html)



An [instant view](https://instantview.telegram.org) webpage preview was generated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|webpage|[WebPage](/API_docs/types/WebPage.html) | Optional|Webpage preview|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateWebPage = ['_' => 'updateWebPage', 'webpage' => WebPage, 'pts' => int, 'pts_count' => int];
```  
