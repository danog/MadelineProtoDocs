---
title: "attachMenuBot"
description: "Represents a bot web app that can be launched from the attachment menu »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: attachMenuBot  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [bot web app that can be launched from the attachment menu »](https://core.telegram.org/api/bots/attach)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inactive|[Bool](/API_docs/types/Bool.html) | Optional|Whether this bot attachment menu entry should be shown in the attachment menu (toggle using [messages.toggleBotInAttachMenu](../methods/messages.toggleBotInAttachMenu.html))|
|has\_settings|[Bool](/API_docs/types/Bool.html) | Optional|True, if the bot supports the ["settings\_button\_pressed" event »](https://core.telegram.org/api/bots/webapps#settings-button-pressed)|
|request\_write\_access|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot would like to send messages to the user.|
|show\_in\_attach\_menu|[Bool](/API_docs/types/Bool.html) | Optional|
|show\_in\_side\_menu|[Bool](/API_docs/types/Bool.html) | Optional|
|side\_menu\_disclaimer\_needed|[Bool](/API_docs/types/Bool.html) | Optional|
|bot\_id|[long](/API_docs/types/long.html) | Yes|Bot ID|
|short\_name|[string](/API_docs/types/string.html) | Yes|Attachment menu item name|
|peer\_types|Array of [AttachMenuPeerType](/API_docs/types/AttachMenuPeerType.html) | Optional|List of dialog types where this attachment menu entry should be shown|
|icons|Array of [AttachMenuBotIcon](/API_docs/types/AttachMenuBotIcon.html) | Yes|List of platform-specific static icons and animations to use for the attachment menu button|



### Type: [AttachMenuBot](/API_docs/types/AttachMenuBot.html)


### Example:

```
$attachMenuBot = ['_' => 'attachMenuBot', 'inactive' => Bool, 'has_settings' => Bool, 'request_write_access' => Bool, 'show_in_attach_menu' => Bool, 'show_in_side_menu' => Bool, 'side_menu_disclaimer_needed' => Bool, 'bot_id' => long, 'short_name' => 'string', 'peer_types' => [AttachMenuPeerType, AttachMenuPeerType], 'icons' => [AttachMenuBotIcon, AttachMenuBotIcon]];
```  
