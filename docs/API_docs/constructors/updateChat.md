---
title: "updateChat"
description: "Chat (chat and/or chatFull) information was updated."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChat  
[Back to constructors index](/API_docs/constructors/index.html)



Chat ([chat](../constructors/chat.html) and/or [chatFull](../constructors/chatFull.html)) information was updated.

This update can only be received through getDifference or in [updates](../constructors/updates.html)/[updatesCombined](../constructors/updatesCombined.html) constructors, so it will **always** come bundled with the updated [chat](../constructors/chat.html), that should be applied [as usual »](https://core.telegram.org/api/peers), **without** re-fetching the info manually.

However, full peer information will not come bundled in updates, so the full peer cache ([chatFull](../constructors/chatFull.html)) must be invalidated for `chat_id` when receiving this update.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|Chat ID|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChat = ['_' => 'updateChat', 'chat_id' => long];
```  
