---
title: "requirementToContactPaidMessages"
description: "This user requires us to pay the specified amount of Telegram Stars to send them a message, see here » for the full flow."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: requirementToContactPaidMessages  
[Back to constructors index](/API_docs/constructors/index.html)



This user requires us to pay the specified amount of [Telegram Stars](https://core.telegram.org/api/stars) to send them a message, see [here »](https://core.telegram.org/api/paid-messages) for the full flow.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stars\_amount|[long](/API_docs/types/long.html) | Yes|The required amount of [Telegram Stars](https://core.telegram.org/api/stars).|



### Type: [RequirementToContact](/API_docs/types/RequirementToContact.html)


### Example:

```
$requirementToContactPaidMessages = ['_' => 'requirementToContactPaidMessages', 'stars_amount' => long];
```  
