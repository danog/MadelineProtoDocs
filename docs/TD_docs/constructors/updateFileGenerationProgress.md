---
title: updateFileGenerationProgress
description: Informs that a file is being generated
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateFileGenerationProgress  
[Back to constructors index](index.md)



Informs that a file is being generated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file\_id|[int](../types/int.md) | Yes|File identifier|
|size|[int](../types/int.md) | Yes|Expected size of the generated file|
|ready|[int](../types/int.md) | Yes|Number of bytes already generated. Negative number means that generation has failed and was terminated|



### Type: [Update](../types/Update.md)


