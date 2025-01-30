---
title: "updateUser"
description: "User (user and/or userFull) information was updated."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUser  
[Back to constructors index](/API_docs/constructors/index.html)



User ([user](../constructors/user.html) and/or [userFull](../constructors/userFull.html)) information was updated.

This update can only be received through getDifference or in [updates](../constructors/updates.html)/[updatesCombined](../constructors/updatesCombined.html) constructors, so it will **always** come bundled with the updated [user](../constructors/user.html), that should be applied [as usual »](https://core.telegram.org/api/peers), **without** re-fetching the info manually.

However, full peer information will not come bundled in updates, so the full peer cache ([userFull](../constructors/userFull.html)) must be invalidated for `user_id` when receiving this update.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateUser = ['_' => 'updateUser', 'user_id' => long];
```  
