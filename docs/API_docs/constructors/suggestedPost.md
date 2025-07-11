---
title: "suggestedPost"
description: "suggestedPost attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: suggestedPost  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|accepted|[Bool](/API_docs/types/Bool.html) | Optional|
|rejected|[Bool](/API_docs/types/Bool.html) | Optional|
|price|[StarsAmount](/API_docs/types/StarsAmount.html) | Optional|
|schedule\_date|[int](/API_docs/types/int.html) | Optional|



### Type: [SuggestedPost](/API_docs/types/SuggestedPost.html)


### Example:

```
$suggestedPost = ['_' => 'suggestedPost', 'accepted' => Bool, 'rejected' => Bool, 'price' => StarsAmount, 'schedule_date' => int];
```  
