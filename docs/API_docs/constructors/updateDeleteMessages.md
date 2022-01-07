---
title: "updateDeleteMessages"
description: "Messages were deleted."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteMessages  
[Back to constructors index](/API_docs/constructors/index.md)



Messages were deleted.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [int](/API_docs/types/int.md) | Yes|List of identifiers of deleted messages|
|pts|[int](/API_docs/types/int.md) | Yes|New quality of actions in a message box|
|pts\_count|[int](/API_docs/types/int.md) | Yes|Number of generated [events](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateDeleteMessages = ['_' => 'updateDeleteMessages', 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  
