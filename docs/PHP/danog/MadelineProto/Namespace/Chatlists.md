---
title: "danog\\MadelineProto\\Namespace\\Chatlists: "
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Namespace\Chatlists`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

  




## Method list:
* [`exportChatlistInvite(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist, string $title = '', list<array|int|string> $peers = []): array{_: \"chatlists.exportedChatlistInvite", filter: array{_: \"dialogFilter", contacts: bool, non_contacts: bool, groups: bool, broadcasts: bool, bots: bool, exclude_muted: bool, exclude_read: bool, exclude_archived: bool, id: int, title: string, emoticon: string, pinned_peers: list<array|int|string>, include_peers: list<array|int|string>, exclude_peers: list<array|int|string>}|array{_: \"dialogFilterDefault"}|array{_: \"dialogFilterChatlist", has_my_invites: bool, id: int, title: string, emoticon: string, pinned_peers: list<array|int|string>, include_peers: list<array|int|string>}, invite: array{_: \"exportedChatlistInvite", title: string, url: string, peers: \list<array|int|string>}} @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ExportedChatlistInvite.ht}}`](#exportchatlistinvite-array-_-inputchatlistdialogfilter-filter_id-int-chatlist-string-title-list-array-int-string-peers-array-_-chatlists-exportedchatlistinvite-filter-array-_-dialogfilter-contacts-bool-non_contacts-bool-groups-bool-broadcasts-bool-bots-bool-exclude_muted-bool-exclude_read-bool-exclude_archived-bool-id-int-title-string-emoticon-string-pinned_peers-list-array-int-string-include_peers-list-array-int-string-exclude_peers-list-array-int-string-array-_-dialogfilterdefault-array-_-dialogfilterchatlist-has_my_invites-bool-id-int-title-string-emoticon-string-pinned_peers-list-array-int-string-include_peers-list-array-int-string-invite-array-_-exportedchatlistinvite-title-string-url-string-peers-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-chatlists-exportedchatlistinvite-ht)
* [`deleteExportedInvite(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist, string $slug = ''): bool`](#deleteexportedinvite-array-_-inputchatlistdialogfilter-filter_id-int-chatlist-string-slug-bool)
* [`editExportedInvite(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist, string $slug = '', string $title = '', list<array|int|string> $peers = []): array{_: \"exportedChatlistInvite", title: string, url: string, peers: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/ExportedChatlistInvite.htm}`](#editexportedinvite-array-_-inputchatlistdialogfilter-filter_id-int-chatlist-string-slug-string-title-list-array-int-string-peers-array-_-exportedchatlistinvite-title-string-url-string-peers-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-exportedchatlistinvite-htm)
* [`getExportedInvites(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist): array{_: \"chatlists.exportedInvites", invites: list<array{_: \"exportedChatlistInvite", title: string, url: string, peers: list<array|int|string>}>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ExportedInvites.htm}`](#getexportedinvites-array-_-inputchatlistdialogfilter-filter_id-int-chatlist-array-_-chatlists-exportedinvites-invites-list-array-_-exportedchatlistinvite-title-string-url-string-peers-list-array-int-string-chats-list-array-int-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-chatlists-exportedinvites-htm)
* [`checkChatlistInvite(string $slug = ''): array{_: \"chatlists.chatlistInviteAlready", filter_id: int, missing_peers: list<array|int|string>, already_peers: list<array|int|string>, chats: list<array|int|string>, users: list<array|int|string>}|array{_: \"chatlists.chatlistInvite", title: string, emoticon: string, peers: list<array|int|string>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ChatlistInvite.htm}`](#checkchatlistinvite-string-slug-array-_-chatlists-chatlistinvitealready-filter_id-int-missing_peers-list-array-int-string-already_peers-list-array-int-string-chats-list-array-int-string-users-list-array-int-string-array-_-chatlists-chatlistinvite-title-string-emoticon-string-peers-list-array-int-string-chats-list-array-int-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-chatlists-chatlistinvite-htm)
* [`joinChatlistInvite(string $slug = '', list<array|int|string> $peers = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#joinchatlistinvite-string-slug-list-array-int-string-peers-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`getChatlistUpdates(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist): array{_: \"chatlists.chatlistUpdates", missing_peers: list<array|int|string>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ChatlistUpdates.htm}`](#getchatlistupdates-array-_-inputchatlistdialogfilter-filter_id-int-chatlist-array-_-chatlists-chatlistupdates-missing_peers-list-array-int-string-chats-list-array-int-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-chatlists-chatlistupdates-htm)
* [`joinChatlistUpdates(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist, list<array|int|string> $peers = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#joinchatlistupdates-array-_-inputchatlistdialogfilter-filter_id-int-chatlist-list-array-int-string-peers-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`hideChatlistUpdates(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist): bool`](#hidechatlistupdates-array-_-inputchatlistdialogfilter-filter_id-int-chatlist-bool)
* [`getLeaveChatlistSuggestions(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist): \list<array|int|string> Array of  @see https://docs.madelineproto.xyz/API_docs/types/Peer.html`](#getleavechatlistsuggestions-array-_-inputchatlistdialogfilter-filter_id-int-chatlist-list-array-int-string-array-of-see-https-docs-madelineproto-xyz-api_docs-types-peer-html)
* [`leaveChatlist(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist, list<array|int|string> $peers = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#leavechatlist-array-_-inputchatlistdialogfilter-filter_id-int-chatlist-list-array-int-string-peers-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)

## Methods:
### `exportChatlistInvite(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist, string $title = '', list<array|int|string> $peers = []): array{_: \"chatlists.exportedChatlistInvite", filter: array{_: \"dialogFilter", contacts: bool, non_contacts: bool, groups: bool, broadcasts: bool, bots: bool, exclude_muted: bool, exclude_read: bool, exclude_archived: bool, id: int, title: string, emoticon: string, pinned_peers: list<array|int|string>, include_peers: list<array|int|string>, exclude_peers: list<array|int|string>}|array{_: \"dialogFilterDefault"}|array{_: \"dialogFilterChatlist", has_my_invites: bool, id: int, title: string, emoticon: string, pinned_peers: list<array|int|string>, include_peers: list<array|int|string>}, invite: array{_: \"exportedChatlistInvite", title: string, url: string, peers: \list<array|int|string>}} @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ExportedChatlistInvite.ht}}`

Export a [folder »](https://core.telegram.org/api/folders), creating a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).


Parameters:

* `$chatlist`: `array{_: \"inputChatlistDialogFilter", filter_id?: int}` The folder to export @see https://docs.madelineproto.xyz/API_docs/types/InputChatlist.html  
* `$title`: `string` An optional name for the link  
* `$peers`: `list<array|int|string>` Array of The list of channels, group and supergroups to share with the link. Basic groups will automatically be [converted to supergroups](https://core.telegram.org/api/channel#migration) when invoking the method. @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ExportedChatlistInvite.html


### `deleteExportedInvite(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist, string $slug = ''): bool`

Delete a previously created [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).


Parameters:

* `$chatlist`: `array{_: \"inputChatlistDialogFilter", filter_id?: int}` The related folder @see https://docs.madelineproto.xyz/API_docs/types/InputChatlist.html  
* `$slug`: `string` `slug` obtained from the [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).  



### `editExportedInvite(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist, string $slug = '', string $title = '', list<array|int|string> $peers = []): array{_: \"exportedChatlistInvite", title: string, url: string, peers: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/ExportedChatlistInvite.htm}`

Edit a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).


Parameters:

* `$chatlist`: `array{_: \"inputChatlistDialogFilter", filter_id?: int}` Folder ID @see https://docs.madelineproto.xyz/API_docs/types/InputChatlist.html  
* `$slug`: `string` `slug` obtained from the [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).  
* `$title`: `string` If set, sets a new name for the link  
* `$peers`: `list<array|int|string>` Array of If set, changes the list of peers shared with the link @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/ExportedChatlistInvite.html


### `getExportedInvites(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist): array{_: \"chatlists.exportedInvites", invites: list<array{_: \"exportedChatlistInvite", title: string, url: string, peers: list<array|int|string>}>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ExportedInvites.htm}`

List all [chat folder deep links »](https://core.telegram.org/api/links#chat-folder-links) associated to a folder


Parameters:

* `$chatlist`: `array{_: \"inputChatlistDialogFilter", filter_id?: int}` The folder @see https://docs.madelineproto.xyz/API_docs/types/InputChatlist.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ExportedInvites.html


### `checkChatlistInvite(string $slug = ''): array{_: \"chatlists.chatlistInviteAlready", filter_id: int, missing_peers: list<array|int|string>, already_peers: list<array|int|string>, chats: list<array|int|string>, users: list<array|int|string>}|array{_: \"chatlists.chatlistInvite", title: string, emoticon: string, peers: list<array|int|string>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ChatlistInvite.htm}`

Obtain information about a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).


Parameters:

* `$slug`: `string` `slug` obtained from the [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ChatlistInvite.html


### `joinChatlistInvite(string $slug = '', list<array|int|string> $peers = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Import a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links), joining some or all the chats in the folder.


Parameters:

* `$slug`: `string` `slug` obtained from a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).  
* `$peers`: `list<array|int|string>` Array of List of new chats to join, fetched using [chatlists.checkChatlistInvite](https://docs.madelineproto.xyz/API_docs/methods/chatlists.checkChatlistInvite.html) and filtered as specified in the [documentation »](https://core.telegram.org/api/folders#shared-folders). @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `getChatlistUpdates(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist): array{_: \"chatlists.chatlistUpdates", missing_peers: list<array|int|string>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ChatlistUpdates.htm}`

Fetch new chats associated with an imported [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links). Must be invoked at most every `chatlist_update_period` seconds (as per the related [client configuration parameter »](https://core.telegram.org/api/config#chatlist-update-period)).


Parameters:

* `$chatlist`: `array{_: \"inputChatlistDialogFilter", filter_id?: int}` The folder @see https://docs.madelineproto.xyz/API_docs/types/InputChatlist.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/chatlists.ChatlistUpdates.html


### `joinChatlistUpdates(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist, list<array|int|string> $peers = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Join channels and supergroups recently added to a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).


Parameters:

* `$chatlist`: `array{_: \"inputChatlistDialogFilter", filter_id?: int}` The folder @see https://docs.madelineproto.xyz/API_docs/types/InputChatlist.html  
* `$peers`: `list<array|int|string>` Array of List of new chats to join, fetched using [chatlists.getChatlistUpdates](https://docs.madelineproto.xyz/API_docs/methods/chatlists.getChatlistUpdates.html) and filtered as specified in the [documentation »](https://core.telegram.org/api/folders#shared-folders). @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `hideChatlistUpdates(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist): bool`

Dismiss new pending peers recently added to a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).


Parameters:

* `$chatlist`: `array{_: \"inputChatlistDialogFilter", filter_id?: int}` The folder @see https://docs.madelineproto.xyz/API_docs/types/InputChatlist.html  



### `getLeaveChatlistSuggestions(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist): \list<array|int|string> Array of  @see https://docs.madelineproto.xyz/API_docs/types/Peer.html`

Returns identifiers of pinned or always included chats from a chat folder imported using a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links), which are suggested to be left when the chat folder is deleted.


Parameters:

* `$chatlist`: `array{_: \"inputChatlistDialogFilter", filter_id?: int}` Folder ID @see https://docs.madelineproto.xyz/API_docs/types/InputChatlist.html  


Return value: Array of  @see https://docs.madelineproto.xyz/API_docs/types/Peer.html


### `leaveChatlist(array{_: \"inputChatlistDialogFilter", filter_id?: int} $chatlist, list<array|int|string> $peers = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Delete a folder imported using a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links)


Parameters:

* `$chatlist`: `array{_: \"inputChatlistDialogFilter", filter_id?: int}` Folder ID @see https://docs.madelineproto.xyz/API_docs/types/InputChatlist.html  
* `$peers`: `list<array|int|string>` Array of Also leave the specified channels and groups @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
