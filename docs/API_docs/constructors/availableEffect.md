---
title: "availableEffect"
description: "Represents a message effect »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: availableEffect  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [message effect »](https://core.telegram.org/api/effects).

All `long` IDs except for `id` are [document](../constructors/document.html).`id`s from the containing [messages.availableEffects](../constructors/messages.availableEffects.html) constructor.

See [here »](https://core.telegram.org/api/effects) for more info on how to use following fields.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|premium\_required|[Bool](/API_docs/types/Bool.html) | Optional|Whether a [Premium](https://core.telegram.org/api/premium) subscription is required to use this effect.|
|id|[long](/API_docs/types/long.html) | Yes|Unique effect ID.|
|emoticon|[string](/API_docs/types/string.html) | Yes|Emoji corresponding to the effect, to be used as icon for the effect if `static_icon_id` is not set.|
|static\_icon\_id|[long](/API_docs/types/long.html) | Optional|ID of the document containing the static icon (WEBP) of the effect.|
|effect\_sticker\_id|[long](/API_docs/types/long.html) | Yes|Contains the preview [animation (TGS format »)](https://core.telegram.org/api/stickers#animated-stickers), used for the effect selection menu.|
|effect\_animation\_id|[long](/API_docs/types/long.html) | Optional|If set, contains the actual animated effect [(TGS format »)](https://core.telegram.org/api/stickers#animated-stickers). If not set, the animated effect must be set equal to the [premium animated sticker effect](https://core.telegram.org/api/stickers#premium-animated-sticker-effects) associated to the animated sticker specified in `effect_sticker_id` (always different from the preview animation, fetched thanks to the [videoSize](../constructors/videoSize.html) of type `f` as specified [here »](https://core.telegram.org/api/stickers#premium-animated-sticker-effects)).|



### Type: [AvailableEffect](/API_docs/types/AvailableEffect.html)


### Example:

```
$availableEffect = ['_' => 'availableEffect', 'premium_required' => Bool, 'id' => long, 'emoticon' => 'string', 'static_icon_id' => long, 'effect_sticker_id' => long, 'effect_animation_id' => long];
```  
