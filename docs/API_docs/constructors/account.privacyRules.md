---
title: "account.privacyRules"
description: "Privacy rules"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_privacyRules.html
---
# Constructor: account.privacyRules  
[Back to constructors index](/API_docs/constructors/index.html)



Privacy rules

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|rules|Array of [PrivacyRule](/API_docs/types/PrivacyRule.html) | Yes|Privacy rules|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats to which the rules apply|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users to which the rules apply|



### Type: [account.PrivacyRules](/API_docs/types/account.PrivacyRules.html)


### Example:

```
$account_privacyRules = ['_' => 'account.privacyRules', 'rules' => [PrivacyRule, PrivacyRule], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
