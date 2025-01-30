---
title: "updateMessageExtendedMedia"
description: "You bought a paid media »: this update contains the revealed media."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessageExtendedMedia  
[Back to constructors index](/API_docs/constructors/index.html)



You [bought a paid media »](https://core.telegram.org/api/paid-media): this update contains the revealed media.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Peer where the paid media was posted|
|msg\_id|[int](/API_docs/types/int.html) | Yes|ID of the message containing the paid media|
|extended\_media|Array of [MessageExtendedMedia](/API_docs/types/MessageExtendedMedia.html) | Yes|Revealed media, contains only [messageExtendedMedia](../constructors/messageExtendedMedia.html) constructors.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMessageExtendedMedia = ['_' => 'updateMessageExtendedMedia', 'peer' => long, 'msg_id' => int, 'extended_media' => [MessageExtendedMedia, MessageExtendedMedia]];
```  
