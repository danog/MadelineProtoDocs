---
title: "updateChannel"
description: "Channel/supergroup (channel and/or channelFull) information was updated."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannel  
[Back to constructors index](/API_docs/constructors/index.html)



Channel/supergroup ([channel](../constructors/channel.html) and/or [channelFull](../constructors/channelFull.html)) information was updated.

This update can only be received through getDifference or in [updates](../constructors/updates.html)/[updatesCombined](../constructors/updatesCombined.html) constructors, so it will **always** come bundled with the updated [channel](../constructors/channel.html), that should be applied [as usual »](https://core.telegram.org/api/peers), **without** re-fetching the info manually.

However, full peer information will not come bundled in updates, so the full peer cache ([channelFull](../constructors/channelFull.html)) must be invalidated for `channel_id` when receiving this update.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel ID|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannel = ['_' => 'updateChannel', 'channel_id' => long];
```  
