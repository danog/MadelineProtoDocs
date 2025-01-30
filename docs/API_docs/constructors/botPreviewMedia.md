---
title: "botPreviewMedia"
description: "Represents a Main Mini App preview media, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botPreviewMedia  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [Main Mini App preview media, see here »](https://core.telegram.org/api/bots/webapps#main-mini-app-previews) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](/API_docs/types/int.html) | Yes|When was this media last updated.|
|media|[MessageMedia](/API_docs/types/MessageMedia.html) | Optional|The actual photo/video.|



### Type: [BotPreviewMedia](/API_docs/types/BotPreviewMedia.html)


### Example:

```
$botPreviewMedia = ['_' => 'botPreviewMedia', 'date' => int, 'media' => MessageMedia];
```  
