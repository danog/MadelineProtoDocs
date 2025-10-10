---
title: "messageActionSuggestedPostApproval"
description: "A suggested post » was approved or rejected."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSuggestedPostApproval  
[Back to constructors index](/API_docs/constructors/index.html)



A [suggested post »](https://core.telegram.org/api/suggested-posts) was approved or rejected.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|rejected|[Bool](/API_docs/types/Bool.html) | Optional|Whether the suggested post was rejected.|
|balance\_too\_low|[Bool](/API_docs/types/Bool.html) | Optional|If set, the post was approved but the user's balance is too low to pay for the suggested post.|
|reject\_comment|[string](/API_docs/types/string.html) | Optional|If the suggested post was rejected, can optionally contain a rejection comment.|
|schedule\_date|[int](/API_docs/types/int.html) | Optional|Scheduling date.|
|price|[StarsAmount](/API_docs/types/StarsAmount.html) | Optional|Price for the suggested post.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionSuggestedPostApproval = ['_' => 'messageActionSuggestedPostApproval', 'rejected' => Bool, 'balance_too_low' => Bool, 'reject_comment' => 'string', 'schedule_date' => int, 'price' => StarsAmount];
```  
