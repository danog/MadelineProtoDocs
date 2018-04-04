---
title: updateFileProgress
description: DEPRECATED. Use updateFile instead. File is partly downloaded/uploaded
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: updateFileProgress  
[Back to constructors index](index.md)



DEPRECATED. Use updateFile instead. File is partly downloaded/uploaded

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file\_id|[int](../types/int.md) | Yes|File identifier|
|size|[int](../types/int.md) | Yes|Total file size (0 means unknown)|
|ready|[int](../types/int.md) | Yes|Number of bytes already downloaded/uploaded. Negative number means that download/upload has failed and was terminated|



### Type: [Update](../types/Update.md)


