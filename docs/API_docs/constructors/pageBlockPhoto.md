---
title: "pageBlockPhoto"
description: "A photo"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockPhoto  
[Back to constructors index](/API_docs/constructors/index.md)



A photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo\_id|[long](/API_docs/types/long.md) | Yes|Photo ID|
|caption|[PageCaption](/API_docs/types/PageCaption.md) | Yes|Caption|
|url|[string](/API_docs/types/string.md) | Optional|HTTP URL of page the photo leads to when clicked|
|webpage\_id|[long](/API_docs/types/long.md) | Optional|ID of preview of the page the photo leads to when clicked|



### Type: [PageBlock](/API_docs/types/PageBlock.md)


### Example:

```php
$pageBlockPhoto = ['_' => 'pageBlockPhoto', 'photo_id' => long, 'caption' => PageCaption, 'url' => 'string', 'webpage_id' => long];
```  
