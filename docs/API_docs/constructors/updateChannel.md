---
title: "updateChannel"
description: "A new channel or supergroup is available, or info about an existing channel has changed and must be refeteched."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannel  
[Back to constructors index](/API_docs/constructors/index.html)



A new channel or supergroup is available, or info about an existing channel has changed and must be refeteched.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel ID|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannel = ['_' => 'updateChannel', 'channel_id' => long];
```  
