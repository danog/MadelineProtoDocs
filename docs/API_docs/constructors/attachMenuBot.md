---
title: "attachMenuBot"
description: "Represents a bot mini app that can be launched from the attachment/side menu »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: attachMenuBot  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [bot mini app that can be launched from the attachment/side menu »](https://core.telegram.org/api/bots/attach)

At least one of the `show_in_attach_menu` or the `show_in_side_menu` flags will always be set.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inactive|[Bool](/API_docs/types/Bool.html) | Optional|If set, before launching the mini app the client should ask the user to add the mini app to the attachment/side menu, and only if the user accepts, after invoking [messages.toggleBotInAttachMenu](../methods/messages.toggleBotInAttachMenu.html) the app should be opened.|
|has\_settings|[Bool](/API_docs/types/Bool.html) | Optional|Deprecated flag, can be ignored.|
|request\_write\_access|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot would like to send messages to the user.|
|show\_in\_attach\_menu|[Bool](/API_docs/types/Bool.html) | Optional|Whether, when installed, an attachment menu entry should be shown for the Mini App.|
|show\_in\_side\_menu|[Bool](/API_docs/types/Bool.html) | Optional|Whether, when installed, an entry in the main view side menu should be shown for the Mini App.|
|side\_menu\_disclaimer\_needed|[Bool](/API_docs/types/Bool.html) | Optional|If `inactive` if set and the user hasn't previously accepted the third-party mini apps [Terms of Service](https://telegram.org/tos/mini-apps) for this bot, when showing the mini app installation prompt, an additional mandatory checkbox to accept the [mini apps TOS](https://telegram.org/tos/mini-apps) and a disclaimer indicating that this Mini App is not affiliated to Telegram should be shown.|
|bot\_id|[long](/API_docs/types/long.html) | Yes|Bot ID|
|short\_name|[string](/API_docs/types/string.html) | Yes|Attachment menu item name|
|peer\_types|Array of [AttachMenuPeerType](/API_docs/types/AttachMenuPeerType.html) | Optional|List of dialog types where this attachment menu entry should be shown|
|icons|Array of [AttachMenuBotIcon](/API_docs/types/AttachMenuBotIcon.html) | Yes|List of platform-specific static icons and animations to use for the attachment menu button|



### Type: [AttachMenuBot](/API_docs/types/AttachMenuBot.html)


### Example:

```
$attachMenuBot = ['_' => 'attachMenuBot', 'inactive' => Bool, 'has_settings' => Bool, 'request_write_access' => Bool, 'show_in_attach_menu' => Bool, 'show_in_side_menu' => Bool, 'side_menu_disclaimer_needed' => Bool, 'bot_id' => long, 'short_name' => 'string', 'peer_types' => [AttachMenuPeerType, AttachMenuPeerType], 'icons' => [AttachMenuBotIcon, AttachMenuBotIcon]];
```  
