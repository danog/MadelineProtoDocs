---
title: "botInfo"
description: "Info about bots (available bot commands, etc)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInfo  
[Back to constructors index](/API_docs/constructors/index.html)



Info about bots (available bot commands, etc)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_preview\_medias|[Bool](/API_docs/types/Bool.html) | Optional|If set, the bot has some [preview medias for the configured Main Mini App, see here »](https://core.telegram.org/api/bots/webapps#main-mini-app-previews) for more info on Main Mini App preview medias.|
|user\_id|[long](/API_docs/types/long.html) | Optional|ID of the bot|
|description|[string](/API_docs/types/string.html) | Optional|Description of the bot|
|description\_photo|[Photo](/API_docs/types/Photo.html) | Optional|Description photo|
|description\_document|[Document](/API_docs/types/Document.html) | Optional|Description animation in MPEG4 format|
|commands|Array of [BotCommand](/API_docs/types/BotCommand.html) | Optional|Bot commands that can be used in the chat|
|menu\_button|[BotMenuButton](/API_docs/types/BotMenuButton.html) | Optional|Indicates the action to execute when pressing the in-UI menu button for bots|
|privacy\_policy\_url|[string](/API_docs/types/string.html) | Optional|The HTTP link to the privacy policy of the bot. If not set, then the `/privacy` command must be used, if supported by the bot (i.e. if it's present in the `commands` vector). If it isn't supported, then <https://telegram.org/privacy-tpa> must be opened, instead.|
|app\_settings|[BotAppSettings](/API_docs/types/BotAppSettings.html) | Optional|[Mini app »](https://core.telegram.org/api/bots/webapps) settings<br>|
|verifier\_settings|[BotVerifierSettings](/API_docs/types/BotVerifierSettings.html) | Optional|



### Type: [BotInfo](/API_docs/types/BotInfo.html)


### Example:

```
$botInfo = ['_' => 'botInfo', 'has_preview_medias' => Bool, 'user_id' => long, 'description' => 'string', 'description_photo' => Photo, 'description_document' => Document, 'commands' => [BotCommand, BotCommand], 'menu_button' => BotMenuButton, 'privacy_policy_url' => 'string', 'app_settings' => BotAppSettings, 'verifier_settings' => BotVerifierSettings];
```  
