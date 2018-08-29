---
title: deleteMessages
description: Deletes messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: deleteMessages  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Deletes messages

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|chat\_id|[int53](../types/int53.md) | Chat identifier | Yes|
|message\_ids|Array of [int53](../types/int53.md) | Identifiers of messages to delete | Yes|
|revoke|[Bool](../types/Bool.md) | Pass true to try to delete sent messages for all chat members (may fail if messages are too old). Is always true for Channels and SecretChats | Yes|


### Return type: [Ok](../types/Ok.md)

