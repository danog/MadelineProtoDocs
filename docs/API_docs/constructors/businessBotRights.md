---
title: "businessBotRights"
description: "businessBotRights attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessBotRights  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|reply|[Bool](/API_docs/types/Bool.html) | Optional|
|read\_messages|[Bool](/API_docs/types/Bool.html) | Optional|
|delete\_sent\_messages|[Bool](/API_docs/types/Bool.html) | Optional|
|delete\_received\_messages|[Bool](/API_docs/types/Bool.html) | Optional|
|edit\_name|[Bool](/API_docs/types/Bool.html) | Optional|
|edit\_bio|[Bool](/API_docs/types/Bool.html) | Optional|
|edit\_profile\_photo|[Bool](/API_docs/types/Bool.html) | Optional|
|edit\_username|[Bool](/API_docs/types/Bool.html) | Optional|
|view\_gifts|[Bool](/API_docs/types/Bool.html) | Optional|
|sell\_gifts|[Bool](/API_docs/types/Bool.html) | Optional|
|change\_gift\_settings|[Bool](/API_docs/types/Bool.html) | Optional|
|transfer\_and\_upgrade\_gifts|[Bool](/API_docs/types/Bool.html) | Optional|
|transfer\_stars|[Bool](/API_docs/types/Bool.html) | Optional|
|manage\_stories|[Bool](/API_docs/types/Bool.html) | Optional|



### Type: [BusinessBotRights](/API_docs/types/BusinessBotRights.html)


### Example:

```
$businessBotRights = ['_' => 'businessBotRights', 'reply' => Bool, 'read_messages' => Bool, 'delete_sent_messages' => Bool, 'delete_received_messages' => Bool, 'edit_name' => Bool, 'edit_bio' => Bool, 'edit_profile_photo' => Bool, 'edit_username' => Bool, 'view_gifts' => Bool, 'sell_gifts' => Bool, 'change_gift_settings' => Bool, 'transfer_and_upgrade_gifts' => Bool, 'transfer_stars' => Bool, 'manage_stories' => Bool];
```  
