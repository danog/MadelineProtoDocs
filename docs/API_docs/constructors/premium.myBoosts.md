---
title: "premium.myBoosts"
description: "premium.myBoosts attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/premium_myBoosts.html
---
# Constructor: premium.myBoosts  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|my\_boosts|Array of [MyBoost](/API_docs/types/MyBoost.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [premium.MyBoosts](/API_docs/types/premium.MyBoosts.html)


### Example:

```
$premium_myBoosts = ['_' => 'premium.myBoosts', 'my_boosts' => [MyBoost, MyBoost], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
