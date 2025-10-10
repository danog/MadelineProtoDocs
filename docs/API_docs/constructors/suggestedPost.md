---
title: "suggestedPost"
description: "Contains info about a suggested post »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: suggestedPost  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [suggested post »](https://core.telegram.org/api/suggested-posts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|accepted|[Bool](/API_docs/types/Bool.html) | Optional|Whether the suggested post was accepted.|
|rejected|[Bool](/API_docs/types/Bool.html) | Optional|Whether the suggested post was rejected.|
|price|[StarsAmount](/API_docs/types/StarsAmount.html) | Optional|Price of the suggested post.|
|schedule\_date|[int](/API_docs/types/int.html) | Optional|Scheduling date.|



### Type: [SuggestedPost](/API_docs/types/SuggestedPost.html)


### Example:

```
$suggestedPost = ['_' => 'suggestedPost', 'accepted' => Bool, 'rejected' => Bool, 'price' => StarsAmount, 'schedule_date' => int];
```  
