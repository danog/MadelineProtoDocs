---
title: "danog\\MadelineProto\\EventHandler\\Calls\\LiveStory: This update represents a Telegram [live story »](https://core.telegram.org/api/group-calls#live-stories):"
description: "a livestream posted as a story by a user, group or channel, of which the poster is the only\npublisher; everyone else joins as a listener.\n\nOn top of what every group call offers ({@see AbstractGroupCall}), a live story takes paid comments\nand Telegram Stars donations. It has no title (its caption is the story's), cannot be scheduled or\nrecorded server-side, and does not support screen sharing.\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\Calls\LiveStory`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

This update represents a Telegram [live story »](https://core.telegram.org/api/group-calls#live-stories):  

a livestream posted as a story by a user, group or channel, of which the poster is the only
publisher; everyone else joins as a listener.

On top of what every group call offers ({@see AbstractGroupCall}), a live story takes paid comments
and Telegram Stars donations. It has no title (its caption is the story's), cannot be scheduled or
recorded server-side, and does not support screen sharing.


## Properties
* `$sendPaidMessagesStars`: `?int` The minimum Telegram Stars donation required to comment, if any.
* `$defaultSendAs`: `?int` Bot API ID of the peer we send in-call messages as by default.
* `$id`: `int` Group call ID.
* `$accessHash`: `int` Access hash of the group call.
* `$peerId`: `?int` Bot API ID of the peer the call belongs to (the group or channel of a video chat, the poster of a live story), if known.
* `$participantsCount`: `int` Number of participants.
* `$joinMuted`: `bool` Whether new participants join muted.
* `$canChangeJoinMuted`: `bool` Whether we may change whether new participants join muted (admins).
* `$joinDateAsc`: `bool` Whether participants are sorted by join date (ascending) rather than by activity.
* `$canStartVideo`: `bool` Whether we may start streaming video (the video limit is not reached yet).
* `$rtmpStream`: `bool` Whether the media is published by an external RTMP application rather than by a participant.
* `$listenersHidden`: `bool` Whether the listeners are hidden.
* `$creator`: `bool` Whether we created this call.
* `$messagesEnabled`: `bool` Whether in-call messages are enabled.
* `$canChangeMessagesEnabled`: `bool` Whether we may enable or disable in-call messages (admins).
* `$inviteLink`: `?string` The invite link of the call, if any.
* `$unmutedVideoCount`: `?int` How many participants are transmitting video.
* `$unmutedVideoLimit`: `int` How many participants may transmit video at once.
* `$streamDcId`: `?int` The DC to use when downloading media chunks in stream mode.
* `$discarded`: `bool` Whether the call has ended.
* `$duration`: `?int` Duration of the call in seconds, once it has ended.

## Method list:
* [`setTitle(string $title): static`](#setTitle)
* [`invite(mixed ...$users): static`](#invite)
* [`exportInvite(bool $canSelfUnmute = false): string`](#exportInvite)
* [`removeParticipant(mixed ...$participants): static`](#removeParticipant)
* [`enablePresentation(): static`](#enablePresentation)
* [`donate(int $stars): \danog\MadelineProto\EventHandler\Calls\LiveStory`](#donate)
* [`getStars(): \danog\MadelineProto\GroupCall\GroupCallStars`](#getStars)
* [`setDefaultSendAs(mixed $peer): \danog\MadelineProto\EventHandler\Calls\LiveStory`](#setDefaultSendAs)
* [`setPaidMessagesStars(?int $stars): \danog\MadelineProto\EventHandler\Calls\LiveStory`](#setPaidMessagesStars)
* [`join(bool $muted = false): static`](#join)
* [`leave(): static`](#leave)
* [`discard(): static`](#discard)
* [`isJoined(): bool`](#isJoined)
* [`getCallState(): \danog\MadelineProto\GroupCall\GroupCallState`](#getCallState)
* [`getParticipants(): array<int, \danog\MadelineProto\GroupCall\Participant>`](#getParticipants)
* [`getParticipant(mixed $participant): ?\danog\MadelineProto\GroupCall\Participant`](#getParticipant)
* [`getVisualization(): ?array`](#getVisualization)
* [`setMuted(bool $muted = true): static`](#setMuted)
* [`isMuted(): bool`](#isMuted)
* [`sendMessage(string $message, (\danog\MadelineProto\ParseMode|null) $parseMode = NULL, (int|null) $paidStars = NULL, mixed $sendAs = NULL): static`](#sendMessage)
* [`sendReaction(string $emoji, (int|null) $customEmojiId = NULL): static`](#sendReaction)
* [`deleteMessages(list<int> $ids, bool $reportSpam = false): static`](#deleteMessages)
* [`deleteParticipantMessages(mixed $participant, bool $reportSpam = false): static`](#deleteParticipantMessages)
* [`setMessagesEnabled(bool $enabled): static`](#setMessagesEnabled)
* [`muteParticipant(mixed $participant, bool $muted = true): static`](#muteParticipant)
* [`setParticipantVolume(mixed $participant, int $volume): static`](#setParticipantVolume)
* [`setVideoPaused(bool $paused): static`](#setVideoPaused)
* [`setJoinMuted(bool $joinMuted): static`](#setJoinMuted)
* [`resetInviteHash(): static`](#resetInviteHash)
* [`setOutput(\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL, ?int $streams = NULL): int`](#setOutput)
* [`setOutputFolder(\danog\MadelineProto\LocalDirectory $dir, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): static`](#setOutputFolder)
* [`play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#play)
* [`playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#playBlocking)
* [`then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#then)
* [`skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#skip)
* [`stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#stop)
* [`pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#pause)
* [`isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`](#isPaused)
* [`resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#resume)
* [`playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): static`](#playOnHold)
* [`getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`](#getCurrent)
* [`disablePresentation(): static`](#disablePresentation)
* [`isSharingScreen(): bool`](#isSharingScreen)
* [`isStreamMode(): bool`](#isStreamMode)
* [`isRtmpMode(): bool`](#isRtmpMode)

## Methods:
### <a name="setTitle"></a> `setTitle(string $title): static`

A live story has no title of its own (its caption is the story's).


Parameters:

* `$title`: `string`   



### <a name="invite"></a> `invite(mixed ...$users): static`

Invite users to watch the live story.


Parameters:

* `...$users`: `mixed`   



### <a name="exportInvite"></a> `exportInvite(bool $canSelfUnmute = false): string`

Export an invite link to the live story.


Parameters:

* `$canSelfUnmute`: `bool` Ignored: only the poster of a live story publishes media.  



### <a name="removeParticipant"></a> `removeParticipant(mixed ...$participants): static`

Viewers cannot be removed from a live story; a viewer's comments can be moderated with
{@see self::deleteParticipantMessages()} instead.  


Parameters:

* `...$participants`: `mixed`   



### <a name="enablePresentation"></a> `enablePresentation(): static`

Live stories do not support screen sharing: the poster publishes a single video stream.



### <a name="donate"></a> `donate(int $stars): \danog\MadelineProto\EventHandler\Calls\LiveStory`

donate Telegram Stars to the streamer, without a message.


Parameters:

* `$stars`: `int`   



### <a name="getStars"></a> `getStars(): \danog\MadelineProto\GroupCall\GroupCallStars`

the Telegram Stars donated so far and the top donors.


#### See also: 
* [`\danog\MadelineProto\GroupCall\GroupCallStars`: The [Telegram Stars donations](https://core.telegram.org/api/group-calls#paid-live-story-donations)](../../../../danog/MadelineProto/GroupCall/GroupCallStars.html)




### <a name="setDefaultSendAs"></a> `setDefaultSendAs(mixed $peer): \danog\MadelineProto\EventHandler\Calls\LiveStory`

the peer we send in-call messages as by default.


Parameters:

* `$peer`: `mixed`   



### <a name="setPaidMessagesStars"></a> `setPaidMessagesStars(?int $stars): \danog\MadelineProto\EventHandler\Calls\LiveStory`

the minimum Telegram Stars donation required to comment, or null to let
everyone comment for free.  


Parameters:

* `$stars`: `?int`   



### <a name="join"></a> `join(bool $muted = false): static`

Join the call.


Parameters:

* `$muted`: `bool` Whether to join muted.  



### <a name="leave"></a> `leave(): static`

Leave the group call, without ending it for the other participants.



### <a name="discard"></a> `discard(): static`

End the group call for all participants.



### <a name="isJoined"></a> `isJoined(): bool`

Whether we are currently in the group call (joined and not left).



### <a name="getCallState"></a> `getCallState(): \danog\MadelineProto\GroupCall\GroupCallState`

Get the state of the group call.


#### See also: 
* [`\danog\MadelineProto\GroupCall\GroupCallState`: State of a group call we are interacting with.](../../../../danog/MadelineProto/GroupCall/GroupCallState.html)




### <a name="getParticipants"></a> `getParticipants(): array<int, \danog\MadelineProto\GroupCall\Participant>`

Get all known participants, indexed by their bot API peer ID.


#### See also: 
* [`\danog\MadelineProto\GroupCall\Participant`: A participant of a group call, mirroring](../../../../danog/MadelineProto/GroupCall/Participant.html)




### <a name="getParticipant"></a> `getParticipant(mixed $participant): ?\danog\MadelineProto\GroupCall\Participant`

A participant of the call by their id, username or peer, or null if they are not in it.


Parameters:

* `$participant`: `mixed`   


#### See also: 
* [`\danog\MadelineProto\GroupCall\Participant`: A participant of a group call, mirroring](../../../../danog/MadelineProto/GroupCall/Participant.html)




### <a name="getVisualization"></a> `getVisualization(): ?array`

Video chats and livestreams are not end-to-end encrypted, so there is no key to verify: always null.



### <a name="setMuted"></a> `setMuted(bool $muted = true): static`

Mute or unmute our own audio stream.


Parameters:

* `$muted`: `bool`   



### <a name="isMuted"></a> `isMuted(): bool`

Whether our own audio stream is muted.



### <a name="sendMessage"></a> `sendMessage(string $message, (\danog\MadelineProto\ParseMode|null) $parseMode = NULL, (int|null) $paidStars = NULL, mixed $sendAs = NULL): static`

Send an [in-call message »](https://core.telegram.org/api/group-calls#in-call-messages), shown as
an overlay by the participants' clients (there is no chat history), if messages are enabled.  


Parameters:

* `$message`: `string` The text; markup in `$parseMode` is converted to entities.  
* `$parseMode`: `(\danog\MadelineProto\ParseMode|null)` Whether to parse HTML or Markdown markup in the text.  
* `$paidStars`: `(int|null)` Live stories only: Telegram Stars to donate with the message (at least {@see self::$sendPaidMessagesStars}).  
* `$sendAs`: `mixed` Live stories only: the peer to send the message as.  


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../../../danog/MadelineProto/ParseMode.html)




### <a name="sendReaction"></a> `sendReaction(string $emoji, (int|null) $customEmojiId = NULL): static`

Send an [in-call reaction »](https://core.telegram.org/api/group-calls#in-call-reactions).


Parameters:

* `$emoji`: `string` The emoji.  
* `$customEmojiId`: `(int|null)` The document id of a custom emoji to send instead, `$emoji` being its fallback.  



### <a name="deleteMessages"></a> `deleteMessages(list<int> $ids, bool $reportSpam = false): static`

Delete in-call messages: our own, or anyone's if we are an admin.


Parameters:

* `$ids`: `list<int>` IDs of the messages to delete.  
* `$reportSpam`: `bool` Also report them as spam (admins only).  



### <a name="deleteParticipantMessages"></a> `deleteParticipantMessages(mixed $participant, bool $reportSpam = false): static`

Delete every in-call message of a participant (admins only).


Parameters:

* `$participant`: `mixed`   
* `$reportSpam`: `bool` Also report them as spam.  



### <a name="setMessagesEnabled"></a> `setMessagesEnabled(bool $enabled): static`

Enable or disable in-call messages (admins only).


Parameters:

* `$enabled`: `bool`   



### <a name="muteParticipant"></a> `muteParticipant(mixed $participant, bool $muted = true): static`

Mute or unmute a participant (admins only; a participant muted by an admin may not unmute
themselves), or, for a non-admin, mute a participant only for ourselves.  


Parameters:

* `$participant`: `mixed`   
* `$muted`: `bool`   



### <a name="setParticipantVolume"></a> `setParticipantVolume(mixed $participant, int $volume): static`

Set our local playback volume of a participant.


Parameters:

* `$participant`: `mixed`   
* `$volume`: `int` From 1 to 20000, where 10000 is 100%.  



### <a name="setVideoPaused"></a> `setVideoPaused(bool $paused): static`

Pause or resume our own video stream, telling the other participants to keep showing the last
frame rather than hiding it.  


Parameters:

* `$paused`: `bool`   



### <a name="setJoinMuted"></a> `setJoinMuted(bool $joinMuted): static`

Whether new participants join muted (admins only).


Parameters:

* `$joinMuted`: `bool`   



### <a name="resetInviteHash"></a> `resetInviteHash(): static`

Invalidate every invite link exported so far (admins only).



### <a name="setOutput"></a> `setOutput(\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL, ?int $streams = NULL): int`

Record one participant into a single file (or stream) with a fixed set of tracks, muxed into
Matroska in pure PHP.  
  
`$participant` (a user id, username or peer) is required — every participant is recorded to  
its own file, see {@see self::setOutputFolder()} to record everyone at once — except in  
[stream mode »](https://core.telegram.org/api/group-calls#stream-mode) ({@see self::isStreamMode()}),  
where there is a single mixed audio (and, for an RTMP livestream, video) stream rather than one per  
participant: pass no `$participant`, and any {@see RecordingFormat}. Our own media is never recorded.  
  
The file holds the streams chosen with `$streams` — a bitmask of {@see CallStream::AUDIO},  
{@see CallStream::VIDEO} and {@see CallStream::SCREEN}, every one of which must be available — or,  
when null, every stream the participant currently sends; the available streams are returned. The  
tracks are fixed for the whole file: a stream turned off stops being written and resumes when it  
comes back, and only a change of codec or the end of the call finishes the file (see  
{@see Call::setOutput()}); every such event is reported by a {@see CallStreams} update.  
  
Participants' frames are stored as-is, so the video tracks are whatever codec they send and the  
audio is OPUS; `$format` picks the {@see RecordingFormat::Mkv} (default) or {@see RecordingFormat::Webm}  
DocType, autodetected from a `.webm` extension.  


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream`   
* `$participant`: `mixed`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   
* `$streams`: `?int` The streams to record, as a bitmask of {@see CallStream} flags, or null for every available one.  


Return value: The streams the participant currently sends, as a bitmask of {@see CallStream} flags.

#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* `\Amp\ByteStream\WritableStream`
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../../../danog/MadelineProto/RecordingFormat.html)




### <a name="setOutputFolder"></a> `setOutputFolder(\danog\MadelineProto\LocalDirectory $dir, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): static`

Record group call media into a directory, muxed into Matroska files in pure PHP.
  
Records every transmitting participant — or only the given `$participant` — as  
`<dir>/<peerId>.<n>_<streams>.mkv` files, one per combination of the audio, camera video and  
screen share they send, each on or off at any time (see {@see Call::setOutputFolder()};  
participants that start transmitting later are picked up too). Our own media is never recorded.  
In [stream mode »](https://core.telegram.org/api/group-calls#stream-mode) the mixed stream is  
recorded as `<dir>/stream.mkv` (or `.ogg` for {@see RecordingFormat::Opus}).  
  
`$format` picks the {@see RecordingFormat::Mkv} (default) or {@see RecordingFormat::Webm} DocType.  


Parameters:

* `$dir`: `\danog\MadelineProto\LocalDirectory`   
* `$participant`: `mixed`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   


#### See also: 
* [`\danog\MadelineProto\LocalDirectory`: Indicates a local directory to write output into.](../../../../danog/MadelineProto/LocalDirectory.html)
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../../../danog/MadelineProto/RecordingFormat.html)




### <a name="play"></a> `play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Play a file, transmitting its audio and, if it carries a transmittable one, its video.
  
A WebM/Matroska file with VP8, VP9 or H.264 video has its video transmitted too; any other  
file (or a raw audio stream) is played as audio only. Frames are demuxed in pure PHP and sent  
as-is where possible, so no transcoding (and thus no FFI extension) is required for  
pre-encoded WebM/OGG-OPUS input.  


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="playBlocking"></a> `playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Play a file, blocking until it has finished playing if a stream is provided.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="then"></a> `then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Play file.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="skip"></a> `skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

When called, skips to the next file in the playlist.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="stop"></a> `stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Stops playing all files, clears the main and the hold playlist.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="pause"></a> `pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Pauses the currently playing file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="isPaused"></a> `isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`

Whether the currently playing file is paused.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="resume"></a> `resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Resumes the currently playing file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="playOnHold"></a> `playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): static`

Files to play on hold.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   
* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="getCurrent"></a> `getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`

Get the file that is currently being played.
  
Will return a string with the object ID of the stream if we're currently playing a stream,  
otherwise returns the related LocalFile or RemoteUrl.  


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)




### <a name="disablePresentation"></a> `disablePresentation(): static`

Stop sharing the screen.



### <a name="isSharingScreen"></a> `isSharingScreen(): bool`

Whether a screen-share is currently being transmitted.



### <a name="isStreamMode"></a> `isStreamMode(): bool`

Whether the server switched us to [stream mode »](https://core.telegram.org/api/group-calls#stream-mode)
(a large livestream, or an RTMP one): the call's media is received by downloading chunks, and  
there is a single mixed stream to record with {@see self::setOutput()} (pass no participant).  



### <a name="isRtmpMode"></a> `isRtmpMode(): bool`

Whether the call's media is published by a single external RTMP publisher.



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
