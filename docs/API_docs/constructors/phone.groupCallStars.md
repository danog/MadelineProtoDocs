---
title: "phone.groupCallStars"
description: "phone.groupCallStars attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_groupCallStars.html
---
# Constructor: phone.groupCallStars  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|total\_stars|[long](/API_docs/types/long.html) | Yes|
|top\_donors|Array of [GroupCallDonor](/API_docs/types/GroupCallDonor.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [phone.GroupCallStars](/API_docs/types/phone.GroupCallStars.html)


### Example:

```
$phone_groupCallStars = ['_' => 'phone.groupCallStars', 'total_stars' => long, 'top_donors' => [GroupCallDonor, GroupCallDonor], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
