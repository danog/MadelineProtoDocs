---
title: "updateChannelViewForumAsMessages"
description: "Users may also choose to display messages from all topics as if they were sent to a normal group, using a 'View as messages' setting in the local client."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelViewForumAsMessages  
[Back to constructors index](/API_docs/constructors/index.html)



Users may also choose to display messages from all topics as if they were sent to a normal group, using a "View as messages" setting in the local client.  
This setting only affects the current account, and is synced to other logged in sessions using the [channels.toggleViewForumAsMessages](../methods/channels.toggleViewForumAsMessages.html) method; invoking this method will update the value of the `view_forum_as_messages` flag of [channelFull](../constructors/channelFull.html) or [dialog](../constructors/dialog.html) and emit an [updateChannelViewForumAsMessages](../constructors/updateChannelViewForumAsMessages.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|The forum ID|
|enabled|[Bool](/API_docs/types/Bool.html) | Yes|The new value of the toggle.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelViewForumAsMessages = ['_' => 'updateChannelViewForumAsMessages', 'channel_id' => long, 'enabled' => Bool];
```  
