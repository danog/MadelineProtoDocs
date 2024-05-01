---
title: "premium.myBoosts"
description: "A list of peers we are currently boosting, and how many boost slots we have left."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/premium_myBoosts.html
---
# Constructor: premium.myBoosts  
[Back to constructors index](/API_docs/constructors/index.html)



A list of peers we are currently [boosting](https://core.telegram.org/api/boost), and how many [boost slots](https://core.telegram.org/api/boost) we have left.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|my\_boosts|Array of [MyBoost](/API_docs/types/MyBoost.html) | Yes|Info about boosted peers and remaining boost slots.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Referenced chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Referenced users|



### Type: [premium.MyBoosts](/API_docs/types/premium.MyBoosts.html)


### Example:

```
$premium_myBoosts = ['_' => 'premium.myBoosts', 'my_boosts' => [MyBoost, MyBoost], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
