---
title: "danog\\MadelineProto\\Namespace\\Photos: "
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Namespace\Photos`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

  




## Method list:
* [`updateProfilePhoto(array $id, bool $fallback = false, array|int|string $bot = []): array{_: \"photos.photo", photo: array{_: \"photoEmpty", id: array}|array{_: \"photo", has_stickers: array, id: array, access_hash: array, file_reference: array, date: array, sizes: list<array>, video_sizes: list<array>, dc_id: array}, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/photos.Photo.htm}`](#updateprofilephoto-array-id-bool-fallback-false-array-int-string-bot-array-_-photos-photo-photo-array-_-photoempty-id-array-array-_-photo-has_stickers-array-id-array-access_hash-array-file_reference-array-date-array-sizes-list-array-video_sizes-list-array-dc_id-array-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-photos-photo-htm)
* [`uploadProfilePhoto(bool $fallback = false, array|int|string $bot = [], mixed $file = [], mixed $video = [], float $video_start_ts = 0.0, array{_: \"videoSize", type?: string, w?: int, h?: int, size?: int, video_start_ts?: float}|array{_: \"videoSizeEmojiMarkup", emoji_id?: int, background_colors?: list<int>}|array{_: \"videoSizeStickerMarkup", stickerset: array{_: \"inputStickerSetEmpty"}|array{_: \"inputStickerSetID", id?: int, access_hash?: int}|array{_: \"inputStickerSetShortName", short_name?: string}|array{_: \"inputStickerSetAnimatedEmoji"}|array{_: \"inputStickerSetDice", emoticon?: string}|array{_: \"inputStickerSetAnimatedEmojiAnimations"}|array{_: \"inputStickerSetPremiumGifts"}|array{_: \"inputStickerSetEmojiGenericAnimations"}|array{_: \"inputStickerSetEmojiDefaultStatuses"}|array{_: \"inputStickerSetEmojiDefaultTopicIcons"}, sticker_id?: int, background_colors?: list<int>} $video_emoji_markup = []): array{_: \"photos.photo", photo: array{_: \"photoEmpty", id: array}|array{_: \"photo", has_stickers: array, id: array, access_hash: array, file_reference: array, date: array, sizes: list<array>, video_sizes: list<array>, dc_id: array}, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/photos.Photo.htm}`](#uploadprofilephoto-bool-fallback-false-array-int-string-bot-mixed-file-mixed-video-float-video_start_ts-0-0-array-_-videosize-type-string-w-int-h-int-size-int-video_start_ts-float-array-_-videosizeemojimarkup-emoji_id-int-background_colors-list-int-array-_-videosizestickermarkup-stickerset-array-_-inputstickersetempty-array-_-inputstickersetid-id-int-access_hash-int-array-_-inputstickersetshortname-short_name-string-array-_-inputstickersetanimatedemoji-array-_-inputstickersetdice-emoticon-string-array-_-inputstickersetanimatedemojianimations-array-_-inputstickersetpremiumgifts-array-_-inputstickersetemojigenericanimations-array-_-inputstickersetemojidefaultstatuses-array-_-inputstickersetemojidefaulttopicicons-sticker_id-int-background_colors-list-int-video_emoji_markup-array-_-photos-photo-photo-array-_-photoempty-id-array-array-_-photo-has_stickers-array-id-array-access_hash-array-file_reference-array-date-array-sizes-list-array-video_sizes-list-array-dc_id-array-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-photos-photo-htm)
* [`deletePhotos(list<array> $id = []): list<int>`](#deletephotos-list-array-id-list-int)
* [`getUserPhotos(array|int|string $user_id, int $offset = 0, int $max_id = 0, int $limit = 0): array{_: \"photos.photos", photos: list<array{_: \"photoEmpty", id: array}|array{_: \"photo", has_stickers: array, id: array, access_hash: array, file_reference: array, date: array, sizes: list<array>, video_sizes: list<array>, dc_id: array}>, users: list<array|int|string>}|array{_: \"photos.photosSlice", count: int, photos: list<array{_: \"photoEmpty", id: array}|array{_: \"photo", has_stickers: array, id: array, access_hash: array, file_reference: array, date: array, sizes: list<array>, video_sizes: list<array>, dc_id: array}>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/photos.Photos.htm}`](#getuserphotos-array-int-string-user_id-int-offset-0-int-max_id-0-int-limit-0-array-_-photos-photos-photos-list-array-_-photoempty-id-array-array-_-photo-has_stickers-array-id-array-access_hash-array-file_reference-array-date-array-sizes-list-array-video_sizes-list-array-dc_id-array-users-list-array-int-string-array-_-photos-photosslice-count-int-photos-list-array-_-photoempty-id-array-array-_-photo-has_stickers-array-id-array-access_hash-array-file_reference-array-date-array-sizes-list-array-video_sizes-list-array-dc_id-array-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-photos-photos-htm)
* [`uploadContactProfilePhoto(array|int|string $user_id, bool $suggest = false, bool $save = false, mixed $file = [], mixed $video = [], float $video_start_ts = 0.0, array{_: \"videoSize", type?: string, w?: int, h?: int, size?: int, video_start_ts?: float}|array{_: \"videoSizeEmojiMarkup", emoji_id?: int, background_colors?: list<int>}|array{_: \"videoSizeStickerMarkup", stickerset: array{_: \"inputStickerSetEmpty"}|array{_: \"inputStickerSetID", id?: int, access_hash?: int}|array{_: \"inputStickerSetShortName", short_name?: string}|array{_: \"inputStickerSetAnimatedEmoji"}|array{_: \"inputStickerSetDice", emoticon?: string}|array{_: \"inputStickerSetAnimatedEmojiAnimations"}|array{_: \"inputStickerSetPremiumGifts"}|array{_: \"inputStickerSetEmojiGenericAnimations"}|array{_: \"inputStickerSetEmojiDefaultStatuses"}|array{_: \"inputStickerSetEmojiDefaultTopicIcons"}, sticker_id?: int, background_colors?: list<int>} $video_emoji_markup = []): array{_: \"photos.photo", photo: array{_: \"photoEmpty", id: array}|array{_: \"photo", has_stickers: array, id: array, access_hash: array, file_reference: array, date: array, sizes: list<array>, video_sizes: list<array>, dc_id: array}, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/photos.Photo.htm}`](#uploadcontactprofilephoto-array-int-string-user_id-bool-suggest-false-bool-save-false-mixed-file-mixed-video-float-video_start_ts-0-0-array-_-videosize-type-string-w-int-h-int-size-int-video_start_ts-float-array-_-videosizeemojimarkup-emoji_id-int-background_colors-list-int-array-_-videosizestickermarkup-stickerset-array-_-inputstickersetempty-array-_-inputstickersetid-id-int-access_hash-int-array-_-inputstickersetshortname-short_name-string-array-_-inputstickersetanimatedemoji-array-_-inputstickersetdice-emoticon-string-array-_-inputstickersetanimatedemojianimations-array-_-inputstickersetpremiumgifts-array-_-inputstickersetemojigenericanimations-array-_-inputstickersetemojidefaultstatuses-array-_-inputstickersetemojidefaulttopicicons-sticker_id-int-background_colors-list-int-video_emoji_markup-array-_-photos-photo-photo-array-_-photoempty-id-array-array-_-photo-has_stickers-array-id-array-access_hash-array-file_reference-array-date-array-sizes-list-array-video_sizes-list-array-dc_id-array-users-list-array-int-string-see-https-docs-madelineproto-xyz-api_docs-types-photos-photo-htm)

## Methods:
### `updateProfilePhoto(array $id, bool $fallback = false, array|int|string $bot = []): array{_: \"photos.photo", photo: array{_: \"photoEmpty", id: array}|array{_: \"photo", has_stickers: array, id: array, access_hash: array, file_reference: array, date: array, sizes: list<array>, video_sizes: list<array>, dc_id: array}, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/photos.Photo.htm}`

Installs a previously uploaded photo as a profile photo.


Parameters:

* `$id`: `array` Input photo @see https://docs.madelineproto.xyz/API_docs/types/InputPhoto.html  
* `$fallback`: `bool` If set, the chosen profile photo will be shown to users that can't display your main profile photo due to your privacy settings.  
* `$bot`: `array|int|string` Can contain info of a bot we own, to change the profile photo of that bot, instead of the current user. @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/photos.Photo.html


### `uploadProfilePhoto(bool $fallback = false, array|int|string $bot = [], mixed $file = [], mixed $video = [], float $video_start_ts = 0.0, array{_: \"videoSize", type?: string, w?: int, h?: int, size?: int, video_start_ts?: float}|array{_: \"videoSizeEmojiMarkup", emoji_id?: int, background_colors?: list<int>}|array{_: \"videoSizeStickerMarkup", stickerset: array{_: \"inputStickerSetEmpty"}|array{_: \"inputStickerSetID", id?: int, access_hash?: int}|array{_: \"inputStickerSetShortName", short_name?: string}|array{_: \"inputStickerSetAnimatedEmoji"}|array{_: \"inputStickerSetDice", emoticon?: string}|array{_: \"inputStickerSetAnimatedEmojiAnimations"}|array{_: \"inputStickerSetPremiumGifts"}|array{_: \"inputStickerSetEmojiGenericAnimations"}|array{_: \"inputStickerSetEmojiDefaultStatuses"}|array{_: \"inputStickerSetEmojiDefaultTopicIcons"}, sticker_id?: int, background_colors?: list<int>} $video_emoji_markup = []): array{_: \"photos.photo", photo: array{_: \"photoEmpty", id: array}|array{_: \"photo", has_stickers: array, id: array, access_hash: array, file_reference: array, date: array, sizes: list<array>, video_sizes: list<array>, dc_id: array}, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/photos.Photo.htm}`

Updates current user profile photo.
The `file`, `video` and `video_emoji_markup` flags are mutually exclusive.

Parameters:

* `$fallback`: `bool` If set, the chosen profile photo will be shown to users that can't display your main profile photo due to your privacy settings.  
* `$bot`: `array|int|string` Can contain info of a bot we own, to change the profile photo of that bot, instead of the current user. @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  
* `$file`: `mixed` A file name or a file URL. You can also use amphp async streams, amphp HTTP response objects, and [much more](https://docs.madelineproto.xyz/docs/FILES.html#downloading-files)!  
* `$video`: `mixed` A file name or a file URL. You can also use amphp async streams, amphp HTTP response objects, and [much more](https://docs.madelineproto.xyz/docs/FILES.html#downloading-files)!  
* `$video_start_ts`: `float` Floating point UNIX timestamp in seconds, indicating the frame of the video/sticker that should be used as static preview; can only be used if `video` or `video_emoji_markup` is set.  
* `$video_emoji_markup`: `array{_: \"videoSize", type?: string, w?: int, h?: int, size?: int, video_start_ts?: float}|array{_: \"videoSizeEmojiMarkup", emoji_id?: int, background_colors?: list<int>}|array{_: \"videoSizeStickerMarkup", stickerset: array{_: \"inputStickerSetEmpty"}|array{_: \"inputStickerSetID", id?: int, access_hash?: int}|array{_: \"inputStickerSetShortName", short_name?: string}|array{_: \"inputStickerSetAnimatedEmoji"}|array{_: \"inputStickerSetDice", emoticon?: string}|array{_: \"inputStickerSetAnimatedEmojiAnimations"}|array{_: \"inputStickerSetPremiumGifts"}|array{_: \"inputStickerSetEmojiGenericAnimations"}|array{_: \"inputStickerSetEmojiDefaultStatuses"}|array{_: \"inputStickerSetEmojiDefaultTopicIcons"}, sticker_id?: int, background_colors?: list<int>}` Animated sticker profile picture, must contain either a [videoSizeEmojiMarkup](https://docs.madelineproto.xyz/API_docs/constructors/videoSizeEmojiMarkup.html) or a [videoSizeStickerMarkup](https://docs.madelineproto.xyz/API_docs/constructors/videoSizeStickerMarkup.html) constructor. @see https://docs.madelineproto.xyz/API_docs/types/VideoSize.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/photos.Photo.html


### `deletePhotos(list<array> $id = []): list<int>`

Deletes profile photos. The method returns a list of successfully deleted photo IDs.


Parameters:

* `$id`: `list<array>` Array of Input photos to delete @see https://docs.madelineproto.xyz/API_docs/types/InputPhoto.html  



### `getUserPhotos(array|int|string $user_id, int $offset = 0, int $max_id = 0, int $limit = 0): array{_: \"photos.photos", photos: list<array{_: \"photoEmpty", id: array}|array{_: \"photo", has_stickers: array, id: array, access_hash: array, file_reference: array, date: array, sizes: list<array>, video_sizes: list<array>, dc_id: array}>, users: list<array|int|string>}|array{_: \"photos.photosSlice", count: int, photos: list<array{_: \"photoEmpty", id: array}|array{_: \"photo", has_stickers: array, id: array, access_hash: array, file_reference: array, date: array, sizes: list<array>, video_sizes: list<array>, dc_id: array}>, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/photos.Photos.htm}`

Returns the list of user photos.


Parameters:

* `$user_id`: `array|int|string` User ID @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  
* `$offset`: `int` Number of list elements to be skipped  
* `$max_id`: `int` If a positive value was transferred, the method will return only photos with IDs less than the set one  
* `$limit`: `int` Number of list elements to be returned  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/photos.Photos.html


### `uploadContactProfilePhoto(array|int|string $user_id, bool $suggest = false, bool $save = false, mixed $file = [], mixed $video = [], float $video_start_ts = 0.0, array{_: \"videoSize", type?: string, w?: int, h?: int, size?: int, video_start_ts?: float}|array{_: \"videoSizeEmojiMarkup", emoji_id?: int, background_colors?: list<int>}|array{_: \"videoSizeStickerMarkup", stickerset: array{_: \"inputStickerSetEmpty"}|array{_: \"inputStickerSetID", id?: int, access_hash?: int}|array{_: \"inputStickerSetShortName", short_name?: string}|array{_: \"inputStickerSetAnimatedEmoji"}|array{_: \"inputStickerSetDice", emoticon?: string}|array{_: \"inputStickerSetAnimatedEmojiAnimations"}|array{_: \"inputStickerSetPremiumGifts"}|array{_: \"inputStickerSetEmojiGenericAnimations"}|array{_: \"inputStickerSetEmojiDefaultStatuses"}|array{_: \"inputStickerSetEmojiDefaultTopicIcons"}, sticker_id?: int, background_colors?: list<int>} $video_emoji_markup = []): array{_: \"photos.photo", photo: array{_: \"photoEmpty", id: array}|array{_: \"photo", has_stickers: array, id: array, access_hash: array, file_reference: array, date: array, sizes: list<array>, video_sizes: list<array>, dc_id: array}, users: \list<array|int|string>} @see https://docs.madelineproto.xyz/API_docs/types/photos.Photo.htm}`

