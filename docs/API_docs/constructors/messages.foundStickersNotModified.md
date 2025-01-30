---
title: "messages.foundStickersNotModified"
description: "No new stickers were found for the specified query"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_foundStickersNotModified.html
---
# Constructor: messages.foundStickersNotModified  
[Back to constructors index](/API_docs/constructors/index.html)



No new stickers were found for the specified query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|next\_offset|[int](/API_docs/types/int.html) | Optional|Offset for [pagination](https://core.telegram.org/api/offsets)|



### Type: [messages.FoundStickers](/API_docs/types/messages.FoundStickers.html)


### Example:

```
$messages_foundStickersNotModified = ['_' => 'messages.foundStickersNotModified', 'next_offset' => int];
```  
