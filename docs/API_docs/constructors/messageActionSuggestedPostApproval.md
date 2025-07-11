---
title: "messageActionSuggestedPostApproval"
description: "messageActionSuggestedPostApproval attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSuggestedPostApproval  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|rejected|[Bool](/API_docs/types/Bool.html) | Optional|
|balance\_too\_low|[Bool](/API_docs/types/Bool.html) | Optional|
|reject\_comment|[string](/API_docs/types/string.html) | Optional|
|schedule\_date|[int](/API_docs/types/int.html) | Optional|
|price|[StarsAmount](/API_docs/types/StarsAmount.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionSuggestedPostApproval = ['_' => 'messageActionSuggestedPostApproval', 'rejected' => Bool, 'balance_too_low' => Bool, 'reject_comment' => 'string', 'schedule_date' => int, 'price' => StarsAmount];
```  