Upload a custom profile picture for a contact, or suggest a new profile picture to a contact.
The `file`, `video` and `video_emoji_markup` flags are mutually exclusive.

Parameters:

* `$user_id`: `array|int|string` The contact @see https://docs.madelineproto.xyz/API_docs/types/InputUser.html  
* `$suggest`: `bool` If set, will send a [messageActionSuggestProfilePhoto](https://docs.madelineproto.xyz/API_docs/constructors/messageActionSuggestProfilePhoto.html) service message to `user_id`, suggesting them to use the specified profile picture; otherwise, will set a personal profile picture for the user (only visible to the current user).  
* `$save`: `bool` If set, removes a previously set personal profile picture (does not affect suggested profile pictures, to remove them simply deleted the [messageActionSuggestProfilePhoto](https://docs.madelineproto.xyz/API_docs/constructors/messageActionSuggestProfilePhoto.html) service message with [messages.deleteMessages](https://docs.madelineproto.xyz/API_docs/methods/messages.deleteMessages.html)).  
* `$file`: `mixed` A file name or a file URL. You can also use amphp async streams, amphp HTTP response objects, and [much more](https://docs.madelineproto.xyz/docs/FILES.html#downloading-files)!  
* `$video`: `mixed` A file name or a file URL. You can also use amphp async streams, amphp HTTP response objects, and [much more](https://docs.madelineproto.xyz/docs/FILES.html#downloading-files)!  
* `$video_start_ts`: `float` Floating point UNIX timestamp in seconds, indicating the frame of the video/sticker that should be used as static preview; can only be used if `video` or `video_emoji_markup` is set.  
* `$video_emoji_markup`: `array{_: \"videoSize", type?: string, w?: int, h?: int, size?: int, video_start_ts?: float}|array{_: \"videoSizeEmojiMarkup", emoji_id?: int, background_colors?: list<int>}|array{_: \"videoSizeStickerMarkup", stickerset: array{_: \"inputStickerSetEmpty"}|array{_: \"inputStickerSetID", id?: int, access_hash?: int}|array{_: \"inputStickerSetShortName", short_name?: string}|array{_: \"inputStickerSetAnimatedEmoji"}|array{_: \"inputStickerSetDice", emoticon?: string}|array{_: \"inputStickerSetAnimatedEmojiAnimations"}|array{_: \"inputStickerSetPremiumGifts"}|array{_: \"inputStickerSetEmojiGenericAnimations"}|array{_: \"inputStickerSetEmojiDefaultStatuses"}|array{_: \"inputStickerSetEmojiDefaultTopicIcons"}, sticker_id?: int, background_colors?: list<int>}` Animated sticker profile picture, must contain either a [videoSizeEmojiMarkup](https://docs.madelineproto.xyz/API_docs/constructors/videoSizeEmojiMarkup.html) or a [videoSizeStickerMarkup](https://docs.madelineproto.xyz/API_docs/constructors/videoSizeStickerMarkup.html) constructor. @see https://docs.madelineproto.xyz/API_docs/types/VideoSize.html  


Return value: @see https://docs.madelineproto.xyz/API_docs/types/photos.Photo.html


---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
