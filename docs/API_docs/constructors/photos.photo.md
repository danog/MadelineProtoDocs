---
title: "photos.photo"
description: "Photo with auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/photos_photo.html
---
# Constructor: photos.photo  
[Back to constructors index](/API_docs/constructors/index.html)



Photo with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|Photo|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [photos.Photo](/API_docs/types/photos.Photo.html)


### Example:

```
$photos_photo = ['_' => 'photos.photo', 'photo' => Photo, 'users' => [User, User]];
```  
