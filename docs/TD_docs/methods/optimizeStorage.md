---
title: optimizeStorage
description: Optimizes storage usage, i.e. deletes some files and return new storage usage statistics. Secret thumbnails can't be deleted
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: optimizeStorage  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Optimizes storage usage, i.e. deletes some files and return new storage usage statistics. Secret thumbnails can't be deleted

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|size|[int53](../types/int53.md) | Limit on total size of files after deletion. Pass -1 to use default limit | Yes|
|ttl|[int](../types/int.md) | Limit on time passed since last access time (or creation time on some filesystems) to a file. Pass -1 to use default limit | Yes|
|count|[int](../types/int.md) | Limit on total count of files after deletion. Pass -1 to use default limit | Yes|
|immunity\_delay|[int](../types/int.md) | Number of seconds after creation of a file, it can't be delited. Pass -1 to use default value | Yes|
|file\_types|Array of [FileType](../types/FileType.md) | If not empty, only files with given types are considered. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted | Yes|
|chat\_ids|Array of [int53](../types/int53.md) | If not empty, only files from the given chats are considered. Use 0 as chat identifier to delete files not belonging to any chat, for example profile photos | Yes|
|exclude\_chat\_ids|Array of [int53](../types/int53.md) | If not empty, files from the given chats are exluded. Use 0 as chat identifier to exclude all files not belonging to any chat, for example profile photos | Yes|
|chat\_limit|[int](../types/int.md) | Same as in getStorageStatistics. Affects only returned statistics | Yes|


### Return type: [StorageStatistics](../types/StorageStatistics.md)

