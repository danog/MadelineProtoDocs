---
title: Constructors
description: List of constructors
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructors  
[Back to API documentation index](..)

***
<br><br>[$accessPointRule](../constructors/accessPointRule.md) = \['phone_prefix_rules' => [string](../types/string.md), 'dc_id' => [int](../types/int.md), 'ips' => \[[IpPort](../types/IpPort.md)\], \];<a name="accessPointRule"></a>  

***
<br><br>[$accountDaysTTL](../constructors/accountDaysTTL.md) = \['days' => [int](../types/int.md), \];<a name="accountDaysTTL"></a>  

***
<br><br>[$account\_authorizationForm](../constructors/account_authorizationForm.md) = \['required_types' => \[[SecureRequiredType](../types/SecureRequiredType.md)\], 'values' => \[[SecureValue](../types/SecureValue.md)\], 'errors' => \[[SecureValueError](../types/SecureValueError.md)\], 'users' => \[[User](../types/User.md)\], 'privacy_policy_url' => [string](../types/string.md), \];<a name="account_authorizationForm"></a>  

[$account\_authorizations](../constructors/account_authorizations.md) = \['authorizations' => \[[Authorization](../types/Authorization.md)\], \];<a name="account_authorizations"></a>  

[$account\_autoDownloadSettings](../constructors/account_autoDownloadSettings.md) = \['low' => [AutoDownloadSettings](../types/AutoDownloadSettings.md), 'medium' => [AutoDownloadSettings](../types/AutoDownloadSettings.md), 'high' => [AutoDownloadSettings](../types/AutoDownloadSettings.md), \];<a name="account_autoDownloadSettings"></a>  

[$account\_password](../constructors/account_password.md) = \['has_recovery' => [Bool](../types/Bool.md), 'has_secure_values' => [Bool](../types/Bool.md), 'has_password' => [Bool](../types/Bool.md), 'current_algo' => [PasswordKdfAlgo](../types/PasswordKdfAlgo.md), 'srp_B' => [bytes](../types/bytes.md), 'srp_id' => [long](../types/long.md), 'hint' => [string](../types/string.md), 'email_unconfirmed_pattern' => [string](../types/string.md), 'new_algo' => [PasswordKdfAlgo](../types/PasswordKdfAlgo.md), 'new_secure_algo' => [SecurePasswordKdfAlgo](../types/SecurePasswordKdfAlgo.md), 'secure_random' => [bytes](../types/bytes.md), \];<a name="account_password"></a>  

[$account\_passwordInputSettings](../constructors/account_passwordInputSettings.md) = \['new_algo' => [PasswordKdfAlgo](../types/PasswordKdfAlgo.md), 'new_password_hash' => [bytes](../types/bytes.md), 'hint' => [string](../types/string.md), 'email' => [string](../types/string.md), 'new_secure_settings' => [SecureSecretSettings](../types/SecureSecretSettings.md), \];<a name="account_passwordInputSettings"></a>  

[$account\_passwordSettings](../constructors/account_passwordSettings.md) = \['email' => [string](../types/string.md), 'secure_settings' => [SecureSecretSettings](../types/SecureSecretSettings.md), \];<a name="account_passwordSettings"></a>  

