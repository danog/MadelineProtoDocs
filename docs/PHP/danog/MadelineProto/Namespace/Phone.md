---
title: "danog\\MadelineProto\\Namespace\\Phone: "
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Namespace\Phone`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

  




## Method list:
* [`getCallConfig(): \mixed Any JSON-encodable data`](#getcallconfig-mixed-any-json-encodable-data)
* [`receivedCall(array{_: \"inputPhoneCall", id?: int, access_hash?: int} $peer): bool`](#receivedcall-array-_-inputphonecall-id-int-access_hash-int-peer-bool)
* [`setCallRating(array{_: \"inputPhoneCall", id?: int, access_hash?: int} $peer, bool $user_initiative = false, int $rating = 0, string $comment = ''): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#setcallrating-array-_-inputphonecall-id-int-access_hash-int-peer-bool-user_initiative-false-int-rating-0-string-comment-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`saveCallDebug(array{_: \"inputPhoneCall", id?: int, access_hash?: int} $peer, mixed $debug): bool`](#savecalldebug-array-_-inputphonecall-id-int-access_hash-int-peer-mixed-debug-bool)
* [`sendSignalingData(array{_: \"inputPhoneCall", id?: int, access_hash?: int} $peer, string $data = ''): bool`](#sendsignalingdata-array-_-inputphonecall-id-int-access_hash-int-peer-string-data-bool)
* [`createGroupCall(array|int|string $peer, bool $rtmp_stream = false, string $title = '', int $schedule_date = 0): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#creategroupcall-array-int-string-peer-bool-rtmp_stream-false-string-title-int-schedule_date-0-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`joinGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, array|int|string $join_as, mixed $params, bool $muted = false, bool $video_stopped = false, string $invite_hash = ''): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#joingroupcall-array-_-inputgroupcall-id-int-access_hash-int-call-array-int-string-join_as-mixed-params-bool-muted-false-bool-video_stopped-false-string-invite_hash-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`leaveGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, int $source = 0): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#leavegroupcall-array-_-inputgroupcall-id-int-access_hash-int-call-int-source-0-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`inviteToGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, list<array|int|string> $users = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#invitetogroupcall-array-_-inputgroupcall-id-int-access_hash-int-call-list-array-int-string-users-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`discardGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#discardgroupcall-array-_-inputgroupcall-id-int-access_hash-int-call-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`toggleGroupCallSettings(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, bool $reset_invite_hash = false, bool $join_muted = false): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#togglegroupcallsettings-array-_-inputgroupcall-id-int-access_hash-int-call-bool-reset_invite_hash-false-bool-join_muted-false-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`getGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, int $limit = 0): array{_: \"phone.groupCall", call: array{_: \"groupCallDiscarded", id: int, access_hash: int, duration: int}|array{_: \"groupCall", join_muted: bool, can_change_join_muted: bool, join_date_asc: bool, schedule_start_subscribed: bool, can_start_video: bool, record_video_active: bool, rtmp_stream: bool, listeners_hidden: bool, id: int, access_hash: int, participants_count: int, title: string, stream_dc_id: int, record_start_date: int, schedule_date: int, unmuted_video_count: int, unmuted_video_limit: int, version: int}, participants: list<array{_: \"groupCallParticipant", peer: array|int|string, muted: bool, left: bool, can_self_unmute: bool, just_joined: bool, versioned: bool, min: bool, muted_by_you: bool, volume_by_admin: bool, self: bool, video_joined: bool, date: int, active_date: int, source: int, volume: int, about: string, raise_hand_rating: int, video?: array{_: \"groupCallParticipantVideo", paused: bool, endpoint: string, source_groups: list<array{_: \"groupCallParticipantVideoSourceGroup", semantics: string, sources: list<int>}>, audio_source: int}, presentation?: array{_: \"groupCallParticipantVideo", paused: bool, endpoint: string, source_groups: list<array{_: \"groupCallParticipantVideoSourceGroup", semantics: string, sources: list<int>}>, audio_source: int}}>, participants_next_offset: string, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupCall.htm}`](#getgroupcall-array-_-inputgroupcall-id-int-access_hash-int-call-int-limit-0-array-_-phone-groupcall-call-array-_-groupcalldiscarded-id-int-access_hash-int-duration-int-array-_-groupcall-join_muted-bool-can_change_join_muted-bool-join_date_asc-bool-schedule_start_subscribed-bool-can_start_video-bool-record_video_active-bool-rtmp_stream-bool-listeners_hidden-bool-id-int-access_hash-int-participants_count-int-title-string-stream_dc_id-int-record_start_date-int-schedule_date-int-unmuted_video_count-int-unmuted_video_limit-int-version-int-participants-list-array-_-groupcallparticipant-peer-array-int-string-muted-bool-left-bool-can_self_unmute-bool-just_joined-bool-versioned-bool-min-bool-muted_by_you-bool-volume_by_admin-bool-self-bool-video_joined-bool-date-int-active_date-int-source-int-volume-int-about-string-raise_hand_rating-int-video-array-_-groupcallparticipantvideo-paused-bool-endpoint-string-source_groups-list-array-_-groupcallparticipantvideosourcegroup-semantics-string-sources-list-int-audio_source-int-presentation-array-_-groupcallparticipantvideo-paused-bool-endpoint-string-source_groups-list-array-_-groupcallparticipantvideosourcegroup-semantics-string-sources-list-int-audio_source-int-participants_next_offset-string-chats-list-array-int-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-phone-groupcall-htm)
* [`getGroupParticipants(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, list<array|int|string> $ids = [], list<int> $sources = [], string $offset = '', int $limit = 0): array{_: \"phone.groupParticipants", count: int, participants: list<array{_: \"groupCallParticipant", peer: array|int|string, muted: bool, left: bool, can_self_unmute: bool, just_joined: bool, versioned: bool, min: bool, muted_by_you: bool, volume_by_admin: bool, self: bool, video_joined: bool, date: int, active_date: int, source: int, volume: int, about: string, raise_hand_rating: int, video?: array{_: \"groupCallParticipantVideo", paused: bool, endpoint: string, source_groups: list<array{_: \"groupCallParticipantVideoSourceGroup", semantics: string, sources: list<int>}>, audio_source: int}, presentation?: array{_: \"groupCallParticipantVideo", paused: bool, endpoint: string, source_groups: list<array{_: \"groupCallParticipantVideoSourceGroup", semantics: string, sources: list<int>}>, audio_source: int}}>, next_offset: string, chats: list<array|int|string>, users: list<array|int|string>, version: \int} @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupParticipants.htm}`](#getgroupparticipants-array-_-inputgroupcall-id-int-access_hash-int-call-list-array-int-string-ids-list-int-sources-string-offset-int-limit-0-array-_-phone-groupparticipants-count-int-participants-list-array-_-groupcallparticipant-peer-array-int-string-muted-bool-left-bool-can_self_unmute-bool-just_joined-bool-versioned-bool-min-bool-muted_by_you-bool-volume_by_admin-bool-self-bool-video_joined-bool-date-int-active_date-int-source-int-volume-int-about-string-raise_hand_rating-int-video-array-_-groupcallparticipantvideo-paused-bool-endpoint-string-source_groups-list-array-_-groupcallparticipantvideosourcegroup-semantics-string-sources-list-int-audio_source-int-presentation-array-_-groupcallparticipantvideo-paused-bool-endpoint-string-source_groups-list-array-_-groupcallparticipantvideosourcegroup-semantics-string-sources-list-int-audio_source-int-next_offset-string-chats-list-array-int-string-users-list-array-int-string-version-int-see-https-docs-madelineproto-xyz-api_docs-types-phone-groupparticipants-htm)
* [`checkGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, list<int> $sources = []): list<int>`](#checkgroupcall-array-_-inputgroupcall-id-int-access_hash-int-call-list-int-sources-list-int)
* [`toggleGroupCallRecord(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, bool $start = false, bool $video = false, string $title = '', bool $video_portrait = false): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#togglegroupcallrecord-array-_-inputgroupcall-id-int-access_hash-int-call-bool-start-false-bool-video-false-string-title-bool-video_portrait-false-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`editGroupCallParticipant(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, array|int|string $participant, bool $muted = false, int $volume = 0, bool $raise_hand = false, bool $video_stopped = false, bool $video_paused = false, bool $presentation_paused = false): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#editgroupcallparticipant-array-_-inputgroupcall-id-int-access_hash-int-call-array-int-string-participant-bool-muted-false-int-volume-0-bool-raise_hand-false-bool-video_stopped-false-bool-video_paused-false-bool-presentation_paused-false-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`editGroupCallTitle(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, string $title = ''): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#editgroupcalltitle-array-_-inputgroupcall-id-int-access_hash-int-call-string-title-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`getGroupCallJoinAs(array|int|string $peer): array{_: \"phone.joinAsPeers", peers: list<array|int|string>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/phone.JoinAsPeers.htm}`](#getgroupcalljoinas-array-int-string-peer-array-_-phone-joinaspeers-peers-list-array-int-string-chats-list-array-int-string-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-phone-joinaspeers-htm)
* [`exportGroupCallInvite(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, bool $can_self_unmute = false): array{_: \"phone.exportedGroupCallInvite", link: \string} @see https://docs.madelineproto.xyz/API_docs/types/phone.ExportedGroupCallInvite.htm}`](#exportgroupcallinvite-array-_-inputgroupcall-id-int-access_hash-int-call-bool-can_self_unmute-false-array-_-phone-exportedgroupcallinvite-link-string-see-https-docs-madelineproto-xyz-api_docs-types-phone-exportedgroupcallinvite-htm)
* [`toggleGroupCallStartSubscription(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, bool $subscribed): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#togglegroupcallstartsubscription-array-_-inputgroupcall-id-int-access_hash-int-call-bool-subscribed-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`startScheduledGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#startscheduledgroupcall-array-_-inputgroupcall-id-int-access_hash-int-call-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`saveDefaultGroupCallJoinAs(array|int|string $peer, array|int|string $join_as): bool`](#savedefaultgroupcalljoinas-array-int-string-peer-array-int-string-join_as-bool)
* [`joinGroupCallPresentation(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, mixed $params): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#joingroupcallpresentation-array-_-inputgroupcall-id-int-access_hash-int-call-mixed-params-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`leaveGroupCallPresentation(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`](#leavegroupcallpresentation-array-_-inputgroupcall-id-int-access_hash-int-call-array-see-https-docs-madelineproto-xyz-api_docs-types-updates-html)
* [`getGroupCallStreamChannels(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call): array{_: \"phone.groupCallStreamChannels", channels: \list<array{_: "groupCallStreamChannel", channel: int, scale: int, last_timestamp_ms: int}>} @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupCallStreamChannels.htm}`](#getgroupcallstreamchannels-array-_-inputgroupcall-id-int-access_hash-int-call-array-_-phone-groupcallstreamchannels-channels-list-array-_-groupcallstreamchannel-channel-int-scale-int-last_timestamp_ms-int-see-https-docs-madelineproto-xyz-api_docs-types-phone-groupcallstreamchannels-htm)
* [`getGroupCallStreamRtmpUrl(array|int|string $peer, bool $revoke): array{_: \"phone.groupCallStreamRtmpUrl", url: string, key: \string} @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupCallStreamRtmpUrl.htm}`](#getgroupcallstreamrtmpurl-array-int-string-peer-bool-revoke-array-_-phone-groupcallstreamrtmpurl-url-string-key-string-see-https-docs-madelineproto-xyz-api_docs-types-phone-groupcallstreamrtmpurl-htm)
* [`saveCallLog(array{_: \"inputPhoneCall", id?: int, access_hash?: int} $peer, mixed $file): bool`](#savecalllog-array-_-inputphonecall-id-int-access_hash-int-peer-mixed-file-bool)

## Methods:
### `getCallConfig(): \mixed Any JSON-encodable data`

Get phone call configuration to be passed to libtgvoip's shared config


Return value: Any JSON-encodable data


### `receivedCall(array{_: \"inputPhoneCall", id?: int, access_hash?: int} $peer): bool`

Optional: notify the server that the user is currently busy in a call: this will automatically refuse all incoming phone calls until the current phone call is ended.


Parameters:

* `$peer`: `array{_: \"inputPhoneCall", id?: int, access_hash?: int}` The phone call we're currently in @see https://docs.madelineproto.xyz/API_docs/types/InputPhoneCall.html  



### `setCallRating(array{_: \"inputPhoneCall", id?: int, access_hash?: int} $peer, bool $user_initiative = false, int $rating = 0, string $comment = ''): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Rate a call, returns info about the rating message sent to the official VoIP bot.


Parameters:

* `$peer`: `array{_: \"inputPhoneCall", id?: int, access_hash?: int}` The call to rate @see https://docs.madelineproto.xyz/API_docs/types/InputPhoneCall.html  
* `$user_initiative`: `bool` Whether the user decided on their own initiative to rate the call  
* `$rating`: `int` Rating in `1-5` stars  
* `$comment`: `string` An additional comment  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `saveCallDebug(array{_: \"inputPhoneCall", id?: int, access_hash?: int} $peer, mixed $debug): bool`

Send phone call debug data to server


Parameters:

* `$peer`: `array{_: \"inputPhoneCall", id?: int, access_hash?: int}` Phone call @see https://docs.madelineproto.xyz/API_docs/types/InputPhoneCall.html  
* `$debug`: `mixed` Any JSON-encodable data  



### `sendSignalingData(array{_: \"inputPhoneCall", id?: int, access_hash?: int} $peer, string $data = ''): bool`

Send VoIP signaling data


Parameters:

* `$peer`: `array{_: \"inputPhoneCall", id?: int, access_hash?: int}` Phone call @see https://docs.madelineproto.xyz/API_docs/types/InputPhoneCall.html  
* `$data`: `string` Signaling payload  



### `createGroupCall(array|int|string $peer, bool $rtmp_stream = false, string $title = '', int $schedule_date = 0): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Create a group call or livestream


Parameters:

* `$peer`: `array|int|string` Associate the group call or livestream to the provided [group/supergroup/channel](https://core.telegram.org/api/channel) @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  
* `$rtmp_stream`: `bool` Whether RTMP stream support should be enabled: only the [group/supergroup/channel](https://core.telegram.org/api/channel) owner can use this flag.  
* `$title`: `string` Call title  
* `$schedule_date`: `int` For scheduled group call or livestreams, the absolute date when the group call will start  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `joinGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, array|int|string $join_as, mixed $params, bool $muted = false, bool $video_stopped = false, string $invite_hash = ''): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Join a group call


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` The group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$join_as`: `array|int|string` Join the group call, presenting yourself as the specified user/channel @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  
* `$params`: `mixed` Any JSON-encodable data  
* `$muted`: `bool` If set, the user will be muted by default upon joining.  
* `$video_stopped`: `bool` If set, the user's video will be disabled by default upon joining.  
* `$invite_hash`: `string` The invitation hash from the [invite link »](https://core.telegram.org/api/links#video-chatlivestream-links), if provided allows speaking in a livestream or muted group chat.  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `leaveGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, int $source = 0): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Leave a group call


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` The group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$source`: `int` Your source ID  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `inviteToGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, list<array|int|string> $users = []): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Invite a set of users to a group call.


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` The group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$users`: `list<array|int|string>` Array of The users to invite. @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `discardGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Terminate a group call


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` The group call to terminate @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `toggleGroupCallSettings(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, bool $reset_invite_hash = false, bool $join_muted = false): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Change group call settings


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` Group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$reset_invite_hash`: `bool` Invalidate existing invite links  
* `$join_muted`: `bool` Whether all users will that join this group call are muted by default upon joining the group call  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `getGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, int $limit = 0): array{_: \"phone.groupCall", call: array{_: \"groupCallDiscarded", id: int, access_hash: int, duration: int}|array{_: \"groupCall", join_muted: bool, can_change_join_muted: bool, join_date_asc: bool, schedule_start_subscribed: bool, can_start_video: bool, record_video_active: bool, rtmp_stream: bool, listeners_hidden: bool, id: int, access_hash: int, participants_count: int, title: string, stream_dc_id: int, record_start_date: int, schedule_date: int, unmuted_video_count: int, unmuted_video_limit: int, version: int}, participants: list<array{_: \"groupCallParticipant", peer: array|int|string, muted: bool, left: bool, can_self_unmute: bool, just_joined: bool, versioned: bool, min: bool, muted_by_you: bool, volume_by_admin: bool, self: bool, video_joined: bool, date: int, active_date: int, source: int, volume: int, about: string, raise_hand_rating: int, video?: array{_: \"groupCallParticipantVideo", paused: bool, endpoint: string, source_groups: list<array{_: \"groupCallParticipantVideoSourceGroup", semantics: string, sources: list<int>}>, audio_source: int}, presentation?: array{_: \"groupCallParticipantVideo", paused: bool, endpoint: string, source_groups: list<array{_: \"groupCallParticipantVideoSourceGroup", semantics: string, sources: list<int>}>, audio_source: int}}>, participants_next_offset: string, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupCall.htm}`

Get info about a group call


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` The group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$limit`: `int` Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupCall.html


### `getGroupParticipants(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, list<array|int|string> $ids = [], list<int> $sources = [], string $offset = '', int $limit = 0): array{_: \"phone.groupParticipants", count: int, participants: list<array{_: \"groupCallParticipant", peer: array|int|string, muted: bool, left: bool, can_self_unmute: bool, just_joined: bool, versioned: bool, min: bool, muted_by_you: bool, volume_by_admin: bool, self: bool, video_joined: bool, date: int, active_date: int, source: int, volume: int, about: string, raise_hand_rating: int, video?: array{_: \"groupCallParticipantVideo", paused: bool, endpoint: string, source_groups: list<array{_: \"groupCallParticipantVideoSourceGroup", semantics: string, sources: list<int>}>, audio_source: int}, presentation?: array{_: \"groupCallParticipantVideo", paused: bool, endpoint: string, source_groups: list<array{_: \"groupCallParticipantVideoSourceGroup", semantics: string, sources: list<int>}>, audio_source: int}}>, next_offset: string, chats: list<array|int|string>, users: list<array|int|string>, version: \int} @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupParticipants.htm}`

Get group call participants


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` Group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$ids`: `list<array|int|string>` Array of If specified, will fetch group participant info about the specified peers @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  
* `$sources`: `list<int>` If specified, will fetch group participant info about the specified WebRTC source IDs  
* `$offset`: `string` Offset for results, taken from the `next_offset` field of [phone.groupParticipants](https://docs.madelineproto.xyz/API_docs/constructors/phone.groupParticipants.html), initially an empty string. <br>Note: if no more results are available, the method call will return an empty `next_offset`; thus, avoid providing the `next_offset` returned in [phone.groupParticipants](https://docs.madelineproto.xyz/API_docs/constructors/phone.groupParticipants.html) if it is empty, to avoid an infinite loop.  
* `$limit`: `int` Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets)  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupParticipants.html


### `checkGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, list<int> $sources = []): list<int>`

Check whether the group call Server Forwarding Unit is currently receiving the streams with the specified WebRTC source IDs.
Returns an intersection of the source IDs specified in `sources`, and the source IDs currently being forwarded by the SFU.

Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` Group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$sources`: `list<int>` Source IDs  



### `toggleGroupCallRecord(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, bool $start = false, bool $video = false, string $title = '', bool $video_portrait = false): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Start or stop recording a group call: the recorded audio and video streams will be automatically sent to `Saved messages` (the chat with ourselves).


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` The group call or livestream @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$start`: `bool` Whether to start or stop recording  
* `$video`: `bool` Whether to also record video streams  
* `$title`: `string` Recording title  
* `$video_portrait`: `bool` If video stream recording is enabled, whether to record in portrait or landscape mode  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `editGroupCallParticipant(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, array|int|string $participant, bool $muted = false, int $volume = 0, bool $raise_hand = false, bool $video_stopped = false, bool $video_paused = false, bool $presentation_paused = false): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Edit information about a given group call participant
Note: [flags](https://core.telegram.org/mtproto/TL-combinators#conditional-fields).N?[Bool](https://docs.madelineproto.xyz/API_docs/types/Bool.html) parameters can have three possible values:  
  
- If the [TL flag](https://core.telegram.org/mtproto/TL-combinators#conditional-fields) is not set, the previous value will not be changed.  
- If the [TL flag](https://core.telegram.org/mtproto/TL-combinators#conditional-fields) is set and contains a [boolTrue](https://docs.madelineproto.xyz/API_docs/constructors/boolTrue.html), the previous value will be overwritten to `true`.  
- If the [TL flag](https://core.telegram.org/mtproto/TL-combinators#conditional-fields) is set and contains a [boolFalse](https://docs.madelineproto.xyz/API_docs/constructors/boolFalse.html), the previous value will be overwritten to `false`.

Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` The group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$participant`: `array|int|string` The group call participant (can also be the user itself) @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  
* `$muted`: `bool` Whether to mute or unmute the specified participant  
* `$volume`: `int` New volume  
* `$raise_hand`: `bool` Raise or lower hand  
* `$video_stopped`: `bool` Start or stop the video stream  
* `$video_paused`: `bool` Pause or resume the video stream  
* `$presentation_paused`: `bool` Pause or resume the screen sharing stream  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `editGroupCallTitle(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, string $title = ''): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Edit the title of a group call or livestream


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` Group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$title`: `string` New title  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `getGroupCallJoinAs(array|int|string $peer): array{_: \"phone.joinAsPeers", peers: list<array|int|string>, chats: list<array|int|string>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/phone.JoinAsPeers.htm}`

Get a list of peers that can be used to join a group call, presenting yourself as a specific user/channel.


Parameters:

* `$peer`: `array|int|string` The dialog whose group call or livestream we're trying to join @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/phone.JoinAsPeers.html


### `exportGroupCallInvite(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, bool $can_self_unmute = false): array{_: \"phone.exportedGroupCallInvite", link: \string} @see https://docs.madelineproto.xyz/API_docs/types/phone.ExportedGroupCallInvite.htm}`

Get an [invite link](https://core.telegram.org/api/links#video-chatlivestream-links) for a group call or livestream


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` The group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$can_self_unmute`: `bool` For livestreams or muted group chats, if set, users that join using this link will be able to speak without explicitly requesting permission by (for example by raising their hand).  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/phone.ExportedGroupCallInvite.html


### `toggleGroupCallStartSubscription(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, bool $subscribed): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Subscribe or unsubscribe to a scheduled group call


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` Scheduled group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$subscribed`: `bool` Enable or disable subscription  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `startScheduledGroupCall(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Start a scheduled group call.


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` The scheduled group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `saveDefaultGroupCallJoinAs(array|int|string $peer, array|int|string $join_as): bool`

Set the default peer that will be used to join a group call in a specific dialog.


Parameters:

* `$peer`: `array|int|string` The dialog @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  
* `$join_as`: `array|int|string` The default peer that will be used to join group calls in this dialog, presenting yourself as a specific user/channel. @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  



### `joinGroupCallPresentation(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call, mixed $params): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Start screen sharing in a call


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` The group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  
* `$params`: `mixed` Any JSON-encodable data  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `leaveGroupCallPresentation(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call): \array @see https://docs.madelineproto.xyz/API_docs/types/Updates.html`

Stop screen sharing in a group call


Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` The group call @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/Updates.html


### `getGroupCallStreamChannels(array{_: \"inputGroupCall", id?: int, access_hash?: int} $call): array{_: \"phone.groupCallStreamChannels", channels: \list<array{_: "groupCallStreamChannel", channel: int, scale: int, last_timestamp_ms: int}>} @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupCallStreamChannels.htm}`

Get info about RTMP streams in a group call or livestream.
This method should be invoked to the same group/channel-related DC used for [downloading livestream chunks](https://core.telegram.org/api/files#downloading-files).  
As usual, the media DC is preferred, if available.

Parameters:

* `$call`: `array{_: \"inputGroupCall", id?: int, access_hash?: int}` Group call or livestream @see https://docs.madelineproto.xyz/API_docs/types/InputGroupCall.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupCallStreamChannels.html


### `getGroupCallStreamRtmpUrl(array|int|string $peer, bool $revoke): array{_: \"phone.groupCallStreamRtmpUrl", url: string, key: \string} @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupCallStreamRtmpUrl.htm}`

Get RTMP URL and stream key for RTMP livestreams. Can be used even before creating the actual RTMP livestream with [phone.createGroupCall](https://docs.madelineproto.xyz/API_docs/methods/phone.createGroupCall.html) (the `rtmp_stream` flag must be set).


Parameters:

* `$peer`: `array|int|string` Peer to livestream into @see https://docs.madelineproto.xyz/API_docs/types/InputPeer.html  
* `$revoke`: `bool` Whether to revoke the previous stream key or simply return the existing one  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/phone.GroupCallStreamRtmpUrl.html


### `saveCallLog(array{_: \"inputPhoneCall", id?: int, access_hash?: int} $peer, mixed $file): bool`

Save phone call debug information


Parameters:

* `$peer`: `array{_: \"inputPhoneCall", id?: int, access_hash?: int}` Phone call @see https://docs.madelineproto.xyz/API_docs/types/InputPhoneCall.html  
* `$file`: `mixed` A file name or a file URL. You can also use amphp async streams, amphp HTTP response objects, and [much more](https://docs.madelineproto.xyz/docs/FILES.html#downloading-files)!  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
