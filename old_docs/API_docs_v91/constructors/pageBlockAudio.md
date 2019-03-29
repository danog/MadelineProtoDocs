---
title: pageBlockAudio
description: Page block audio
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockAudio  
[Back to constructors index](index.md)



Page block audio

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|audio\_id|[long](../types/long.md) | Yes|Audio ID|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockAudio = ['_' => 'pageBlockAudio', 'audio_id' => long, 'caption' => PageCaption];
```  


Or, if you're into Lua:

```lua
pageBlockAudio={_='pageBlockAudio', audio_id=long, caption=PageCaption}

```


