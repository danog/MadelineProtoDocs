---
title: "help.premiumPromo"
description: "help.premiumPromo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_premiumPromo.html
---
# Constructor: help.premiumPromo  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|status\_text|[string](/API_docs/types/string.html) | Yes|
|status\_entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Yes|
|video\_sections|Array of [string](/API_docs/types/string.html) | Yes|
|videos|Array of [Document](/API_docs/types/Document.html) | Yes|
|currency|[string](/API_docs/types/string.html) | Yes|
|monthly\_amount|[long](/API_docs/types/long.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [help.PremiumPromo](/API_docs/types/help.PremiumPromo.html)


### Example:

```
$help_premiumPromo = ['_' => 'help.premiumPromo', 'status_text' => 'string', 'status_entities' => [MessageEntity, MessageEntity], 'video_sections' => ['string', 'string'], 'videos' => [Document, Document], 'currency' => 'string', 'monthly_amount' => long, 'users' => [User, User]];
```  
