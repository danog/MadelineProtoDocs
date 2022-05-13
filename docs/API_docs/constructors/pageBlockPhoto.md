---
title: "pageBlockPhoto"
description: "A photo"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockPhoto  
[Back to constructors index](/API_docs/constructors/index.html)



A photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo\_id|[long](/API_docs/types/long.html) | Yes|Photo ID|
|caption|[PageCaption](/API_docs/types/PageCaption.html) | Yes|Caption|
|url|[string](/API_docs/types/string.html) | Optional|HTTP URL of page the photo leads to when clicked|
|webpage\_id|[long](/API_docs/types/long.html) | Optional|ID of preview of the page the photo leads to when clicked|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockPhoto = ['_' => 'pageBlockPhoto', 'photo_id' => long, 'caption' => PageCaption, 'url' => 'string', 'webpage_id' => long];
```  
