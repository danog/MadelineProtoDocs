---
title: "botVerifierSettings"
description: "Info about the current verifier bot »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botVerifierSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Info about the current [verifier bot »](https://core.telegram.org/api/bots/verification).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_modify\_custom\_description|[Bool](/API_docs/types/Bool.html) | Optional|Indicates whether the bot is allowed to set a custom description field for individual verified peers, different from the `custom_description` provided here.|
|icon|[long](/API_docs/types/long.html) | Yes|Verification icon|
|company|[string](/API_docs/types/string.html) | Yes|The name of the organization that provides the verification|
|custom\_description|[string](/API_docs/types/string.html) | Optional|An optional default description for the verification|



### Type: [BotVerifierSettings](/API_docs/types/BotVerifierSettings.html)


### Example:

```
$botVerifierSettings = ['_' => 'botVerifierSettings', 'can_modify_custom_description' => Bool, 'icon' => long, 'company' => 'string', 'custom_description' => 'string'];
```  