[$account\_privacyRules](../constructors/account_privacyRules.md) = \['rules' => \[[PrivacyRule](../types/PrivacyRule.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="account_privacyRules"></a>  

[$account\_sentEmailCode](../constructors/account_sentEmailCode.md) = \['email_pattern' => [string](../types/string.md), 'length' => [int](../types/int.md), \];<a name="account_sentEmailCode"></a>  

[$account\_takeout](../constructors/account_takeout.md) = \['id' => [long](../types/long.md), \];<a name="account_takeout"></a>  

[$account\_themes](../constructors/account_themes.md) = \['hash' => [int](../types/int.md), 'themes' => \[[Theme](../types/Theme.md)\], \];<a name="account_themes"></a>  

[$account\_themesNotModified](../constructors/account_themesNotModified.md) = \[\];<a name="account_themesNotModified"></a>  

[$account\_tmpPassword](../constructors/account_tmpPassword.md) = \['tmp_password' => [bytes](../types/bytes.md), 'valid_until' => [int](../types/int.md), \];<a name="account_tmpPassword"></a>  

[$account\_wallPapers](../constructors/account_wallPapers.md) = \['hash' => [int](../types/int.md), 'wallpapers' => \[[WallPaper](../types/WallPaper.md)\], \];<a name="account_wallPapers"></a>  

[$account\_wallPapersNotModified](../constructors/account_wallPapersNotModified.md) = \[\];<a name="account_wallPapersNotModified"></a>  

[$account\_webAuthorizations](../constructors/account_webAuthorizations.md) = \['authorizations' => \[[WebAuthorization](../types/WebAuthorization.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="account_webAuthorizations"></a>  

***
<br><br>[$auth\_authorization](../constructors/auth_authorization.md) = \['tmp_sessions' => [int](../types/int.md), 'user' => [User](../types/User.md), \];<a name="auth_authorization"></a>  

[$auth\_authorizationSignUpRequired](../constructors/auth_authorizationSignUpRequired.md) = \['terms_of_service' => [help\_TermsOfService](../types/help_TermsOfService.md), \];<a name="auth_authorizationSignUpRequired"></a>  

[$auth\_codeTypeCall](../constructors/auth_codeTypeCall.md) = \[\];<a name="auth_codeTypeCall"></a>  

[$auth\_codeTypeFlashCall](../constructors/auth_codeTypeFlashCall.md) = \[\];<a name="auth_codeTypeFlashCall"></a>  

[$auth\_codeTypeSms](../constructors/auth_codeTypeSms.md) = \[\];<a name="auth_codeTypeSms"></a>  

[$auth\_exportedAuthorization](../constructors/auth_exportedAuthorization.md) = \['id' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \];<a name="auth_exportedAuthorization"></a>  

[$auth\_passwordRecovery](../constructors/auth_passwordRecovery.md) = \['email_pattern' => [string](../types/string.md), \];<a name="auth_passwordRecovery"></a>  

[$auth\_sentCode](../constructors/auth_sentCode.md) = \['type' => [auth\_SentCodeType](../types/auth_SentCodeType.md), 'phone_code_hash' => [string](../types/string.md), 'next_type' => [auth\_CodeType](../types/auth_CodeType.md), 'timeout' => [int](../types/int.md), \];<a name="auth_sentCode"></a>  

[$auth\_sentCodeTypeApp](../constructors/auth_sentCodeTypeApp.md) = \['length' => [int](../types/int.md), \];<a name="auth_sentCodeTypeApp"></a>  

[$auth\_sentCodeTypeCall](../constructors/auth_sentCodeTypeCall.md) = \['length' => [int](../types/int.md), \];<a name="auth_sentCodeTypeCall"></a>  

[$auth\_sentCodeTypeFlashCall](../constructors/auth_sentCodeTypeFlashCall.md) = \['pattern' => [string](../types/string.md), \];<a name="auth_sentCodeTypeFlashCall"></a>  

[$auth\_sentCodeTypeSms](../constructors/auth_sentCodeTypeSms.md) = \['length' => [int](../types/int.md), \];<a name="auth_sentCodeTypeSms"></a>  

***
<br><br>[$authorization](../constructors/authorization.md) = \['current' => [Bool](../types/Bool.md), 'official_app' => [Bool](../types/Bool.md), 'password_pending' => [Bool](../types/Bool.md), 'hash' => [long](../types/long.md), 'device_model' => [string](../types/string.md), 'platform' => [string](../types/string.md), 'system_version' => [string](../types/string.md), 'api_id' => [int](../types/int.md), 'app_name' => [string](../types/string.md), 'app_version' => [string](../types/string.md), 'date_created' => [int](../types/int.md), 'date_active' => [int](../types/int.md), 'ip' => [string](../types/string.md), 'country' => [string](../types/string.md), 'region' => [string](../types/string.md), \];<a name="authorization"></a>  

***
<br><br>[$autoDownloadSettings](../constructors/autoDownloadSettings.md) = \['disabled' => [Bool](../types/Bool.md), 'video_preload_large' => [Bool](../types/Bool.md), 'audio_preload_next' => [Bool](../types/Bool.md), 'phonecalls_less_data' => [Bool](../types/Bool.md), 'photo_size_max' => [int](../types/int.md), 'video_size_max' => [int](../types/int.md), 'file_size_max' => [int](../types/int.md), \];<a name="autoDownloadSettings"></a>  

***
<br><br>[$boolFalse](../constructors/boolFalse.md) = \[\];<a name="boolFalse"></a>  

***
<br><br>[$boolTrue](../constructors/boolTrue.md) = \[\];<a name="boolTrue"></a>  

***
<br><br>[$botCommand](../constructors/botCommand.md) = \['command' => [string](../types/string.md), 'description' => [string](../types/string.md), \];<a name="botCommand"></a>  

***
<br><br>[$botInfo](../constructors/botInfo.md) = \['user_id' => [int](../types/int.md), 'description' => [string](../types/string.md), 'commands' => \[[BotCommand](../types/BotCommand.md)\], \];<a name="botInfo"></a>  

***
<br><br>[$botInlineMediaResult](../constructors/botInlineMediaResult.md) = \['id' => [string](../types/string.md), 'type' => [string](../types/string.md), 'photo' => [Photo](../types/Photo.md), 'document' => [Document](../types/Document.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'send_message' => [BotInlineMessage](../types/BotInlineMessage.md), \];<a name="botInlineMediaResult"></a>  

***
<br><br>[$botInlineMessageMediaAuto](../constructors/botInlineMessageMediaAuto.md) = \['message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="botInlineMessageMediaAuto"></a>  

***
<br><br>[$botInlineMessageMediaContact](../constructors/botInlineMessageMediaContact.md) = \['phone_number' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'vcard' => [string](../types/string.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="botInlineMessageMediaContact"></a>  

***
<br><br>[$botInlineMessageMediaGeo](../constructors/botInlineMessageMediaGeo.md) = \['geo' => [GeoPoint](../types/GeoPoint.md), 'period' => [int](../types/int.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="botInlineMessageMediaGeo"></a>  

***
<br><br>[$botInlineMessageMediaVenue](../constructors/botInlineMessageMediaVenue.md) = \['geo' => [GeoPoint](../types/GeoPoint.md), 'title' => [string](../types/string.md), 'address' => [string](../types/string.md), 'provider' => [string](../types/string.md), 'venue_id' => [string](../types/string.md), 'venue_type' => [string](../types/string.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="botInlineMessageMediaVenue"></a>  

***
<br><br>[$botInlineMessageText](../constructors/botInlineMessageText.md) = \['no_webpage' => [Bool](../types/Bool.md), 'message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="botInlineMessageText"></a>  

***
<br><br>[$botInlineResult](../constructors/botInlineResult.md) = \['id' => [string](../types/string.md), 'type' => [string](../types/string.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'url' => [string](../types/string.md), 'thumb' => [WebDocument](../types/WebDocument.md), 'content' => [WebDocument](../types/WebDocument.md), 'send_message' => [BotInlineMessage](../types/BotInlineMessage.md), \];<a name="botInlineResult"></a>  

***
<br><br>[$cdnConfig](../constructors/cdnConfig.md) = \['public_keys' => \[[CdnPublicKey](../types/CdnPublicKey.md)\], \];<a name="cdnConfig"></a>  

***
<br><br>[$cdnPublicKey](../constructors/cdnPublicKey.md) = \['dc_id' => [int](../types/int.md), 'public_key' => [string](../types/string.md), \];<a name="cdnPublicKey"></a>  

***
<br><br>[$channel](../constructors/channel.md) = \['creator' => [Bool](../types/Bool.md), 'left' => [Bool](../types/Bool.md), 'broadcast' => [Bool](../types/Bool.md), 'verified' => [Bool](../types/Bool.md), 'megagroup' => [Bool](../types/Bool.md), 'restricted' => [Bool](../types/Bool.md), 'signatures' => [Bool](../types/Bool.md), 'min' => [Bool](../types/Bool.md), 'scam' => [Bool](../types/Bool.md), 'has_link' => [Bool](../types/Bool.md), 'has_geo' => [Bool](../types/Bool.md), 'slowmode_enabled' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), 'title' => [string](../types/string.md), 'username' => [string](../types/string.md), 'photo' => [ChatPhoto](../types/ChatPhoto.md), 'date' => [int](../types/int.md), 'version' => [int](../types/int.md), 'restriction_reason' => \[[RestrictionReason](../types/RestrictionReason.md)\], 'admin_rights' => [ChatAdminRights](../types/ChatAdminRights.md), 'banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), 'default_banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), 'participants_count' => [int](../types/int.md), \];<a name="channel"></a>  

***
<br><br>[$channelAdminLogEvent](../constructors/channelAdminLogEvent.md) = \['id' => [long](../types/long.md), 'date' => [int](../types/int.md), 'user_id' => [int](../types/int.md), 'action' => [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md), \];<a name="channelAdminLogEvent"></a>  

***
<br><br>[$channelAdminLogEventActionChangeAbout](../constructors/channelAdminLogEventActionChangeAbout.md) = \['prev_value' => [string](../types/string.md), 'new_value' => [string](../types/string.md), \];<a name="channelAdminLogEventActionChangeAbout"></a>  

***
<br><br>[$channelAdminLogEventActionChangeLinkedChat](../constructors/channelAdminLogEventActionChangeLinkedChat.md) = \['prev_value' => [int](../types/int.md), 'new_value' => [int](../types/int.md), \];<a name="channelAdminLogEventActionChangeLinkedChat"></a>  

***
<br><br>[$channelAdminLogEventActionChangeLocation](../constructors/channelAdminLogEventActionChangeLocation.md) = \['prev_value' => [ChannelLocation](../types/ChannelLocation.md), 'new_value' => [ChannelLocation](../types/ChannelLocation.md), \];<a name="channelAdminLogEventActionChangeLocation"></a>  

***
<br><br>[$channelAdminLogEventActionChangePhoto](../constructors/channelAdminLogEventActionChangePhoto.md) = \['prev_photo' => [Photo](../types/Photo.md), 'new_photo' => [Photo](../types/Photo.md), \];<a name="channelAdminLogEventActionChangePhoto"></a>  

***
<br><br>[$channelAdminLogEventActionChangeStickerSet](../constructors/channelAdminLogEventActionChangeStickerSet.md) = \['prev_stickerset' => [InputStickerSet](../types/InputStickerSet.md), 'new_stickerset' => [InputStickerSet](../types/InputStickerSet.md), \];<a name="channelAdminLogEventActionChangeStickerSet"></a>  

***
<br><br>[$channelAdminLogEventActionChangeTitle](../constructors/channelAdminLogEventActionChangeTitle.md) = \['prev_value' => [string](../types/string.md), 'new_value' => [string](../types/string.md), \];<a name="channelAdminLogEventActionChangeTitle"></a>  

***
<br><br>[$channelAdminLogEventActionChangeUsername](../constructors/channelAdminLogEventActionChangeUsername.md) = \['prev_value' => [string](../types/string.md), 'new_value' => [string](../types/string.md), \];<a name="channelAdminLogEventActionChangeUsername"></a>  

***
<br><br>[$channelAdminLogEventActionDefaultBannedRights](../constructors/channelAdminLogEventActionDefaultBannedRights.md) = \['prev_banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), 'new_banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), \];<a name="channelAdminLogEventActionDefaultBannedRights"></a>  

***
<br><br>[$channelAdminLogEventActionDeleteMessage](../constructors/channelAdminLogEventActionDeleteMessage.md) = \['message' => [Message](../types/Message.md), \];<a name="channelAdminLogEventActionDeleteMessage"></a>  

***
<br><br>[$channelAdminLogEventActionEditMessage](../constructors/channelAdminLogEventActionEditMessage.md) = \['prev_message' => [Message](../types/Message.md), 'new_message' => [Message](../types/Message.md), \];<a name="channelAdminLogEventActionEditMessage"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantInvite](../constructors/channelAdminLogEventActionParticipantInvite.md) = \['participant' => [ChannelParticipant](../types/ChannelParticipant.md), \];<a name="channelAdminLogEventActionParticipantInvite"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantJoin](../constructors/channelAdminLogEventActionParticipantJoin.md) = \[\];<a name="channelAdminLogEventActionParticipantJoin"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantLeave](../constructors/channelAdminLogEventActionParticipantLeave.md) = \[\];<a name="channelAdminLogEventActionParticipantLeave"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantToggleAdmin](../constructors/channelAdminLogEventActionParticipantToggleAdmin.md) = \['prev_participant' => [ChannelParticipant](../types/ChannelParticipant.md), 'new_participant' => [ChannelParticipant](../types/ChannelParticipant.md), \];<a name="channelAdminLogEventActionParticipantToggleAdmin"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantToggleBan](../constructors/channelAdminLogEventActionParticipantToggleBan.md) = \['prev_participant' => [ChannelParticipant](../types/ChannelParticipant.md), 'new_participant' => [ChannelParticipant](../types/ChannelParticipant.md), \];<a name="channelAdminLogEventActionParticipantToggleBan"></a>  

***
<br><br>[$channelAdminLogEventActionStopPoll](../constructors/channelAdminLogEventActionStopPoll.md) = \['message' => [Message](../types/Message.md), \];<a name="channelAdminLogEventActionStopPoll"></a>  

***
<br><br>[$channelAdminLogEventActionToggleInvites](../constructors/channelAdminLogEventActionToggleInvites.md) = \['new_value' => [Bool](../types/Bool.md), \];<a name="channelAdminLogEventActionToggleInvites"></a>  

***
<br><br>[$channelAdminLogEventActionTogglePreHistoryHidden](../constructors/channelAdminLogEventActionTogglePreHistoryHidden.md) = \['new_value' => [Bool](../types/Bool.md), \];<a name="channelAdminLogEventActionTogglePreHistoryHidden"></a>  

***
<br><br>[$channelAdminLogEventActionToggleSignatures](../constructors/channelAdminLogEventActionToggleSignatures.md) = \['new_value' => [Bool](../types/Bool.md), \];<a name="channelAdminLogEventActionToggleSignatures"></a>  

***
<br><br>[$channelAdminLogEventActionToggleSlowMode](../constructors/channelAdminLogEventActionToggleSlowMode.md) = \['prev_value' => [int](../types/int.md), 'new_value' => [int](../types/int.md), \];<a name="channelAdminLogEventActionToggleSlowMode"></a>  

***
<br><br>[$channelAdminLogEventActionUpdatePinned](../constructors/channelAdminLogEventActionUpdatePinned.md) = \['message' => [Message](../types/Message.md), \];<a name="channelAdminLogEventActionUpdatePinned"></a>  

***
<br><br>[$channelAdminLogEventsFilter](../constructors/channelAdminLogEventsFilter.md) = \['join' => [Bool](../types/Bool.md), 'leave' => [Bool](../types/Bool.md), 'invite' => [Bool](../types/Bool.md), 'ban' => [Bool](../types/Bool.md), 'unban' => [Bool](../types/Bool.md), 'kick' => [Bool](../types/Bool.md), 'unkick' => [Bool](../types/Bool.md), 'promote' => [Bool](../types/Bool.md), 'demote' => [Bool](../types/Bool.md), 'info' => [Bool](../types/Bool.md), 'settings' => [Bool](../types/Bool.md), 'pinned' => [Bool](../types/Bool.md), 'edit' => [Bool](../types/Bool.md), 'delete' => [Bool](../types/Bool.md), \];<a name="channelAdminLogEventsFilter"></a>  

***
<br><br>[$channelForbidden](../constructors/channelForbidden.md) = \['broadcast' => [Bool](../types/Bool.md), 'megagroup' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), 'title' => [string](../types/string.md), 'until_date' => [int](../types/int.md), \];<a name="channelForbidden"></a>  

***
<br><br>[$channelFull](../constructors/channelFull.md) = \['can_view_participants' => [Bool](../types/Bool.md), 'can_set_username' => [Bool](../types/Bool.md), 'can_set_stickers' => [Bool](../types/Bool.md), 'hidden_prehistory' => [Bool](../types/Bool.md), 'can_view_stats' => [Bool](../types/Bool.md), 'can_set_location' => [Bool](../types/Bool.md), 'has_scheduled' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'about' => [string](../types/string.md), 'participants_count' => [int](../types/int.md), 'admins_count' => [int](../types/int.md), 'kicked_count' => [int](../types/int.md), 'banned_count' => [int](../types/int.md), 'online_count' => [int](../types/int.md), 'read_inbox_max_id' => [int](../types/int.md), 'read_outbox_max_id' => [int](../types/int.md), 'unread_count' => [int](../types/int.md), 'chat_photo' => [Photo](../types/Photo.md), 'notify_settings' => [PeerNotifySettings](../types/PeerNotifySettings.md), 'exported_invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'bot_info' => \[[BotInfo](../types/BotInfo.md)\], 'migrated_from_chat_id' => [int](../types/int.md), 'migrated_from_max_id' => [int](../types/int.md), 'pinned_msg_id' => [int](../types/int.md), 'stickerset' => [StickerSet](../types/StickerSet.md), 'available_min_id' => [int](../types/int.md), 'folder_id' => [int](../types/int.md), 'linked_chat_id' => [int](../types/int.md), 'location' => [ChannelLocation](../types/ChannelLocation.md), 'slowmode_seconds' => [int](../types/int.md), 'slowmode_next_send_date' => [int](../types/int.md), 'pts' => [int](../types/int.md), \];<a name="channelFull"></a>  

***
<br><br>[$channelLocation](../constructors/channelLocation.md) = \['geo_point' => [GeoPoint](../types/GeoPoint.md), 'address' => [string](../types/string.md), \];<a name="channelLocation"></a>  

***
<br><br>[$channelLocationEmpty](../constructors/channelLocationEmpty.md) = \[\];<a name="channelLocationEmpty"></a>  

***
<br><br>[$channelMessagesFilter](../constructors/channelMessagesFilter.md) = \['exclude_new_messages' => [Bool](../types/Bool.md), 'ranges' => \[[MessageRange](../types/MessageRange.md)\], \];<a name="channelMessagesFilter"></a>  

***
<br><br>[$channelMessagesFilterEmpty](../constructors/channelMessagesFilterEmpty.md) = \[\];<a name="channelMessagesFilterEmpty"></a>  

***
<br><br>[$channelParticipant](../constructors/channelParticipant.md) = \['user_id' => [int](../types/int.md), 'date' => [int](../types/int.md), \];<a name="channelParticipant"></a>  

***
<br><br>[$channelParticipantAdmin](../constructors/channelParticipantAdmin.md) = \['can_edit' => [Bool](../types/Bool.md), 'self' => [Bool](../types/Bool.md), 'user_id' => [int](../types/int.md), 'inviter_id' => [int](../types/int.md), 'promoted_by' => [int](../types/int.md), 'date' => [int](../types/int.md), 'admin_rights' => [ChatAdminRights](../types/ChatAdminRights.md), 'rank' => [string](../types/string.md), \];<a name="channelParticipantAdmin"></a>  

***
<br><br>[$channelParticipantBanned](../constructors/channelParticipantBanned.md) = \['left' => [Bool](../types/Bool.md), 'user_id' => [int](../types/int.md), 'kicked_by' => [int](../types/int.md), 'date' => [int](../types/int.md), 'banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), \];<a name="channelParticipantBanned"></a>  

***
<br><br>[$channelParticipantCreator](../constructors/channelParticipantCreator.md) = \['user_id' => [int](../types/int.md), 'rank' => [string](../types/string.md), \];<a name="channelParticipantCreator"></a>  

***
<br><br>[$channelParticipantSelf](../constructors/channelParticipantSelf.md) = \['user_id' => [int](../types/int.md), 'inviter_id' => [int](../types/int.md), 'date' => [int](../types/int.md), \];<a name="channelParticipantSelf"></a>  

***
<br><br>[$channelParticipantsAdmins](../constructors/channelParticipantsAdmins.md) = \[\];<a name="channelParticipantsAdmins"></a>  

***
<br><br>[$channelParticipantsBanned](../constructors/channelParticipantsBanned.md) = \['q' => [string](../types/string.md), \];<a name="channelParticipantsBanned"></a>  

***
<br><br>[$channelParticipantsBots](../constructors/channelParticipantsBots.md) = \[\];<a name="channelParticipantsBots"></a>  

***
<br><br>[$channelParticipantsContacts](../constructors/channelParticipantsContacts.md) = \['q' => [string](../types/string.md), \];<a name="channelParticipantsContacts"></a>  

***
<br><br>[$channelParticipantsKicked](../constructors/channelParticipantsKicked.md) = \['q' => [string](../types/string.md), \];<a name="channelParticipantsKicked"></a>  

***
<br><br>[$channelParticipantsRecent](../constructors/channelParticipantsRecent.md) = \[\];<a name="channelParticipantsRecent"></a>  

***
<br><br>[$channelParticipantsSearch](../constructors/channelParticipantsSearch.md) = \['q' => [string](../types/string.md), \];<a name="channelParticipantsSearch"></a>  

***
<br><br>[$channels\_adminLogResults](../constructors/channels_adminLogResults.md) = \['events' => \[[ChannelAdminLogEvent](../types/ChannelAdminLogEvent.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="channels_adminLogResults"></a>  

[$channels\_channelParticipant](../constructors/channels_channelParticipant.md) = \['participant' => [ChannelParticipant](../types/ChannelParticipant.md), 'users' => \[[User](../types/User.md)\], \];<a name="channels_channelParticipant"></a>  

[$channels\_channelParticipants](../constructors/channels_channelParticipants.md) = \['count' => [int](../types/int.md), 'participants' => \[[ChannelParticipant](../types/ChannelParticipant.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="channels_channelParticipants"></a>  

[$channels\_channelParticipantsNotModified](../constructors/channels_channelParticipantsNotModified.md) = \[\];<a name="channels_channelParticipantsNotModified"></a>  

***
<br><br>[$chat](../constructors/chat.md) = \['creator' => [Bool](../types/Bool.md), 'kicked' => [Bool](../types/Bool.md), 'left' => [Bool](../types/Bool.md), 'deactivated' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'title' => [string](../types/string.md), 'photo' => [ChatPhoto](../types/ChatPhoto.md), 'participants_count' => [int](../types/int.md), 'date' => [int](../types/int.md), 'version' => [int](../types/int.md), 'migrated_to' => [InputChannel](../types/InputChannel.md), 'admin_rights' => [ChatAdminRights](../types/ChatAdminRights.md), 'default_banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), \];<a name="chat"></a>  

***
<br><br>[$chatAdminRights](../constructors/chatAdminRights.md) = \['change_info' => [Bool](../types/Bool.md), 'post_messages' => [Bool](../types/Bool.md), 'edit_messages' => [Bool](../types/Bool.md), 'delete_messages' => [Bool](../types/Bool.md), 'ban_users' => [Bool](../types/Bool.md), 'invite_users' => [Bool](../types/Bool.md), 'pin_messages' => [Bool](../types/Bool.md), 'add_admins' => [Bool](../types/Bool.md), \];<a name="chatAdminRights"></a>  

***
<br><br>[$chatBannedRights](../constructors/chatBannedRights.md) = \['view_messages' => [Bool](../types/Bool.md), 'send_messages' => [Bool](../types/Bool.md), 'send_media' => [Bool](../types/Bool.md), 'send_stickers' => [Bool](../types/Bool.md), 'send_gifs' => [Bool](../types/Bool.md), 'send_games' => [Bool](../types/Bool.md), 'send_inline' => [Bool](../types/Bool.md), 'embed_links' => [Bool](../types/Bool.md), 'send_polls' => [Bool](../types/Bool.md), 'change_info' => [Bool](../types/Bool.md), 'invite_users' => [Bool](../types/Bool.md), 'pin_messages' => [Bool](../types/Bool.md), 'until_date' => [int](../types/int.md), \];<a name="chatBannedRights"></a>  

***
<br><br>[$chatEmpty](../constructors/chatEmpty.md) = \['id' => [int](../types/int.md), \];<a name="chatEmpty"></a>  

***
<br><br>[$chatForbidden](../constructors/chatForbidden.md) = \['id' => [int](../types/int.md), 'title' => [string](../types/string.md), \];<a name="chatForbidden"></a>  

***
<br><br>[$chatFull](../constructors/chatFull.md) = \['can_set_username' => [Bool](../types/Bool.md), 'has_scheduled' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'about' => [string](../types/string.md), 'participants' => [ChatParticipants](../types/ChatParticipants.md), 'chat_photo' => [Photo](../types/Photo.md), 'notify_settings' => [PeerNotifySettings](../types/PeerNotifySettings.md), 'exported_invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'bot_info' => \[[BotInfo](../types/BotInfo.md)\], 'pinned_msg_id' => [int](../types/int.md), 'folder_id' => [int](../types/int.md), \];<a name="chatFull"></a>  

***
<br><br>[$chatInvite](../constructors/chatInvite.md) = \['channel' => [Bool](../types/Bool.md), 'broadcast' => [Bool](../types/Bool.md), 'public' => [Bool](../types/Bool.md), 'megagroup' => [Bool](../types/Bool.md), 'title' => [string](../types/string.md), 'photo' => [Photo](../types/Photo.md), 'participants_count' => [int](../types/int.md), 'participants' => \[[User](../types/User.md)\], \];<a name="chatInvite"></a>  

***
<br><br>[$chatInviteAlready](../constructors/chatInviteAlready.md) = \['chat' => [Chat](../types/Chat.md), \];<a name="chatInviteAlready"></a>  

***
<br><br>[$chatInviteEmpty](../constructors/chatInviteEmpty.md) = \[\];<a name="chatInviteEmpty"></a>  

***
<br><br>[$chatInviteExported](../constructors/chatInviteExported.md) = \['link' => [string](../types/string.md), \];<a name="chatInviteExported"></a>  

***
<br><br>[$chatOnlines](../constructors/chatOnlines.md) = \['onlines' => [int](../types/int.md), \];<a name="chatOnlines"></a>  

***
<br><br>[$chatParticipant](../constructors/chatParticipant.md) = \['user_id' => [int](../types/int.md), 'inviter_id' => [int](../types/int.md), 'date' => [int](../types/int.md), \];<a name="chatParticipant"></a>  

***
<br><br>[$chatParticipantAdmin](../constructors/chatParticipantAdmin.md) = \['user_id' => [int](../types/int.md), 'inviter_id' => [int](../types/int.md), 'date' => [int](../types/int.md), \];<a name="chatParticipantAdmin"></a>  

***
<br><br>[$chatParticipantCreator](../constructors/chatParticipantCreator.md) = \['user_id' => [int](../types/int.md), \];<a name="chatParticipantCreator"></a>  

***
<br><br>[$chatParticipants](../constructors/chatParticipants.md) = \['chat_id' => [int](../types/int.md), 'participants' => \[[ChatParticipant](../types/ChatParticipant.md)\], 'version' => [int](../types/int.md), \];<a name="chatParticipants"></a>  

***
<br><br>[$chatParticipantsForbidden](../constructors/chatParticipantsForbidden.md) = \['chat_id' => [int](../types/int.md), 'self_participant' => [ChatParticipant](../types/ChatParticipant.md), \];<a name="chatParticipantsForbidden"></a>  

***
<br><br>[$chatPhoto](../constructors/chatPhoto.md) = \['photo_small' => [FileLocation](../types/FileLocation.md), 'photo_big' => [FileLocation](../types/FileLocation.md), 'dc_id' => [int](../types/int.md), \];<a name="chatPhoto"></a>  

***
<br><br>[$chatPhotoEmpty](../constructors/chatPhotoEmpty.md) = \[\];<a name="chatPhotoEmpty"></a>  

***
<br><br>[$codeSettings](../constructors/codeSettings.md) = \['allow_flashcall' => [Bool](../types/Bool.md), 'current_number' => [Bool](../types/Bool.md), 'allow_app_hash' => [Bool](../types/Bool.md), \];<a name="codeSettings"></a>  

***
<br><br>[$config](../constructors/config.md) = \['phonecalls_enabled' => [Bool](../types/Bool.md), 'default_p2p_contacts' => [Bool](../types/Bool.md), 'preload_featured_stickers' => [Bool](../types/Bool.md), 'ignore_phone_entities' => [Bool](../types/Bool.md), 'revoke_pm_inbox' => [Bool](../types/Bool.md), 'blocked_mode' => [Bool](../types/Bool.md), 'pfs_enabled' => [Bool](../types/Bool.md), 'date' => [int](../types/int.md), 'expires' => [int](../types/int.md), 'test_mode' => [Bool](../types/Bool.md), 'this_dc' => [int](../types/int.md), 'dc_options' => \[[DcOption](../types/DcOption.md)\], 'dc_txt_domain_name' => [string](../types/string.md), 'chat_size_max' => [int](../types/int.md), 'megagroup_size_max' => [int](../types/int.md), 'forwarded_count_max' => [int](../types/int.md), 'online_update_period_ms' => [int](../types/int.md), 'offline_blur_timeout_ms' => [int](../types/int.md), 'offline_idle_timeout_ms' => [int](../types/int.md), 'online_cloud_timeout_ms' => [int](../types/int.md), 'notify_cloud_delay_ms' => [int](../types/int.md), 'notify_default_delay_ms' => [int](../types/int.md), 'push_chat_period_ms' => [int](../types/int.md), 'push_chat_limit' => [int](../types/int.md), 'saved_gifs_limit' => [int](../types/int.md), 'edit_time_limit' => [int](../types/int.md), 'revoke_time_limit' => [int](../types/int.md), 'revoke_pm_time_limit' => [int](../types/int.md), 'rating_e_decay' => [int](../types/int.md), 'stickers_recent_limit' => [int](../types/int.md), 'stickers_faved_limit' => [int](../types/int.md), 'channels_read_media_period' => [int](../types/int.md), 'tmp_sessions' => [int](../types/int.md), 'pinned_dialogs_count_max' => [int](../types/int.md), 'pinned_infolder_count_max' => [int](../types/int.md), 'call_receive_timeout_ms' => [int](../types/int.md), 'call_ring_timeout_ms' => [int](../types/int.md), 'call_connect_timeout_ms' => [int](../types/int.md), 'call_packet_timeout_ms' => [int](../types/int.md), 'me_url_prefix' => [string](../types/string.md), 'autoupdate_url_prefix' => [string](../types/string.md), 'gif_search_username' => [string](../types/string.md), 'venue_search_username' => [string](../types/string.md), 'img_search_username' => [string](../types/string.md), 'static_maps_provider' => [string](../types/string.md), 'caption_length_max' => [int](../types/int.md), 'message_length_max' => [int](../types/int.md), 'webfile_dc_id' => [int](../types/int.md), 'suggested_lang_code' => [string](../types/string.md), 'lang_pack_version' => [int](../types/int.md), 'base_lang_pack_version' => [int](../types/int.md), \];<a name="config"></a>  

***
<br><br>[$contact](../constructors/contact.md) = \['user_id' => [int](../types/int.md), 'mutual' => [Bool](../types/Bool.md), \];<a name="contact"></a>  

***
<br><br>[$contactBlocked](../constructors/contactBlocked.md) = \['user_id' => [int](../types/int.md), 'date' => [int](../types/int.md), \];<a name="contactBlocked"></a>  

***
<br><br>[$contactStatus](../constructors/contactStatus.md) = \['user_id' => [int](../types/int.md), 'status' => [UserStatus](../types/UserStatus.md), \];<a name="contactStatus"></a>  

***
<br><br>[$contacts\_blocked](../constructors/contacts_blocked.md) = \['blocked' => \[[ContactBlocked](../types/ContactBlocked.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts_blocked"></a>  

[$contacts\_blockedSlice](../constructors/contacts_blockedSlice.md) = \['count' => [int](../types/int.md), 'blocked' => \[[ContactBlocked](../types/ContactBlocked.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts_blockedSlice"></a>  

[$contacts\_contacts](../constructors/contacts_contacts.md) = \['contacts' => \[[Contact](../types/Contact.md)\], 'saved_count' => [int](../types/int.md), 'users' => \[[User](../types/User.md)\], \];<a name="contacts_contacts"></a>  

[$contacts\_contactsNotModified](../constructors/contacts_contactsNotModified.md) = \[\];<a name="contacts_contactsNotModified"></a>  

[$contacts\_found](../constructors/contacts_found.md) = \['my_results' => \[[Peer](../types/Peer.md)\], 'results' => \[[Peer](../types/Peer.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts_found"></a>  

[$contacts\_importedContacts](../constructors/contacts_importedContacts.md) = \['imported' => \[[ImportedContact](../types/ImportedContact.md)\], 'popular_invites' => \[[PopularContact](../types/PopularContact.md)\], 'retry_contacts' => \[[long](../types/long.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts_importedContacts"></a>  

[$contacts\_resolvedPeer](../constructors/contacts_resolvedPeer.md) = \['peer' => [Peer](../types/Peer.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts_resolvedPeer"></a>  

[$contacts\_topPeers](../constructors/contacts_topPeers.md) = \['categories' => \[[TopPeerCategoryPeers](../types/TopPeerCategoryPeers.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts_topPeers"></a>  

[$contacts\_topPeersDisabled](../constructors/contacts_topPeersDisabled.md) = \[\];<a name="contacts_topPeersDisabled"></a>  

[$contacts\_topPeersNotModified](../constructors/contacts_topPeersNotModified.md) = \[\];<a name="contacts_topPeersNotModified"></a>  

***
<br><br>[$dataJSON](../constructors/dataJSON.md) = \['data' => [string](../types/string.md), \];<a name="dataJSON"></a>  

***
<br><br>[$dcOption](../constructors/dcOption.md) = \['ipv6' => [Bool](../types/Bool.md), 'media_only' => [Bool](../types/Bool.md), 'tcpo_only' => [Bool](../types/Bool.md), 'cdn' => [Bool](../types/Bool.md), 'static' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'ip_address' => [string](../types/string.md), 'port' => [int](../types/int.md), 'secret' => [bytes](../types/bytes.md), \];<a name="dcOption"></a>  

***
<br><br>[$dialog](../constructors/dialog.md) = \['pinned' => [Bool](../types/Bool.md), 'unread_mark' => [Bool](../types/Bool.md), 'peer' => [Peer](../types/Peer.md), 'top_message' => [int](../types/int.md), 'read_inbox_max_id' => [int](../types/int.md), 'read_outbox_max_id' => [int](../types/int.md), 'unread_count' => [int](../types/int.md), 'unread_mentions_count' => [int](../types/int.md), 'notify_settings' => [PeerNotifySettings](../types/PeerNotifySettings.md), 'pts' => [int](../types/int.md), 'draft' => [DraftMessage](../types/DraftMessage.md), 'folder_id' => [int](../types/int.md), \];<a name="dialog"></a>  

***
<br><br>[$dialogFolder](../constructors/dialogFolder.md) = \['pinned' => [Bool](../types/Bool.md), 'folder' => [Folder](../types/Folder.md), 'peer' => [Peer](../types/Peer.md), 'top_message' => [int](../types/int.md), 'unread_muted_peers_count' => [int](../types/int.md), 'unread_unmuted_peers_count' => [int](../types/int.md), 'unread_muted_messages_count' => [int](../types/int.md), 'unread_unmuted_messages_count' => [int](../types/int.md), \];<a name="dialogFolder"></a>  

***
<br><br>[$dialogPeer](../constructors/dialogPeer.md) = \['peer' => [Peer](../types/Peer.md), \];<a name="dialogPeer"></a>  

***
<br><br>[$dialogPeerFolder](../constructors/dialogPeerFolder.md) = \['folder_id' => [int](../types/int.md), \];<a name="dialogPeerFolder"></a>  

***
<br><br>[$document](../constructors/document.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'file_reference' => [bytes](../types/bytes.md), 'date' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'size' => [int](../types/int.md), 'thumbs' => \[[PhotoSize](../types/PhotoSize.md)\], 'dc_id' => [int](../types/int.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], \];<a name="document"></a>  

***
<br><br>[$documentAttributeAnimated](../constructors/documentAttributeAnimated.md) = \[\];<a name="documentAttributeAnimated"></a>  

***
<br><br>[$documentAttributeAudio](../constructors/documentAttributeAudio.md) = \['voice' => [Bool](../types/Bool.md), 'duration' => [int](../types/int.md), 'title' => [string](../types/string.md), 'performer' => [string](../types/string.md), 'waveform' => [bytes](../types/bytes.md), \];<a name="documentAttributeAudio"></a>  

***
<br><br>[$documentAttributeFilename](../constructors/documentAttributeFilename.md) = \['file_name' => [string](../types/string.md), \];<a name="documentAttributeFilename"></a>  

***
<br><br>[$documentAttributeHasStickers](../constructors/documentAttributeHasStickers.md) = \[\];<a name="documentAttributeHasStickers"></a>  

***
<br><br>[$documentAttributeImageSize](../constructors/documentAttributeImageSize.md) = \['w' => [int](../types/int.md), 'h' => [int](../types/int.md), \];<a name="documentAttributeImageSize"></a>  

***
<br><br>[$documentAttributeSticker](../constructors/documentAttributeSticker.md) = \['mask' => [Bool](../types/Bool.md), 'alt' => [string](../types/string.md), 'stickerset' => [InputStickerSet](../types/InputStickerSet.md), 'mask_coords' => [MaskCoords](../types/MaskCoords.md), \];<a name="documentAttributeSticker"></a>  

***
<br><br>[$documentAttributeVideo](../constructors/documentAttributeVideo.md) = \['round_message' => [Bool](../types/Bool.md), 'supports_streaming' => [Bool](../types/Bool.md), 'duration' => [int](../types/int.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), \];<a name="documentAttributeVideo"></a>  

***
<br><br>[$documentEmpty](../constructors/documentEmpty.md) = \['id' => [long](../types/long.md), \];<a name="documentEmpty"></a>  

***
<br><br>[$draftMessage](../constructors/draftMessage.md) = \['no_webpage' => [Bool](../types/Bool.md), 'reply_to_msg_id' => [int](../types/int.md), 'message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'date' => [int](../types/int.md), \];<a name="draftMessage"></a>  

***
<br><br>[$draftMessageEmpty](../constructors/draftMessageEmpty.md) = \['date' => [int](../types/int.md), \];<a name="draftMessageEmpty"></a>  

***
<br><br>[$emojiKeyword](../constructors/emojiKeyword.md) = \['keyword' => [string](../types/string.md), 'emoticons' => \[[string](../types/string.md)\], \];<a name="emojiKeyword"></a>  

***
<br><br>[$emojiKeywordDeleted](../constructors/emojiKeywordDeleted.md) = \['keyword' => [string](../types/string.md), 'emoticons' => \[[string](../types/string.md)\], \];<a name="emojiKeywordDeleted"></a>  

***
<br><br>[$emojiKeywordsDifference](../constructors/emojiKeywordsDifference.md) = \['lang_code' => [string](../types/string.md), 'from_version' => [int](../types/int.md), 'version' => [int](../types/int.md), 'keywords' => \[[EmojiKeyword](../types/EmojiKeyword.md)\], \];<a name="emojiKeywordsDifference"></a>  

***
<br><br>[$emojiLanguage](../constructors/emojiLanguage.md) = \['lang_code' => [string](../types/string.md), \];<a name="emojiLanguage"></a>  

***
<br><br>[$emojiURL](../constructors/emojiURL.md) = \['url' => [string](../types/string.md), \];<a name="emojiURL"></a>  

***
<br><br>[$encryptedChat](../constructors/encryptedChat.md) = \['id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [int](../types/int.md), 'participant_id' => [int](../types/int.md), 'g_a_or_b' => [bytes](../types/bytes.md), 'key_fingerprint' => [long](../types/long.md), \];<a name="encryptedChat"></a>  

***
<br><br>[$encryptedChatDiscarded](../constructors/encryptedChatDiscarded.md) = \['id' => [int](../types/int.md), \];<a name="encryptedChatDiscarded"></a>  

***
<br><br>[$encryptedChatEmpty](../constructors/encryptedChatEmpty.md) = \['id' => [int](../types/int.md), \];<a name="encryptedChatEmpty"></a>  

***
<br><br>[$encryptedChatRequested](../constructors/encryptedChatRequested.md) = \['id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [int](../types/int.md), 'participant_id' => [int](../types/int.md), 'g_a' => [bytes](../types/bytes.md), \];<a name="encryptedChatRequested"></a>  

***
<br><br>[$encryptedChatWaiting](../constructors/encryptedChatWaiting.md) = \['id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [int](../types/int.md), 'participant_id' => [int](../types/int.md), \];<a name="encryptedChatWaiting"></a>  

***
<br><br>[$encryptedFile](../constructors/encryptedFile.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'size' => [int](../types/int.md), 'dc_id' => [int](../types/int.md), 'key_fingerprint' => [int](../types/int.md), \];<a name="encryptedFile"></a>  

***
<br><br>[$encryptedFileEmpty](../constructors/encryptedFileEmpty.md) = \[\];<a name="encryptedFileEmpty"></a>  

***
<br><br>[$encryptedMessage](../constructors/encryptedMessage.md) = \['chat_id' => [int](../types/int.md), 'date' => [int](../types/int.md), 'decrypted_message' => [DecryptedMessage](../types/DecryptedMessage.md), 'file' => [EncryptedFile](../types/EncryptedFile.md), \];<a name="encryptedMessage"></a>  

***
<br><br>[$encryptedMessageService](../constructors/encryptedMessageService.md) = \['chat_id' => [int](../types/int.md), 'date' => [int](../types/int.md), 'decrypted_message' => [DecryptedMessage](../types/DecryptedMessage.md), \];<a name="encryptedMessageService"></a>  

***
<br><br>[$error](../constructors/error.md) = \['code' => [int](../types/int.md), 'text' => [string](../types/string.md), \];<a name="error"></a>  

***
<br><br>[$exportedMessageLink](../constructors/exportedMessageLink.md) = \['link' => [string](../types/string.md), 'html' => [string](../types/string.md), \];<a name="exportedMessageLink"></a>  

***
<br><br>[$fileHash](../constructors/fileHash.md) = \['offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), 'hash' => [bytes](../types/bytes.md), \];<a name="fileHash"></a>  

***
<br><br>[$fileLocationToBeDeprecated](../constructors/fileLocationToBeDeprecated.md) = \['volume_id' => [long](../types/long.md), 'local_id' => [int](../types/int.md), \];<a name="fileLocationToBeDeprecated"></a>  

***
<br><br>[$folder](../constructors/folder.md) = \['autofill_new_broadcasts' => [Bool](../types/Bool.md), 'autofill_public_groups' => [Bool](../types/Bool.md), 'autofill_new_correspondents' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'title' => [string](../types/string.md), 'photo' => [ChatPhoto](../types/ChatPhoto.md), \];<a name="folder"></a>  

***
<br><br>[$folderPeer](../constructors/folderPeer.md) = \['peer' => [Peer](../types/Peer.md), 'folder_id' => [int](../types/int.md), \];<a name="folderPeer"></a>  

***
<br><br>[$foundGif](../constructors/foundGif.md) = \['url' => [string](../types/string.md), 'thumb_url' => [string](../types/string.md), 'content_url' => [string](../types/string.md), 'content_type' => [string](../types/string.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), \];<a name="foundGif"></a>  

***
<br><br>[$foundGifCached](../constructors/foundGifCached.md) = \['url' => [string](../types/string.md), 'photo' => [Photo](../types/Photo.md), 'document' => [Document](../types/Document.md), \];<a name="foundGifCached"></a>  

***
<br><br>[$game](../constructors/game.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'short_name' => [string](../types/string.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'photo' => [Photo](../types/Photo.md), 'document' => [Document](../types/Document.md), \];<a name="game"></a>  

***
<br><br>[$geoPoint](../constructors/geoPoint.md) = \['long' => [double](../types/double.md), 'lat' => [double](../types/double.md), 'access_hash' => [long](../types/long.md), \];<a name="geoPoint"></a>  

***
<br><br>[$geoPointEmpty](../constructors/geoPointEmpty.md) = \[\];<a name="geoPointEmpty"></a>  

***
<br><br>[$help\_appUpdate](../constructors/help_appUpdate.md) = \['can_not_skip' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'version' => [string](../types/string.md), 'text' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'document' => [Document](../types/Document.md), 'url' => [string](../types/string.md), \];<a name="help_appUpdate"></a>  

[$help\_configSimple](../constructors/help_configSimple.md) = \['date' => [int](../types/int.md), 'expires' => [int](../types/int.md), 'rules' => \[[AccessPointRule](../types/AccessPointRule.md)\], \];<a name="help_configSimple"></a>  

[$help\_deepLinkInfo](../constructors/help_deepLinkInfo.md) = \['update_app' => [Bool](../types/Bool.md), 'message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \];<a name="help_deepLinkInfo"></a>  

[$help\_deepLinkInfoEmpty](../constructors/help_deepLinkInfoEmpty.md) = \[\];<a name="help_deepLinkInfoEmpty"></a>  

[$help\_inviteText](../constructors/help_inviteText.md) = \['message' => [string](../types/string.md), \];<a name="help_inviteText"></a>  

[$help\_noAppUpdate](../constructors/help_noAppUpdate.md) = \[\];<a name="help_noAppUpdate"></a>  

[$help\_passportConfig](../constructors/help_passportConfig.md) = \['hash' => [int](../types/int.md), 'countries_langs' => [DataJSON](../types/DataJSON.md), \];<a name="help_passportConfig"></a>  

[$help\_passportConfigNotModified](../constructors/help_passportConfigNotModified.md) = \[\];<a name="help_passportConfigNotModified"></a>  

[$help\_proxyDataEmpty](../constructors/help_proxyDataEmpty.md) = \['expires' => [int](../types/int.md), \];<a name="help_proxyDataEmpty"></a>  

[$help\_proxyDataPromo](../constructors/help_proxyDataPromo.md) = \['expires' => [int](../types/int.md), 'peer' => [Peer](../types/Peer.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="help_proxyDataPromo"></a>  

[$help\_recentMeUrls](../constructors/help_recentMeUrls.md) = \['urls' => \[[RecentMeUrl](../types/RecentMeUrl.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="help_recentMeUrls"></a>  

[$help\_support](../constructors/help_support.md) = \['phone_number' => [string](../types/string.md), 'user' => [User](../types/User.md), \];<a name="help_support"></a>  

[$help\_supportName](../constructors/help_supportName.md) = \['name' => [string](../types/string.md), \];<a name="help_supportName"></a>  

[$help\_termsOfService](../constructors/help_termsOfService.md) = \['popup' => [Bool](../types/Bool.md), 'id' => [DataJSON](../types/DataJSON.md), 'text' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'min_age_confirm' => [int](../types/int.md), \];<a name="help_termsOfService"></a>  

[$help\_termsOfServiceUpdate](../constructors/help_termsOfServiceUpdate.md) = \['expires' => [int](../types/int.md), 'terms_of_service' => [help\_TermsOfService](../types/help_TermsOfService.md), \];<a name="help_termsOfServiceUpdate"></a>  

[$help\_termsOfServiceUpdateEmpty](../constructors/help_termsOfServiceUpdateEmpty.md) = \['expires' => [int](../types/int.md), \];<a name="help_termsOfServiceUpdateEmpty"></a>  

[$help\_userInfo](../constructors/help_userInfo.md) = \['message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'author' => [string](../types/string.md), 'date' => [int](../types/int.md), \];<a name="help_userInfo"></a>  

[$help\_userInfoEmpty](../constructors/help_userInfoEmpty.md) = \[\];<a name="help_userInfoEmpty"></a>  

***
<br><br>[$highScore](../constructors/highScore.md) = \['pos' => [int](../types/int.md), 'user_id' => [int](../types/int.md), 'score' => [int](../types/int.md), \];<a name="highScore"></a>  

***
<br><br>[$importedContact](../constructors/importedContact.md) = \['user_id' => [int](../types/int.md), 'client_id' => [long](../types/long.md), \];<a name="importedContact"></a>  

***
<br><br>[$inlineBotSwitchPM](../constructors/inlineBotSwitchPM.md) = \['text' => [string](../types/string.md), 'start_param' => [string](../types/string.md), \];<a name="inlineBotSwitchPM"></a>  

***
<br><br>[$inputAppEvent](../constructors/inputAppEvent.md) = \['time' => [double](../types/double.md), 'type' => [string](../types/string.md), 'peer' => [long](../types/long.md), 'data' => [JSONValue](../types/JSONValue.md), \];<a name="inputAppEvent"></a>  

***
<br><br>[$inputBotInlineMessageGame](../constructors/inputBotInlineMessageGame.md) = \['reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="inputBotInlineMessageGame"></a>  

***
<br><br>[$inputBotInlineMessageID](../constructors/inputBotInlineMessageID.md) = \['dc_id' => [int](../types/int.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputBotInlineMessageID"></a>  

***
<br><br>[$inputBotInlineMessageMediaAuto](../constructors/inputBotInlineMessageMediaAuto.md) = \['message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaAuto"></a>  

***
<br><br>[$inputBotInlineMessageMediaContact](../constructors/inputBotInlineMessageMediaContact.md) = \['phone_number' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'vcard' => [string](../types/string.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaContact"></a>  

***
<br><br>[$inputBotInlineMessageMediaGeo](../constructors/inputBotInlineMessageMediaGeo.md) = \['geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'period' => [int](../types/int.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaGeo"></a>  

***
<br><br>[$inputBotInlineMessageMediaVenue](../constructors/inputBotInlineMessageMediaVenue.md) = \['geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'title' => [string](../types/string.md), 'address' => [string](../types/string.md), 'provider' => [string](../types/string.md), 'venue_id' => [string](../types/string.md), 'venue_type' => [string](../types/string.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaVenue"></a>  

***
<br><br>[$inputBotInlineMessageText](../constructors/inputBotInlineMessageText.md) = \['no_webpage' => [Bool](../types/Bool.md), 'message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="inputBotInlineMessageText"></a>  

***
<br><br>[$inputBotInlineResult](../constructors/inputBotInlineResult.md) = \['id' => [string](../types/string.md), 'type' => [string](../types/string.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'url' => [string](../types/string.md), 'thumb' => [InputWebDocument](../types/InputWebDocument.md), 'content' => [InputWebDocument](../types/InputWebDocument.md), 'send_message' => [InputBotInlineMessage](../types/InputBotInlineMessage.md), \];<a name="inputBotInlineResult"></a>  

***
<br><br>[$inputBotInlineResultDocument](../constructors/inputBotInlineResultDocument.md) = \['id' => [string](../types/string.md), 'type' => [string](../types/string.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'document' => [InputDocument](../types/InputDocument.md), 'send_message' => [InputBotInlineMessage](../types/InputBotInlineMessage.md), \];<a name="inputBotInlineResultDocument"></a>  

***
<br><br>[$inputBotInlineResultGame](../constructors/inputBotInlineResultGame.md) = \['id' => [string](../types/string.md), 'short_name' => [string](../types/string.md), 'send_message' => [InputBotInlineMessage](../types/InputBotInlineMessage.md), \];<a name="inputBotInlineResultGame"></a>  

***
<br><br>[$inputBotInlineResultPhoto](../constructors/inputBotInlineResultPhoto.md) = \['id' => [string](../types/string.md), 'type' => [string](../types/string.md), 'photo' => [InputPhoto](../types/InputPhoto.md), 'send_message' => [InputBotInlineMessage](../types/InputBotInlineMessage.md), \];<a name="inputBotInlineResultPhoto"></a>  

***
<br><br>[$inputChannel](../constructors/inputChannel.md) = \['channel_id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), \];<a name="inputChannel"></a>  

***
<br><br>[$inputChannelEmpty](../constructors/inputChannelEmpty.md) = \[\];<a name="inputChannelEmpty"></a>  

***
<br><br>[$inputChannelFromMessage](../constructors/inputChannelFromMessage.md) = \['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'channel_id' => [int](../types/int.md), \];<a name="inputChannelFromMessage"></a>  

***
<br><br>[$inputChatPhoto](../constructors/inputChatPhoto.md) = \['id' => [InputPhoto](../types/InputPhoto.md), \];<a name="inputChatPhoto"></a>  

***
<br><br>[$inputChatPhotoEmpty](../constructors/inputChatPhotoEmpty.md) = \[\];<a name="inputChatPhotoEmpty"></a>  

***
<br><br>[$inputChatUploadedPhoto](../constructors/inputChatUploadedPhoto.md) = \['file' => [InputFile](../types/InputFile.md), \];<a name="inputChatUploadedPhoto"></a>  

***
<br><br>[$inputCheckPasswordEmpty](../constructors/inputCheckPasswordEmpty.md) = \[\];<a name="inputCheckPasswordEmpty"></a>  

***
<br><br>[$inputCheckPasswordSRP](../constructors/inputCheckPasswordSRP.md) = \['srp_id' => [long](../types/long.md), 'A' => [bytes](../types/bytes.md), 'M1' => [bytes](../types/bytes.md), \];<a name="inputCheckPasswordSRP"></a>  

***
<br><br>[$inputClientProxy](../constructors/inputClientProxy.md) = \['address' => [string](../types/string.md), 'port' => [int](../types/int.md), \];<a name="inputClientProxy"></a>  

***
<br><br>[$inputDialogPeer](../constructors/inputDialogPeer.md) = \['peer' => [InputPeer](../types/InputPeer.md), \];<a name="inputDialogPeer"></a>  

***
<br><br>[$inputDialogPeerFolder](../constructors/inputDialogPeerFolder.md) = \['folder_id' => [int](../types/int.md), \];<a name="inputDialogPeerFolder"></a>  

***
<br><br>[$inputDocument](../constructors/inputDocument.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'file_reference' => [bytes](../types/bytes.md), \];<a name="inputDocument"></a>  

***
<br><br>[$inputDocumentEmpty](../constructors/inputDocumentEmpty.md) = \[\];<a name="inputDocumentEmpty"></a>  

***
<br><br>[$inputDocumentFileLocation](../constructors/inputDocumentFileLocation.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'file_reference' => [bytes](../types/bytes.md), 'thumb_size' => [string](../types/string.md), \];<a name="inputDocumentFileLocation"></a>  

***
<br><br>[$inputEncryptedChat](../constructors/inputEncryptedChat.md) = \['chat_id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), \];<a name="inputEncryptedChat"></a>  

***
<br><br>[$inputEncryptedFile](../constructors/inputEncryptedFile.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputEncryptedFile"></a>  

***
<br><br>[$inputEncryptedFileBigUploaded](../constructors/inputEncryptedFileBigUploaded.md) = \['id' => [long](../types/long.md), 'parts' => [int](../types/int.md), 'key_fingerprint' => [int](../types/int.md), \];<a name="inputEncryptedFileBigUploaded"></a>  

***
<br><br>[$inputEncryptedFileEmpty](../constructors/inputEncryptedFileEmpty.md) = \[\];<a name="inputEncryptedFileEmpty"></a>  

***
<br><br>[$inputEncryptedFileLocation](../constructors/inputEncryptedFileLocation.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputEncryptedFileLocation"></a>  

***
<br><br>[$inputEncryptedFileUploaded](../constructors/inputEncryptedFileUploaded.md) = \['id' => [long](../types/long.md), 'parts' => [int](../types/int.md), 'md5_checksum' => [string](../types/string.md), 'key_fingerprint' => [int](../types/int.md), \];<a name="inputEncryptedFileUploaded"></a>  

***
<br><br>[$inputFile](../constructors/inputFile.md) = \['id' => [long](../types/long.md), 'parts' => [int](../types/int.md), 'name' => [string](../types/string.md), 'md5_checksum' => [string](../types/string.md), \];<a name="inputFile"></a>  

***
<br><br>[$inputFileBig](../constructors/inputFileBig.md) = \['id' => [long](../types/long.md), 'parts' => [int](../types/int.md), 'name' => [string](../types/string.md), \];<a name="inputFileBig"></a>  

***
<br><br>[$inputFileLocation](../constructors/inputFileLocation.md) = \['volume_id' => [long](../types/long.md), 'local_id' => [int](../types/int.md), 'secret' => [long](../types/long.md), 'file_reference' => [bytes](../types/bytes.md), \];<a name="inputFileLocation"></a>  

***
<br><br>[$inputFolderPeer](../constructors/inputFolderPeer.md) = \['peer' => [InputPeer](../types/InputPeer.md), 'folder_id' => [int](../types/int.md), \];<a name="inputFolderPeer"></a>  

***
<br><br>[$inputGameID](../constructors/inputGameID.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputGameID"></a>  

***
<br><br>[$inputGameShortName](../constructors/inputGameShortName.md) = \['bot_id' => [InputUser](../types/InputUser.md), 'short_name' => [string](../types/string.md), \];<a name="inputGameShortName"></a>  

***
<br><br>[$inputGeoPoint](../constructors/inputGeoPoint.md) = \['lat' => [double](../types/double.md), 'long' => [double](../types/double.md), \];<a name="inputGeoPoint"></a>  

***
<br><br>[$inputGeoPointEmpty](../constructors/inputGeoPointEmpty.md) = \[\];<a name="inputGeoPointEmpty"></a>  

***
<br><br>[$inputKeyboardButtonUrlAuth](../constructors/inputKeyboardButtonUrlAuth.md) = \['request_write_access' => [Bool](../types/Bool.md), 'text' => [string](../types/string.md), 'fwd_text' => [string](../types/string.md), 'url' => [string](../types/string.md), 'bot' => [InputUser](../types/InputUser.md), \];<a name="inputKeyboardButtonUrlAuth"></a>  

***
<br><br>[$inputMediaContact](../constructors/inputMediaContact.md) = \['phone_number' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'vcard' => [string](../types/string.md), \];<a name="inputMediaContact"></a>  

***
<br><br>[$inputMediaDocument](../constructors/inputMediaDocument.md) = \['id' => [InputDocument](../types/InputDocument.md), 'ttl_seconds' => [int](../types/int.md), \];<a name="inputMediaDocument"></a>  

***
<br><br>[$inputMediaDocumentExternal](../constructors/inputMediaDocumentExternal.md) = \['url' => [string](../types/string.md), 'ttl_seconds' => [int](../types/int.md), \];<a name="inputMediaDocumentExternal"></a>  

***
<br><br>[$inputMediaEmpty](../constructors/inputMediaEmpty.md) = \[\];<a name="inputMediaEmpty"></a>  

***
<br><br>[$inputMediaGame](../constructors/inputMediaGame.md) = \['id' => [InputGame](../types/InputGame.md), \];<a name="inputMediaGame"></a>  

***
<br><br>[$inputMediaGeoLive](../constructors/inputMediaGeoLive.md) = \['stopped' => [Bool](../types/Bool.md), 'geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'period' => [int](../types/int.md), \];<a name="inputMediaGeoLive"></a>  

***
<br><br>[$inputMediaGeoPoint](../constructors/inputMediaGeoPoint.md) = \['geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), \];<a name="inputMediaGeoPoint"></a>  

***
<br><br>[$inputMediaGifExternal](../constructors/inputMediaGifExternal.md) = \['url' => [string](../types/string.md), 'q' => [string](../types/string.md), \];<a name="inputMediaGifExternal"></a>  

***
<br><br>[$inputMediaInvoice](../constructors/inputMediaInvoice.md) = \['title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'photo' => [InputWebDocument](../types/InputWebDocument.md), 'invoice' => [Invoice](../types/Invoice.md), 'payload' => [bytes](../types/bytes.md), 'provider' => [string](../types/string.md), 'provider_data' => [DataJSON](../types/DataJSON.md), 'start_param' => [string](../types/string.md), \];<a name="inputMediaInvoice"></a>  

***
<br><br>[$inputMediaPhoto](../constructors/inputMediaPhoto.md) = \['id' => [InputPhoto](../types/InputPhoto.md), 'ttl_seconds' => [int](../types/int.md), \];<a name="inputMediaPhoto"></a>  

***
<br><br>[$inputMediaPhotoExternal](../constructors/inputMediaPhotoExternal.md) = \['url' => [string](../types/string.md), 'ttl_seconds' => [int](../types/int.md), \];<a name="inputMediaPhotoExternal"></a>  

***
<br><br>[$inputMediaPoll](../constructors/inputMediaPoll.md) = \['poll' => [Poll](../types/Poll.md), \];<a name="inputMediaPoll"></a>  

***
<br><br>[$inputMediaUploadedDocument](../constructors/inputMediaUploadedDocument.md) = \['nosound_video' => [Bool](../types/Bool.md), 'file' => [InputFile](../types/InputFile.md), 'thumb' => [InputFile](../types/InputFile.md), 'mime_type' => [string](../types/string.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], 'stickers' => \[[InputDocument](../types/InputDocument.md)\], 'ttl_seconds' => [int](../types/int.md), \];<a name="inputMediaUploadedDocument"></a>  

***
<br><br>[$inputMediaUploadedPhoto](../constructors/inputMediaUploadedPhoto.md) = \['file' => [InputFile](../types/InputFile.md), 'stickers' => \[[InputDocument](../types/InputDocument.md)\], 'ttl_seconds' => [int](../types/int.md), \];<a name="inputMediaUploadedPhoto"></a>  

***
<br><br>[$inputMediaVenue](../constructors/inputMediaVenue.md) = \['geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'title' => [string](../types/string.md), 'address' => [string](../types/string.md), 'provider' => [string](../types/string.md), 'venue_id' => [string](../types/string.md), 'venue_type' => [string](../types/string.md), \];<a name="inputMediaVenue"></a>  

***
<br><br>[$inputMessageEntityMentionName](../constructors/inputMessageEntityMentionName.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), 'user_id' => [InputUser](../types/InputUser.md), \];<a name="inputMessageEntityMentionName"></a>  

***
<br><br>[$inputMessageID](../constructors/inputMessageID.md) = \['id' => [int](../types/int.md), \];<a name="inputMessageID"></a>  

***
<br><br>[$inputMessagePinned](../constructors/inputMessagePinned.md) = \[\];<a name="inputMessagePinned"></a>  

***
<br><br>[$inputMessageReplyTo](../constructors/inputMessageReplyTo.md) = \['id' => [int](../types/int.md), \];<a name="inputMessageReplyTo"></a>  

***
<br><br>[$inputMessagesFilterChatPhotos](../constructors/inputMessagesFilterChatPhotos.md) = \[\];<a name="inputMessagesFilterChatPhotos"></a>  

***
<br><br>[$inputMessagesFilterContacts](../constructors/inputMessagesFilterContacts.md) = \[\];<a name="inputMessagesFilterContacts"></a>  

***
<br><br>[$inputMessagesFilterDocument](../constructors/inputMessagesFilterDocument.md) = \[\];<a name="inputMessagesFilterDocument"></a>  

***
<br><br>[$inputMessagesFilterEmpty](../constructors/inputMessagesFilterEmpty.md) = \[\];<a name="inputMessagesFilterEmpty"></a>  

***
<br><br>[$inputMessagesFilterGeo](../constructors/inputMessagesFilterGeo.md) = \[\];<a name="inputMessagesFilterGeo"></a>  

***
<br><br>[$inputMessagesFilterGif](../constructors/inputMessagesFilterGif.md) = \[\];<a name="inputMessagesFilterGif"></a>  

***
<br><br>[$inputMessagesFilterMusic](../constructors/inputMessagesFilterMusic.md) = \[\];<a name="inputMessagesFilterMusic"></a>  

***
<br><br>[$inputMessagesFilterMyMentions](../constructors/inputMessagesFilterMyMentions.md) = \[\];<a name="inputMessagesFilterMyMentions"></a>  

***
<br><br>[$inputMessagesFilterPhoneCalls](../constructors/inputMessagesFilterPhoneCalls.md) = \['missed' => [Bool](../types/Bool.md), \];<a name="inputMessagesFilterPhoneCalls"></a>  

***
<br><br>[$inputMessagesFilterPhotoVideo](../constructors/inputMessagesFilterPhotoVideo.md) = \[\];<a name="inputMessagesFilterPhotoVideo"></a>  

***
<br><br>[$inputMessagesFilterPhotos](../constructors/inputMessagesFilterPhotos.md) = \[\];<a name="inputMessagesFilterPhotos"></a>  

***
<br><br>[$inputMessagesFilterRoundVideo](../constructors/inputMessagesFilterRoundVideo.md) = \[\];<a name="inputMessagesFilterRoundVideo"></a>  

***
<br><br>[$inputMessagesFilterRoundVoice](../constructors/inputMessagesFilterRoundVoice.md) = \[\];<a name="inputMessagesFilterRoundVoice"></a>  

***
<br><br>[$inputMessagesFilterUrl](../constructors/inputMessagesFilterUrl.md) = \[\];<a name="inputMessagesFilterUrl"></a>  

***
<br><br>[$inputMessagesFilterVideo](../constructors/inputMessagesFilterVideo.md) = \[\];<a name="inputMessagesFilterVideo"></a>  

***
<br><br>[$inputMessagesFilterVoice](../constructors/inputMessagesFilterVoice.md) = \[\];<a name="inputMessagesFilterVoice"></a>  

***
<br><br>[$inputNotifyBroadcasts](../constructors/inputNotifyBroadcasts.md) = \[\];<a name="inputNotifyBroadcasts"></a>  

***
<br><br>[$inputNotifyChats](../constructors/inputNotifyChats.md) = \[\];<a name="inputNotifyChats"></a>  

***
<br><br>[$inputNotifyPeer](../constructors/inputNotifyPeer.md) = \['peer' => [InputPeer](../types/InputPeer.md), \];<a name="inputNotifyPeer"></a>  

***
<br><br>[$inputNotifyUsers](../constructors/inputNotifyUsers.md) = \[\];<a name="inputNotifyUsers"></a>  

***
<br><br>[$inputPaymentCredentials](../constructors/inputPaymentCredentials.md) = \['save' => [Bool](../types/Bool.md), 'data' => [DataJSON](../types/DataJSON.md), \];<a name="inputPaymentCredentials"></a>  

***
<br><br>[$inputPaymentCredentialsAndroidPay](../constructors/inputPaymentCredentialsAndroidPay.md) = \['payment_token' => [DataJSON](../types/DataJSON.md), 'google_transaction_id' => [string](../types/string.md), \];<a name="inputPaymentCredentialsAndroidPay"></a>  

***
<br><br>[$inputPaymentCredentialsApplePay](../constructors/inputPaymentCredentialsApplePay.md) = \['payment_data' => [DataJSON](../types/DataJSON.md), \];<a name="inputPaymentCredentialsApplePay"></a>  

***
<br><br>[$inputPaymentCredentialsSaved](../constructors/inputPaymentCredentialsSaved.md) = \['id' => [string](../types/string.md), 'tmp_password' => [bytes](../types/bytes.md), \];<a name="inputPaymentCredentialsSaved"></a>  

***
<br><br>[$inputPeerChannel](../constructors/inputPeerChannel.md) = \['channel_id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), \];<a name="inputPeerChannel"></a>  

***
<br><br>[$inputPeerChannelFromMessage](../constructors/inputPeerChannelFromMessage.md) = \['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'channel_id' => [int](../types/int.md), \];<a name="inputPeerChannelFromMessage"></a>  

***
<br><br>[$inputPeerChat](../constructors/inputPeerChat.md) = \['chat_id' => [int](../types/int.md), \];<a name="inputPeerChat"></a>  

***
<br><br>[$inputPeerEmpty](../constructors/inputPeerEmpty.md) = \[\];<a name="inputPeerEmpty"></a>  

***
<br><br>[$inputPeerNotifySettings](../constructors/inputPeerNotifySettings.md) = \['show_previews' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'mute_until' => [int](../types/int.md), 'sound' => [string](../types/string.md), \];<a name="inputPeerNotifySettings"></a>  

***
<br><br>[$inputPeerPhotoFileLocation](../constructors/inputPeerPhotoFileLocation.md) = \['big' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'volume_id' => [long](../types/long.md), 'local_id' => [int](../types/int.md), \];<a name="inputPeerPhotoFileLocation"></a>  

***
<br><br>[$inputPeerSelf](../constructors/inputPeerSelf.md) = \[\];<a name="inputPeerSelf"></a>  

***
<br><br>[$inputPeerUser](../constructors/inputPeerUser.md) = \['user_id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), \];<a name="inputPeerUser"></a>  

***
<br><br>[$inputPeerUserFromMessage](../constructors/inputPeerUserFromMessage.md) = \['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'user_id' => [int](../types/int.md), \];<a name="inputPeerUserFromMessage"></a>  

***
<br><br>[$inputPhoneCall](../constructors/inputPhoneCall.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputPhoneCall"></a>  

***
<br><br>[$inputPhoneContact](../constructors/inputPhoneContact.md) = \['client_id' => [long](../types/long.md), 'phone' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), \];<a name="inputPhoneContact"></a>  

***
<br><br>[$inputPhoto](../constructors/inputPhoto.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'file_reference' => [bytes](../types/bytes.md), \];<a name="inputPhoto"></a>  

***
<br><br>[$inputPhotoEmpty](../constructors/inputPhotoEmpty.md) = \[\];<a name="inputPhotoEmpty"></a>  

***
<br><br>[$inputPhotoFileLocation](../constructors/inputPhotoFileLocation.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'file_reference' => [bytes](../types/bytes.md), 'thumb_size' => [string](../types/string.md), \];<a name="inputPhotoFileLocation"></a>  

***
<br><br>[$inputPrivacyKeyAddedByPhone](../constructors/inputPrivacyKeyAddedByPhone.md) = \[\];<a name="inputPrivacyKeyAddedByPhone"></a>  

***
<br><br>[$inputPrivacyKeyChatInvite](../constructors/inputPrivacyKeyChatInvite.md) = \[\];<a name="inputPrivacyKeyChatInvite"></a>  

***
<br><br>[$inputPrivacyKeyForwards](../constructors/inputPrivacyKeyForwards.md) = \[\];<a name="inputPrivacyKeyForwards"></a>  

***
<br><br>[$inputPrivacyKeyPhoneCall](../constructors/inputPrivacyKeyPhoneCall.md) = \[\];<a name="inputPrivacyKeyPhoneCall"></a>  

***
<br><br>[$inputPrivacyKeyPhoneNumber](../constructors/inputPrivacyKeyPhoneNumber.md) = \[\];<a name="inputPrivacyKeyPhoneNumber"></a>  

***
<br><br>[$inputPrivacyKeyPhoneP2P](../constructors/inputPrivacyKeyPhoneP2P.md) = \[\];<a name="inputPrivacyKeyPhoneP2P"></a>  

***
<br><br>[$inputPrivacyKeyProfilePhoto](../constructors/inputPrivacyKeyProfilePhoto.md) = \[\];<a name="inputPrivacyKeyProfilePhoto"></a>  

***
<br><br>[$inputPrivacyKeyStatusTimestamp](../constructors/inputPrivacyKeyStatusTimestamp.md) = \[\];<a name="inputPrivacyKeyStatusTimestamp"></a>  

***
<br><br>[$inputPrivacyValueAllowAll](../constructors/inputPrivacyValueAllowAll.md) = \[\];<a name="inputPrivacyValueAllowAll"></a>  

***
<br><br>[$inputPrivacyValueAllowChatParticipants](../constructors/inputPrivacyValueAllowChatParticipants.md) = \['chats' => \[[int](../types/int.md)\], \];<a name="inputPrivacyValueAllowChatParticipants"></a>  

***
<br><br>[$inputPrivacyValueAllowContacts](../constructors/inputPrivacyValueAllowContacts.md) = \[\];<a name="inputPrivacyValueAllowContacts"></a>  

***
<br><br>[$inputPrivacyValueAllowUsers](../constructors/inputPrivacyValueAllowUsers.md) = \['users' => \[[InputUser](../types/InputUser.md)\], \];<a name="inputPrivacyValueAllowUsers"></a>  

***
<br><br>[$inputPrivacyValueDisallowAll](../constructors/inputPrivacyValueDisallowAll.md) = \[\];<a name="inputPrivacyValueDisallowAll"></a>  

***
<br><br>[$inputPrivacyValueDisallowChatParticipants](../constructors/inputPrivacyValueDisallowChatParticipants.md) = \['chats' => \[[int](../types/int.md)\], \];<a name="inputPrivacyValueDisallowChatParticipants"></a>  

***
<br><br>[$inputPrivacyValueDisallowContacts](../constructors/inputPrivacyValueDisallowContacts.md) = \[\];<a name="inputPrivacyValueDisallowContacts"></a>  

***
<br><br>[$inputPrivacyValueDisallowUsers](../constructors/inputPrivacyValueDisallowUsers.md) = \['users' => \[[InputUser](../types/InputUser.md)\], \];<a name="inputPrivacyValueDisallowUsers"></a>  

***
<br><br>[$inputReportReasonChildAbuse](../constructors/inputReportReasonChildAbuse.md) = \[\];<a name="inputReportReasonChildAbuse"></a>  

***
<br><br>[$inputReportReasonCopyright](../constructors/inputReportReasonCopyright.md) = \[\];<a name="inputReportReasonCopyright"></a>  

***
<br><br>[$inputReportReasonGeoIrrelevant](../constructors/inputReportReasonGeoIrrelevant.md) = \[\];<a name="inputReportReasonGeoIrrelevant"></a>  

***
<br><br>[$inputReportReasonOther](../constructors/inputReportReasonOther.md) = \['text' => [string](../types/string.md), \];<a name="inputReportReasonOther"></a>  

***
<br><br>[$inputReportReasonPornography](../constructors/inputReportReasonPornography.md) = \[\];<a name="inputReportReasonPornography"></a>  

***
<br><br>[$inputReportReasonSpam](../constructors/inputReportReasonSpam.md) = \[\];<a name="inputReportReasonSpam"></a>  

***
<br><br>[$inputReportReasonViolence](../constructors/inputReportReasonViolence.md) = \[\];<a name="inputReportReasonViolence"></a>  

***
<br><br>[$inputSecureFile](../constructors/inputSecureFile.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputSecureFile"></a>  

***
<br><br>[$inputSecureFileLocation](../constructors/inputSecureFileLocation.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputSecureFileLocation"></a>  

***
<br><br>[$inputSecureFileUploaded](../constructors/inputSecureFileUploaded.md) = \['id' => [long](../types/long.md), 'parts' => [int](../types/int.md), 'md5_checksum' => [string](../types/string.md), 'file_hash' => [bytes](../types/bytes.md), 'secret' => [bytes](../types/bytes.md), \];<a name="inputSecureFileUploaded"></a>  

***
<br><br>[$inputSecureValue](../constructors/inputSecureValue.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'data' => [SecureData](../types/SecureData.md), 'front_side' => [InputSecureFile](../types/InputSecureFile.md), 'reverse_side' => [InputSecureFile](../types/InputSecureFile.md), 'selfie' => [InputSecureFile](../types/InputSecureFile.md), 'translation' => \[[InputSecureFile](../types/InputSecureFile.md)\], 'files' => \[[InputSecureFile](../types/InputSecureFile.md)\], 'plain_data' => [SecurePlainData](../types/SecurePlainData.md), \];<a name="inputSecureValue"></a>  

***
<br><br>[$inputSingleMedia](../constructors/inputSingleMedia.md) = \['media' => [InputMedia](../types/InputMedia.md), 'message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \];<a name="inputSingleMedia"></a>  

***
<br><br>[$inputStickerSetAnimatedEmoji](../constructors/inputStickerSetAnimatedEmoji.md) = \[\];<a name="inputStickerSetAnimatedEmoji"></a>  

***
<br><br>[$inputStickerSetEmpty](../constructors/inputStickerSetEmpty.md) = \[\];<a name="inputStickerSetEmpty"></a>  

***
<br><br>[$inputStickerSetID](../constructors/inputStickerSetID.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputStickerSetID"></a>  

***
<br><br>[$inputStickerSetItem](../constructors/inputStickerSetItem.md) = \['document' => [InputDocument](../types/InputDocument.md), 'emoji' => [string](../types/string.md), 'mask_coords' => [MaskCoords](../types/MaskCoords.md), \];<a name="inputStickerSetItem"></a>  

***
<br><br>[$inputStickerSetShortName](../constructors/inputStickerSetShortName.md) = \['short_name' => [string](../types/string.md), \];<a name="inputStickerSetShortName"></a>  

***
<br><br>[$inputStickerSetThumb](../constructors/inputStickerSetThumb.md) = \['stickerset' => [InputStickerSet](../types/InputStickerSet.md), 'volume_id' => [long](../types/long.md), 'local_id' => [int](../types/int.md), \];<a name="inputStickerSetThumb"></a>  

***
<br><br>[$inputStickeredMediaDocument](../constructors/inputStickeredMediaDocument.md) = \['id' => [InputDocument](../types/InputDocument.md), \];<a name="inputStickeredMediaDocument"></a>  

***
<br><br>[$inputStickeredMediaPhoto](../constructors/inputStickeredMediaPhoto.md) = \['id' => [InputPhoto](../types/InputPhoto.md), \];<a name="inputStickeredMediaPhoto"></a>  

***
<br><br>[$inputTakeoutFileLocation](../constructors/inputTakeoutFileLocation.md) = \[\];<a name="inputTakeoutFileLocation"></a>  

***
<br><br>[$inputTheme](../constructors/inputTheme.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputTheme"></a>  

***
<br><br>[$inputThemeSlug](../constructors/inputThemeSlug.md) = \['slug' => [string](../types/string.md), \];<a name="inputThemeSlug"></a>  

***
<br><br>[$inputUser](../constructors/inputUser.md) = \['user_id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), \];<a name="inputUser"></a>  

***
<br><br>[$inputUserEmpty](../constructors/inputUserEmpty.md) = \[\];<a name="inputUserEmpty"></a>  

***
<br><br>[$inputUserFromMessage](../constructors/inputUserFromMessage.md) = \['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'user_id' => [int](../types/int.md), \];<a name="inputUserFromMessage"></a>  

***
<br><br>[$inputUserSelf](../constructors/inputUserSelf.md) = \[\];<a name="inputUserSelf"></a>  

***
<br><br>[$inputWallPaper](../constructors/inputWallPaper.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputWallPaper"></a>  

***
<br><br>[$inputWallPaperSlug](../constructors/inputWallPaperSlug.md) = \['slug' => [string](../types/string.md), \];<a name="inputWallPaperSlug"></a>  

***
<br><br>[$inputWebDocument](../constructors/inputWebDocument.md) = \['url' => [string](../types/string.md), 'size' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], \];<a name="inputWebDocument"></a>  

***
<br><br>[$inputWebFileGeoPointLocation](../constructors/inputWebFileGeoPointLocation.md) = \['geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'access_hash' => [long](../types/long.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'zoom' => [int](../types/int.md), 'scale' => [int](../types/int.md), \];<a name="inputWebFileGeoPointLocation"></a>  

***
<br><br>[$inputWebFileLocation](../constructors/inputWebFileLocation.md) = \['url' => [string](../types/string.md), 'access_hash' => [long](../types/long.md), \];<a name="inputWebFileLocation"></a>  

***
<br><br>[$invoice](../constructors/invoice.md) = \['test' => [Bool](../types/Bool.md), 'name_requested' => [Bool](../types/Bool.md), 'phone_requested' => [Bool](../types/Bool.md), 'email_requested' => [Bool](../types/Bool.md), 'shipping_address_requested' => [Bool](../types/Bool.md), 'flexible' => [Bool](../types/Bool.md), 'phone_to_provider' => [Bool](../types/Bool.md), 'email_to_provider' => [Bool](../types/Bool.md), 'currency' => [string](../types/string.md), 'prices' => \[[LabeledPrice](../types/LabeledPrice.md)\], \];<a name="invoice"></a>  

***
<br><br>[$ipPort](../constructors/ipPort.md) = \['ipv4' => [int](../types/int.md), 'port' => [int](../types/int.md), \];<a name="ipPort"></a>  

***
<br><br>[$ipPortSecret](../constructors/ipPortSecret.md) = \['ipv4' => [int](../types/int.md), 'port' => [int](../types/int.md), 'secret' => [bytes](../types/bytes.md), \];<a name="ipPortSecret"></a>  

***
<br><br>[$jsonArray](../constructors/jsonArray.md) = \['value' => \[[JSONValue](../types/JSONValue.md)\], \];<a name="jsonArray"></a>  

***
<br><br>[$jsonBool](../constructors/jsonBool.md) = \['value' => [Bool](../types/Bool.md), \];<a name="jsonBool"></a>  

***
<br><br>[$jsonNull](../constructors/jsonNull.md) = \[\];<a name="jsonNull"></a>  

***
<br><br>[$jsonNumber](../constructors/jsonNumber.md) = \['value' => [double](../types/double.md), \];<a name="jsonNumber"></a>  

***
<br><br>[$jsonObject](../constructors/jsonObject.md) = \['value' => \[[JSONObjectValue](../types/JSONObjectValue.md)\], \];<a name="jsonObject"></a>  

***
<br><br>[$jsonObjectValue](../constructors/jsonObjectValue.md) = \['key' => [string](../types/string.md), 'value' => [JSONValue](../types/JSONValue.md), \];<a name="jsonObjectValue"></a>  

***
<br><br>[$jsonString](../constructors/jsonString.md) = \['value' => [string](../types/string.md), \];<a name="jsonString"></a>  

***
<br><br>[$keyboardButton](../constructors/keyboardButton.md) = \['text' => [string](../types/string.md), \];<a name="keyboardButton"></a>  

***
<br><br>[$keyboardButtonBuy](../constructors/keyboardButtonBuy.md) = \['text' => [string](../types/string.md), \];<a name="keyboardButtonBuy"></a>  

***
<br><br>[$keyboardButtonCallback](../constructors/keyboardButtonCallback.md) = \['text' => [string](../types/string.md), 'data' => [bytes](../types/bytes.md), \];<a name="keyboardButtonCallback"></a>  

***
<br><br>[$keyboardButtonGame](../constructors/keyboardButtonGame.md) = \['text' => [string](../types/string.md), \];<a name="keyboardButtonGame"></a>  

***
<br><br>[$keyboardButtonRequestGeoLocation](../constructors/keyboardButtonRequestGeoLocation.md) = \['text' => [string](../types/string.md), \];<a name="keyboardButtonRequestGeoLocation"></a>  

***
<br><br>[$keyboardButtonRequestPhone](../constructors/keyboardButtonRequestPhone.md) = \['text' => [string](../types/string.md), \];<a name="keyboardButtonRequestPhone"></a>  

***
<br><br>[$keyboardButtonRow](../constructors/keyboardButtonRow.md) = \['buttons' => \[[KeyboardButton](../types/KeyboardButton.md)\], \];<a name="keyboardButtonRow"></a>  

***
<br><br>[$keyboardButtonSwitchInline](../constructors/keyboardButtonSwitchInline.md) = \['same_peer' => [Bool](../types/Bool.md), 'text' => [string](../types/string.md), 'query' => [string](../types/string.md), \];<a name="keyboardButtonSwitchInline"></a>  

***
<br><br>[$keyboardButtonUrl](../constructors/keyboardButtonUrl.md) = \['text' => [string](../types/string.md), 'url' => [string](../types/string.md), \];<a name="keyboardButtonUrl"></a>  

***
<br><br>[$keyboardButtonUrlAuth](../constructors/keyboardButtonUrlAuth.md) = \['text' => [string](../types/string.md), 'fwd_text' => [string](../types/string.md), 'url' => [string](../types/string.md), 'button_id' => [int](../types/int.md), \];<a name="keyboardButtonUrlAuth"></a>  

***
<br><br>[$labeledPrice](../constructors/labeledPrice.md) = \['label' => [string](../types/string.md), 'amount' => [long](../types/long.md), \];<a name="labeledPrice"></a>  

***
<br><br>[$langPackDifference](../constructors/langPackDifference.md) = \['lang_code' => [string](../types/string.md), 'from_version' => [int](../types/int.md), 'version' => [int](../types/int.md), 'strings' => \[[LangPackString](../types/LangPackString.md)\], \];<a name="langPackDifference"></a>  

***
<br><br>[$langPackLanguage](../constructors/langPackLanguage.md) = \['official' => [Bool](../types/Bool.md), 'rtl' => [Bool](../types/Bool.md), 'beta' => [Bool](../types/Bool.md), 'name' => [string](../types/string.md), 'native_name' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), 'base_lang_code' => [string](../types/string.md), 'plural_code' => [string](../types/string.md), 'strings_count' => [int](../types/int.md), 'translated_count' => [int](../types/int.md), 'translations_url' => [string](../types/string.md), \];<a name="langPackLanguage"></a>  

***
<br><br>[$langPackString](../constructors/langPackString.md) = \['key' => [string](../types/string.md), 'value' => [string](../types/string.md), \];<a name="langPackString"></a>  

***
<br><br>[$langPackStringDeleted](../constructors/langPackStringDeleted.md) = \['key' => [string](../types/string.md), \];<a name="langPackStringDeleted"></a>  

***
<br><br>[$langPackStringPluralized](../constructors/langPackStringPluralized.md) = \['key' => [string](../types/string.md), 'zero_value' => [string](../types/string.md), 'one_value' => [string](../types/string.md), 'two_value' => [string](../types/string.md), 'few_value' => [string](../types/string.md), 'many_value' => [string](../types/string.md), 'other_value' => [string](../types/string.md), \];<a name="langPackStringPluralized"></a>  

***
<br><br>[$maskCoords](../constructors/maskCoords.md) = \['n' => [int](../types/int.md), 'x' => [double](../types/double.md), 'y' => [double](../types/double.md), 'zoom' => [double](../types/double.md), \];<a name="maskCoords"></a>  

***
<br><br>[$message](../constructors/message.md) = \['out' => [Bool](../types/Bool.md), 'mentioned' => [Bool](../types/Bool.md), 'media_unread' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'post' => [Bool](../types/Bool.md), 'from_scheduled' => [Bool](../types/Bool.md), 'legacy' => [Bool](../types/Bool.md), 'edit_hide' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'from_id' => [int](../types/int.md), 'to_id' => [Peer](../types/Peer.md), 'fwd_from' => [MessageFwdHeader](../types/MessageFwdHeader.md), 'via_bot_id' => [int](../types/int.md), 'reply_to_msg_id' => [int](../types/int.md), 'date' => [int](../types/int.md), 'message' => [string](../types/string.md), 'media' => [MessageMedia](../types/MessageMedia.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'views' => [int](../types/int.md), 'edit_date' => [int](../types/int.md), 'post_author' => [string](../types/string.md), 'grouped_id' => [long](../types/long.md), 'restriction_reason' => \[[RestrictionReason](../types/RestrictionReason.md)\], \];<a name="message"></a>  

***
<br><br>[$messageActionBotAllowed](../constructors/messageActionBotAllowed.md) = \['domain' => [string](../types/string.md), \];<a name="messageActionBotAllowed"></a>  

***
<br><br>[$messageActionChannelCreate](../constructors/messageActionChannelCreate.md) = \['title' => [string](../types/string.md), \];<a name="messageActionChannelCreate"></a>  

***
<br><br>[$messageActionChannelMigrateFrom](../constructors/messageActionChannelMigrateFrom.md) = \['title' => [string](../types/string.md), 'chat_id' => [int](../types/int.md), \];<a name="messageActionChannelMigrateFrom"></a>  

***
<br><br>[$messageActionChatAddUser](../constructors/messageActionChatAddUser.md) = \['users' => \[[int](../types/int.md)\], \];<a name="messageActionChatAddUser"></a>  

***
<br><br>[$messageActionChatCreate](../constructors/messageActionChatCreate.md) = \['title' => [string](../types/string.md), 'users' => \[[int](../types/int.md)\], \];<a name="messageActionChatCreate"></a>  

***
<br><br>[$messageActionChatDeletePhoto](../constructors/messageActionChatDeletePhoto.md) = \[\];<a name="messageActionChatDeletePhoto"></a>  

***
<br><br>[$messageActionChatDeleteUser](../constructors/messageActionChatDeleteUser.md) = \['user_id' => [int](../types/int.md), \];<a name="messageActionChatDeleteUser"></a>  

***
<br><br>[$messageActionChatEditPhoto](../constructors/messageActionChatEditPhoto.md) = \['photo' => [Photo](../types/Photo.md), \];<a name="messageActionChatEditPhoto"></a>  

***
<br><br>[$messageActionChatEditTitle](../constructors/messageActionChatEditTitle.md) = \['title' => [string](../types/string.md), \];<a name="messageActionChatEditTitle"></a>  

***
<br><br>[$messageActionChatJoinedByLink](../constructors/messageActionChatJoinedByLink.md) = \['inviter_id' => [int](../types/int.md), \];<a name="messageActionChatJoinedByLink"></a>  

***
<br><br>[$messageActionChatMigrateTo](../constructors/messageActionChatMigrateTo.md) = \['channel_id' => [int](../types/int.md), \];<a name="messageActionChatMigrateTo"></a>  

***
<br><br>[$messageActionContactSignUp](../constructors/messageActionContactSignUp.md) = \[\];<a name="messageActionContactSignUp"></a>  

***
<br><br>[$messageActionCustomAction](../constructors/messageActionCustomAction.md) = \['message' => [string](../types/string.md), \];<a name="messageActionCustomAction"></a>  

***
<br><br>[$messageActionEmpty](../constructors/messageActionEmpty.md) = \[\];<a name="messageActionEmpty"></a>  

***
<br><br>[$messageActionGameScore](../constructors/messageActionGameScore.md) = \['game_id' => [long](../types/long.md), 'score' => [int](../types/int.md), \];<a name="messageActionGameScore"></a>  

***
<br><br>[$messageActionHistoryClear](../constructors/messageActionHistoryClear.md) = \[\];<a name="messageActionHistoryClear"></a>  

***
<br><br>[$messageActionPaymentSent](../constructors/messageActionPaymentSent.md) = \['currency' => [string](../types/string.md), 'total_amount' => [long](../types/long.md), \];<a name="messageActionPaymentSent"></a>  

***
<br><br>[$messageActionPaymentSentMe](../constructors/messageActionPaymentSentMe.md) = \['currency' => [string](../types/string.md), 'total_amount' => [long](../types/long.md), 'payload' => [bytes](../types/bytes.md), 'info' => [PaymentRequestedInfo](../types/PaymentRequestedInfo.md), 'shipping_option_id' => [string](../types/string.md), 'charge' => [PaymentCharge](../types/PaymentCharge.md), \];<a name="messageActionPaymentSentMe"></a>  

***
<br><br>[$messageActionPhoneCall](../constructors/messageActionPhoneCall.md) = \['video' => [Bool](../types/Bool.md), 'call_id' => [long](../types/long.md), 'reason' => [PhoneCallDiscardReason](../types/PhoneCallDiscardReason.md), 'duration' => [int](../types/int.md), \];<a name="messageActionPhoneCall"></a>  

***
<br><br>[$messageActionPinMessage](../constructors/messageActionPinMessage.md) = \[\];<a name="messageActionPinMessage"></a>  

***
<br><br>[$messageActionScreenshotTaken](../constructors/messageActionScreenshotTaken.md) = \[\];<a name="messageActionScreenshotTaken"></a>  

***
<br><br>[$messageActionSecureValuesSent](../constructors/messageActionSecureValuesSent.md) = \['types' => \[[SecureValueType](../types/SecureValueType.md)\], \];<a name="messageActionSecureValuesSent"></a>  

***
<br><br>[$messageActionSecureValuesSentMe](../constructors/messageActionSecureValuesSentMe.md) = \['values' => \[[SecureValue](../types/SecureValue.md)\], 'credentials' => [SecureCredentialsEncrypted](../types/SecureCredentialsEncrypted.md), \];<a name="messageActionSecureValuesSentMe"></a>  

***
<br><br>[$messageEmpty](../constructors/messageEmpty.md) = \['id' => [int](../types/int.md), \];<a name="messageEmpty"></a>  

***
<br><br>[$messageEntityBlockquote](../constructors/messageEntityBlockquote.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityBlockquote"></a>  

***
<br><br>[$messageEntityBold](../constructors/messageEntityBold.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityBold"></a>  

***
<br><br>[$messageEntityBotCommand](../constructors/messageEntityBotCommand.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityBotCommand"></a>  

***
<br><br>[$messageEntityCashtag](../constructors/messageEntityCashtag.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityCashtag"></a>  

***
<br><br>[$messageEntityCode](../constructors/messageEntityCode.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityCode"></a>  

***
<br><br>[$messageEntityEmail](../constructors/messageEntityEmail.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityEmail"></a>  

***
<br><br>[$messageEntityHashtag](../constructors/messageEntityHashtag.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityHashtag"></a>  

***
<br><br>[$messageEntityItalic](../constructors/messageEntityItalic.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityItalic"></a>  

***
<br><br>[$messageEntityMention](../constructors/messageEntityMention.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityMention"></a>  

***
<br><br>[$messageEntityMentionName](../constructors/messageEntityMentionName.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), 'user_id' => [int](../types/int.md), \];<a name="messageEntityMentionName"></a>  

***
<br><br>[$messageEntityPhone](../constructors/messageEntityPhone.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityPhone"></a>  

***
<br><br>[$messageEntityPre](../constructors/messageEntityPre.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), 'language' => [string](../types/string.md), \];<a name="messageEntityPre"></a>  

***
<br><br>[$messageEntityStrike](../constructors/messageEntityStrike.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityStrike"></a>  

***
<br><br>[$messageEntityTextUrl](../constructors/messageEntityTextUrl.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), 'url' => [string](../types/string.md), \];<a name="messageEntityTextUrl"></a>  

***
<br><br>[$messageEntityUnderline](../constructors/messageEntityUnderline.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityUnderline"></a>  

***
<br><br>[$messageEntityUnknown](../constructors/messageEntityUnknown.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityUnknown"></a>  

***
<br><br>[$messageEntityUrl](../constructors/messageEntityUrl.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityUrl"></a>  

***
<br><br>[$messageFwdHeader](../constructors/messageFwdHeader.md) = \['from_id' => [int](../types/int.md), 'from_name' => [string](../types/string.md), 'date' => [int](../types/int.md), 'channel_id' => [int](../types/int.md), 'channel_post' => [int](../types/int.md), 'post_author' => [string](../types/string.md), 'saved_from_peer' => [Peer](../types/Peer.md), 'saved_from_msg_id' => [int](../types/int.md), \];<a name="messageFwdHeader"></a>  

***
<br><br>[$messageMediaContact](../constructors/messageMediaContact.md) = \['phone_number' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'vcard' => [string](../types/string.md), 'user_id' => [int](../types/int.md), \];<a name="messageMediaContact"></a>  

***
<br><br>[$messageMediaDocument](../constructors/messageMediaDocument.md) = \['document' => [Document](../types/Document.md), 'ttl_seconds' => [int](../types/int.md), \];<a name="messageMediaDocument"></a>  

***
<br><br>[$messageMediaEmpty](../constructors/messageMediaEmpty.md) = \[\];<a name="messageMediaEmpty"></a>  

***
<br><br>[$messageMediaGame](../constructors/messageMediaGame.md) = \['game' => [Game](../types/Game.md), \];<a name="messageMediaGame"></a>  

***
<br><br>[$messageMediaGeo](../constructors/messageMediaGeo.md) = \['geo' => [GeoPoint](../types/GeoPoint.md), \];<a name="messageMediaGeo"></a>  

***
<br><br>[$messageMediaGeoLive](../constructors/messageMediaGeoLive.md) = \['geo' => [GeoPoint](../types/GeoPoint.md), 'period' => [int](../types/int.md), \];<a name="messageMediaGeoLive"></a>  

***
<br><br>[$messageMediaInvoice](../constructors/messageMediaInvoice.md) = \['shipping_address_requested' => [Bool](../types/Bool.md), 'test' => [Bool](../types/Bool.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'photo' => [WebDocument](../types/WebDocument.md), 'receipt_msg_id' => [int](../types/int.md), 'currency' => [string](../types/string.md), 'total_amount' => [long](../types/long.md), 'start_param' => [string](../types/string.md), \];<a name="messageMediaInvoice"></a>  

***
<br><br>[$messageMediaPhoto](../constructors/messageMediaPhoto.md) = \['photo' => [Photo](../types/Photo.md), 'ttl_seconds' => [int](../types/int.md), \];<a name="messageMediaPhoto"></a>  

***
<br><br>[$messageMediaPoll](../constructors/messageMediaPoll.md) = \['poll' => [Poll](../types/Poll.md), 'results' => [PollResults](../types/PollResults.md), \];<a name="messageMediaPoll"></a>  

***
<br><br>[$messageMediaUnsupported](../constructors/messageMediaUnsupported.md) = \[\];<a name="messageMediaUnsupported"></a>  

***
<br><br>[$messageMediaVenue](../constructors/messageMediaVenue.md) = \['geo' => [GeoPoint](../types/GeoPoint.md), 'title' => [string](../types/string.md), 'address' => [string](../types/string.md), 'provider' => [string](../types/string.md), 'venue_id' => [string](../types/string.md), 'venue_type' => [string](../types/string.md), \];<a name="messageMediaVenue"></a>  

***
<br><br>[$messageMediaWebPage](../constructors/messageMediaWebPage.md) = \['webpage' => [WebPage](../types/WebPage.md), \];<a name="messageMediaWebPage"></a>  

***
<br><br>[$messageRange](../constructors/messageRange.md) = \['min_id' => [int](../types/int.md), 'max_id' => [int](../types/int.md), \];<a name="messageRange"></a>  

***
<br><br>[$messageService](../constructors/messageService.md) = \['out' => [Bool](../types/Bool.md), 'mentioned' => [Bool](../types/Bool.md), 'media_unread' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'post' => [Bool](../types/Bool.md), 'legacy' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'from_id' => [int](../types/int.md), 'to_id' => [Peer](../types/Peer.md), 'reply_to_msg_id' => [int](../types/int.md), 'date' => [int](../types/int.md), 'action' => [MessageAction](../types/MessageAction.md), \];<a name="messageService"></a>  

***
<br><br>[$messages\_affectedHistory](../constructors/messages_affectedHistory.md) = \['pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), 'offset' => [int](../types/int.md), \];<a name="messages_affectedHistory"></a>  

[$messages\_affectedMessages](../constructors/messages_affectedMessages.md) = \['pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="messages_affectedMessages"></a>  

[$messages\_allStickers](../constructors/messages_allStickers.md) = \['hash' => [int](../types/int.md), 'sets' => \[[StickerSet](../types/StickerSet.md)\], \];<a name="messages_allStickers"></a>  

[$messages\_allStickersNotModified](../constructors/messages_allStickersNotModified.md) = \[\];<a name="messages_allStickersNotModified"></a>  

[$messages\_archivedStickers](../constructors/messages_archivedStickers.md) = \['count' => [int](../types/int.md), 'sets' => \[[StickerSetCovered](../types/StickerSetCovered.md)\], \];<a name="messages_archivedStickers"></a>  

[$messages\_botCallbackAnswer](../constructors/messages_botCallbackAnswer.md) = \['alert' => [Bool](../types/Bool.md), 'has_url' => [Bool](../types/Bool.md), 'native_ui' => [Bool](../types/Bool.md), 'message' => [string](../types/string.md), 'url' => [string](../types/string.md), 'cache_time' => [int](../types/int.md), \];<a name="messages_botCallbackAnswer"></a>  

[$messages\_botResults](../constructors/messages_botResults.md) = \['gallery' => [Bool](../types/Bool.md), 'query_id' => [long](../types/long.md), 'next_offset' => [string](../types/string.md), 'switch_pm' => [InlineBotSwitchPM](../types/InlineBotSwitchPM.md), 'results' => \[[BotInlineResult](../types/BotInlineResult.md)\], 'cache_time' => [int](../types/int.md), 'users' => \[[User](../types/User.md)\], \];<a name="messages_botResults"></a>  

[$messages\_channelMessages](../constructors/messages_channelMessages.md) = \['inexact' => [Bool](../types/Bool.md), 'pts' => [int](../types/int.md), 'count' => [int](../types/int.md), 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages_channelMessages"></a>  

[$messages\_chatFull](../constructors/messages_chatFull.md) = \['full_chat' => [ChatFull](../types/ChatFull.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages_chatFull"></a>  

[$messages\_chats](../constructors/messages_chats.md) = \['chats' => \[[Chat](../types/Chat.md)\], \];<a name="messages_chats"></a>  

[$messages\_chatsSlice](../constructors/messages_chatsSlice.md) = \['count' => [int](../types/int.md), 'chats' => \[[Chat](../types/Chat.md)\], \];<a name="messages_chatsSlice"></a>  

[$messages\_dhConfig](../constructors/messages_dhConfig.md) = \['g' => [int](../types/int.md), 'p' => [bytes](../types/bytes.md), 'version' => [int](../types/int.md), 'random' => [bytes](../types/bytes.md), \];<a name="messages_dhConfig"></a>  

[$messages\_dhConfigNotModified](../constructors/messages_dhConfigNotModified.md) = \['random' => [bytes](../types/bytes.md), \];<a name="messages_dhConfigNotModified"></a>  

[$messages\_dialogs](../constructors/messages_dialogs.md) = \['dialogs' => \[[Dialog](../types/Dialog.md)\], 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages_dialogs"></a>  

[$messages\_dialogsNotModified](../constructors/messages_dialogsNotModified.md) = \['count' => [int](../types/int.md), \];<a name="messages_dialogsNotModified"></a>  

[$messages\_dialogsSlice](../constructors/messages_dialogsSlice.md) = \['count' => [int](../types/int.md), 'dialogs' => \[[Dialog](../types/Dialog.md)\], 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages_dialogsSlice"></a>  

[$messages\_favedStickers](../constructors/messages_favedStickers.md) = \['hash' => [int](../types/int.md), 'packs' => \[[StickerPack](../types/StickerPack.md)\], 'stickers' => \[[Document](../types/Document.md)\], \];<a name="messages_favedStickers"></a>  

[$messages\_favedStickersNotModified](../constructors/messages_favedStickersNotModified.md) = \[\];<a name="messages_favedStickersNotModified"></a>  

[$messages\_featuredStickers](../constructors/messages_featuredStickers.md) = \['hash' => [int](../types/int.md), 'sets' => \[[StickerSetCovered](../types/StickerSetCovered.md)\], 'unread' => \[[long](../types/long.md)\], \];<a name="messages_featuredStickers"></a>  

[$messages\_featuredStickersNotModified](../constructors/messages_featuredStickersNotModified.md) = \[\];<a name="messages_featuredStickersNotModified"></a>  

[$messages\_foundGifs](../constructors/messages_foundGifs.md) = \['next_offset' => [int](../types/int.md), 'results' => \[[FoundGif](../types/FoundGif.md)\], \];<a name="messages_foundGifs"></a>  

[$messages\_foundStickerSets](../constructors/messages_foundStickerSets.md) = \['hash' => [int](../types/int.md), 'sets' => \[[StickerSetCovered](../types/StickerSetCovered.md)\], \];<a name="messages_foundStickerSets"></a>  

[$messages\_foundStickerSetsNotModified](../constructors/messages_foundStickerSetsNotModified.md) = \[\];<a name="messages_foundStickerSetsNotModified"></a>  

[$messages\_highScores](../constructors/messages_highScores.md) = \['scores' => \[[HighScore](../types/HighScore.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages_highScores"></a>  

[$messages\_messageEditData](../constructors/messages_messageEditData.md) = \['caption' => [Bool](../types/Bool.md), \];<a name="messages_messageEditData"></a>  

[$messages\_messages](../constructors/messages_messages.md) = \['messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages_messages"></a>  

[$messages\_messagesNotModified](../constructors/messages_messagesNotModified.md) = \['count' => [int](../types/int.md), \];<a name="messages_messagesNotModified"></a>  

[$messages\_messagesSlice](../constructors/messages_messagesSlice.md) = \['inexact' => [Bool](../types/Bool.md), 'count' => [int](../types/int.md), 'next_rate' => [int](../types/int.md), 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages_messagesSlice"></a>  

[$messages\_peerDialogs](../constructors/messages_peerDialogs.md) = \['dialogs' => \[[Dialog](../types/Dialog.md)\], 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], 'state' => [updates\_State](../types/updates_State.md), \];<a name="messages_peerDialogs"></a>  

[$messages\_recentStickers](../constructors/messages_recentStickers.md) = \['hash' => [int](../types/int.md), 'packs' => \[[StickerPack](../types/StickerPack.md)\], 'stickers' => \[[Document](../types/Document.md)\], 'dates' => \[[int](../types/int.md)\], \];<a name="messages_recentStickers"></a>  

[$messages\_recentStickersNotModified](../constructors/messages_recentStickersNotModified.md) = \[\];<a name="messages_recentStickersNotModified"></a>  

[$messages\_savedGifs](../constructors/messages_savedGifs.md) = \['hash' => [int](../types/int.md), 'gifs' => \[[Document](../types/Document.md)\], \];<a name="messages_savedGifs"></a>  

[$messages\_savedGifsNotModified](../constructors/messages_savedGifsNotModified.md) = \[\];<a name="messages_savedGifsNotModified"></a>  

[$messages\_searchCounter](../constructors/messages_searchCounter.md) = \['inexact' => [Bool](../types/Bool.md), 'filter' => [MessagesFilter](../types/MessagesFilter.md), 'count' => [int](../types/int.md), \];<a name="messages_searchCounter"></a>  

[$messages\_sentEncryptedFile](../constructors/messages_sentEncryptedFile.md) = \['date' => [int](../types/int.md), 'file' => [EncryptedFile](../types/EncryptedFile.md), \];<a name="messages_sentEncryptedFile"></a>  

[$messages\_sentEncryptedMessage](../constructors/messages_sentEncryptedMessage.md) = \['date' => [int](../types/int.md), \];<a name="messages_sentEncryptedMessage"></a>  

[$messages\_stickerSet](../constructors/messages_stickerSet.md) = \['set' => [StickerSet](../types/StickerSet.md), 'packs' => \[[StickerPack](../types/StickerPack.md)\], 'documents' => \[[Document](../types/Document.md)\], \];<a name="messages_stickerSet"></a>  

[$messages\_stickerSetInstallResultArchive](../constructors/messages_stickerSetInstallResultArchive.md) = \['sets' => \[[StickerSetCovered](../types/StickerSetCovered.md)\], \];<a name="messages_stickerSetInstallResultArchive"></a>  

[$messages\_stickerSetInstallResultSuccess](../constructors/messages_stickerSetInstallResultSuccess.md) = \[\];<a name="messages_stickerSetInstallResultSuccess"></a>  

[$messages\_stickers](../constructors/messages_stickers.md) = \['hash' => [int](../types/int.md), 'stickers' => \[[Document](../types/Document.md)\], \];<a name="messages_stickers"></a>  

[$messages\_stickersNotModified](../constructors/messages_stickersNotModified.md) = \[\];<a name="messages_stickersNotModified"></a>  

***
<br><br>[$nearestDc](../constructors/nearestDc.md) = \['country' => [string](../types/string.md), 'this_dc' => [int](../types/int.md), 'nearest_dc' => [int](../types/int.md), \];<a name="nearestDc"></a>  

***
<br><br>[$notifyBroadcasts](../constructors/notifyBroadcasts.md) = \[\];<a name="notifyBroadcasts"></a>  

***
<br><br>[$notifyChats](../constructors/notifyChats.md) = \[\];<a name="notifyChats"></a>  

***
<br><br>[$notifyPeer](../constructors/notifyPeer.md) = \['peer' => [Peer](../types/Peer.md), \];<a name="notifyPeer"></a>  

***
<br><br>[$notifyUsers](../constructors/notifyUsers.md) = \[\];<a name="notifyUsers"></a>  

***
<br><br>[$null](../constructors/null.md) = \[\];<a name="null"></a>  

***
<br><br>[$page](../constructors/page.md) = \['part' => [Bool](../types/Bool.md), 'rtl' => [Bool](../types/Bool.md), 'v2' => [Bool](../types/Bool.md), 'url' => [string](../types/string.md), 'blocks' => \[[PageBlock](../types/PageBlock.md)\], 'photos' => \[[Photo](../types/Photo.md)\], 'documents' => \[[Document](../types/Document.md)\], \];<a name="page"></a>  

***
<br><br>[$pageBlockAnchor](../constructors/pageBlockAnchor.md) = \['name' => [string](../types/string.md), \];<a name="pageBlockAnchor"></a>  

***
<br><br>[$pageBlockAudio](../constructors/pageBlockAudio.md) = \['audio_id' => [long](../types/long.md), 'caption' => [PageCaption](../types/PageCaption.md), \];<a name="pageBlockAudio"></a>  

***
<br><br>[$pageBlockAuthorDate](../constructors/pageBlockAuthorDate.md) = \['author' => [RichText](../types/RichText.md), 'published_date' => [int](../types/int.md), \];<a name="pageBlockAuthorDate"></a>  

***
<br><br>[$pageBlockBlockquote](../constructors/pageBlockBlockquote.md) = \['text' => [RichText](../types/RichText.md), 'caption' => [RichText](../types/RichText.md), \];<a name="pageBlockBlockquote"></a>  

***
<br><br>[$pageBlockChannel](../constructors/pageBlockChannel.md) = \['channel' => [Chat](../types/Chat.md), \];<a name="pageBlockChannel"></a>  

***
<br><br>[$pageBlockCollage](../constructors/pageBlockCollage.md) = \['items' => \[[PageBlock](../types/PageBlock.md)\], 'caption' => [PageCaption](../types/PageCaption.md), \];<a name="pageBlockCollage"></a>  

***
<br><br>[$pageBlockCover](../constructors/pageBlockCover.md) = \['cover' => [PageBlock](../types/PageBlock.md), \];<a name="pageBlockCover"></a>  

***
<br><br>[$pageBlockDetails](../constructors/pageBlockDetails.md) = \['open' => [Bool](../types/Bool.md), 'blocks' => \[[PageBlock](../types/PageBlock.md)\], 'title' => [RichText](../types/RichText.md), \];<a name="pageBlockDetails"></a>  

***
<br><br>[$pageBlockDivider](../constructors/pageBlockDivider.md) = \[\];<a name="pageBlockDivider"></a>  

***
<br><br>[$pageBlockEmbed](../constructors/pageBlockEmbed.md) = \['full_width' => [Bool](../types/Bool.md), 'allow_scrolling' => [Bool](../types/Bool.md), 'url' => [string](../types/string.md), 'html' => [string](../types/string.md), 'poster_photo_id' => [long](../types/long.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'caption' => [PageCaption](../types/PageCaption.md), \];<a name="pageBlockEmbed"></a>  

***
<br><br>[$pageBlockEmbedPost](../constructors/pageBlockEmbedPost.md) = \['url' => [string](../types/string.md), 'webpage_id' => [long](../types/long.md), 'author_photo_id' => [long](../types/long.md), 'author' => [string](../types/string.md), 'date' => [int](../types/int.md), 'blocks' => \[[PageBlock](../types/PageBlock.md)\], 'caption' => [PageCaption](../types/PageCaption.md), \];<a name="pageBlockEmbedPost"></a>  

***
<br><br>[$pageBlockFooter](../constructors/pageBlockFooter.md) = \['text' => [RichText](../types/RichText.md), \];<a name="pageBlockFooter"></a>  

***
<br><br>[$pageBlockHeader](../constructors/pageBlockHeader.md) = \['text' => [RichText](../types/RichText.md), \];<a name="pageBlockHeader"></a>  

***
<br><br>[$pageBlockKicker](../constructors/pageBlockKicker.md) = \['text' => [RichText](../types/RichText.md), \];<a name="pageBlockKicker"></a>  

***
<br><br>[$pageBlockList](../constructors/pageBlockList.md) = \['items' => \[[PageListItem](../types/PageListItem.md)\], \];<a name="pageBlockList"></a>  

***
<br><br>[$pageBlockMap](../constructors/pageBlockMap.md) = \['geo' => [GeoPoint](../types/GeoPoint.md), 'zoom' => [int](../types/int.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'caption' => [PageCaption](../types/PageCaption.md), \];<a name="pageBlockMap"></a>  

***
<br><br>[$pageBlockOrderedList](../constructors/pageBlockOrderedList.md) = \['items' => \[[PageListOrderedItem](../types/PageListOrderedItem.md)\], \];<a name="pageBlockOrderedList"></a>  

***
<br><br>[$pageBlockParagraph](../constructors/pageBlockParagraph.md) = \['text' => [RichText](../types/RichText.md), \];<a name="pageBlockParagraph"></a>  

***
<br><br>[$pageBlockPhoto](../constructors/pageBlockPhoto.md) = \['photo_id' => [long](../types/long.md), 'caption' => [PageCaption](../types/PageCaption.md), 'url' => [string](../types/string.md), 'webpage_id' => [long](../types/long.md), \];<a name="pageBlockPhoto"></a>  

***
<br><br>[$pageBlockPreformatted](../constructors/pageBlockPreformatted.md) = \['text' => [RichText](../types/RichText.md), 'language' => [string](../types/string.md), \];<a name="pageBlockPreformatted"></a>  

***
<br><br>[$pageBlockPullquote](../constructors/pageBlockPullquote.md) = \['text' => [RichText](../types/RichText.md), 'caption' => [RichText](../types/RichText.md), \];<a name="pageBlockPullquote"></a>  

***
<br><br>[$pageBlockRelatedArticles](../constructors/pageBlockRelatedArticles.md) = \['title' => [RichText](../types/RichText.md), 'articles' => \[[PageRelatedArticle](../types/PageRelatedArticle.md)\], \];<a name="pageBlockRelatedArticles"></a>  

***
<br><br>[$pageBlockSlideshow](../constructors/pageBlockSlideshow.md) = \['items' => \[[PageBlock](../types/PageBlock.md)\], 'caption' => [PageCaption](../types/PageCaption.md), \];<a name="pageBlockSlideshow"></a>  

***
<br><br>[$pageBlockSubheader](../constructors/pageBlockSubheader.md) = \['text' => [RichText](../types/RichText.md), \];<a name="pageBlockSubheader"></a>  

***
<br><br>[$pageBlockSubtitle](../constructors/pageBlockSubtitle.md) = \['text' => [RichText](../types/RichText.md), \];<a name="pageBlockSubtitle"></a>  

***
<br><br>[$pageBlockTable](../constructors/pageBlockTable.md) = \['bordered' => [Bool](../types/Bool.md), 'striped' => [Bool](../types/Bool.md), 'title' => [RichText](../types/RichText.md), 'rows' => \[[PageTableRow](../types/PageTableRow.md)\], \];<a name="pageBlockTable"></a>  

***
<br><br>[$pageBlockTitle](../constructors/pageBlockTitle.md) = \['text' => [RichText](../types/RichText.md), \];<a name="pageBlockTitle"></a>  

***
<br><br>[$pageBlockUnsupported](../constructors/pageBlockUnsupported.md) = \[\];<a name="pageBlockUnsupported"></a>  

***
<br><br>[$pageBlockVideo](../constructors/pageBlockVideo.md) = \['autoplay' => [Bool](../types/Bool.md), 'loop' => [Bool](../types/Bool.md), 'video_id' => [long](../types/long.md), 'caption' => [PageCaption](../types/PageCaption.md), \];<a name="pageBlockVideo"></a>  

***
<br><br>[$pageCaption](../constructors/pageCaption.md) = \['text' => [RichText](../types/RichText.md), 'credit' => [RichText](../types/RichText.md), \];<a name="pageCaption"></a>  

***
<br><br>[$pageListItemBlocks](../constructors/pageListItemBlocks.md) = \['blocks' => \[[PageBlock](../types/PageBlock.md)\], \];<a name="pageListItemBlocks"></a>  

***
<br><br>[$pageListItemText](../constructors/pageListItemText.md) = \['text' => [RichText](../types/RichText.md), \];<a name="pageListItemText"></a>  

***
<br><br>[$pageListOrderedItemBlocks](../constructors/pageListOrderedItemBlocks.md) = \['num' => [string](../types/string.md), 'blocks' => \[[PageBlock](../types/PageBlock.md)\], \];<a name="pageListOrderedItemBlocks"></a>  

***
<br><br>[$pageListOrderedItemText](../constructors/pageListOrderedItemText.md) = \['num' => [string](../types/string.md), 'text' => [RichText](../types/RichText.md), \];<a name="pageListOrderedItemText"></a>  

***
<br><br>[$pageRelatedArticle](../constructors/pageRelatedArticle.md) = \['url' => [string](../types/string.md), 'webpage_id' => [long](../types/long.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'photo_id' => [long](../types/long.md), 'author' => [string](../types/string.md), 'published_date' => [int](../types/int.md), \];<a name="pageRelatedArticle"></a>  

***
<br><br>[$pageTableCell](../constructors/pageTableCell.md) = \['header' => [Bool](../types/Bool.md), 'align_center' => [Bool](../types/Bool.md), 'align_right' => [Bool](../types/Bool.md), 'valign_middle' => [Bool](../types/Bool.md), 'valign_bottom' => [Bool](../types/Bool.md), 'text' => [RichText](../types/RichText.md), 'colspan' => [int](../types/int.md), 'rowspan' => [int](../types/int.md), \];<a name="pageTableCell"></a>  

***
<br><br>[$pageTableRow](../constructors/pageTableRow.md) = \['cells' => \[[PageTableCell](../types/PageTableCell.md)\], \];<a name="pageTableRow"></a>  

***
<br><br>[$passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow](../constructors/passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow.md) = \['salt1' => [bytes](../types/bytes.md), 'salt2' => [bytes](../types/bytes.md), 'g' => [int](../types/int.md), 'p' => [bytes](../types/bytes.md), \];<a name="passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow"></a>  

***
<br><br>[$passwordKdfAlgoUnknown](../constructors/passwordKdfAlgoUnknown.md) = \[\];<a name="passwordKdfAlgoUnknown"></a>  

***
<br><br>[$paymentCharge](../constructors/paymentCharge.md) = \['id' => [string](../types/string.md), 'provider_charge_id' => [string](../types/string.md), \];<a name="paymentCharge"></a>  

***
<br><br>[$paymentRequestedInfo](../constructors/paymentRequestedInfo.md) = \['name' => [string](../types/string.md), 'phone' => [string](../types/string.md), 'email' => [string](../types/string.md), 'shipping_address' => [PostAddress](../types/PostAddress.md), \];<a name="paymentRequestedInfo"></a>  

***
<br><br>[$paymentSavedCredentialsCard](../constructors/paymentSavedCredentialsCard.md) = \['id' => [string](../types/string.md), 'title' => [string](../types/string.md), \];<a name="paymentSavedCredentialsCard"></a>  

***
<br><br>[$payments\_paymentForm](../constructors/payments_paymentForm.md) = \['can_save_credentials' => [Bool](../types/Bool.md), 'password_missing' => [Bool](../types/Bool.md), 'bot_id' => [int](../types/int.md), 'invoice' => [Invoice](../types/Invoice.md), 'provider_id' => [int](../types/int.md), 'url' => [string](../types/string.md), 'native_provider' => [string](../types/string.md), 'native_params' => [DataJSON](../types/DataJSON.md), 'saved_info' => [PaymentRequestedInfo](../types/PaymentRequestedInfo.md), 'saved_credentials' => [PaymentSavedCredentials](../types/PaymentSavedCredentials.md), 'users' => \[[User](../types/User.md)\], \];<a name="payments_paymentForm"></a>  

[$payments\_paymentReceipt](../constructors/payments_paymentReceipt.md) = \['date' => [int](../types/int.md), 'bot_id' => [int](../types/int.md), 'invoice' => [Invoice](../types/Invoice.md), 'provider_id' => [int](../types/int.md), 'info' => [PaymentRequestedInfo](../types/PaymentRequestedInfo.md), 'shipping' => [ShippingOption](../types/ShippingOption.md), 'currency' => [string](../types/string.md), 'total_amount' => [long](../types/long.md), 'credentials_title' => [string](../types/string.md), 'users' => \[[User](../types/User.md)\], \];<a name="payments_paymentReceipt"></a>  

[$payments\_paymentResult](../constructors/payments_paymentResult.md) = \['updates' => [Updates](../types/Updates.md), \];<a name="payments_paymentResult"></a>  

[$payments\_paymentVerificationNeeded](../constructors/payments_paymentVerificationNeeded.md) = \['url' => [string](../types/string.md), \];<a name="payments_paymentVerificationNeeded"></a>  

[$payments\_savedInfo](../constructors/payments_savedInfo.md) = \['has_saved_credentials' => [Bool](../types/Bool.md), 'saved_info' => [PaymentRequestedInfo](../types/PaymentRequestedInfo.md), \];<a name="payments_savedInfo"></a>  

[$payments\_validatedRequestedInfo](../constructors/payments_validatedRequestedInfo.md) = \['id' => [string](../types/string.md), 'shipping_options' => \[[ShippingOption](../types/ShippingOption.md)\], \];<a name="payments_validatedRequestedInfo"></a>  

***
<br><br>[$peerChannel](../constructors/peerChannel.md) = \['channel_id' => [int](../types/int.md), \];<a name="peerChannel"></a>  

***
<br><br>[$peerChat](../constructors/peerChat.md) = \['chat_id' => [int](../types/int.md), \];<a name="peerChat"></a>  

***
<br><br>[$peerLocated](../constructors/peerLocated.md) = \['peer' => [Peer](../types/Peer.md), 'expires' => [int](../types/int.md), 'distance' => [int](../types/int.md), \];<a name="peerLocated"></a>  

***
<br><br>[$peerNotifySettings](../constructors/peerNotifySettings.md) = \['show_previews' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'mute_until' => [int](../types/int.md), 'sound' => [string](../types/string.md), \];<a name="peerNotifySettings"></a>  

***
<br><br>[$peerSettings](../constructors/peerSettings.md) = \['report_spam' => [Bool](../types/Bool.md), 'add_contact' => [Bool](../types/Bool.md), 'block_contact' => [Bool](../types/Bool.md), 'share_contact' => [Bool](../types/Bool.md), 'need_contacts_exception' => [Bool](../types/Bool.md), 'report_geo' => [Bool](../types/Bool.md), \];<a name="peerSettings"></a>  

***
<br><br>[$peerUser](../constructors/peerUser.md) = \['user_id' => [int](../types/int.md), \];<a name="peerUser"></a>  

***
<br><br>[$phoneCall](../constructors/phoneCall.md) = \['p2p_allowed' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [int](../types/int.md), 'participant_id' => [int](../types/int.md), 'g_a_or_b' => [bytes](../types/bytes.md), 'key_fingerprint' => [long](../types/long.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), 'connections' => \[[PhoneConnection](../types/PhoneConnection.md)\], 'start_date' => [int](../types/int.md), \];<a name="phoneCall"></a>  

***
<br><br>[$phoneCallAccepted](../constructors/phoneCallAccepted.md) = \['video' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [int](../types/int.md), 'participant_id' => [int](../types/int.md), 'g_b' => [bytes](../types/bytes.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), \];<a name="phoneCallAccepted"></a>  

***
<br><br>[$phoneCallDiscardReasonBusy](../constructors/phoneCallDiscardReasonBusy.md) = \[\];<a name="phoneCallDiscardReasonBusy"></a>  

***
<br><br>[$phoneCallDiscardReasonDisconnect](../constructors/phoneCallDiscardReasonDisconnect.md) = \[\];<a name="phoneCallDiscardReasonDisconnect"></a>  

***
<br><br>[$phoneCallDiscardReasonHangup](../constructors/phoneCallDiscardReasonHangup.md) = \[\];<a name="phoneCallDiscardReasonHangup"></a>  

***
<br><br>[$phoneCallDiscardReasonMissed](../constructors/phoneCallDiscardReasonMissed.md) = \[\];<a name="phoneCallDiscardReasonMissed"></a>  

***
<br><br>[$phoneCallDiscarded](../constructors/phoneCallDiscarded.md) = \['need_rating' => [Bool](../types/Bool.md), 'need_debug' => [Bool](../types/Bool.md), 'video' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'reason' => [PhoneCallDiscardReason](../types/PhoneCallDiscardReason.md), 'duration' => [int](../types/int.md), \];<a name="phoneCallDiscarded"></a>  

***
<br><br>[$phoneCallEmpty](../constructors/phoneCallEmpty.md) = \['id' => [long](../types/long.md), \];<a name="phoneCallEmpty"></a>  

***
<br><br>[$phoneCallProtocol](../constructors/phoneCallProtocol.md) = \['udp_p2p' => [Bool](../types/Bool.md), 'udp_reflector' => [Bool](../types/Bool.md), 'min_layer' => [int](../types/int.md), 'max_layer' => [int](../types/int.md), \];<a name="phoneCallProtocol"></a>  

***
<br><br>[$phoneCallRequested](../constructors/phoneCallRequested.md) = \['video' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [int](../types/int.md), 'participant_id' => [int](../types/int.md), 'g_a_hash' => [bytes](../types/bytes.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), \];<a name="phoneCallRequested"></a>  

***
<br><br>[$phoneCallWaiting](../constructors/phoneCallWaiting.md) = \['video' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [int](../types/int.md), 'participant_id' => [int](../types/int.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), 'receive_date' => [int](../types/int.md), \];<a name="phoneCallWaiting"></a>  

***
<br><br>[$phoneConnection](../constructors/phoneConnection.md) = \['id' => [long](../types/long.md), 'ip' => [string](../types/string.md), 'ipv6' => [string](../types/string.md), 'port' => [int](../types/int.md), 'peer_tag' => [bytes](../types/bytes.md), \];<a name="phoneConnection"></a>  

***
<br><br>[$phone\_phoneCall](../constructors/phone_phoneCall.md) = \['phone_call' => [PhoneCall](../types/PhoneCall.md), 'users' => \[[User](../types/User.md)\], \];<a name="phone_phoneCall"></a>  

***
<br><br>[$photo](../constructors/photo.md) = \['has_stickers' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'file_reference' => [bytes](../types/bytes.md), 'date' => [int](../types/int.md), 'sizes' => \[[PhotoSize](../types/PhotoSize.md)\], 'dc_id' => [int](../types/int.md), \];<a name="photo"></a>  

***
<br><br>[$photoCachedSize](../constructors/photoCachedSize.md) = \['type' => [string](../types/string.md), 'location' => [FileLocation](../types/FileLocation.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \];<a name="photoCachedSize"></a>  

***
<br><br>[$photoEmpty](../constructors/photoEmpty.md) = \['id' => [long](../types/long.md), \];<a name="photoEmpty"></a>  

***
<br><br>[$photoSize](../constructors/photoSize.md) = \['type' => [string](../types/string.md), 'location' => [FileLocation](../types/FileLocation.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'size' => [int](../types/int.md), \];<a name="photoSize"></a>  

***
<br><br>[$photoSizeEmpty](../constructors/photoSizeEmpty.md) = \['type' => [string](../types/string.md), \];<a name="photoSizeEmpty"></a>  

***
<br><br>[$photoStrippedSize](../constructors/photoStrippedSize.md) = \['type' => [string](../types/string.md), 'bytes' => [bytes](../types/bytes.md), \];<a name="photoStrippedSize"></a>  

***
<br><br>[$photos\_photo](../constructors/photos_photo.md) = \['photo' => [Photo](../types/Photo.md), 'users' => \[[User](../types/User.md)\], \];<a name="photos_photo"></a>  

[$photos\_photos](../constructors/photos_photos.md) = \['photos' => \[[Photo](../types/Photo.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="photos_photos"></a>  

[$photos\_photosSlice](../constructors/photos_photosSlice.md) = \['count' => [int](../types/int.md), 'photos' => \[[Photo](../types/Photo.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="photos_photosSlice"></a>  

***
<br><br>[$poll](../constructors/poll.md) = \['id' => [long](../types/long.md), 'closed' => [Bool](../types/Bool.md), 'question' => [string](../types/string.md), 'answers' => \[[PollAnswer](../types/PollAnswer.md)\], \];<a name="poll"></a>  

***
<br><br>[$pollAnswer](../constructors/pollAnswer.md) = \['text' => [string](../types/string.md), 'option' => [bytes](../types/bytes.md), \];<a name="pollAnswer"></a>  

***
<br><br>[$pollAnswerVoters](../constructors/pollAnswerVoters.md) = \['chosen' => [Bool](../types/Bool.md), 'option' => [bytes](../types/bytes.md), 'voters' => [int](../types/int.md), \];<a name="pollAnswerVoters"></a>  

***
<br><br>[$pollResults](../constructors/pollResults.md) = \['min' => [Bool](../types/Bool.md), 'results' => \[[PollAnswerVoters](../types/PollAnswerVoters.md)\], 'total_voters' => [int](../types/int.md), \];<a name="pollResults"></a>  

***
<br><br>[$popularContact](../constructors/popularContact.md) = \['client_id' => [long](../types/long.md), 'importers' => [int](../types/int.md), \];<a name="popularContact"></a>  

***
<br><br>[$postAddress](../constructors/postAddress.md) = \['street_line1' => [string](../types/string.md), 'street_line2' => [string](../types/string.md), 'city' => [string](../types/string.md), 'state' => [string](../types/string.md), 'country_iso2' => [string](../types/string.md), 'post_code' => [string](../types/string.md), \];<a name="postAddress"></a>  

***
<br><br>[$privacyKeyAddedByPhone](../constructors/privacyKeyAddedByPhone.md) = \[\];<a name="privacyKeyAddedByPhone"></a>  

***
<br><br>[$privacyKeyChatInvite](../constructors/privacyKeyChatInvite.md) = \[\];<a name="privacyKeyChatInvite"></a>  

***
<br><br>[$privacyKeyForwards](../constructors/privacyKeyForwards.md) = \[\];<a name="privacyKeyForwards"></a>  

***
<br><br>[$privacyKeyPhoneCall](../constructors/privacyKeyPhoneCall.md) = \[\];<a name="privacyKeyPhoneCall"></a>  

***
<br><br>[$privacyKeyPhoneNumber](../constructors/privacyKeyPhoneNumber.md) = \[\];<a name="privacyKeyPhoneNumber"></a>  

***
<br><br>[$privacyKeyPhoneP2P](../constructors/privacyKeyPhoneP2P.md) = \[\];<a name="privacyKeyPhoneP2P"></a>  

***
<br><br>[$privacyKeyProfilePhoto](../constructors/privacyKeyProfilePhoto.md) = \[\];<a name="privacyKeyProfilePhoto"></a>  

***
<br><br>[$privacyKeyStatusTimestamp](../constructors/privacyKeyStatusTimestamp.md) = \[\];<a name="privacyKeyStatusTimestamp"></a>  

***
<br><br>[$privacyValueAllowAll](../constructors/privacyValueAllowAll.md) = \[\];<a name="privacyValueAllowAll"></a>  

***
<br><br>[$privacyValueAllowChatParticipants](../constructors/privacyValueAllowChatParticipants.md) = \['chats' => \[[int](../types/int.md)\], \];<a name="privacyValueAllowChatParticipants"></a>  

***
<br><br>[$privacyValueAllowContacts](../constructors/privacyValueAllowContacts.md) = \[\];<a name="privacyValueAllowContacts"></a>  

***
<br><br>[$privacyValueAllowUsers](../constructors/privacyValueAllowUsers.md) = \['users' => \[[int](../types/int.md)\], \];<a name="privacyValueAllowUsers"></a>  

***
<br><br>[$privacyValueDisallowAll](../constructors/privacyValueDisallowAll.md) = \[\];<a name="privacyValueDisallowAll"></a>  

***
<br><br>[$privacyValueDisallowChatParticipants](../constructors/privacyValueDisallowChatParticipants.md) = \['chats' => \[[int](../types/int.md)\], \];<a name="privacyValueDisallowChatParticipants"></a>  

***
<br><br>[$privacyValueDisallowContacts](../constructors/privacyValueDisallowContacts.md) = \[\];<a name="privacyValueDisallowContacts"></a>  

***
<br><br>[$privacyValueDisallowUsers](../constructors/privacyValueDisallowUsers.md) = \['users' => \[[int](../types/int.md)\], \];<a name="privacyValueDisallowUsers"></a>  

***
<br><br>[$receivedNotifyMessage](../constructors/receivedNotifyMessage.md) = \['id' => [int](../types/int.md), \];<a name="receivedNotifyMessage"></a>  

***
<br><br>[$recentMeUrlChat](../constructors/recentMeUrlChat.md) = \['url' => [string](../types/string.md), 'chat_id' => [int](../types/int.md), \];<a name="recentMeUrlChat"></a>  

***
<br><br>[$recentMeUrlChatInvite](../constructors/recentMeUrlChatInvite.md) = \['url' => [string](../types/string.md), 'chat_invite' => [ChatInvite](../types/ChatInvite.md), \];<a name="recentMeUrlChatInvite"></a>  

***
<br><br>[$recentMeUrlStickerSet](../constructors/recentMeUrlStickerSet.md) = \['url' => [string](../types/string.md), 'set' => [StickerSetCovered](../types/StickerSetCovered.md), \];<a name="recentMeUrlStickerSet"></a>  

***
<br><br>[$recentMeUrlUnknown](../constructors/recentMeUrlUnknown.md) = \['url' => [string](../types/string.md), \];<a name="recentMeUrlUnknown"></a>  

***
<br><br>[$recentMeUrlUser](../constructors/recentMeUrlUser.md) = \['url' => [string](../types/string.md), 'user_id' => [int](../types/int.md), \];<a name="recentMeUrlUser"></a>  

***
<br><br>[$replyInlineMarkup](../constructors/replyInlineMarkup.md) = \['rows' => \[[KeyboardButtonRow](../types/KeyboardButtonRow.md)\], \];<a name="replyInlineMarkup"></a>  

***
<br><br>[$replyKeyboardForceReply](../constructors/replyKeyboardForceReply.md) = \['single_use' => [Bool](../types/Bool.md), 'selective' => [Bool](../types/Bool.md), \];<a name="replyKeyboardForceReply"></a>  

***
<br><br>[$replyKeyboardHide](../constructors/replyKeyboardHide.md) = \['selective' => [Bool](../types/Bool.md), \];<a name="replyKeyboardHide"></a>  

***
<br><br>[$replyKeyboardMarkup](../constructors/replyKeyboardMarkup.md) = \['resize' => [Bool](../types/Bool.md), 'single_use' => [Bool](../types/Bool.md), 'selective' => [Bool](../types/Bool.md), 'rows' => \[[KeyboardButtonRow](../types/KeyboardButtonRow.md)\], \];<a name="replyKeyboardMarkup"></a>  

***
<br><br>[$restrictionReason](../constructors/restrictionReason.md) = \['platform' => [string](../types/string.md), 'reason' => [string](../types/string.md), 'text' => [string](../types/string.md), \];<a name="restrictionReason"></a>  

***
<br><br>[$savedPhoneContact](../constructors/savedPhoneContact.md) = \['phone' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'date' => [int](../types/int.md), \];<a name="savedPhoneContact"></a>  

***
<br><br>[$secureCredentialsEncrypted](../constructors/secureCredentialsEncrypted.md) = \['data' => [bytes](../types/bytes.md), 'hash' => [bytes](../types/bytes.md), 'secret' => [bytes](../types/bytes.md), \];<a name="secureCredentialsEncrypted"></a>  

***
<br><br>[$secureData](../constructors/secureData.md) = \['data' => [bytes](../types/bytes.md), 'data_hash' => [bytes](../types/bytes.md), 'secret' => [bytes](../types/bytes.md), \];<a name="secureData"></a>  

***
<br><br>[$secureFile](../constructors/secureFile.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'size' => [int](../types/int.md), 'dc_id' => [int](../types/int.md), 'date' => [int](../types/int.md), 'file_hash' => [bytes](../types/bytes.md), 'secret' => [bytes](../types/bytes.md), \];<a name="secureFile"></a>  

***
<br><br>[$secureFileEmpty](../constructors/secureFileEmpty.md) = \[\];<a name="secureFileEmpty"></a>  

***
<br><br>[$securePasswordKdfAlgoPBKDF2HMACSHA512iter100000](../constructors/securePasswordKdfAlgoPBKDF2HMACSHA512iter100000.md) = \['salt' => [bytes](../types/bytes.md), \];<a name="securePasswordKdfAlgoPBKDF2HMACSHA512iter100000"></a>  

***
<br><br>[$securePasswordKdfAlgoSHA512](../constructors/securePasswordKdfAlgoSHA512.md) = \['salt' => [bytes](../types/bytes.md), \];<a name="securePasswordKdfAlgoSHA512"></a>  

***
<br><br>[$securePasswordKdfAlgoUnknown](../constructors/securePasswordKdfAlgoUnknown.md) = \[\];<a name="securePasswordKdfAlgoUnknown"></a>  

***
<br><br>[$securePlainEmail](../constructors/securePlainEmail.md) = \['email' => [string](../types/string.md), \];<a name="securePlainEmail"></a>  

***
<br><br>[$securePlainPhone](../constructors/securePlainPhone.md) = \['phone' => [string](../types/string.md), \];<a name="securePlainPhone"></a>  

***
<br><br>[$secureRequiredType](../constructors/secureRequiredType.md) = \['native_names' => [Bool](../types/Bool.md), 'selfie_required' => [Bool](../types/Bool.md), 'translation_required' => [Bool](../types/Bool.md), 'type' => [SecureValueType](../types/SecureValueType.md), \];<a name="secureRequiredType"></a>  

***
<br><br>[$secureRequiredTypeOneOf](../constructors/secureRequiredTypeOneOf.md) = \['types' => \[[SecureRequiredType](../types/SecureRequiredType.md)\], \];<a name="secureRequiredTypeOneOf"></a>  

***
<br><br>[$secureSecretSettings](../constructors/secureSecretSettings.md) = \['secure_algo' => [SecurePasswordKdfAlgo](../types/SecurePasswordKdfAlgo.md), 'secure_secret' => [bytes](../types/bytes.md), 'secure_secret_id' => [long](../types/long.md), \];<a name="secureSecretSettings"></a>  

***
<br><br>[$secureValue](../constructors/secureValue.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'data' => [SecureData](../types/SecureData.md), 'front_side' => [SecureFile](../types/SecureFile.md), 'reverse_side' => [SecureFile](../types/SecureFile.md), 'selfie' => [SecureFile](../types/SecureFile.md), 'translation' => \[[SecureFile](../types/SecureFile.md)\], 'files' => \[[SecureFile](../types/SecureFile.md)\], 'plain_data' => [SecurePlainData](../types/SecurePlainData.md), 'hash' => [bytes](../types/bytes.md), \];<a name="secureValue"></a>  

***
<br><br>[$secureValueError](../constructors/secureValueError.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'hash' => [bytes](../types/bytes.md), 'text' => [string](../types/string.md), \];<a name="secureValueError"></a>  

***
<br><br>[$secureValueErrorData](../constructors/secureValueErrorData.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'data_hash' => [bytes](../types/bytes.md), 'field' => [string](../types/string.md), 'text' => [string](../types/string.md), \];<a name="secureValueErrorData"></a>  

***
<br><br>[$secureValueErrorFile](../constructors/secureValueErrorFile.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'file_hash' => [bytes](../types/bytes.md), 'text' => [string](../types/string.md), \];<a name="secureValueErrorFile"></a>  

***
<br><br>[$secureValueErrorFiles](../constructors/secureValueErrorFiles.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'file_hash' => \[[bytes](../types/bytes.md)\], 'text' => [string](../types/string.md), \];<a name="secureValueErrorFiles"></a>  

***
<br><br>[$secureValueErrorFrontSide](../constructors/secureValueErrorFrontSide.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'file_hash' => [bytes](../types/bytes.md), 'text' => [string](../types/string.md), \];<a name="secureValueErrorFrontSide"></a>  

***
<br><br>[$secureValueErrorReverseSide](../constructors/secureValueErrorReverseSide.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'file_hash' => [bytes](../types/bytes.md), 'text' => [string](../types/string.md), \];<a name="secureValueErrorReverseSide"></a>  

***
<br><br>[$secureValueErrorSelfie](../constructors/secureValueErrorSelfie.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'file_hash' => [bytes](../types/bytes.md), 'text' => [string](../types/string.md), \];<a name="secureValueErrorSelfie"></a>  

***
<br><br>[$secureValueErrorTranslationFile](../constructors/secureValueErrorTranslationFile.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'file_hash' => [bytes](../types/bytes.md), 'text' => [string](../types/string.md), \];<a name="secureValueErrorTranslationFile"></a>  

***
<br><br>[$secureValueErrorTranslationFiles](../constructors/secureValueErrorTranslationFiles.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'file_hash' => \[[bytes](../types/bytes.md)\], 'text' => [string](../types/string.md), \];<a name="secureValueErrorTranslationFiles"></a>  

***
<br><br>[$secureValueHash](../constructors/secureValueHash.md) = \['type' => [SecureValueType](../types/SecureValueType.md), 'hash' => [bytes](../types/bytes.md), \];<a name="secureValueHash"></a>  

***
<br><br>[$secureValueTypeAddress](../constructors/secureValueTypeAddress.md) = \[\];<a name="secureValueTypeAddress"></a>  

***
<br><br>[$secureValueTypeBankStatement](../constructors/secureValueTypeBankStatement.md) = \[\];<a name="secureValueTypeBankStatement"></a>  

***
<br><br>[$secureValueTypeDriverLicense](../constructors/secureValueTypeDriverLicense.md) = \[\];<a name="secureValueTypeDriverLicense"></a>  

***
<br><br>[$secureValueTypeEmail](../constructors/secureValueTypeEmail.md) = \[\];<a name="secureValueTypeEmail"></a>  

***
<br><br>[$secureValueTypeIdentityCard](../constructors/secureValueTypeIdentityCard.md) = \[\];<a name="secureValueTypeIdentityCard"></a>  

***
<br><br>[$secureValueTypeInternalPassport](../constructors/secureValueTypeInternalPassport.md) = \[\];<a name="secureValueTypeInternalPassport"></a>  

***
<br><br>[$secureValueTypePassport](../constructors/secureValueTypePassport.md) = \[\];<a name="secureValueTypePassport"></a>  

***
<br><br>[$secureValueTypePassportRegistration](../constructors/secureValueTypePassportRegistration.md) = \[\];<a name="secureValueTypePassportRegistration"></a>  

***
<br><br>[$secureValueTypePersonalDetails](../constructors/secureValueTypePersonalDetails.md) = \[\];<a name="secureValueTypePersonalDetails"></a>  

***
<br><br>[$secureValueTypePhone](../constructors/secureValueTypePhone.md) = \[\];<a name="secureValueTypePhone"></a>  

***
<br><br>[$secureValueTypeRentalAgreement](../constructors/secureValueTypeRentalAgreement.md) = \[\];<a name="secureValueTypeRentalAgreement"></a>  

***
<br><br>[$secureValueTypeTemporaryRegistration](../constructors/secureValueTypeTemporaryRegistration.md) = \[\];<a name="secureValueTypeTemporaryRegistration"></a>  

***
<br><br>[$secureValueTypeUtilityBill](../constructors/secureValueTypeUtilityBill.md) = \[\];<a name="secureValueTypeUtilityBill"></a>  

***
<br><br>[$sendMessageCancelAction](../constructors/sendMessageCancelAction.md) = \[\];<a name="sendMessageCancelAction"></a>  

***
<br><br>[$sendMessageChooseContactAction](../constructors/sendMessageChooseContactAction.md) = \[\];<a name="sendMessageChooseContactAction"></a>  

***
<br><br>[$sendMessageGamePlayAction](../constructors/sendMessageGamePlayAction.md) = \[\];<a name="sendMessageGamePlayAction"></a>  

***
<br><br>[$sendMessageGeoLocationAction](../constructors/sendMessageGeoLocationAction.md) = \[\];<a name="sendMessageGeoLocationAction"></a>  

***
<br><br>[$sendMessageRecordAudioAction](../constructors/sendMessageRecordAudioAction.md) = \[\];<a name="sendMessageRecordAudioAction"></a>  

***
<br><br>[$sendMessageRecordRoundAction](../constructors/sendMessageRecordRoundAction.md) = \[\];<a name="sendMessageRecordRoundAction"></a>  

***
<br><br>[$sendMessageRecordVideoAction](../constructors/sendMessageRecordVideoAction.md) = \[\];<a name="sendMessageRecordVideoAction"></a>  

***
<br><br>[$sendMessageTypingAction](../constructors/sendMessageTypingAction.md) = \[\];<a name="sendMessageTypingAction"></a>  

***
<br><br>[$sendMessageUploadAudioAction](../constructors/sendMessageUploadAudioAction.md) = \['progress' => [int](../types/int.md), \];<a name="sendMessageUploadAudioAction"></a>  

***
<br><br>[$sendMessageUploadDocumentAction](../constructors/sendMessageUploadDocumentAction.md) = \['progress' => [int](../types/int.md), \];<a name="sendMessageUploadDocumentAction"></a>  

***
<br><br>[$sendMessageUploadPhotoAction](../constructors/sendMessageUploadPhotoAction.md) = \['progress' => [int](../types/int.md), \];<a name="sendMessageUploadPhotoAction"></a>  

***
<br><br>[$sendMessageUploadRoundAction](../constructors/sendMessageUploadRoundAction.md) = \['progress' => [int](../types/int.md), \];<a name="sendMessageUploadRoundAction"></a>  

***
<br><br>[$sendMessageUploadVideoAction](../constructors/sendMessageUploadVideoAction.md) = \['progress' => [int](../types/int.md), \];<a name="sendMessageUploadVideoAction"></a>  

***
<br><br>[$shippingOption](../constructors/shippingOption.md) = \['id' => [string](../types/string.md), 'title' => [string](../types/string.md), 'prices' => \[[LabeledPrice](../types/LabeledPrice.md)\], \];<a name="shippingOption"></a>  

***
<br><br>[$statsURL](../constructors/statsURL.md) = \['url' => [string](../types/string.md), \];<a name="statsURL"></a>  

***
<br><br>[$stickerPack](../constructors/stickerPack.md) = \['emoticon' => [string](../types/string.md), 'documents' => \[[long](../types/long.md)\], \];<a name="stickerPack"></a>  

***
<br><br>[$stickerSet](../constructors/stickerSet.md) = \['archived' => [Bool](../types/Bool.md), 'official' => [Bool](../types/Bool.md), 'masks' => [Bool](../types/Bool.md), 'animated' => [Bool](../types/Bool.md), 'installed_date' => [int](../types/int.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'title' => [string](../types/string.md), 'short_name' => [string](../types/string.md), 'thumb' => [PhotoSize](../types/PhotoSize.md), 'thumb_dc_id' => [int](../types/int.md), 'count' => [int](../types/int.md), 'hash' => [int](../types/int.md), \];<a name="stickerSet"></a>  

***
<br><br>[$stickerSetCovered](../constructors/stickerSetCovered.md) = \['set' => [StickerSet](../types/StickerSet.md), 'cover' => [Document](../types/Document.md), \];<a name="stickerSetCovered"></a>  

***
<br><br>[$stickerSetMultiCovered](../constructors/stickerSetMultiCovered.md) = \['set' => [StickerSet](../types/StickerSet.md), 'covers' => \[[Document](../types/Document.md)\], \];<a name="stickerSetMultiCovered"></a>  

***
<br><br>[$storage\_fileGif](../constructors/storage_fileGif.md) = \[\];<a name="storage_fileGif"></a>  

[$storage\_fileJpeg](../constructors/storage_fileJpeg.md) = \[\];<a name="storage_fileJpeg"></a>  

[$storage\_fileMov](../constructors/storage_fileMov.md) = \[\];<a name="storage_fileMov"></a>  

[$storage\_fileMp3](../constructors/storage_fileMp3.md) = \[\];<a name="storage_fileMp3"></a>  

[$storage\_fileMp4](../constructors/storage_fileMp4.md) = \[\];<a name="storage_fileMp4"></a>  

[$storage\_filePartial](../constructors/storage_filePartial.md) = \[\];<a name="storage_filePartial"></a>  

[$storage\_filePdf](../constructors/storage_filePdf.md) = \[\];<a name="storage_filePdf"></a>  

[$storage\_filePng](../constructors/storage_filePng.md) = \[\];<a name="storage_filePng"></a>  

[$storage\_fileUnknown](../constructors/storage_fileUnknown.md) = \[\];<a name="storage_fileUnknown"></a>  

[$storage\_fileWebp](../constructors/storage_fileWebp.md) = \[\];<a name="storage_fileWebp"></a>  

***
<br><br>[$textAnchor](../constructors/textAnchor.md) = \['text' => [RichText](../types/RichText.md), 'name' => [string](../types/string.md), \];<a name="textAnchor"></a>  

***
<br><br>[$textBold](../constructors/textBold.md) = \['text' => [RichText](../types/RichText.md), \];<a name="textBold"></a>  

***
<br><br>[$textConcat](../constructors/textConcat.md) = \['texts' => \[[RichText](../types/RichText.md)\], \];<a name="textConcat"></a>  

***
<br><br>[$textEmail](../constructors/textEmail.md) = \['text' => [RichText](../types/RichText.md), 'email' => [string](../types/string.md), \];<a name="textEmail"></a>  

***
<br><br>[$textEmpty](../constructors/textEmpty.md) = \[\];<a name="textEmpty"></a>  

***
<br><br>[$textFixed](../constructors/textFixed.md) = \['text' => [RichText](../types/RichText.md), \];<a name="textFixed"></a>  

***
<br><br>[$textImage](../constructors/textImage.md) = \['document_id' => [long](../types/long.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), \];<a name="textImage"></a>  

***
<br><br>[$textItalic](../constructors/textItalic.md) = \['text' => [RichText](../types/RichText.md), \];<a name="textItalic"></a>  

***
<br><br>[$textMarked](../constructors/textMarked.md) = \['text' => [RichText](../types/RichText.md), \];<a name="textMarked"></a>  

***
<br><br>[$textPhone](../constructors/textPhone.md) = \['text' => [RichText](../types/RichText.md), 'phone' => [string](../types/string.md), \];<a name="textPhone"></a>  

***
<br><br>[$textPlain](../constructors/textPlain.md) = \['text' => [string](../types/string.md), \];<a name="textPlain"></a>  

***
<br><br>[$textStrike](../constructors/textStrike.md) = \['text' => [RichText](../types/RichText.md), \];<a name="textStrike"></a>  

***
<br><br>[$textSubscript](../constructors/textSubscript.md) = \['text' => [RichText](../types/RichText.md), \];<a name="textSubscript"></a>  

***
<br><br>[$textSuperscript](../constructors/textSuperscript.md) = \['text' => [RichText](../types/RichText.md), \];<a name="textSuperscript"></a>  

***
<br><br>[$textUnderline](../constructors/textUnderline.md) = \['text' => [RichText](../types/RichText.md), \];<a name="textUnderline"></a>  

***
<br><br>[$textUrl](../constructors/textUrl.md) = \['text' => [RichText](../types/RichText.md), 'url' => [string](../types/string.md), 'webpage_id' => [long](../types/long.md), \];<a name="textUrl"></a>  

***
<br><br>[$theme](../constructors/theme.md) = \['creator' => [Bool](../types/Bool.md), 'default' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'slug' => [string](../types/string.md), 'title' => [string](../types/string.md), 'document' => [Document](../types/Document.md), 'installs_count' => [int](../types/int.md), \];<a name="theme"></a>  

***
<br><br>[$themeDocumentNotModified](../constructors/themeDocumentNotModified.md) = \[\];<a name="themeDocumentNotModified"></a>  

***
<br><br>[$topPeer](../constructors/topPeer.md) = \['peer' => [Peer](../types/Peer.md), 'rating' => [double](../types/double.md), \];<a name="topPeer"></a>  

***
<br><br>[$topPeerCategoryBotsInline](../constructors/topPeerCategoryBotsInline.md) = \[\];<a name="topPeerCategoryBotsInline"></a>  

***
<br><br>[$topPeerCategoryBotsPM](../constructors/topPeerCategoryBotsPM.md) = \[\];<a name="topPeerCategoryBotsPM"></a>  

***
<br><br>[$topPeerCategoryChannels](../constructors/topPeerCategoryChannels.md) = \[\];<a name="topPeerCategoryChannels"></a>  

***
<br><br>[$topPeerCategoryCorrespondents](../constructors/topPeerCategoryCorrespondents.md) = \[\];<a name="topPeerCategoryCorrespondents"></a>  

***
<br><br>[$topPeerCategoryForwardChats](../constructors/topPeerCategoryForwardChats.md) = \[\];<a name="topPeerCategoryForwardChats"></a>  

***
<br><br>[$topPeerCategoryForwardUsers](../constructors/topPeerCategoryForwardUsers.md) = \[\];<a name="topPeerCategoryForwardUsers"></a>  

***
<br><br>[$topPeerCategoryGroups](../constructors/topPeerCategoryGroups.md) = \[\];<a name="topPeerCategoryGroups"></a>  

***
<br><br>[$topPeerCategoryPeers](../constructors/topPeerCategoryPeers.md) = \['category' => [TopPeerCategory](../types/TopPeerCategory.md), 'count' => [int](../types/int.md), 'peers' => \[[TopPeer](../types/TopPeer.md)\], \];<a name="topPeerCategoryPeers"></a>  

***
<br><br>[$topPeerCategoryPhoneCalls](../constructors/topPeerCategoryPhoneCalls.md) = \[\];<a name="topPeerCategoryPhoneCalls"></a>  

***
<br><br>[$true](../constructors/true.md) = \[\];<a name="true"></a>  

***
<br><br>[$updateBotCallbackQuery](../constructors/updateBotCallbackQuery.md) = \['query_id' => [long](../types/long.md), 'user_id' => [int](../types/int.md), 'peer' => [Peer](../types/Peer.md), 'msg_id' => [int](../types/int.md), 'chat_instance' => [long](../types/long.md), 'data' => [bytes](../types/bytes.md), 'game_short_name' => [string](../types/string.md), \];<a name="updateBotCallbackQuery"></a>  

***
<br><br>[$updateBotInlineQuery](../constructors/updateBotInlineQuery.md) = \['query_id' => [long](../types/long.md), 'user_id' => [int](../types/int.md), 'query' => [string](../types/string.md), 'geo' => [GeoPoint](../types/GeoPoint.md), 'offset' => [string](../types/string.md), \];<a name="updateBotInlineQuery"></a>  

***
<br><br>[$updateBotInlineSend](../constructors/updateBotInlineSend.md) = \['user_id' => [int](../types/int.md), 'query' => [string](../types/string.md), 'geo' => [GeoPoint](../types/GeoPoint.md), 'id' => [string](../types/string.md), 'msg_id' => [InputBotInlineMessageID](../types/InputBotInlineMessageID.md), \];<a name="updateBotInlineSend"></a>  

***
<br><br>[$updateBotPrecheckoutQuery](../constructors/updateBotPrecheckoutQuery.md) = \['query_id' => [long](../types/long.md), 'user_id' => [int](../types/int.md), 'payload' => [bytes](../types/bytes.md), 'info' => [PaymentRequestedInfo](../types/PaymentRequestedInfo.md), 'shipping_option_id' => [string](../types/string.md), 'currency' => [string](../types/string.md), 'total_amount' => [long](../types/long.md), \];<a name="updateBotPrecheckoutQuery"></a>  

***
<br><br>[$updateBotShippingQuery](../constructors/updateBotShippingQuery.md) = \['query_id' => [long](../types/long.md), 'user_id' => [int](../types/int.md), 'payload' => [bytes](../types/bytes.md), 'shipping_address' => [PostAddress](../types/PostAddress.md), \];<a name="updateBotShippingQuery"></a>  

***
<br><br>[$updateBotWebhookJSON](../constructors/updateBotWebhookJSON.md) = \['data' => [DataJSON](../types/DataJSON.md), \];<a name="updateBotWebhookJSON"></a>  

***
<br><br>[$updateBotWebhookJSONQuery](../constructors/updateBotWebhookJSONQuery.md) = \['query_id' => [long](../types/long.md), 'data' => [DataJSON](../types/DataJSON.md), 'timeout' => [int](../types/int.md), \];<a name="updateBotWebhookJSONQuery"></a>  

***
<br><br>[$updateChannel](../constructors/updateChannel.md) = \['channel_id' => [int](../types/int.md), \];<a name="updateChannel"></a>  

***
<br><br>[$updateChannelAvailableMessages](../constructors/updateChannelAvailableMessages.md) = \['channel_id' => [int](../types/int.md), 'available_min_id' => [int](../types/int.md), \];<a name="updateChannelAvailableMessages"></a>  

***
<br><br>[$updateChannelMessageViews](../constructors/updateChannelMessageViews.md) = \['channel_id' => [int](../types/int.md), 'id' => [int](../types/int.md), 'views' => [int](../types/int.md), \];<a name="updateChannelMessageViews"></a>  

***
<br><br>[$updateChannelPinnedMessage](../constructors/updateChannelPinnedMessage.md) = \['channel_id' => [int](../types/int.md), 'id' => [int](../types/int.md), \];<a name="updateChannelPinnedMessage"></a>  

***
<br><br>[$updateChannelReadMessagesContents](../constructors/updateChannelReadMessagesContents.md) = \['channel_id' => [int](../types/int.md), 'messages' => \[[int](../types/int.md)\], \];<a name="updateChannelReadMessagesContents"></a>  

***
<br><br>[$updateChannelTooLong](../constructors/updateChannelTooLong.md) = \['channel_id' => [int](../types/int.md), 'pts' => [int](../types/int.md), \];<a name="updateChannelTooLong"></a>  

***
<br><br>[$updateChannelWebPage](../constructors/updateChannelWebPage.md) = \['channel_id' => [int](../types/int.md), 'webpage' => [WebPage](../types/WebPage.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateChannelWebPage"></a>  

***
<br><br>[$updateChatDefaultBannedRights](../constructors/updateChatDefaultBannedRights.md) = \['peer' => [Peer](../types/Peer.md), 'default_banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), 'version' => [int](../types/int.md), \];<a name="updateChatDefaultBannedRights"></a>  

***
<br><br>[$updateChatParticipantAdd](../constructors/updateChatParticipantAdd.md) = \['chat_id' => [int](../types/int.md), 'user_id' => [int](../types/int.md), 'inviter_id' => [int](../types/int.md), 'date' => [int](../types/int.md), 'version' => [int](../types/int.md), \];<a name="updateChatParticipantAdd"></a>  

***
<br><br>[$updateChatParticipantAdmin](../constructors/updateChatParticipantAdmin.md) = \['chat_id' => [int](../types/int.md), 'user_id' => [int](../types/int.md), 'is_admin' => [Bool](../types/Bool.md), 'version' => [int](../types/int.md), \];<a name="updateChatParticipantAdmin"></a>  

***
<br><br>[$updateChatParticipantDelete](../constructors/updateChatParticipantDelete.md) = \['chat_id' => [int](../types/int.md), 'user_id' => [int](../types/int.md), 'version' => [int](../types/int.md), \];<a name="updateChatParticipantDelete"></a>  

***
<br><br>[$updateChatParticipants](../constructors/updateChatParticipants.md) = \['participants' => [ChatParticipants](../types/ChatParticipants.md), \];<a name="updateChatParticipants"></a>  

***
<br><br>[$updateChatPinnedMessage](../constructors/updateChatPinnedMessage.md) = \['chat_id' => [int](../types/int.md), 'id' => [int](../types/int.md), 'version' => [int](../types/int.md), \];<a name="updateChatPinnedMessage"></a>  

***
<br><br>[$updateChatUserTyping](../constructors/updateChatUserTyping.md) = \['chat_id' => [int](../types/int.md), 'user_id' => [int](../types/int.md), 'action' => [SendMessageAction](../types/SendMessageAction.md), \];<a name="updateChatUserTyping"></a>  

***
<br><br>[$updateConfig](../constructors/updateConfig.md) = \[\];<a name="updateConfig"></a>  

***
<br><br>[$updateContactsReset](../constructors/updateContactsReset.md) = \[\];<a name="updateContactsReset"></a>  

***
<br><br>[$updateDcOptions](../constructors/updateDcOptions.md) = \['dc_options' => \[[DcOption](../types/DcOption.md)\], \];<a name="updateDcOptions"></a>  

***
<br><br>[$updateDeleteChannelMessages](../constructors/updateDeleteChannelMessages.md) = \['channel_id' => [int](../types/int.md), 'messages' => \[[int](../types/int.md)\], 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateDeleteChannelMessages"></a>  

***
<br><br>[$updateDeleteMessages](../constructors/updateDeleteMessages.md) = \['messages' => \[[int](../types/int.md)\], 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateDeleteMessages"></a>  

***
<br><br>[$updateDeleteScheduledMessages](../constructors/updateDeleteScheduledMessages.md) = \['peer' => [Peer](../types/Peer.md), 'messages' => \[[int](../types/int.md)\], \];<a name="updateDeleteScheduledMessages"></a>  

***
<br><br>[$updateDialogPinned](../constructors/updateDialogPinned.md) = \['pinned' => [Bool](../types/Bool.md), 'folder_id' => [int](../types/int.md), 'peer' => [DialogPeer](../types/DialogPeer.md), \];<a name="updateDialogPinned"></a>  

***
<br><br>[$updateDialogUnreadMark](../constructors/updateDialogUnreadMark.md) = \['unread' => [Bool](../types/Bool.md), 'peer' => [DialogPeer](../types/DialogPeer.md), \];<a name="updateDialogUnreadMark"></a>  

***
<br><br>[$updateDraftMessage](../constructors/updateDraftMessage.md) = \['peer' => [Peer](../types/Peer.md), 'draft' => [DraftMessage](../types/DraftMessage.md), \];<a name="updateDraftMessage"></a>  

***
<br><br>[$updateEditChannelMessage](../constructors/updateEditChannelMessage.md) = \['message' => [Message](../types/Message.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateEditChannelMessage"></a>  

***
<br><br>[$updateEditMessage](../constructors/updateEditMessage.md) = \['message' => [Message](../types/Message.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateEditMessage"></a>  

***
<br><br>[$updateEncryptedChatTyping](../constructors/updateEncryptedChatTyping.md) = \['chat_id' => [int](../types/int.md), \];<a name="updateEncryptedChatTyping"></a>  

***
<br><br>[$updateEncryptedMessagesRead](../constructors/updateEncryptedMessagesRead.md) = \['chat_id' => [int](../types/int.md), 'max_date' => [int](../types/int.md), 'date' => [int](../types/int.md), \];<a name="updateEncryptedMessagesRead"></a>  

***
<br><br>[$updateEncryption](../constructors/updateEncryption.md) = \['chat' => [EncryptedChat](../types/EncryptedChat.md), 'date' => [int](../types/int.md), \];<a name="updateEncryption"></a>  

***
<br><br>[$updateFavedStickers](../constructors/updateFavedStickers.md) = \[\];<a name="updateFavedStickers"></a>  

***
<br><br>[$updateFolderPeers](../constructors/updateFolderPeers.md) = \['folder_peers' => \[[FolderPeer](../types/FolderPeer.md)\], 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateFolderPeers"></a>  

***
<br><br>[$updateInlineBotCallbackQuery](../constructors/updateInlineBotCallbackQuery.md) = \['query_id' => [long](../types/long.md), 'user_id' => [int](../types/int.md), 'msg_id' => [InputBotInlineMessageID](../types/InputBotInlineMessageID.md), 'chat_instance' => [long](../types/long.md), 'data' => [bytes](../types/bytes.md), 'game_short_name' => [string](../types/string.md), \];<a name="updateInlineBotCallbackQuery"></a>  

***
<br><br>[$updateLangPack](../constructors/updateLangPack.md) = \['difference' => [LangPackDifference](../types/LangPackDifference.md), \];<a name="updateLangPack"></a>  

***
<br><br>[$updateLangPackTooLong](../constructors/updateLangPackTooLong.md) = \['lang_code' => [string](../types/string.md), \];<a name="updateLangPackTooLong"></a>  

***
<br><br>[$updateMessageID](../constructors/updateMessageID.md) = \['id' => [int](../types/int.md), \];<a name="updateMessageID"></a>  

***
<br><br>[$updateMessagePoll](../constructors/updateMessagePoll.md) = \['poll_id' => [long](../types/long.md), 'poll' => [Poll](../types/Poll.md), 'results' => [PollResults](../types/PollResults.md), \];<a name="updateMessagePoll"></a>  

***
<br><br>[$updateNewChannelMessage](../constructors/updateNewChannelMessage.md) = \['message' => [Message](../types/Message.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateNewChannelMessage"></a>  

***
<br><br>[$updateNewEncryptedMessage](../constructors/updateNewEncryptedMessage.md) = \['message' => [EncryptedMessage](../types/EncryptedMessage.md), 'qts' => [int](../types/int.md), \];<a name="updateNewEncryptedMessage"></a>  

***
<br><br>[$updateNewMessage](../constructors/updateNewMessage.md) = \['message' => [Message](../types/Message.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateNewMessage"></a>  

***
<br><br>[$updateNewScheduledMessage](../constructors/updateNewScheduledMessage.md) = \['message' => [Message](../types/Message.md), \];<a name="updateNewScheduledMessage"></a>  

***
<br><br>[$updateNewStickerSet](../constructors/updateNewStickerSet.md) = \['stickerset' => [messages\_StickerSet](../types/messages_StickerSet.md), \];<a name="updateNewStickerSet"></a>  

***
<br><br>[$updateNotifySettings](../constructors/updateNotifySettings.md) = \['peer' => [NotifyPeer](../types/NotifyPeer.md), 'notify_settings' => [PeerNotifySettings](../types/PeerNotifySettings.md), \];<a name="updateNotifySettings"></a>  

***
<br><br>[$updatePeerLocated](../constructors/updatePeerLocated.md) = \['peers' => \[[PeerLocated](../types/PeerLocated.md)\], \];<a name="updatePeerLocated"></a>  

***
<br><br>[$updatePeerSettings](../constructors/updatePeerSettings.md) = \['peer' => [Peer](../types/Peer.md), 'settings' => [PeerSettings](../types/PeerSettings.md), \];<a name="updatePeerSettings"></a>  

***
<br><br>[$updatePhoneCall](../constructors/updatePhoneCall.md) = \['phone_call' => [PhoneCall](../types/PhoneCall.md), \];<a name="updatePhoneCall"></a>  

***
<br><br>[$updatePinnedDialogs](../constructors/updatePinnedDialogs.md) = \['folder_id' => [int](../types/int.md), 'order' => \[[DialogPeer](../types/DialogPeer.md)\], \];<a name="updatePinnedDialogs"></a>  

***
<br><br>[$updatePrivacy](../constructors/updatePrivacy.md) = \['key' => [PrivacyKey](../types/PrivacyKey.md), 'rules' => \[[PrivacyRule](../types/PrivacyRule.md)\], \];<a name="updatePrivacy"></a>  

***
<br><br>[$updatePtsChanged](../constructors/updatePtsChanged.md) = \[\];<a name="updatePtsChanged"></a>  

***
<br><br>[$updateReadChannelInbox](../constructors/updateReadChannelInbox.md) = \['folder_id' => [int](../types/int.md), 'channel_id' => [int](../types/int.md), 'max_id' => [int](../types/int.md), 'still_unread_count' => [int](../types/int.md), 'pts' => [int](../types/int.md), \];<a name="updateReadChannelInbox"></a>  

***
<br><br>[$updateReadChannelOutbox](../constructors/updateReadChannelOutbox.md) = \['channel_id' => [int](../types/int.md), 'max_id' => [int](../types/int.md), \];<a name="updateReadChannelOutbox"></a>  

***
<br><br>[$updateReadFeaturedStickers](../constructors/updateReadFeaturedStickers.md) = \[\];<a name="updateReadFeaturedStickers"></a>  

***
<br><br>[$updateReadHistoryInbox](../constructors/updateReadHistoryInbox.md) = \['folder_id' => [int](../types/int.md), 'peer' => [Peer](../types/Peer.md), 'max_id' => [int](../types/int.md), 'still_unread_count' => [int](../types/int.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateReadHistoryInbox"></a>  

***
<br><br>[$updateReadHistoryOutbox](../constructors/updateReadHistoryOutbox.md) = \['peer' => [Peer](../types/Peer.md), 'max_id' => [int](../types/int.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateReadHistoryOutbox"></a>  

***
<br><br>[$updateReadMessagesContents](../constructors/updateReadMessagesContents.md) = \['messages' => \[[int](../types/int.md)\], 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateReadMessagesContents"></a>  

***
<br><br>[$updateRecentStickers](../constructors/updateRecentStickers.md) = \[\];<a name="updateRecentStickers"></a>  

***
<br><br>[$updateSavedGifs](../constructors/updateSavedGifs.md) = \[\];<a name="updateSavedGifs"></a>  

***
<br><br>[$updateServiceNotification](../constructors/updateServiceNotification.md) = \['popup' => [Bool](../types/Bool.md), 'inbox_date' => [int](../types/int.md), 'type' => [string](../types/string.md), 'message' => [string](../types/string.md), 'media' => [MessageMedia](../types/MessageMedia.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \];<a name="updateServiceNotification"></a>  

***
<br><br>[$updateShort](../constructors/updateShort.md) = \['update' => [Update](../types/Update.md), 'date' => [int](../types/int.md), \];<a name="updateShort"></a>  

***
<br><br>[$updateShortChatMessage](../constructors/updateShortChatMessage.md) = \['out' => [Bool](../types/Bool.md), 'mentioned' => [Bool](../types/Bool.md), 'media_unread' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'from_id' => [int](../types/int.md), 'chat_id' => [int](../types/int.md), 'message' => [string](../types/string.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), 'date' => [int](../types/int.md), 'fwd_from' => [MessageFwdHeader](../types/MessageFwdHeader.md), 'via_bot_id' => [int](../types/int.md), 'reply_to_msg_id' => [int](../types/int.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \];<a name="updateShortChatMessage"></a>  

***
<br><br>[$updateShortMessage](../constructors/updateShortMessage.md) = \['out' => [Bool](../types/Bool.md), 'mentioned' => [Bool](../types/Bool.md), 'media_unread' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'user_id' => [int](../types/int.md), 'message' => [string](../types/string.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), 'date' => [int](../types/int.md), 'fwd_from' => [MessageFwdHeader](../types/MessageFwdHeader.md), 'via_bot_id' => [int](../types/int.md), 'reply_to_msg_id' => [int](../types/int.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \];<a name="updateShortMessage"></a>  

***
<br><br>[$updateShortSentMessage](../constructors/updateShortSentMessage.md) = \['out' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), 'date' => [int](../types/int.md), 'media' => [MessageMedia](../types/MessageMedia.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \];<a name="updateShortSentMessage"></a>  

***
<br><br>[$updateStickerSets](../constructors/updateStickerSets.md) = \[\];<a name="updateStickerSets"></a>  

***
<br><br>[$updateStickerSetsOrder](../constructors/updateStickerSetsOrder.md) = \['masks' => [Bool](../types/Bool.md), 'order' => \[[long](../types/long.md)\], \];<a name="updateStickerSetsOrder"></a>  

***
<br><br>[$updateTheme](../constructors/updateTheme.md) = \['theme' => [Theme](../types/Theme.md), \];<a name="updateTheme"></a>  

***
<br><br>[$updateUserBlocked](../constructors/updateUserBlocked.md) = \['user_id' => [int](../types/int.md), 'blocked' => [Bool](../types/Bool.md), \];<a name="updateUserBlocked"></a>  

***
<br><br>[$updateUserName](../constructors/updateUserName.md) = \['user_id' => [int](../types/int.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'username' => [string](../types/string.md), \];<a name="updateUserName"></a>  

***
<br><br>[$updateUserPhone](../constructors/updateUserPhone.md) = \['user_id' => [int](../types/int.md), 'phone' => [string](../types/string.md), \];<a name="updateUserPhone"></a>  

***
<br><br>[$updateUserPhoto](../constructors/updateUserPhoto.md) = \['user_id' => [int](../types/int.md), 'date' => [int](../types/int.md), 'photo' => [UserProfilePhoto](../types/UserProfilePhoto.md), 'previous' => [Bool](../types/Bool.md), \];<a name="updateUserPhoto"></a>  

***
<br><br>[$updateUserPinnedMessage](../constructors/updateUserPinnedMessage.md) = \['user_id' => [int](../types/int.md), 'id' => [int](../types/int.md), \];<a name="updateUserPinnedMessage"></a>  

***
<br><br>[$updateUserStatus](../constructors/updateUserStatus.md) = \['user_id' => [int](../types/int.md), 'status' => [UserStatus](../types/UserStatus.md), \];<a name="updateUserStatus"></a>  

***
<br><br>[$updateUserTyping](../constructors/updateUserTyping.md) = \['user_id' => [int](../types/int.md), 'action' => [SendMessageAction](../types/SendMessageAction.md), \];<a name="updateUserTyping"></a>  

***
<br><br>[$updateWebPage](../constructors/updateWebPage.md) = \['webpage' => [WebPage](../types/WebPage.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateWebPage"></a>  

***
<br><br>[$updates](../constructors/updates.md) = \['updates' => \[[Update](../types/Update.md)\], 'users' => \[[User](../types/User.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'date' => [int](../types/int.md), 'seq' => [int](../types/int.md), \];<a name="updates"></a>  

***
<br><br>[$updatesCombined](../constructors/updatesCombined.md) = \['updates' => \[[Update](../types/Update.md)\], 'users' => \[[User](../types/User.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'date' => [int](../types/int.md), 'seq_start' => [int](../types/int.md), 'seq' => [int](../types/int.md), \];<a name="updatesCombined"></a>  

***
<br><br>[$updatesTooLong](../constructors/updatesTooLong.md) = \[\];<a name="updatesTooLong"></a>  

***
<br><br>[$updates\_channelDifference](../constructors/updates_channelDifference.md) = \['final' => [Bool](../types/Bool.md), 'pts' => [int](../types/int.md), 'timeout' => [int](../types/int.md), 'new_messages' => \[[Message](../types/Message.md)\], 'other_updates' => \[[Update](../types/Update.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="updates_channelDifference"></a>  

[$updates\_channelDifferenceEmpty](../constructors/updates_channelDifferenceEmpty.md) = \['final' => [Bool](../types/Bool.md), 'pts' => [int](../types/int.md), 'timeout' => [int](../types/int.md), \];<a name="updates_channelDifferenceEmpty"></a>  

[$updates\_channelDifferenceTooLong](../constructors/updates_channelDifferenceTooLong.md) = \['final' => [Bool](../types/Bool.md), 'timeout' => [int](../types/int.md), 'dialog' => [Dialog](../types/Dialog.md), 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="updates_channelDifferenceTooLong"></a>  

[$updates\_difference](../constructors/updates_difference.md) = \['new_messages' => \[[Message](../types/Message.md)\], 'new_encrypted_messages' => \[[EncryptedMessage](../types/EncryptedMessage.md)\], 'other_updates' => \[[Update](../types/Update.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], 'state' => [updates\_State](../types/updates_State.md), \];<a name="updates_difference"></a>  

[$updates\_differenceEmpty](../constructors/updates_differenceEmpty.md) = \['date' => [int](../types/int.md), 'seq' => [int](../types/int.md), \];<a name="updates_differenceEmpty"></a>  

[$updates\_differenceSlice](../constructors/updates_differenceSlice.md) = \['new_messages' => \[[Message](../types/Message.md)\], 'new_encrypted_messages' => \[[EncryptedMessage](../types/EncryptedMessage.md)\], 'other_updates' => \[[Update](../types/Update.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], 'intermediate_state' => [updates\_State](../types/updates_State.md), \];<a name="updates_differenceSlice"></a>  

[$updates\_differenceTooLong](../constructors/updates_differenceTooLong.md) = \['pts' => [int](../types/int.md), \];<a name="updates_differenceTooLong"></a>  

[$updates\_state](../constructors/updates_state.md) = \['pts' => [int](../types/int.md), 'qts' => [int](../types/int.md), 'date' => [int](../types/int.md), 'seq' => [int](../types/int.md), 'unread_count' => [int](../types/int.md), \];<a name="updates_state"></a>  

***
<br><br>[$upload\_cdnFile](../constructors/upload_cdnFile.md) = \['bytes' => [bytes](../types/bytes.md), \];<a name="upload_cdnFile"></a>  

[$upload\_cdnFileReuploadNeeded](../constructors/upload_cdnFileReuploadNeeded.md) = \['request_token' => [bytes](../types/bytes.md), \];<a name="upload_cdnFileReuploadNeeded"></a>  

[$upload\_file](../constructors/upload_file.md) = \['type' => [storage\_FileType](../types/storage_FileType.md), 'mtime' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \];<a name="upload_file"></a>  

[$upload\_fileCdnRedirect](../constructors/upload_fileCdnRedirect.md) = \['dc_id' => [int](../types/int.md), 'file_token' => [bytes](../types/bytes.md), 'encryption_key' => [bytes](../types/bytes.md), 'encryption_iv' => [bytes](../types/bytes.md), 'file_hashes' => \[[FileHash](../types/FileHash.md)\], \];<a name="upload_fileCdnRedirect"></a>  

[$upload\_webFile](../constructors/upload_webFile.md) = \['size' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'file_type' => [storage\_FileType](../types/storage_FileType.md), 'mtime' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \];<a name="upload_webFile"></a>  

***
<br><br>[$urlAuthResultAccepted](../constructors/urlAuthResultAccepted.md) = \['url' => [string](../types/string.md), \];<a name="urlAuthResultAccepted"></a>  

***
<br><br>[$urlAuthResultDefault](../constructors/urlAuthResultDefault.md) = \[\];<a name="urlAuthResultDefault"></a>  

***
<br><br>[$urlAuthResultRequest](../constructors/urlAuthResultRequest.md) = \['request_write_access' => [Bool](../types/Bool.md), 'bot' => [User](../types/User.md), 'domain' => [string](../types/string.md), \];<a name="urlAuthResultRequest"></a>  

***
<br><br>[$user](../constructors/user.md) = \['self' => [Bool](../types/Bool.md), 'contact' => [Bool](../types/Bool.md), 'mutual_contact' => [Bool](../types/Bool.md), 'deleted' => [Bool](../types/Bool.md), 'bot' => [Bool](../types/Bool.md), 'bot_chat_history' => [Bool](../types/Bool.md), 'bot_nochats' => [Bool](../types/Bool.md), 'verified' => [Bool](../types/Bool.md), 'restricted' => [Bool](../types/Bool.md), 'min' => [Bool](../types/Bool.md), 'bot_inline_geo' => [Bool](../types/Bool.md), 'support' => [Bool](../types/Bool.md), 'scam' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'username' => [string](../types/string.md), 'phone' => [string](../types/string.md), 'photo' => [UserProfilePhoto](../types/UserProfilePhoto.md), 'status' => [UserStatus](../types/UserStatus.md), 'bot_info_version' => [int](../types/int.md), 'restriction_reason' => \[[RestrictionReason](../types/RestrictionReason.md)\], 'bot_inline_placeholder' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), \];<a name="user"></a>  

***
<br><br>[$userEmpty](../constructors/userEmpty.md) = \['id' => [int](../types/int.md), \];<a name="userEmpty"></a>  

***
<br><br>[$userFull](../constructors/userFull.md) = \['blocked' => [Bool](../types/Bool.md), 'phone_calls_available' => [Bool](../types/Bool.md), 'phone_calls_private' => [Bool](../types/Bool.md), 'can_pin_message' => [Bool](../types/Bool.md), 'has_scheduled' => [Bool](../types/Bool.md), 'user' => [User](../types/User.md), 'about' => [string](../types/string.md), 'settings' => [PeerSettings](../types/PeerSettings.md), 'profile_photo' => [Photo](../types/Photo.md), 'notify_settings' => [PeerNotifySettings](../types/PeerNotifySettings.md), 'bot_info' => [BotInfo](../types/BotInfo.md), 'pinned_msg_id' => [int](../types/int.md), 'common_chats_count' => [int](../types/int.md), 'folder_id' => [int](../types/int.md), \];<a name="userFull"></a>  

***
<br><br>[$userProfilePhoto](../constructors/userProfilePhoto.md) = \['photo_id' => [long](../types/long.md), 'photo_small' => [FileLocation](../types/FileLocation.md), 'photo_big' => [FileLocation](../types/FileLocation.md), 'dc_id' => [int](../types/int.md), \];<a name="userProfilePhoto"></a>  

***
<br><br>[$userProfilePhotoEmpty](../constructors/userProfilePhotoEmpty.md) = \[\];<a name="userProfilePhotoEmpty"></a>  

***
<br><br>[$userStatusEmpty](../constructors/userStatusEmpty.md) = \[\];<a name="userStatusEmpty"></a>  

***
<br><br>[$userStatusLastMonth](../constructors/userStatusLastMonth.md) = \[\];<a name="userStatusLastMonth"></a>  

***
<br><br>[$userStatusLastWeek](../constructors/userStatusLastWeek.md) = \[\];<a name="userStatusLastWeek"></a>  

***
<br><br>[$userStatusOffline](../constructors/userStatusOffline.md) = \['was_online' => [int](../types/int.md), \];<a name="userStatusOffline"></a>  

***
<br><br>[$userStatusOnline](../constructors/userStatusOnline.md) = \['expires' => [int](../types/int.md), \];<a name="userStatusOnline"></a>  

***
<br><br>[$userStatusRecently](../constructors/userStatusRecently.md) = \[\];<a name="userStatusRecently"></a>  

***
<br><br>[$wallPaper](../constructors/wallPaper.md) = \['id' => [long](../types/long.md), 'creator' => [Bool](../types/Bool.md), 'default' => [Bool](../types/Bool.md), 'pattern' => [Bool](../types/Bool.md), 'dark' => [Bool](../types/Bool.md), 'access_hash' => [long](../types/long.md), 'slug' => [string](../types/string.md), 'document' => [Document](../types/Document.md), 'settings' => [WallPaperSettings](../types/WallPaperSettings.md), \];<a name="wallPaper"></a>  

***
<br><br>[$wallPaperSettings](../constructors/wallPaperSettings.md) = \['blur' => [Bool](../types/Bool.md), 'motion' => [Bool](../types/Bool.md), 'background_color' => [int](../types/int.md), 'intensity' => [int](../types/int.md), \];<a name="wallPaperSettings"></a>  

***
<br><br>[$webAuthorization](../constructors/webAuthorization.md) = \['hash' => [long](../types/long.md), 'bot_id' => [int](../types/int.md), 'domain' => [string](../types/string.md), 'browser' => [string](../types/string.md), 'platform' => [string](../types/string.md), 'date_created' => [int](../types/int.md), 'date_active' => [int](../types/int.md), 'ip' => [string](../types/string.md), 'region' => [string](../types/string.md), \];<a name="webAuthorization"></a>  

***
<br><br>[$webDocument](../constructors/webDocument.md) = \['url' => [string](../types/string.md), 'access_hash' => [long](../types/long.md), 'size' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], \];<a name="webDocument"></a>  

***
<br><br>[$webDocumentNoProxy](../constructors/webDocumentNoProxy.md) = \['url' => [string](../types/string.md), 'size' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], \];<a name="webDocumentNoProxy"></a>  

***
<br><br>[$webPage](../constructors/webPage.md) = \['id' => [long](../types/long.md), 'url' => [string](../types/string.md), 'display_url' => [string](../types/string.md), 'hash' => [int](../types/int.md), 'type' => [string](../types/string.md), 'site_name' => [string](../types/string.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'photo' => [Photo](../types/Photo.md), 'embed_url' => [string](../types/string.md), 'embed_type' => [string](../types/string.md), 'embed_width' => [int](../types/int.md), 'embed_height' => [int](../types/int.md), 'duration' => [int](../types/int.md), 'author' => [string](../types/string.md), 'document' => [Document](../types/Document.md), 'documents' => \[[Document](../types/Document.md)\], 'cached_page' => [Page](../types/Page.md), \];<a name="webPage"></a>  

***
<br><br>[$webPageEmpty](../constructors/webPageEmpty.md) = \['id' => [long](../types/long.md), \];<a name="webPageEmpty"></a>  

***
<br><br>[$webPageNotModified](../constructors/webPageNotModified.md) = \[\];<a name="webPageNotModified"></a>  

***
<br><br>[$webPagePending](../constructors/webPagePending.md) = \['id' => [long](../types/long.md), 'date' => [int](../types/int.md), \];<a name="webPagePending"></a>  

