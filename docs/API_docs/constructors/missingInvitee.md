---
title: "missingInvitee"
description: "missingInvitee attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: missingInvitee  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|premium\_would\_allow\_invite|[Bool](/API_docs/types/Bool.html) | Optional|
|premium\_required\_for\_pm|[Bool](/API_docs/types/Bool.html) | Optional|
|user\_id|[long](/API_docs/types/long.html) | Yes|



### Type: [MissingInvitee](/API_docs/types/MissingInvitee.html)


### Example:

```
$missingInvitee = ['_' => 'missingInvitee', 'premium_would_allow_invite' => Bool, 'premium_required_for_pm' => Bool, 'user_id' => long];
```  
