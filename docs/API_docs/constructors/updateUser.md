---
title: "updateUser"
description: "User information was updated, it must be refetched using users.getFullUser."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUser  
[Back to constructors index](/API_docs/constructors/index.html)



User information was updated, it must be refetched using [users.getFullUser](../methods/users.getFullUser.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateUser = ['_' => 'updateUser', 'user_id' => long];
```  
