---
title: createTemporaryPassword
description: Creates new temporary password for payments processing
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: createTemporaryPassword  
[Back to methods index](index.md)


YOU CANNOT USE THIS METHOD IN MADELINEPROTO


Creates new temporary password for payments processing

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|password|[string](../types/string.md) | Persistent user password | Yes|
|valid\_for|[int](../types/int.md) | Time before temporary password will expire, seconds. Should be between 60 and 86400 | Yes|


### Return type: [TemporaryPasswordState](../types/TemporaryPasswordState.md)

