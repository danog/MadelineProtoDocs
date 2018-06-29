---
title: upload.getFileHashes
description: Get file hashes
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: upload.getFileHashes  
[Back to methods index](index.md)


Get file hashes

### Parameters:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|location|[InputFileLocation](../types/InputFileLocation.md) | Yes|The file|
|offset|[int](../types/int.md) | Yes|Offset|


### Return type: [Vector\_of\_FileHash](../types/FileHash.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Vector_of_FileHash = $MadelineProto->upload->getFileHashes(['location' => InputFileLocation, 'offset' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - upload.getFileHashes
* params - `{"location": InputFileLocation, "offset": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/upload.getFileHashes`

Parameters:

location - Json encoded InputFileLocation

offset - Json encoded int




Or, if you're into Lua:

```
Vector_of_FileHash = upload.getFileHashes({location=InputFileLocation, offset=int, })
```

