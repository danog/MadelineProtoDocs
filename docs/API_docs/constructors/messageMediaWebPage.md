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
|force\_large\_media|[Bool](/API_docs/types/Bool.html) | Optional|If set, specifies that a large media preview should be used.|
|force\_small\_media|[Bool](/API_docs/types/Bool.html) | Optional|If set, specifies that a small media preview should be used.|
|manual|[Bool](/API_docs/types/Bool.html) | Optional|If set, indicates that the URL used for the webpage preview was specified manually using [inputMediaWebPage](../constructors/inputMediaWebPage.html), and may not be related to any of the URLs specified in the message.|
|safe|[Bool](/API_docs/types/Bool.html) | Optional|If set, the webpage can be opened directly without user confirmation; otherwise, user confirmation is required, showing the exact URL that will be opened.|
|webpage|[WebPage](/API_docs/types/WebPage.html) | Optional|Webpage preview|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaWebPage = ['_' => 'messageMediaWebPage', 'force_large_media' => Bool, 'force_small_media' => Bool, 'manual' => Bool, 'safe' => Bool, 'webpage' => WebPage];
```  
