---
title: "updateChannelMessageViews"
description: "The view counter of a message in a channel has changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelMessageViews  
[Back to constructors index](/API_docs/constructors/index.md)



The view counter of a message in a channel has changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.md) | Yes|
|id|[int](/API_docs/types/int.md) | Yes|ID of the message|
|views|[int](/API_docs/types/int.md) | Yes|New view counter|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updateChannelMessageViews = ['_' => 'updateChannelMessageViews', 'channel_id' => long, 'id' => int, 'views' => int];
```  
