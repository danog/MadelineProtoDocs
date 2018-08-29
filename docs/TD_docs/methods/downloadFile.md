---
title: downloadFile
description: Asynchronously downloads file from cloud. Updates updateFile will notify about download progress and successful download
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: downloadFile  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Asynchronously downloads file from cloud. Updates updateFile will notify about download progress and successful download

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file\_id|[int](../types/int.md) | Identifier of file to download | Yes|
|priority|[int](../types/int.md) | Priority of download, 1-32. The higher priority, the earlier file will be downloaded. If priorities of two files are equal then the last one for which downloadFile is called will be downloaded first | Yes|


### Return type: [Ok](../types/Ok.md)

