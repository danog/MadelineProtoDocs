---
title: "availableEffect"
description: "availableEffect attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: availableEffect  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|premium\_required|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|
|emoticon|[string](/API_docs/types/string.html) | Yes|
|static\_icon\_id|[long](/API_docs/types/long.html) | Optional|
|effect\_sticker\_id|[long](/API_docs/types/long.html) | Yes|
|effect\_animation\_id|[long](/API_docs/types/long.html) | Optional|



### Type: [AvailableEffect](/API_docs/types/AvailableEffect.html)


### Example:

```
$availableEffect = ['_' => 'availableEffect', 'premium_required' => Bool, 'id' => long, 'emoticon' => 'string', 'static_icon_id' => long, 'effect_sticker_id' => long, 'effect_animation_id' => long];
```  
