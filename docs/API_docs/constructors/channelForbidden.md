---
title: "channelForbidden"
description: "Indicates a channel/supergroup we can't access because we were banned, or for some other reason."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelForbidden  
[Back to constructors index](/API_docs/constructors/index.md)



Indicates a channel/supergroup we can't access because we were banned, or for some other reason.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|broadcast|[Bool](/API_docs/types/Bool.md) | Optional|Is this a channel|
|megagroup|[Bool](/API_docs/types/Bool.md) | Optional|Is this a supergroup|
|id|[long](/API_docs/types/long.md) | Yes|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Access hash|
|title|[string](/API_docs/types/string.md) | Yes|Title|
|until\_date|[int](/API_docs/types/int.md) | Optional|The ban is valid until the specified date|



### Type: [Chat](/API_docs/types/Chat.md)


### Example:

```php
$channelForbidden = ['_' => 'channelForbidden', 'broadcast' => Bool, 'megagroup' => Bool, 'id' => long, 'access_hash' => long, 'title' => 'string', 'until_date' => int];
```  
