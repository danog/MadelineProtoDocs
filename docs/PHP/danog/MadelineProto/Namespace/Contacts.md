---
title: "danog\\MadelineProto\\Namespace\\Contacts: "
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Namespace\Contacts`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

  




## Method list:
* [`getContactIDs(list<int> $hash = []): list<int>`](#getcontactids-list-int-hash-list-int)
* [`getStatuses(): \list<array{_: "contactStatus", status: array{_: "userStatusEmpty"}|array{_: "userStatusOnline", expires: int}|array{_: "userStatusOffline", was_online: int}|array{_: "userStatusRecently"}|array{_: "userStatusLastWeek"}|array{_: "userStatusLastMonth"}, user_id: int}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/ContactStatus.html`](#getstatuses-list-array-_-contactstatus-status-array-_-userstatusempty-array-_-userstatusonline-expires-int-array-_-userstatusoffline-was_online-int-array-_-userstatusrecently-array-_-userstatuslastweek-array-_-userstatuslastmonth-user_id-int-array-of-see-https-docs-madelineproto-xyz-api_docs-types-contactstatus-html)
* [`getContacts(list<int> $hash = []): array{_: \"contacts.contactsNotModified"}|array{_: \"contacts.contacts", contacts: list<array{_: \"contact", mutual: bool, user_id: int}>, saved_count: int, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/contacts.Contacts.htm}`](#getcontacts-list-int-hash-array-_-contacts-contactsnotmodified-array-_-contacts-contacts-contacts-list-array-_-contact-mutual-bool-user_id-int-saved_count-int-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-contacts-contacts-htm)
* [`importContacts(list<array{_: \"inputPhoneContact", client_id?: int, phone?: string, first_name?: string, last_name?: string}> $contacts = []): array{_: \"contacts.importedContacts", imported: list<array{_: \"importedContact", user_id: int, client_id: int}>, popular_invites: list<array{_: \"popularContact", client_id: int, importers: int}>, retry_contacts: list<int>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/contacts.ImportedContacts.htm}`](#importcontacts-list-array-_-inputphonecontact-client_id-int-phone-string-first_name-string-last_name-string-contacts-array-_-contacts-importedcontacts-imported-list-array-_-importedcontact-user_id-int-client_id-int-popular_invites-list-array-_-popularcontact-client_id-int-importers-int-retry_contacts-list-int-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-contacts-importedcontacts-htm)
* [`deleteContacts(list<array|int|string> $id = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#deletecontacts-list-array-int-string-id-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`deleteByPhones(list<string> $phones = []): bool`](#deletebyphones-list-string-phones-bool)
* [`block(array|int|string $id): bool`](#block-array-int-string-id-bool)
* [`unblock(array|int|string $id): bool`](#unblock-array-int-string-id-bool)
* [`getBlocked(int $offset = 0, int $limit = 0): array{_: \"contacts.blocked", blocked: list<array{_: \"peerBlocked", peer_id: array|int|string, date: int}>, chats: list<array|int|string>, users: list<array|int|string>}|array{_: \"contacts.blockedSlice", count: int, blocked: list<array{_: \"peerBlocked", peer_id: array|int|string, date: int}>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/contacts.Blocked.htm}`](#getblocked-int-offset-0-int-limit-0-array-_-contacts-blocked-blocked-list-array-_-peerblocked-peer_id-array-int-string-date-int-chats-list-array-int-string-users-list-array-int-string-array-_-contacts-blockedslice-count-int-blocked-list-array-_-peerblocked-peer_id-array-int-string-date-int-chats-list-array-int-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-contacts-blocked-htm)
* [`search(string $q = '', int $limit = 0): array{_: \"contacts.found", my_results: list<array|int|string>, results: list<array|int|string>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/contacts.Found.htm}`](#search-string-q-int-limit-0-array-_-contacts-found-my_results-list-array-int-string-results-list-array-int-string-chats-list-array-int-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-contacts-found-htm)
* [`getTopPeers(bool $correspondents = false, bool $bots_pm = false, bool $bots_inline = false, bool $phone_calls = false, bool $forward_users = false, bool $forward_chats = false, bool $groups = false, bool $channels = false, int $offset = 0, int $limit = 0, list<int> $hash = []): array{_: \"contacts.topPeersNotModified"}|array{_: \"contacts.topPeers", categories: list<array{_: \"topPeerCategoryPeers", category: array{_: \"topPeerCategoryBotsPM"}|array{_: \"topPeerCategoryBotsInline"}|array{_: \"topPeerCategoryCorrespondents"}|array{_: \"topPeerCategoryGroups"}|array{_: \"topPeerCategoryChannels"}|array{_: \"topPeerCategoryPhoneCalls"}|array{_: \"topPeerCategoryForwardUsers"}|array{_: \"topPeerCategoryForwardChats"}, count: int, peers: list<array{_: \"topPeer", peer: array|int|string, rating: float}>}>, chats: list<array|int|string>, users: list<array|int|string>}|array{_: \"contacts.topPeersDisabled"} @see https://docs.madelineproto.xyz/API_docs/types/contacts.TopPeers.htm}`](#gettoppeers-bool-correspondents-false-bool-bots_pm-false-bool-bots_inline-false-bool-phone_calls-false-bool-forward_users-false-bool-forward_chats-false-bool-groups-false-bool-channels-false-int-offset-0-int-limit-0-list-int-hash-array-_-contacts-toppeersnotmodified-array-_-contacts-toppeers-categories-list-array-_-toppeercategorypeers-category-array-_-toppeercategorybotspm-array-_-toppeercategorybotsinline-array-_-toppeercategorycorrespondents-array-_-toppeercategorygroups-array-_-toppeercategorychannels-array-_-toppeercategoryphonecalls-array-_-toppeercategoryforwardusers-array-_-toppeercategoryforwardchats-count-int-peers-list-array-_-toppeer-peer-array-int-string-rating-float-chats-list-array-int-string-users-list-array-int-string-array-_-contacts-toppeersdisabled-see-https-docs-madelineproto-xyz-api_docs-types-contacts-toppeers-htm)
* [`resetTopPeerRating(array{_: \"topPeerCategoryBotsPM"}|array{_: \"topPeerCategoryBotsInline"}|array{_: \"topPeerCategoryCorrespondents"}|array{_: \"topPeerCategoryGroups"}|array{_: \"topPeerCategoryChannels"}|array{_: \"topPeerCategoryPhoneCalls"}|array{_: \"topPeerCategoryForwardUsers"}|array{_: \"topPeerCategoryForwardChats"} $category, array|int|string $peer): bool`](#resettoppeerrating-array-_-toppeercategorybotspm-array-_-toppeercategorybotsinline-array-_-toppeercategorycorrespondents-array-_-toppeercategorygroups-array-_-toppeercategorychannels-array-_-toppeercategoryphonecalls-array-_-toppeercategoryforwardusers-array-_-toppeercategoryforwardchats-category-array-int-string-peer-bool)
* [`resetSaved(): bool`](#resetsaved-bool)
* [`getSaved(): \list<array{_: "savedPhoneContact", phone: string, first_name: string, last_name: string, date: int}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/SavedContact.html`](#getsaved-list-array-_-savedphonecontact-phone-string-first_name-string-last_name-string-date-int-array-of-see-https-docs-madelineproto-xyz-api_docs-types-savedcontact-html)
* [`toggleTopPeers(bool $enabled): bool`](#toggletoppeers-bool-enabled-bool)
* [`addContact(array|int|string $id, bool $add_phone_privacy_exception = false, string $first_name = '', string $last_name = '', string $phone = ''): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#addcontact-array-int-string-id-bool-add_phone_privacy_exception-false-string-first_name-string-last_name-string-phone-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`acceptContact(array|int|string $id): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#acceptcontact-array-int-string-id-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`getLocated(array{_: \"inputGeoPointEmpty"}|array{_: \"inputGeoPoint", lat: float, long: float, accuracy_radius?: int} $geo_point, bool $background = false, int $self_expires = 0): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#getlocated-array-_-inputgeopointempty-array-_-inputgeopoint-lat-float-long-float-accuracy_radius-int-geo_point-bool-background-false-int-self_expires-0-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`blockFromReplies(bool $delete_message = false, bool $delete_history = false, bool $report_spam = false, int $msg_id = 0): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#blockfromreplies-bool-delete_message-false-bool-delete_history-false-bool-report_spam-false-int-msg_id-0-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`resolvePhone(string $phone = ''): array{_: \"contacts.resolvedPeer", peer: array|int|string, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/contacts.ResolvedPeer.htm}`](#resolvephone-string-phone-array-_-contacts-resolvedpeer-peer-array-int-string-chats-list-array-int-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-contacts-resolvedpeer-htm)
* [`exportContactToken(): array{_: \"exportedContactToken", url: string, expires: \int} @see https://docs.madelineproto.xyz/API_docs/types/ExportedContactToken.htm}`](#exportcontacttoken-array-_-exportedcontacttoken-url-string-expires-int-see-https-docs-madelineproto-xyz-api_docs-types-exportedcontacttoken-htm)
* [`importContactToken(string $token = ''): array|int|\string @see https://docs.madelineproto.xyz/API_docs/types/User.html`](#importcontacttoken-string-token-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-user-html)

## Methods:
### `getContactIDs(list<int> $hash = []): list<int>`

Get contact by telegram IDs


Parameters:

* `$hash`: `list<int>` [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)  



### `getStatuses(): \list<array{_: "contactStatus", status: array{_: "userStatusEmpty"}|array{_: "userStatusOnline", expires: int}|array{_: "userStatusOffline", was_online: int}|array{_: "userStatusRecently"}|array{_: "userStatusLastWeek"}|array{_: "userStatusLastMonth"}, user_id: int}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/ContactStatus.html`

Returns the list of contact statuses.


Return value: Array of  @see https://docs.madelineproto.xyz/API_docs/types/ContactStatus.html


### `getContacts(list<int> $hash = []): array{_: \"contacts.contactsNotModified"}|array{_: \"contacts.contacts", contacts: list<array{_: \"contact", mutual: bool, user_id: int}>, saved_count: int, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/contacts.Contacts.htm}`

Returns the current user's contact list.


Parameters:

* `$hash`: `list<int>` If there already is a full contact list on the client, a [hash](https://core.telegram.org/api/offsets#hash-generation) of a the list of contact IDs in ascending order may be passed in this parameter. If the contact set was not changed, [(contacts.contactsNotModified)](https://docs.madelineproto.xyz/API_docs/constructors/contacts.contactsNotModified.html) will be returned.  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/contacts.Contacts.html


### `importContacts(list<array{_: \"inputPhoneContact", client_id?: int, phone?: string, first_name?: string, last_name?: string}> $contacts = []): array{_: \"contacts.importedContacts", imported: list<array{_: \"importedContact", user_id: int, client_id: int}>, popular_invites: list<array{_: \"popularContact", client_id: int, importers: int}>, retry_contacts: list<int>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/contacts.ImportedContacts.htm}`

Imports contacts: saves a full list on the server, adds already registered contacts to the contact list, returns added contacts and their info.
Use [contacts.addContact](https://docs.madelineproto.xyz/API_docs/methods/contacts.addContact.html) to add Telegram contacts without actually using their phone number.

Parameters:

* `$contacts`: `list<array{_: \"inputPhoneContact", client_id?: int, phone?: string, first_name?: string, last_name?: string}>` Array of List of contacts to import @see https://docs.madelineproto.xyz/API_docs/types/InputContact.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/contacts.ImportedContacts.html


### `deleteContacts(list<array|int|string> $id = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Deletes several contacts from the list.


Parameters:

* `$id`: `list<array|int|string>` Array of User ID list @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `deleteByPhones(list<string> $phones = []): bool`

Delete contacts by phone number


Parameters:

* `$phones`: `list<string>` Phone numbers  



### `block(array|int|string $id): bool`

Adds the user to the blacklist.


Parameters:

* `$id`: `array|int|string` User ID @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  



### `unblock(array|int|string $id): bool`

Deletes the user from the blacklist.


Parameters:

* `$id`: `array|int|string` User ID @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  



### `getBlocked(int $offset = 0, int $limit = 0): array{_: \"contacts.blocked", blocked: list<array{_: \"peerBlocked", peer_id: array|int|string, date: int}>, chats: list<array|int|string>, users: list<array|int|string>}|array{_: \"contacts.blockedSlice", count: int, blocked: list<array{_: \"peerBlocked", peer_id: array|int|string, date: int}>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/contacts.Blocked.htm}`

Returns the list of blocked users.


Parameters:

* `$offset`: `int` The number of list elements to be skipped  
* `$limit`: `int` The number of list elements to be returned  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/contacts.Blocked.html


### `search(string $q = '', int $limit = 0): array{_: \"contacts.found", my_results: list<array|int|string>, results: list<array|int|string>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/contacts.Found.htm}`

Returns users found by username substring.


Parameters:

* `$q`: `string` Target substring  
* `$limit`: `int` Maximum number of users to be returned  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/contacts.Found.html


### `getTopPeers(bool $correspondents = false, bool $bots_pm = false, bool $bots_inline = false, bool $phone_calls = false, bool $forward_users = false, bool $forward_chats = false, bool $groups = false, bool $channels = false, int $offset = 0, int $limit = 0, list<int> $hash = []): array{_: \"contacts.topPeersNotModified"}|array{_: \"contacts.topPeers", categories: list<array{_: \"topPeerCategoryPeers", category: array{_: \"topPeerCategoryBotsPM"}|array{_: \"topPeerCategoryBotsInline"}|array{_: \"topPeerCategoryCorrespondents"}|array{_: \"topPeerCategoryGroups"}|array{_: \"topPeerCategoryChannels"}|array{_: \"topPeerCategoryPhoneCalls"}|array{_: \"topPeerCategoryForwardUsers"}|array{_: \"topPeerCategoryForwardChats"}, count: int, peers: list<array{_: \"topPeer", peer: array|int|string, rating: float}>}>, chats: list<array|int|string>, users: list<array|int|string>}|array{_: \"contacts.topPeersDisabled"} @see https://docs.madelineproto.xyz/API_docs/types/contacts.TopPeers.htm}`

Get most used peers


Parameters:

* `$correspondents`: `bool` Users we've chatted most frequently with  
* `$bots_pm`: `bool` Most used bots  
* `$bots_inline`: `bool` Most used inline bots  
* `$phone_calls`: `bool` Most frequently called users  
* `$forward_users`: `bool` Users to which the users often forwards messages to  
* `$forward_chats`: `bool` Chats to which the users often forwards messages to  
* `$groups`: `bool` Often-opened groups and supergroups  
* `$channels`: `bool` Most frequently visited channels  
* `$offset`: `int` Offset for [pagination](https://core.telegram.org/api/offsets)  
* `$limit`: `int` Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets)  
* `$hash`: `list<int>` [Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/contacts.TopPeers.html


### `resetTopPeerRating(array{_: \"topPeerCategoryBotsPM"}|array{_: \"topPeerCategoryBotsInline"}|array{_: \"topPeerCategoryCorrespondents"}|array{_: \"topPeerCategoryGroups"}|array{_: \"topPeerCategoryChannels"}|array{_: \"topPeerCategoryPhoneCalls"}|array{_: \"topPeerCategoryForwardUsers"}|array{_: \"topPeerCategoryForwardChats"} $category, array|int|string $peer): bool`

Reset [rating](https://core.telegram.org/api/top-rating) of top peer


Parameters:

* `$category`: `array{_: \"topPeerCategoryBotsPM"}|array{_: \"topPeerCategoryBotsInline"}|array{_: \"topPeerCategoryCorrespondents"}|array{_: \"topPeerCategoryGroups"}|array{_: \"topPeerCategoryChannels"}|array{_: \"topPeerCategoryPhoneCalls"}|array{_: \"topPeerCategoryForwardUsers"}|array{_: \"topPeerCategoryForwardChats"}` Top peer category @see https://docs.madelineproto.xyz/API_docs/types/TopPeerCategory.html  
* `$peer`: `array|int|string` Peer whose rating should be reset @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  



### `resetSaved(): bool`

Delete saved contacts



### `getSaved(): \list<array{_: "savedPhoneContact", phone: string, first_name: string, last_name: string, date: int}> Array of  @see https://docs.madelineproto.xyz/API_docs/types/SavedContact.html`

Get all contacts


Return value: Array of  @see https://docs.madelineproto.xyz/API_docs/types/SavedContact.html


### `toggleTopPeers(bool $enabled): bool`

Enable/disable [top peers](https://core.telegram.org/api/top-rating)


Parameters:

* `$enabled`: `bool` Enable/disable  



### `addContact(array|int|string $id, bool $add_phone_privacy_exception = false, string $first_name = '', string $last_name = '', string $phone = ''): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Add an existing telegram user as contact.
Use [contacts.importContacts](https://docs.madelineproto.xyz/API_docs/methods/contacts.importContacts.html) to add contacts by phone number, without knowing their Telegram ID.

Parameters:

* `$id`: `array|int|string` Telegram ID of the other user @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  
* `$add_phone_privacy_exception`: `bool` Allow the other user to see our phone number?  
* `$first_name`: `string` First name  
* `$last_name`: `string` Last name  
* `$phone`: `string` User's phone number  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `acceptContact(array|int|string $id): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

If the [peer settings](https://docs.madelineproto.xyz/API_docs/constructors/peerSettings.html) of a new user allow us to add them as contact, add that user as contact


Parameters:

* `$id`: `array|int|string` The user to add as contact @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `getLocated(array{_: \"inputGeoPointEmpty"}|array{_: \"inputGeoPoint", lat: float, long: float, accuracy_radius?: int} $geo_point, bool $background = false, int $self_expires = 0): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Get contacts near you


Parameters:

* `$geo_point`: `array{_: \"inputGeoPointEmpty"}|array{_: \"inputGeoPoint", lat: float, long: float, accuracy_radius?: int}` Geolocation @see https://docs.madelineproto.xyz/API_docs/types/InputGeoPoint.html  
* `$background`: `bool` While the geolocation of the current user is public, clients should update it in the background every half-an-hour or so, while setting this flag. <br>Do this only if the new location is more than 1 KM away from the previous one, or if the previous location is unknown.  
* `$self_expires`: `int` If set, the geolocation of the current user will be public for the specified number of seconds; pass 0x7fffffff to disable expiry, 0 to make the current geolocation private; if the flag isn't set, no changes will be applied.  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `blockFromReplies(bool $delete_message = false, bool $delete_history = false, bool $report_spam = false, int $msg_id = 0): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Stop getting notifications about [thread replies](https://core.telegram.org/api/threads) of a certain user in `@replies`


Parameters:

* `$delete_message`: `bool` Whether to delete the specified message as well  
* `$delete_history`: `bool` Whether to delete all `@replies` messages from this user as well  
* `$report_spam`: `bool` Whether to also report this user for spam  
* `$msg_id`: `int` ID of the message in the [@replies](https://core.telegram.org/api/threads#replies) chat  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `resolvePhone(string $phone = ''): array{_: \"contacts.resolvedPeer", peer: array|int|string, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/contacts.ResolvedPeer.htm}`

Resolve a phone number to get user info, if their privacy settings allow it.


Parameters:

* `$phone`: `string` Phone number in international format, possibly obtained from a [phone number deep link](https://core.telegram.org/api/links#phone-number-links).  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/contacts.ResolvedPeer.html


### `exportContactToken(): array{_: \"exportedContactToken", url: string, expires: \int} @see https://docs.madelineproto.xyz/API_docs/types/ExportedContactToken.htm}`

Generates a [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links) for the currently logged-in user.


Return value: @see https://docs.madelineproto.xyz/API_docs/types/ExportedContactToken.html


### `importContactToken(string $token = ''): array|int|\string @see https://docs.madelineproto.xyz/API_docs/types/User.html`

Obtain user info from a [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links).


Parameters:

* `$token`: `string` The token extracted from the [temporary profile link](https://core.telegram.org/api/links#temporary-profile-links).  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/User.html


---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
