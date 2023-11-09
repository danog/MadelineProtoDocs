---
title: "messageMediaWebPage"
description: "Preview of webpage"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaWebPage  
[Back to constructors index](/API_docs/constructors/index.html)



Preview of webpage

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|force\_large\_media|[Bool](/API_docs/types/Bool.html) | Optional|
|force\_small\_media|[Bool](/API_docs/types/Bool.html) | Optional|
|manual|[Bool](/API_docs/types/Bool.html) | Optional|
|safe|[Bool](/API_docs/types/Bool.html) | Optional|
|webpage|[WebPage](/API_docs/types/WebPage.html) | Optional|Webpage preview|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaWebPage = ['_' => 'messageMediaWebPage', 'force_large_media' => Bool, 'force_small_media' => Bool, 'manual' => Bool, 'safe' => Bool, 'webpage' => WebPage];
```  
