---
title: "messageMediaDocument"
description: "Document (video, audio, voice, sticker, any media type except photo)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaDocument  
[Back to constructors index](/API_docs/constructors/index.html)



Document (video, audio, voice, sticker, any media type except photo)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|nopremium|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a normal sticker, if not set this is a premium sticker and a premium sticker animation must be played.|
|document|[Document](/API_docs/types/Document.html) | Optional|Attached document|
|ttl\_seconds|[int](/API_docs/types/int.html) | Optional|Time to live of self-destructing document|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaDocument = ['_' => 'messageMediaDocument', 'nopremium' => Bool, 'document' => Document, 'ttl_seconds' => int];
```  
