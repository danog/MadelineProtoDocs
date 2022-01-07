---
title: "updateUserPhoto"
description: "Change of contact's profile photo."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserPhoto  
[Back to constructors index](/API_docs/constructors/index.md)



Change of contact's profile photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.md) | Yes|
|date|[int](/API_docs/types/int.md) | Yes|Date of photo update.|
|photo|[UserProfilePhoto](/API_docs/types/UserProfilePhoto.md) | Optional|New profile photo|
|previous|[Bool](/API_docs/types/Bool.md) | Yes|([boolTrue](../constructors/boolTrue.md)), if one of the previously used photos is set a profile photo.|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateUserPhoto = ['_' => 'updateUserPhoto', 'user_id' => long, 'date' => int, 'photo' => UserProfilePhoto, 'previous' => Bool];
```  
