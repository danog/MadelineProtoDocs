---
title: uploadFile
description: Asynchronously uploads file to the cloud without sending it in a message. Updates updateFile will notify about upload progress and successful upload. The file will not have persistent identifier until it will be sent in a message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: uploadFile  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Asynchronously uploads file to the cloud without sending it in a message. Updates updateFile will notify about upload progress and successful upload. The file will not have persistent identifier until it will be sent in a message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|file|[InputFile](../types/InputFile.md) | File to upload | Yes|
|file\_type|[FileType](../types/FileType.md) | File type | Yes|
|priority|[int](../types/int.md) | Priority of upload, 1-32. The higher priority, the earlier file will be uploaded. If priorities of two files are equal then the first one for which uploadFile is called will be uploaded first | Yes|


### Return type: [File](../types/File.md)

