---
title: "help.premiumPromo"
description: "Telegram Premium promotion information"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_premiumPromo.html
---
# Constructor: help.premiumPromo  
[Back to constructors index](/API_docs/constructors/index.html)



Telegram Premium promotion information

Note that the `video_sections`+`videos` fields are a list of videos, and the corresponding premium feature identifiers.  
They're equivalent to a section =&gt; video dictionary, with keys from `video_section` and values from `videos`.  
The keys in `video_sections` correspond to a specific feature identifier, and the associated promotional video should be shown when the associated feature row is clicked.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|status\_text|[string](/API_docs/types/string.html) | Yes|Description of the current state of the user's Telegram Premium subscription|
|status\_entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Yes|[Message entities for styled text](https://core.telegram.org/api/entities)|
|video\_sections|Array of [string](/API_docs/types/string.html) | Yes|A list of [premium feature identifiers »](https://core.telegram.org/api/premium), associated to each video|
|videos|Array of [Document](/API_docs/types/Document.html) | Yes|A list of videos|
|period\_options|Array of [PremiumSubscriptionOption](/API_docs/types/PremiumSubscriptionOption.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|Related user information|



### Type: [help.PremiumPromo](/API_docs/types/help.PremiumPromo.html)


### Example:

```
$help_premiumPromo = ['_' => 'help.premiumPromo', 'status_text' => 'string', 'status_entities' => [MessageEntity, MessageEntity], 'video_sections' => ['string', 'string'], 'videos' => [Document, Document], 'period_options' => [PremiumSubscriptionOption, PremiumSubscriptionOption], 'users' => [User, User]];
```  
