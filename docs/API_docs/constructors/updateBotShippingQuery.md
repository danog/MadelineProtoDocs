---
title: "updateBotShippingQuery"
description: "This object contains information about an incoming shipping query."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotShippingQuery  
[Back to constructors index](/API_docs/constructors/index.html)



This object contains information about an incoming shipping query.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](/API_docs/types/long.html) | Yes|Unique query identifier|
|user\_id|[long](/API_docs/types/long.html) | Yes|User who sent the query|
|payload|[bytes](/API_docs/types/bytes.html) | Yes|Bot specified invoice payload|
|shipping\_address|[PostAddress](/API_docs/types/PostAddress.html) | Yes|User specified shipping address|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotShippingQuery = ['_' => 'updateBotShippingQuery', 'query_id' => long, 'user_id' => long, 'payload' => 'bytes', 'shipping_address' => PostAddress];
```  
