---
title: "messageActionTopicCreate"
description: "A forum topic was created."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionTopicCreate  
[Back to constructors index](/API_docs/constructors/index.html)



A [forum topic](https://core.telegram.org/api/forum#forum-topics) was created.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Topic name.|
|icon\_color|[int](/API_docs/types/int.html) | Yes|If no custom emoji icon is specified, specifies the color of the fallback topic icon (RGB), one of `0x6FB9F0`, `0xFFD67E`, `0xCB86DB`, `0x8EEE98`, `0xFF93B2`, or `0xFB6F5F`.|
|icon\_emoji\_id|[long](/API_docs/types/long.html) | Optional|ID of the [custom emoji](https://core.telegram.org/api/custom-emoji) used as topic icon.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionTopicCreate = ['_' => 'messageActionTopicCreate', 'title' => 'string', 'icon_color' => int, 'icon_emoji_id' => long];
```  
