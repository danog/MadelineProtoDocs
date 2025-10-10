---
title: "businessBotRights"
description: "Business bot rights."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessBotRights  
[Back to constructors index](/API_docs/constructors/index.html)



[Business bot rights](https://core.telegram.org/api/bots/connected-business-bots).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|reply|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can send and edit messages in private chats that had incoming messages in the last 24 hours.|
|read\_messages|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can mark incoming private messages as read.|
|delete\_sent\_messages|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can delete messages sent by the bot.|
|delete\_received\_messages|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can delete received private messages in managed chats.|
|edit\_name|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can edit the first and last name of the business account.|
|edit\_bio|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can edit the bio of the business account.|
|edit\_profile\_photo|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can edit the profile photo of the business account.|
|edit\_username|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can edit the username of the business account.|
|view\_gifts|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can view gifts and the amount of Telegram Stars owned by the business account.|
|sell\_gifts|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can convert regular gifts owned by the business account to Telegram Stars.|
|change\_gift\_settings|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can change the privacy settings pertaining to gifts for the business account.|
|transfer\_and\_upgrade\_gifts|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can transfer and upgrade gifts owned by the business account.|
|transfer\_stars|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can transfer Telegram Stars received by the business account to its own account, or use them to upgrade and transfer gifts.|
|manage\_stories|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can post, edit and delete stories on behalf of the business account.|



### Type: [BusinessBotRights](/API_docs/types/BusinessBotRights.html)


### Example:

```
$businessBotRights = ['_' => 'businessBotRights', 'reply' => Bool, 'read_messages' => Bool, 'delete_sent_messages' => Bool, 'delete_received_messages' => Bool, 'edit_name' => Bool, 'edit_bio' => Bool, 'edit_profile_photo' => Bool, 'edit_username' => Bool, 'view_gifts' => Bool, 'sell_gifts' => Bool, 'change_gift_settings' => Bool, 'transfer_and_upgrade_gifts' => Bool, 'transfer_stars' => Bool, 'manage_stories' => Bool];
```  
