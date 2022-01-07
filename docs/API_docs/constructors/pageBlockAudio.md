---
title: "pageBlockAudio"
description: "Audio"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockAudio  
[Back to constructors index](/API_docs/constructors/index.md)



Audio

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|audio\_id|[long](/API_docs/types/long.md) | Yes|Audio ID (to be fetched from the container [page](../constructors/page.md) constructor|
|caption|[PageCaption](/API_docs/types/PageCaption.md) | Yes|Audio caption|



### Type: [PageBlock](/API_docs/types/PageBlock.md)


### Example:

```php
$pageBlockAudio = ['_' => 'pageBlockAudio', 'audio_id' => long, 'caption' => PageCaption];
```  
