---
title: getUserProfilePhotos
description: Returns profile photos of the user. Result of this query may be outdated: some photos may be already deleted
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: getUserProfilePhotos  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Returns profile photos of the user. Result of this query may be outdated: some photos may be already deleted

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|user\_id|[int](../types/int.md) | User identifier | Yes|
|offset|[int](../types/int.md) | Photos to skip, must be non-negative | Yes|
|limit|[int](../types/int.md) | Maximum number of photos to be returned, can't be greater than 100 | Yes|


### Return type: [UserProfilePhotos](../types/UserProfilePhotos.md)

