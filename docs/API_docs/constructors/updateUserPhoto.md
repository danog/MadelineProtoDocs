---
title: "updateUserPhoto"
description: "Change of contact's profile photo."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserPhoto  
[Back to constructors index](/API_docs/constructors/index.html)



Change of contact's profile photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User identifier|
|date|[int](/API_docs/types/int.html) | Yes|Date of photo update.|
|photo|[UserProfilePhoto](/API_docs/types/UserProfilePhoto.html) | Optional|New profile photo|
|previous|[Bool](/API_docs/types/Bool.html) | Yes|([boolTrue](../constructors/boolTrue.html)), if one of the previously used photos is set a profile photo.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateUserPhoto = ['_' => 'updateUserPhoto', 'user_id' => long, 'date' => int, 'photo' => UserProfilePhoto, 'previous' => Bool];
```  
