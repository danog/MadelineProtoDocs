---
title: "textUrl"
description: "Link"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textUrl  
[Back to constructors index](/API_docs/constructors/index.html)



Link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](/API_docs/types/RichText.html) | Yes|Text of link|
|url|[string](/API_docs/types/string.html) | Yes|Webpage HTTP URL|
|webpage\_id|[long](/API_docs/types/long.html) | Yes|If a preview was already generated for the page, the page ID|



### Type: [RichText](/API_docs/types/RichText.html)


### Example:

```
$textUrl = ['_' => 'textUrl', 'text' => RichText, 'url' => 'string', 'webpage_id' => long];
```  
