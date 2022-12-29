---
title: "inputMediaPhoto"
description: "Forwarded photo"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPhoto  
[Back to constructors index](/API_docs/constructors/index.html)



Forwarded photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|spoiler|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[MessageMedia, Message, Update or InputPhoto](/API_docs/types/InputPhoto.html) | Optional|Photo to be forwarded|
|ttl\_seconds|[int](/API_docs/types/int.html) | Optional|Time to live in seconds of self-destructing photo|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaPhoto = ['_' => 'inputMediaPhoto', 'spoiler' => Bool, 'id' => InputPhoto, 'ttl_seconds' => int];
```  
