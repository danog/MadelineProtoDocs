---
title: "chatInvite"
description: "Chat invite info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInvite  
[Back to constructors index](/API_docs/constructors/index.html)



Chat invite info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a [channel/supergroup](https://core.telegram.org/api/channel) or a [normal group](https://core.telegram.org/api/channel)|
|broadcast|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a [channel](https://core.telegram.org/api/channel)|
|public|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a public [channel/supergroup](https://core.telegram.org/api/channel)|
|megagroup|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a [supergroup](https://core.telegram.org/api/channel)|
|request\_needed|[Bool](/API_docs/types/Bool.html) | Optional|Whether the [join request »](https://core.telegram.org/api/invites#join-requests) must be first approved by an administrator|
|verified|[Bool](/API_docs/types/Bool.html) | Optional|Is this chat or channel verified by Telegram?|
|scam|[Bool](/API_docs/types/Bool.html) | Optional|This chat is probably a scam|
|fake|[Bool](/API_docs/types/Bool.html) | Optional|If set, this chat was reported by many users as a fake or scam: be careful when interacting with it.|
|can\_refulfill\_subscription|[Bool](/API_docs/types/Bool.html) | Optional|
|title|[string](/API_docs/types/string.html) | Yes|Chat/supergroup/channel title|
|about|[string](/API_docs/types/string.html) | Optional|Description of the group of channel|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|Chat/supergroup/channel photo|
|participants\_count|[int](/API_docs/types/int.html) | Yes|Participant count|
|participants|Array of [User](/API_docs/types/User.html) | Optional|A few of the participants that are in the group|
|color|[int](/API_docs/types/int.html) | Yes|[Profile color palette ID](https://core.telegram.org/api/colors)|
|subscription\_pricing|[StarsSubscriptionPricing](/API_docs/types/StarsSubscriptionPricing.html) | Optional|
|subscription\_form\_id|[long](/API_docs/types/long.html) | Optional|
|bot\_verification|[BotVerification](/API_docs/types/BotVerification.html) | Optional|



### Type: [ChatInvite](/API_docs/types/ChatInvite.html)


### Example:

```
$chatInvite = ['_' => 'chatInvite', 'channel' => Bool, 'broadcast' => Bool, 'public' => Bool, 'megagroup' => Bool, 'request_needed' => Bool, 'verified' => Bool, 'scam' => Bool, 'fake' => Bool, 'can_refulfill_subscription' => Bool, 'title' => 'string', 'about' => 'string', 'photo' => Photo, 'participants_count' => int, 'participants' => [User, User], 'color' => int, 'subscription_pricing' => StarsSubscriptionPricing, 'subscription_form_id' => long, 'bot_verification' => BotVerification];
```  
