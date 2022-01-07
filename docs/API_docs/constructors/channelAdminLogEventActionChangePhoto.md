---
title: "channelAdminLogEventActionChangePhoto"
description: "The channel/supergroup's picture was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangePhoto  
[Back to constructors index](/API_docs/constructors/index.md)



The channel/supergroup's picture was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_photo|[Photo](/API_docs/types/Photo.md) | Optional|Previous picture|
|new\_photo|[Photo](/API_docs/types/Photo.md) | Optional|New picture|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionChangePhoto = ['_' => 'channelAdminLogEventActionChangePhoto', 'prev_photo' => Photo, 'new_photo' => Photo];
```  
