---
title: "danog\\MadelineProto\\Namespace\\Bots: "
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Namespace\Bots`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

  




## Method list:
* [`sendCustomRequest(mixed $params, string $custom_method = ''): \mixed Any JSON-encodable data`](#sendcustomrequest-mixed-params-string-custom_method-mixed-any-json-encodable-data)
* [`answerWebhookJSONQuery(mixed $data, int $query_id = 0): bool`](#answerwebhookjsonquery-mixed-data-int-query_id-0-bool)
* [`setBotCommands(array{_: \"botCommandScopeDefault"}|array{_: \"botCommandScopeUsers"}|array{_: \"botCommandScopeChats"}|array{_: \"botCommandScopeChatAdmins"}|array{_: \"botCommandScopePeer", peer: array|int|string}|array{_: \"botCommandScopePeerAdmins", peer: array|int|string}|array{_: \"botCommandScopePeerUser", peer: array|int|string, user_id: array|int|string} $scope, string $lang_code = '', list<array{_: \"botCommand", command?: string, description?: string}> $commands = []): bool`](#setbotcommands-array-_-botcommandscopedefault-array-_-botcommandscopeusers-array-_-botcommandscopechats-array-_-botcommandscopechatadmins-array-_-botcommandscopepeer-peer-array-int-string-array-_-botcommandscopepeeradmins-peer-array-int-string-array-_-botcommandscopepeeruser-peer-array-int-string-user_id-array-int-string-scope-string-lang_code-list-array-_-botcommand-command-string-description-string-commands-bool)
* [`resetBotCommands(array{_: \"botCommandScopeDefault"}|array{_: \"botCommandScopeUsers"}|array{_: \"botCommandScopeChats"}|array{_: \"botCommandScopeChatAdmins"}|array{_: \"botCommandScopePeer", peer: array|int|string}|array{_: \"botCommandScopePeerAdmins", peer: array|int|string}|array{_: \"botCommandScopePeerUser", peer: array|int|string, user_id: array|int|string} $scope, string $lang_code = ''): bool`](#resetbotcommands-array-_-botcommandscopedefault-array-_-botcommandscopeusers-array-_-botcommandscopechats-array-_-botcommandscopechatadmins-array-_-botcommandscopepeer-peer-array-int-string-array-_-botcommandscopepeeradmins-peer-array-int-string-array-_-botcommandscopepeeruser-peer-array-int-string-user_id-array-int-string-scope-string-lang_code-bool)
* [`getBotCommands(array{_: \"botCommandScopeDefault"}|array{_: \"botCommandScopeUsers"}|array{_: \"botCommandScopeChats"}|array{_: \"botCommandScopeChatAdmins"}|array{_: \"botCommandScopePeer", peer: array|int|string}|array{_: \"botCommandScopePeerAdmins", peer: array|int|string}|array{_: \"botCommandScopePeerUser", peer: array|int|string, user_id: array|int|string} $scope, string $lang_code = ''): \list<array{_: "botCommand", command: string, description: string}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/BotCommand.html`](#getbotcommands-array-_-botcommandscopedefault-array-_-botcommandscopeusers-array-_-botcommandscopechats-array-_-botcommandscopechatadmins-array-_-botcommandscopepeer-peer-array-int-string-array-_-botcommandscopepeeradmins-peer-array-int-string-array-_-botcommandscopepeeruser-peer-array-int-string-user_id-array-int-string-scope-string-lang_code-list-array-_-botcommand-command-string-description-string-array-of-see-https-docs-madelineproto-xyz-api_docs-types-botcommand-html)
* [`setBotMenuButton(array|int|string $user_id, array{_: \"botMenuButtonDefault"}|array{_: \"botMenuButtonCommands"}|array{_: \"botMenuButton", text?: string, url?: string} $button): bool`](#setbotmenubutton-array-int-string-user_id-array-_-botmenubuttondefault-array-_-botmenubuttoncommands-array-_-botmenubutton-text-string-url-string-button-bool)
* [`getBotMenuButton(array|int|string $user_id): array{_: \"botMenuButtonDefault"}|array{_: \"botMenuButtonCommands"}|array{_: \"botMenuButton", text: string, url: \string} @see https://docs.madelineproto.xyz/API_docs/types/BotMenuButton.htm}`](#getbotmenubutton-array-int-string-user_id-array-_-botmenubuttondefault-array-_-botmenubuttoncommands-array-_-botmenubutton-text-string-url-string-see-https-docs-madelineproto-xyz-api_docs-types-botmenubutton-htm)
* [`setBotBroadcastDefaultAdminRights(array{_: \"chatAdminRights", change_info?: bool, post_messages?: bool, edit_messages?: bool, delete_messages?: bool, ban_users?: bool, invite_users?: bool, pin_messages?: bool, add_admins?: bool, anonymous?: bool, manage_call?: bool, other?: bool, manage_topics?: bool} $admin_rights): bool`](#setbotbroadcastdefaultadminrights-array-_-chatadminrights-change_info-bool-post_messages-bool-edit_messages-bool-delete_messages-bool-ban_users-bool-invite_users-bool-pin_messages-bool-add_admins-bool-anonymous-bool-manage_call-bool-other-bool-manage_topics-bool-admin_rights-bool)
* [`setBotGroupDefaultAdminRights(array{_: \"chatAdminRights", change_info?: bool, post_messages?: bool, edit_messages?: bool, delete_messages?: bool, ban_users?: bool, invite_users?: bool, pin_messages?: bool, add_admins?: bool, anonymous?: bool, manage_call?: bool, other?: bool, manage_topics?: bool} $admin_rights): bool`](#setbotgroupdefaultadminrights-array-_-chatadminrights-change_info-bool-post_messages-bool-edit_messages-bool-delete_messages-bool-ban_users-bool-invite_users-bool-pin_messages-bool-add_admins-bool-anonymous-bool-manage_call-bool-other-bool-manage_topics-bool-admin_rights-bool)
* [`setBotInfo(array|int|string $bot = [], string $lang_code = '', string $name = '', string $about = '', string $description = ''): bool`](#setbotinfo-array-int-string-bot-string-lang_code-string-name-string-about-string-description-bool)
* [`getBotInfo(array|int|string $bot = [], string $lang_code = ''): array{_: \"bots.botInfo", name: string, about: string, description: \string} @see https://docs.madelineproto.xyz/API_docs/types/bots.BotInfo.htm}`](#getbotinfo-array-int-string-bot-string-lang_code-array-_-bots-botinfo-name-string-about-string-description-string-see-https-docs-madelineproto-xyz-api_docs-types-bots-botinfo-htm)
* [`reorderUsernames(array|int|string $bot, list<string> $order = []): bool`](#reorderusernames-array-int-string-bot-list-string-order-bool)
* [`toggleUsername(array|int|string $bot, bool $active, string $username = ''): bool`](#toggleusername-array-int-string-bot-bool-active-string-username-bool)

## Methods:
### `sendCustomRequest(mixed $params, string $custom_method = ''): \mixed Any JSON-encodable data`

Sends a custom request; for bots only


Parameters:

* `$params`: `mixed` Any JSON-encodable data  
* `$custom_method`: `string` The method name  


Return value: Any JSON-encodable data


### `answerWebhookJSONQuery(mixed $data, int $query_id = 0): bool`

Answers a custom query; for bots only


Parameters:

* `$data`: `mixed` Any JSON-encodable data  
* `$query_id`: `int` Identifier of a custom query  



### `setBotCommands(array{_: \"botCommandScopeDefault"}|array{_: \"botCommandScopeUsers"}|array{_: \"botCommandScopeChats"}|array{_: \"botCommandScopeChatAdmins"}|array{_: \"botCommandScopePeer", peer: array|int|string}|array{_: \"botCommandScopePeerAdmins", peer: array|int|string}|array{_: \"botCommandScopePeerUser", peer: array|int|string, user_id: array|int|string} $scope, string $lang_code = '', list<array{_: \"botCommand", command?: string, description?: string}> $commands = []): bool`

Set bot command list


Parameters:

* `$scope`: `array{_: \"botCommandScopeDefault"}|array{_: \"botCommandScopeUsers"}|array{_: \"botCommandScopeChats"}|array{_: \"botCommandScopeChatAdmins"}|array{_: \"botCommandScopePeer", peer: array|int|string}|array{_: \"botCommandScopePeerAdmins", peer: array|int|string}|array{_: \"botCommandScopePeerUser", peer: array|int|string, user_id: array|int|string}` Command scope @see https://docs.madelineproto.xyz/API_docs/types/BotCommandScope.html  
* `$lang_code`: `string` Language code  
* `$commands`: `list<array{_: \"botCommand", command?: string, description?: string}>` Array of Bot commands @see https://docs.madelineproto.xyz/API_docs/types/BotCommand.html  



### `resetBotCommands(array{_: \"botCommandScopeDefault"}|array{_: \"botCommandScopeUsers"}|array{_: \"botCommandScopeChats"}|array{_: \"botCommandScopeChatAdmins"}|array{_: \"botCommandScopePeer", peer: array|int|string}|array{_: \"botCommandScopePeerAdmins", peer: array|int|string}|array{_: \"botCommandScopePeerUser", peer: array|int|string, user_id: array|int|string} $scope, string $lang_code = ''): bool`

Clear bot commands for the specified bot scope and language code


Parameters:

* `$scope`: `array{_: \"botCommandScopeDefault"}|array{_: \"botCommandScopeUsers"}|array{_: \"botCommandScopeChats"}|array{_: \"botCommandScopeChatAdmins"}|array{_: \"botCommandScopePeer", peer: array|int|string}|array{_: \"botCommandScopePeerAdmins", peer: array|int|string}|array{_: \"botCommandScopePeerUser", peer: array|int|string, user_id: array|int|string}` Command scope @see https://docs.madelineproto.xyz/API_docs/types/BotCommandScope.html  
* `$lang_code`: `string` Language code  



### `getBotCommands(array{_: \"botCommandScopeDefault"}|array{_: \"botCommandScopeUsers"}|array{_: \"botCommandScopeChats"}|array{_: \"botCommandScopeChatAdmins"}|array{_: \"botCommandScopePeer", peer: array|int|string}|array{_: \"botCommandScopePeerAdmins", peer: array|int|string}|array{_: \"botCommandScopePeerUser", peer: array|int|string, user_id: array|int|string} $scope, string $lang_code = ''): \list<array{_: "botCommand", command: string, description: string}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/BotCommand.html`

Obtain a list of bot commands for the specified bot scope and language code


Parameters:

* `$scope`: `array{_: \"botCommandScopeDefault"}|array{_: \"botCommandScopeUsers"}|array{_: \"botCommandScopeChats"}|array{_: \"botCommandScopeChatAdmins"}|array{_: \"botCommandScopePeer", peer: array|int|string}|array{_: \"botCommandScopePeerAdmins", peer: array|int|string}|array{_: \"botCommandScopePeerUser", peer: array|int|string, user_id: array|int|string}` Command scope @see https://docs.madelineproto.xyz/API_docs/types/BotCommandScope.html  
* `$lang_code`: `string` Language code  


Return value: Array of  @see https://docs.madelineproto.xyz/API_docs/types/BotCommand.html


### `setBotMenuButton(array|int|string $user_id, array{_: \"botMenuButtonDefault"}|array{_: \"botMenuButtonCommands"}|array{_: \"botMenuButton", text?: string, url?: string} $button): bool`

Sets the [menu button action »](https://core.telegram.org/api/bots/menu) for a given user or for all users


Parameters:

* `$user_id`: `array|int|string` User ID @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  
* `$button`: `array{_: \"botMenuButtonDefault"}|array{_: \"botMenuButtonCommands"}|array{_: \"botMenuButton", text?: string, url?: string}` Bot menu button action @see https://docs.madelineproto.xyz/API_docs/types/BotMenuButton.html  



### `getBotMenuButton(array|int|string $user_id): array{_: \"botMenuButtonDefault"}|array{_: \"botMenuButtonCommands"}|array{_: \"botMenuButton", text: string, url: \string} @see https://docs.madelineproto.xyz/API_docs/types/BotMenuButton.htm}`

Gets the menu button action for a given user or for all users, previously set using [bots.setBotMenuButton](https://docs.madelineproto.xyz/API_docs/methods/bots.setBotMenuButton.html); users can see this information in the [botInfo](https://docs.madelineproto.xyz/API_docs/constructors/botInfo.html) constructor.


Parameters:

* `$user_id`: `array|int|string` User ID or empty for the default menu button. @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/BotMenuButton.html


### `setBotBroadcastDefaultAdminRights(array{_: \"chatAdminRights", change_info?: bool, post_messages?: bool, edit_messages?: bool, delete_messages?: bool, ban_users?: bool, invite_users?: bool, pin_messages?: bool, add_admins?: bool, anonymous?: bool, manage_call?: bool, other?: bool, manage_topics?: bool} $admin_rights): bool`

Set the default [suggested admin rights](https://core.telegram.org/api/rights#suggested-bot-rights) for bots being added as admins to channels, see [here for more info on how to handle them »](https://core.telegram.org/api/rights#suggested-bot-rights).


Parameters:

* `$admin_rights`: `array{_: \"chatAdminRights", change_info?: bool, post_messages?: bool, edit_messages?: bool, delete_messages?: bool, ban_users?: bool, invite_users?: bool, pin_messages?: bool, add_admins?: bool, anonymous?: bool, manage_call?: bool, other?: bool, manage_topics?: bool}` Admin rights @see https://docs.madelineproto.xyz/API_docs/types/ChatAdminRights.html  



### `setBotGroupDefaultAdminRights(array{_: \"chatAdminRights", change_info?: bool, post_messages?: bool, edit_messages?: bool, delete_messages?: bool, ban_users?: bool, invite_users?: bool, pin_messages?: bool, add_admins?: bool, anonymous?: bool, manage_call?: bool, other?: bool, manage_topics?: bool} $admin_rights): bool`

Set the default [suggested admin rights](https://core.telegram.org/api/rights#suggested-bot-rights) for bots being added as admins to groups, see [here for more info on how to handle them »](https://core.telegram.org/api/rights#suggested-bot-rights).


Parameters:

* `$admin_rights`: `array{_: \"chatAdminRights", change_info?: bool, post_messages?: bool, edit_messages?: bool, delete_messages?: bool, ban_users?: bool, invite_users?: bool, pin_messages?: bool, add_admins?: bool, anonymous?: bool, manage_call?: bool, other?: bool, manage_topics?: bool}` Admin rights @see https://docs.madelineproto.xyz/API_docs/types/ChatAdminRights.html  



### `setBotInfo(array|int|string $bot = [], string $lang_code = '', string $name = '', string $about = '', string $description = ''): bool`

Set localized name, about text and description of a bot (or of the current account, if called by a bot).


Parameters:

* `$bot`: `array|int|string` If called by a user, **must** contain the peer of a bot we own. @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  
* `$lang_code`: `string` Language code, if left empty update the fallback about text and description  
* `$name`: `string` New bot name  
* `$about`: `string` New about text  
* `$description`: `string` New description  



### `getBotInfo(array|int|string $bot = [], string $lang_code = ''): array{_: \"bots.botInfo", name: string, about: string, description: \string} @see https://docs.madelineproto.xyz/API_docs/types/bots.BotInfo.htm}`

Get localized name, about text and description of a bot (or of the current account, if called by a bot).


Parameters:

* `$bot`: `array|int|string` If called by a user, **must** contain the peer of a bot we own. @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  
* `$lang_code`: `string` Language code, if left empty this method will return the fallback about text and description.  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/bots.BotInfo.html


### `reorderUsernames(array|int|string $bot, list<string> $order = []): bool`

Reorder usernames associated to a bot we own.


Parameters:

* `$bot`: `array|int|string` The bot @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  
* `$order`: `list<string>` The new order for active usernames. All active usernames must be specified.  



### `toggleUsername(array|int|string $bot, bool $active, string $username = ''): bool`

Activate or deactivate a purchased [fragment.com](https://fragment.com) username associated to a bot we own.


Parameters:

* `$bot`: `array|int|string` The bot @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  
* `$active`: `bool` Whether to activate or deactivate it  
* `$username`: `string` Username  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
