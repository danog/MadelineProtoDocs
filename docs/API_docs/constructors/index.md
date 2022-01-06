---
title: Constructors
description: List of constructors
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructors  
[Back to API documentation index](..)

***
<br><br>[$account.authorizationForm](../constructors/account.authorizationForm.md) = \['required_types' => \[[SecureRequiredType](../types/SecureRequiredType.md)\], 'values' => \[[SecureValue](../types/SecureValue.md)\], 'errors' => \[[SecureValueError](../types/SecureValueError.md)\], 'users' => \[[User](../types/User.md)\], 'privacy_policy_url' => [string](../types/string.md), \];<a name="account.authorizationForm"></a>  

***
<br><br>[$account.authorizations](../constructors/account.authorizations.md) = \['authorization_ttl_days' => [int](../types/int.md), 'authorizations' => \[[Authorization](../types/Authorization.md)\], \];<a name="account.authorizations"></a>  

***
<br><br>[$account.autoDownloadSettings](../constructors/account.autoDownloadSettings.md) = \['low' => [AutoDownloadSettings](../types/AutoDownloadSettings.md), 'medium' => [AutoDownloadSettings](../types/AutoDownloadSettings.md), 'high' => [AutoDownloadSettings](../types/AutoDownloadSettings.md), \];<a name="account.autoDownloadSettings"></a>  

***
<br><br>[$account.contentSettings](../constructors/account.contentSettings.md) = \['sensitive_enabled' => [Bool](../types/Bool.md), 'sensitive_can_change' => [Bool](../types/Bool.md), \];<a name="account.contentSettings"></a>  

***
<br><br>[$account.password](../constructors/account.password.md) = \['has_recovery' => [Bool](../types/Bool.md), 'has_secure_values' => [Bool](../types/Bool.md), 'has_password' => [Bool](../types/Bool.md), 'current_algo' => [PasswordKdfAlgo](../types/PasswordKdfAlgo.md), 'srp_B' => [bytes](../types/bytes.md), 'srp_id' => [long](../types/long.md), 'hint' => [string](../types/string.md), 'email_unconfirmed_pattern' => [string](../types/string.md), 'new_algo' => [PasswordKdfAlgo](../types/PasswordKdfAlgo.md), 'new_secure_algo' => [SecurePasswordKdfAlgo](../types/SecurePasswordKdfAlgo.md), 'secure_random' => [bytes](../types/bytes.md), 'pending_reset_date' => [int](../types/int.md), \];<a name="account.password"></a>  

***
<br><br>[$account.passwordInputSettings](../constructors/account.passwordInputSettings.md) = \['new_algo' => [PasswordKdfAlgo](../types/PasswordKdfAlgo.md), 'new_password_hash' => [bytes](../types/bytes.md), 'hint' => [string](../types/string.md), 'email' => [string](../types/string.md), 'new_secure_settings' => [SecureSecretSettings](../types/SecureSecretSettings.md), \];<a name="account.passwordInputSettings"></a>  

***
<br><br>[$account.passwordSettings](../constructors/account.passwordSettings.md) = \['email' => [string](../types/string.md), 'secure_settings' => [SecureSecretSettings](../types/SecureSecretSettings.md), \];<a name="account.passwordSettings"></a>  

***
<br><br>[$account.privacyRules](../constructors/account.privacyRules.md) = \['rules' => \[[PrivacyRule](../types/PrivacyRule.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="account.privacyRules"></a>  

***
<br><br>[$account.resetPasswordFailedWait](../constructors/account.resetPasswordFailedWait.md) = \['retry_date' => [int](../types/int.md), \];<a name="account.resetPasswordFailedWait"></a>  

***
<br><br>[$account.resetPasswordOk](../constructors/account.resetPasswordOk.md) = \[\];<a name="account.resetPasswordOk"></a>  

***
<br><br>[$account.resetPasswordRequestedWait](../constructors/account.resetPasswordRequestedWait.md) = \['until_date' => [int](../types/int.md), \];<a name="account.resetPasswordRequestedWait"></a>  

***
<br><br>[$account.sentEmailCode](../constructors/account.sentEmailCode.md) = \['email_pattern' => [string](../types/string.md), 'length' => [int](../types/int.md), \];<a name="account.sentEmailCode"></a>  

***
<br><br>[$account.takeout](../constructors/account.takeout.md) = \['id' => [long](../types/long.md), \];<a name="account.takeout"></a>  

***
<br><br>[$account.themes](../constructors/account.themes.md) = \['hash' => [long](../types/long.md), 'themes' => \[[Theme](../types/Theme.md)\], \];<a name="account.themes"></a>  

***
<br><br>[$account.themesNotModified](../constructors/account.themesNotModified.md) = \[\];<a name="account.themesNotModified"></a>  

***
<br><br>[$account.tmpPassword](../constructors/account.tmpPassword.md) = \['tmp_password' => [bytes](../types/bytes.md), 'valid_until' => [int](../types/int.md), \];<a name="account.tmpPassword"></a>  

***
<br><br>[$account.wallPapers](../constructors/account.wallPapers.md) = \['hash' => [long](../types/long.md), 'wallpapers' => \[[WallPaper](../types/WallPaper.md)\], \];<a name="account.wallPapers"></a>  

***
<br><br>[$account.wallPapersNotModified](../constructors/account.wallPapersNotModified.md) = \[\];<a name="account.wallPapersNotModified"></a>  

***
<br><br>[$account.webAuthorizations](../constructors/account.webAuthorizations.md) = \['authorizations' => \[[WebAuthorization](../types/WebAuthorization.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="account.webAuthorizations"></a>  

***
<br><br>[$accountDaysTTL](../constructors/accountDaysTTL.md) = \['days' => [int](../types/int.md), \];<a name="accountDaysTTL"></a>  

***
<br><br>[$auth.authorization](../constructors/auth.authorization.md) = \['setup_password_required' => [Bool](../types/Bool.md), 'otherwise_relogin_days' => [int](../types/int.md), 'tmp_sessions' => [int](../types/int.md), 'user' => [User](../types/User.md), \];<a name="auth.authorization"></a>  

***
<br><br>[$auth.authorizationSignUpRequired](../constructors/auth.authorizationSignUpRequired.md) = \['terms_of_service' => [help.TermsOfService](../types/help.TermsOfService.md), \];<a name="auth.authorizationSignUpRequired"></a>  

***
<br><br>[$auth.codeTypeCall](../constructors/auth.codeTypeCall.md) = \[\];<a name="auth.codeTypeCall"></a>  

***
<br><br>[$auth.codeTypeFlashCall](../constructors/auth.codeTypeFlashCall.md) = \[\];<a name="auth.codeTypeFlashCall"></a>  

***
<br><br>[$auth.codeTypeMissedCall](../constructors/auth.codeTypeMissedCall.md) = \[\];<a name="auth.codeTypeMissedCall"></a>  

***
<br><br>[$auth.codeTypeSms](../constructors/auth.codeTypeSms.md) = \[\];<a name="auth.codeTypeSms"></a>  

***
<br><br>[$auth.exportedAuthorization](../constructors/auth.exportedAuthorization.md) = \['id' => [long](../types/long.md), 'bytes' => [bytes](../types/bytes.md), \];<a name="auth.exportedAuthorization"></a>  

***
<br><br>[$auth.loggedOut](../constructors/auth.loggedOut.md) = \['future_auth_token' => [bytes](../types/bytes.md), \];<a name="auth.loggedOut"></a>  

***
<br><br>[$auth.loginToken](../constructors/auth.loginToken.md) = \['expires' => [int](../types/int.md), 'token' => [bytes](../types/bytes.md), \];<a name="auth.loginToken"></a>  

***
<br><br>[$auth.loginTokenMigrateTo](../constructors/auth.loginTokenMigrateTo.md) = \['dc_id' => [int](../types/int.md), 'token' => [bytes](../types/bytes.md), \];<a name="auth.loginTokenMigrateTo"></a>  

***
<br><br>[$auth.loginTokenSuccess](../constructors/auth.loginTokenSuccess.md) = \['authorization' => [auth.Authorization](../types/auth.Authorization.md), \];<a name="auth.loginTokenSuccess"></a>  

***
<br><br>[$auth.passwordRecovery](../constructors/auth.passwordRecovery.md) = \['email_pattern' => [string](../types/string.md), \];<a name="auth.passwordRecovery"></a>  

***
<br><br>[$auth.sentCode](../constructors/auth.sentCode.md) = \['type' => [auth.SentCodeType](../types/auth.SentCodeType.md), 'phone_code_hash' => [string](../types/string.md), 'next_type' => [auth.CodeType](../types/auth.CodeType.md), 'timeout' => [int](../types/int.md), \];<a name="auth.sentCode"></a>  

***
<br><br>[$auth.sentCodeTypeApp](../constructors/auth.sentCodeTypeApp.md) = \['length' => [int](../types/int.md), \];<a name="auth.sentCodeTypeApp"></a>  

***
<br><br>[$auth.sentCodeTypeCall](../constructors/auth.sentCodeTypeCall.md) = \['length' => [int](../types/int.md), \];<a name="auth.sentCodeTypeCall"></a>  

***
<br><br>[$auth.sentCodeTypeFlashCall](../constructors/auth.sentCodeTypeFlashCall.md) = \['pattern' => [string](../types/string.md), \];<a name="auth.sentCodeTypeFlashCall"></a>  

***
<br><br>[$auth.sentCodeTypeMissedCall](../constructors/auth.sentCodeTypeMissedCall.md) = \['prefix' => [string](../types/string.md), 'length' => [int](../types/int.md), \];<a name="auth.sentCodeTypeMissedCall"></a>  

***
<br><br>[$auth.sentCodeTypeSms](../constructors/auth.sentCodeTypeSms.md) = \['length' => [int](../types/int.md), \];<a name="auth.sentCodeTypeSms"></a>  

***
<br><br>[$authorization](../constructors/authorization.md) = \['current' => [Bool](../types/Bool.md), 'official_app' => [Bool](../types/Bool.md), 'password_pending' => [Bool](../types/Bool.md), 'encrypted_requests_disabled' => [Bool](../types/Bool.md), 'call_requests_disabled' => [Bool](../types/Bool.md), 'hash' => [long](../types/long.md), 'device_model' => [string](../types/string.md), 'platform' => [string](../types/string.md), 'system_version' => [string](../types/string.md), 'api_id' => [int](../types/int.md), 'app_name' => [string](../types/string.md), 'app_version' => [string](../types/string.md), 'date_created' => [int](../types/int.md), 'date_active' => [int](../types/int.md), 'ip' => [string](../types/string.md), 'country' => [string](../types/string.md), 'region' => [string](../types/string.md), \];<a name="authorization"></a>  

***
<br><br>[$autoDownloadSettings](../constructors/autoDownloadSettings.md) = \['disabled' => [Bool](../types/Bool.md), 'video_preload_large' => [Bool](../types/Bool.md), 'audio_preload_next' => [Bool](../types/Bool.md), 'phonecalls_less_data' => [Bool](../types/Bool.md), 'photo_size_max' => [int](../types/int.md), 'video_size_max' => [int](../types/int.md), 'file_size_max' => [int](../types/int.md), 'video_upload_maxbitrate' => [int](../types/int.md), \];<a name="autoDownloadSettings"></a>  

***
<br><br>[$availableReaction](../constructors/availableReaction.md) = \['inactive' => [Bool](../types/Bool.md), 'reaction' => [string](../types/string.md), 'title' => [string](../types/string.md), 'static_icon' => [Document](../types/Document.md), 'appear_animation' => [Document](../types/Document.md), 'select_animation' => [Document](../types/Document.md), 'activate_animation' => [Document](../types/Document.md), 'effect_animation' => [Document](../types/Document.md), \];<a name="availableReaction"></a>  

***
<br><br>[$bankCardOpenUrl](../constructors/bankCardOpenUrl.md) = \['url' => [string](../types/string.md), 'name' => [string](../types/string.md), \];<a name="bankCardOpenUrl"></a>  

***
<br><br>[$baseThemeArctic](../constructors/baseThemeArctic.md) = \[\];<a name="baseThemeArctic"></a>  

***
<br><br>[$baseThemeClassic](../constructors/baseThemeClassic.md) = \[\];<a name="baseThemeClassic"></a>  

***
<br><br>[$baseThemeDay](../constructors/baseThemeDay.md) = \[\];<a name="baseThemeDay"></a>  

***
<br><br>[$baseThemeNight](../constructors/baseThemeNight.md) = \[\];<a name="baseThemeNight"></a>  

***
<br><br>[$baseThemeTinted](../constructors/baseThemeTinted.md) = \[\];<a name="baseThemeTinted"></a>  

***
<br><br>[$boolFalse](../constructors/boolFalse.md) = \[\];<a name="boolFalse"></a>  

***
<br><br>[$boolTrue](../constructors/boolTrue.md) = \[\];<a name="boolTrue"></a>  

***
<br><br>[$botCommand](../constructors/botCommand.md) = \['command' => [string](../types/string.md), 'description' => [string](../types/string.md), \];<a name="botCommand"></a>  

***
<br><br>[$botCommandScopeChatAdmins](../constructors/botCommandScopeChatAdmins.md) = \[\];<a name="botCommandScopeChatAdmins"></a>  

***
<br><br>[$botCommandScopeChats](../constructors/botCommandScopeChats.md) = \[\];<a name="botCommandScopeChats"></a>  

***
<br><br>[$botCommandScopeDefault](../constructors/botCommandScopeDefault.md) = \[\];<a name="botCommandScopeDefault"></a>  

***
<br><br>[$botCommandScopePeer](../constructors/botCommandScopePeer.md) = \['peer' => [InputPeer](../types/InputPeer.md), \];<a name="botCommandScopePeer"></a>  

***
<br><br>[$botCommandScopePeerAdmins](../constructors/botCommandScopePeerAdmins.md) = \['peer' => [InputPeer](../types/InputPeer.md), \];<a name="botCommandScopePeerAdmins"></a>  

***
<br><br>[$botCommandScopePeerUser](../constructors/botCommandScopePeerUser.md) = \['peer' => [InputPeer](../types/InputPeer.md), 'user_id' => [InputUser](../types/InputUser.md), \];<a name="botCommandScopePeerUser"></a>  

***
<br><br>[$botCommandScopeUsers](../constructors/botCommandScopeUsers.md) = \[\];<a name="botCommandScopeUsers"></a>  

***
<br><br>[$botInfo](../constructors/botInfo.md) = \['user_id' => [long](../types/long.md), 'description' => [string](../types/string.md), 'commands' => \[[BotCommand](../types/BotCommand.md)\], \];<a name="botInfo"></a>  

***
<br><br>[$botInlineMediaResult](../constructors/botInlineMediaResult.md) = \['id' => [string](../types/string.md), 'type' => [string](../types/string.md), 'photo' => [Photo](../types/Photo.md), 'document' => [Document](../types/Document.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'send_message' => [BotInlineMessage](../types/BotInlineMessage.md), \];<a name="botInlineMediaResult"></a>  

***
<br><br>[$botInlineMessageMediaAuto](../constructors/botInlineMessageMediaAuto.md) = \['message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="botInlineMessageMediaAuto"></a>  

***
<br><br>[$botInlineMessageMediaContact](../constructors/botInlineMessageMediaContact.md) = \['phone_number' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'vcard' => [string](../types/string.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="botInlineMessageMediaContact"></a>  

***
<br><br>[$botInlineMessageMediaGeo](../constructors/botInlineMessageMediaGeo.md) = \['geo' => [GeoPoint](../types/GeoPoint.md), 'heading' => [int](../types/int.md), 'period' => [int](../types/int.md), 'proximity_notification_radius' => [int](../types/int.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="botInlineMessageMediaGeo"></a>  

***
<br><br>[$botInlineMessageMediaInvoice](../constructors/botInlineMessageMediaInvoice.md) = \['shipping_address_requested' => [Bool](../types/Bool.md), 'test' => [Bool](../types/Bool.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'photo' => [WebDocument](../types/WebDocument.md), 'currency' => [string](../types/string.md), 'total_amount' => [long](../types/long.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="botInlineMessageMediaInvoice"></a>  

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
<br><br>[$channel](../constructors/channel.md) = \['creator' => [Bool](../types/Bool.md), 'left' => [Bool](../types/Bool.md), 'broadcast' => [Bool](../types/Bool.md), 'verified' => [Bool](../types/Bool.md), 'megagroup' => [Bool](../types/Bool.md), 'restricted' => [Bool](../types/Bool.md), 'signatures' => [Bool](../types/Bool.md), 'min' => [Bool](../types/Bool.md), 'scam' => [Bool](../types/Bool.md), 'has_link' => [Bool](../types/Bool.md), 'has_geo' => [Bool](../types/Bool.md), 'slowmode_enabled' => [Bool](../types/Bool.md), 'call_active' => [Bool](../types/Bool.md), 'call_not_empty' => [Bool](../types/Bool.md), 'fake' => [Bool](../types/Bool.md), 'gigagroup' => [Bool](../types/Bool.md), 'noforwards' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'title' => [string](../types/string.md), 'username' => [string](../types/string.md), 'photo' => [ChatPhoto](../types/ChatPhoto.md), 'date' => [int](../types/int.md), 'restriction_reason' => \[[RestrictionReason](../types/RestrictionReason.md)\], 'admin_rights' => [ChatAdminRights](../types/ChatAdminRights.md), 'banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), 'default_banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), 'participants_count' => [int](../types/int.md), \];<a name="channel"></a>  

***
<br><br>[$channelAdminLogEvent](../constructors/channelAdminLogEvent.md) = \['id' => [long](../types/long.md), 'date' => [int](../types/int.md), 'user_id' => [long](../types/long.md), 'action' => [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md), \];<a name="channelAdminLogEvent"></a>  

***
<br><br>[$channelAdminLogEventActionChangeAbout](../constructors/channelAdminLogEventActionChangeAbout.md) = \['prev_value' => [string](../types/string.md), 'new_value' => [string](../types/string.md), \];<a name="channelAdminLogEventActionChangeAbout"></a>  

***
<br><br>[$channelAdminLogEventActionChangeAvailableReactions](../constructors/channelAdminLogEventActionChangeAvailableReactions.md) = \['prev_value' => \[[string](../types/string.md)\], 'new_value' => \[[string](../types/string.md)\], \];<a name="channelAdminLogEventActionChangeAvailableReactions"></a>  

***
<br><br>[$channelAdminLogEventActionChangeHistoryTTL](../constructors/channelAdminLogEventActionChangeHistoryTTL.md) = \['prev_value' => [int](../types/int.md), 'new_value' => [int](../types/int.md), \];<a name="channelAdminLogEventActionChangeHistoryTTL"></a>  

***
<br><br>[$channelAdminLogEventActionChangeLinkedChat](../constructors/channelAdminLogEventActionChangeLinkedChat.md) = \['prev_value' => [long](../types/long.md), 'new_value' => [long](../types/long.md), \];<a name="channelAdminLogEventActionChangeLinkedChat"></a>  

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
<br><br>[$channelAdminLogEventActionDiscardGroupCall](../constructors/channelAdminLogEventActionDiscardGroupCall.md) = \['call' => [InputGroupCall](../types/InputGroupCall.md), \];<a name="channelAdminLogEventActionDiscardGroupCall"></a>  

***
<br><br>[$channelAdminLogEventActionEditMessage](../constructors/channelAdminLogEventActionEditMessage.md) = \['prev_message' => [Message](../types/Message.md), 'new_message' => [Message](../types/Message.md), \];<a name="channelAdminLogEventActionEditMessage"></a>  

***
<br><br>[$channelAdminLogEventActionExportedInviteDelete](../constructors/channelAdminLogEventActionExportedInviteDelete.md) = \['invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), \];<a name="channelAdminLogEventActionExportedInviteDelete"></a>  

***
<br><br>[$channelAdminLogEventActionExportedInviteEdit](../constructors/channelAdminLogEventActionExportedInviteEdit.md) = \['prev_invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'new_invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), \];<a name="channelAdminLogEventActionExportedInviteEdit"></a>  

***
<br><br>[$channelAdminLogEventActionExportedInviteRevoke](../constructors/channelAdminLogEventActionExportedInviteRevoke.md) = \['invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), \];<a name="channelAdminLogEventActionExportedInviteRevoke"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantInvite](../constructors/channelAdminLogEventActionParticipantInvite.md) = \['participant' => [ChannelParticipant](../types/ChannelParticipant.md), \];<a name="channelAdminLogEventActionParticipantInvite"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantJoin](../constructors/channelAdminLogEventActionParticipantJoin.md) = \[\];<a name="channelAdminLogEventActionParticipantJoin"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantJoinByInvite](../constructors/channelAdminLogEventActionParticipantJoinByInvite.md) = \['invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), \];<a name="channelAdminLogEventActionParticipantJoinByInvite"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantJoinByRequest](../constructors/channelAdminLogEventActionParticipantJoinByRequest.md) = \['invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'approved_by' => [long](../types/long.md), \];<a name="channelAdminLogEventActionParticipantJoinByRequest"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantLeave](../constructors/channelAdminLogEventActionParticipantLeave.md) = \[\];<a name="channelAdminLogEventActionParticipantLeave"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantMute](../constructors/channelAdminLogEventActionParticipantMute.md) = \['participant' => [GroupCallParticipant](../types/GroupCallParticipant.md), \];<a name="channelAdminLogEventActionParticipantMute"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantToggleAdmin](../constructors/channelAdminLogEventActionParticipantToggleAdmin.md) = \['prev_participant' => [ChannelParticipant](../types/ChannelParticipant.md), 'new_participant' => [ChannelParticipant](../types/ChannelParticipant.md), \];<a name="channelAdminLogEventActionParticipantToggleAdmin"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantToggleBan](../constructors/channelAdminLogEventActionParticipantToggleBan.md) = \['prev_participant' => [ChannelParticipant](../types/ChannelParticipant.md), 'new_participant' => [ChannelParticipant](../types/ChannelParticipant.md), \];<a name="channelAdminLogEventActionParticipantToggleBan"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantUnmute](../constructors/channelAdminLogEventActionParticipantUnmute.md) = \['participant' => [GroupCallParticipant](../types/GroupCallParticipant.md), \];<a name="channelAdminLogEventActionParticipantUnmute"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantVolume](../constructors/channelAdminLogEventActionParticipantVolume.md) = \['participant' => [GroupCallParticipant](../types/GroupCallParticipant.md), \];<a name="channelAdminLogEventActionParticipantVolume"></a>  

***
<br><br>[$channelAdminLogEventActionSendMessage](../constructors/channelAdminLogEventActionSendMessage.md) = \['message' => [Message](../types/Message.md), \];<a name="channelAdminLogEventActionSendMessage"></a>  

***
<br><br>[$channelAdminLogEventActionStartGroupCall](../constructors/channelAdminLogEventActionStartGroupCall.md) = \['call' => [InputGroupCall](../types/InputGroupCall.md), \];<a name="channelAdminLogEventActionStartGroupCall"></a>  

***
<br><br>[$channelAdminLogEventActionStopPoll](../constructors/channelAdminLogEventActionStopPoll.md) = \['message' => [Message](../types/Message.md), \];<a name="channelAdminLogEventActionStopPoll"></a>  

***
<br><br>[$channelAdminLogEventActionToggleGroupCallSetting](../constructors/channelAdminLogEventActionToggleGroupCallSetting.md) = \['join_muted' => [Bool](../types/Bool.md), \];<a name="channelAdminLogEventActionToggleGroupCallSetting"></a>  

***
<br><br>[$channelAdminLogEventActionToggleInvites](../constructors/channelAdminLogEventActionToggleInvites.md) = \['new_value' => [Bool](../types/Bool.md), \];<a name="channelAdminLogEventActionToggleInvites"></a>  

***
<br><br>[$channelAdminLogEventActionToggleNoForwards](../constructors/channelAdminLogEventActionToggleNoForwards.md) = \['new_value' => [Bool](../types/Bool.md), \];<a name="channelAdminLogEventActionToggleNoForwards"></a>  

***
<br><br>[$channelAdminLogEventActionTogglePreHistoryHidden](../constructors/channelAdminLogEventActionTogglePreHistoryHidden.md) = \['new_value' => [Bool](../types/Bool.md), \];<a name="channelAdminLogEventActionTogglePreHistoryHidden"></a>  

***
<br><br>[$channelAdminLogEventActionToggleSignatures](../constructors/channelAdminLogEventActionToggleSignatures.md) = \['new_value' => [Bool](../types/Bool.md), \];<a name="channelAdminLogEventActionToggleSignatures"></a>  

***
<br><br>[$channelAdminLogEventActionToggleSlowMode](../constructors/channelAdminLogEventActionToggleSlowMode.md) = \['prev_value' => [int](../types/int.md), 'new_value' => [int](../types/int.md), \];<a name="channelAdminLogEventActionToggleSlowMode"></a>  

***
<br><br>[$channelAdminLogEventActionUpdatePinned](../constructors/channelAdminLogEventActionUpdatePinned.md) = \['message' => [Message](../types/Message.md), \];<a name="channelAdminLogEventActionUpdatePinned"></a>  

***
<br><br>[$channelAdminLogEventsFilter](../constructors/channelAdminLogEventsFilter.md) = \['join' => [Bool](../types/Bool.md), 'leave' => [Bool](../types/Bool.md), 'invite' => [Bool](../types/Bool.md), 'ban' => [Bool](../types/Bool.md), 'unban' => [Bool](../types/Bool.md), 'kick' => [Bool](../types/Bool.md), 'unkick' => [Bool](../types/Bool.md), 'promote' => [Bool](../types/Bool.md), 'demote' => [Bool](../types/Bool.md), 'info' => [Bool](../types/Bool.md), 'settings' => [Bool](../types/Bool.md), 'pinned' => [Bool](../types/Bool.md), 'edit' => [Bool](../types/Bool.md), 'delete' => [Bool](../types/Bool.md), 'group_call' => [Bool](../types/Bool.md), 'invites' => [Bool](../types/Bool.md), 'send' => [Bool](../types/Bool.md), \];<a name="channelAdminLogEventsFilter"></a>  

***
<br><br>[$channelForbidden](../constructors/channelForbidden.md) = \['broadcast' => [Bool](../types/Bool.md), 'megagroup' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'title' => [string](../types/string.md), 'until_date' => [int](../types/int.md), \];<a name="channelForbidden"></a>  

***
<br><br>[$channelFull](../constructors/channelFull.md) = \['can_view_participants' => [Bool](../types/Bool.md), 'can_set_username' => [Bool](../types/Bool.md), 'can_set_stickers' => [Bool](../types/Bool.md), 'hidden_prehistory' => [Bool](../types/Bool.md), 'can_set_location' => [Bool](../types/Bool.md), 'has_scheduled' => [Bool](../types/Bool.md), 'can_view_stats' => [Bool](../types/Bool.md), 'blocked' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'about' => [string](../types/string.md), 'participants_count' => [int](../types/int.md), 'admins_count' => [int](../types/int.md), 'kicked_count' => [int](../types/int.md), 'banned_count' => [int](../types/int.md), 'online_count' => [int](../types/int.md), 'read_inbox_max_id' => [int](../types/int.md), 'read_outbox_max_id' => [int](../types/int.md), 'unread_count' => [int](../types/int.md), 'chat_photo' => [Photo](../types/Photo.md), 'notify_settings' => [PeerNotifySettings](../types/PeerNotifySettings.md), 'exported_invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'bot_info' => \[[BotInfo](../types/BotInfo.md)\], 'migrated_from_chat_id' => [long](../types/long.md), 'migrated_from_max_id' => [int](../types/int.md), 'pinned_msg_id' => [int](../types/int.md), 'stickerset' => [StickerSet](../types/StickerSet.md), 'available_min_id' => [int](../types/int.md), 'folder_id' => [int](../types/int.md), 'linked_chat_id' => [long](../types/long.md), 'location' => [ChannelLocation](../types/ChannelLocation.md), 'slowmode_seconds' => [int](../types/int.md), 'slowmode_next_send_date' => [int](../types/int.md), 'stats_dc' => [int](../types/int.md), 'pts' => [int](../types/int.md), 'call' => [InputGroupCall](../types/InputGroupCall.md), 'ttl_period' => [int](../types/int.md), 'pending_suggestions' => \[[string](../types/string.md)\], 'groupcall_default_join_as' => [Peer](../types/Peer.md), 'theme_emoticon' => [string](../types/string.md), 'requests_pending' => [int](../types/int.md), 'recent_requesters' => \[[long](../types/long.md)\], 'default_send_as' => [Peer](../types/Peer.md), 'available_reactions' => \[[string](../types/string.md)\], \];<a name="channelFull"></a>  

***
<br><br>[$channelLocation](../constructors/channelLocation.md) = \['geo_point' => [GeoPoint](../types/GeoPoint.md), 'address' => [string](../types/string.md), \];<a name="channelLocation"></a>  

***
<br><br>[$channelLocationEmpty](../constructors/channelLocationEmpty.md) = \[\];<a name="channelLocationEmpty"></a>  

***
<br><br>[$channelMessagesFilter](../constructors/channelMessagesFilter.md) = \['exclude_new_messages' => [Bool](../types/Bool.md), 'ranges' => \[[MessageRange](../types/MessageRange.md)\], \];<a name="channelMessagesFilter"></a>  

***
<br><br>[$channelMessagesFilterEmpty](../constructors/channelMessagesFilterEmpty.md) = \[\];<a name="channelMessagesFilterEmpty"></a>  

***
<br><br>[$channelParticipant](../constructors/channelParticipant.md) = \['user_id' => [long](../types/long.md), 'date' => [int](../types/int.md), \];<a name="channelParticipant"></a>  

***
<br><br>[$channelParticipantAdmin](../constructors/channelParticipantAdmin.md) = \['can_edit' => [Bool](../types/Bool.md), 'self' => [Bool](../types/Bool.md), 'user_id' => [long](../types/long.md), 'inviter_id' => [long](../types/long.md), 'promoted_by' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_rights' => [ChatAdminRights](../types/ChatAdminRights.md), 'rank' => [string](../types/string.md), \];<a name="channelParticipantAdmin"></a>  

***
<br><br>[$channelParticipantBanned](../constructors/channelParticipantBanned.md) = \['left' => [Bool](../types/Bool.md), 'peer' => [Peer](../types/Peer.md), 'kicked_by' => [long](../types/long.md), 'date' => [int](../types/int.md), 'banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), \];<a name="channelParticipantBanned"></a>  

***
<br><br>[$channelParticipantCreator](../constructors/channelParticipantCreator.md) = \['user_id' => [long](../types/long.md), 'admin_rights' => [ChatAdminRights](../types/ChatAdminRights.md), 'rank' => [string](../types/string.md), \];<a name="channelParticipantCreator"></a>  

***
<br><br>[$channelParticipantLeft](../constructors/channelParticipantLeft.md) = \['peer' => [Peer](../types/Peer.md), \];<a name="channelParticipantLeft"></a>  

***
<br><br>[$channelParticipantSelf](../constructors/channelParticipantSelf.md) = \['via_request' => [Bool](../types/Bool.md), 'user_id' => [long](../types/long.md), 'inviter_id' => [long](../types/long.md), 'date' => [int](../types/int.md), \];<a name="channelParticipantSelf"></a>  

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
<br><br>[$channelParticipantsMentions](../constructors/channelParticipantsMentions.md) = \['q' => [string](../types/string.md), 'top_msg_id' => [int](../types/int.md), \];<a name="channelParticipantsMentions"></a>  

***
<br><br>[$channelParticipantsRecent](../constructors/channelParticipantsRecent.md) = \[\];<a name="channelParticipantsRecent"></a>  

***
<br><br>[$channelParticipantsSearch](../constructors/channelParticipantsSearch.md) = \['q' => [string](../types/string.md), \];<a name="channelParticipantsSearch"></a>  

***
<br><br>[$channels.adminLogResults](../constructors/channels.adminLogResults.md) = \['events' => \[[ChannelAdminLogEvent](../types/ChannelAdminLogEvent.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="channels.adminLogResults"></a>  

***
<br><br>[$channels.channelParticipant](../constructors/channels.channelParticipant.md) = \['participant' => [ChannelParticipant](../types/ChannelParticipant.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="channels.channelParticipant"></a>  

***
<br><br>[$channels.channelParticipants](../constructors/channels.channelParticipants.md) = \['count' => [int](../types/int.md), 'participants' => \[[ChannelParticipant](../types/ChannelParticipant.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="channels.channelParticipants"></a>  

***
<br><br>[$channels.channelParticipantsNotModified](../constructors/channels.channelParticipantsNotModified.md) = \[\];<a name="channels.channelParticipantsNotModified"></a>  

***
<br><br>[$channels.sendAsPeers](../constructors/channels.sendAsPeers.md) = \['peers' => \[[Peer](../types/Peer.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="channels.sendAsPeers"></a>  

***
<br><br>[$chat](../constructors/chat.md) = \['creator' => [Bool](../types/Bool.md), 'kicked' => [Bool](../types/Bool.md), 'left' => [Bool](../types/Bool.md), 'deactivated' => [Bool](../types/Bool.md), 'call_active' => [Bool](../types/Bool.md), 'call_not_empty' => [Bool](../types/Bool.md), 'noforwards' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'title' => [string](../types/string.md), 'photo' => [ChatPhoto](../types/ChatPhoto.md), 'participants_count' => [int](../types/int.md), 'date' => [int](../types/int.md), 'version' => [int](../types/int.md), 'migrated_to' => [InputChannel](../types/InputChannel.md), 'admin_rights' => [ChatAdminRights](../types/ChatAdminRights.md), 'default_banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), \];<a name="chat"></a>  

***
<br><br>[$chatAdminRights](../constructors/chatAdminRights.md) = \['change_info' => [Bool](../types/Bool.md), 'post_messages' => [Bool](../types/Bool.md), 'edit_messages' => [Bool](../types/Bool.md), 'delete_messages' => [Bool](../types/Bool.md), 'ban_users' => [Bool](../types/Bool.md), 'invite_users' => [Bool](../types/Bool.md), 'pin_messages' => [Bool](../types/Bool.md), 'add_admins' => [Bool](../types/Bool.md), 'anonymous' => [Bool](../types/Bool.md), 'manage_call' => [Bool](../types/Bool.md), 'other' => [Bool](../types/Bool.md), \];<a name="chatAdminRights"></a>  

***
<br><br>[$chatAdminWithInvites](../constructors/chatAdminWithInvites.md) = \['admin_id' => [long](../types/long.md), 'invites_count' => [int](../types/int.md), 'revoked_invites_count' => [int](../types/int.md), \];<a name="chatAdminWithInvites"></a>  

***
<br><br>[$chatBannedRights](../constructors/chatBannedRights.md) = \['view_messages' => [Bool](../types/Bool.md), 'send_messages' => [Bool](../types/Bool.md), 'send_media' => [Bool](../types/Bool.md), 'send_stickers' => [Bool](../types/Bool.md), 'send_gifs' => [Bool](../types/Bool.md), 'send_games' => [Bool](../types/Bool.md), 'send_inline' => [Bool](../types/Bool.md), 'embed_links' => [Bool](../types/Bool.md), 'send_polls' => [Bool](../types/Bool.md), 'change_info' => [Bool](../types/Bool.md), 'invite_users' => [Bool](../types/Bool.md), 'pin_messages' => [Bool](../types/Bool.md), 'until_date' => [int](../types/int.md), \];<a name="chatBannedRights"></a>  

***
<br><br>[$chatEmpty](../constructors/chatEmpty.md) = \['id' => [long](../types/long.md), \];<a name="chatEmpty"></a>  

***
<br><br>[$chatForbidden](../constructors/chatForbidden.md) = \['id' => [long](../types/long.md), 'title' => [string](../types/string.md), \];<a name="chatForbidden"></a>  

***
<br><br>[$chatFull](../constructors/chatFull.md) = \['can_set_username' => [Bool](../types/Bool.md), 'has_scheduled' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'about' => [string](../types/string.md), 'participants' => [ChatParticipants](../types/ChatParticipants.md), 'chat_photo' => [Photo](../types/Photo.md), 'notify_settings' => [PeerNotifySettings](../types/PeerNotifySettings.md), 'exported_invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'bot_info' => \[[BotInfo](../types/BotInfo.md)\], 'pinned_msg_id' => [int](../types/int.md), 'folder_id' => [int](../types/int.md), 'call' => [InputGroupCall](../types/InputGroupCall.md), 'ttl_period' => [int](../types/int.md), 'groupcall_default_join_as' => [Peer](../types/Peer.md), 'theme_emoticon' => [string](../types/string.md), 'requests_pending' => [int](../types/int.md), 'recent_requesters' => \[[long](../types/long.md)\], 'available_reactions' => \[[string](../types/string.md)\], \];<a name="chatFull"></a>  

***
<br><br>[$chatInvite](../constructors/chatInvite.md) = \['channel' => [Bool](../types/Bool.md), 'broadcast' => [Bool](../types/Bool.md), 'public' => [Bool](../types/Bool.md), 'megagroup' => [Bool](../types/Bool.md), 'request_needed' => [Bool](../types/Bool.md), 'title' => [string](../types/string.md), 'about' => [string](../types/string.md), 'photo' => [Photo](../types/Photo.md), 'participants_count' => [int](../types/int.md), 'participants' => \[[User](../types/User.md)\], \];<a name="chatInvite"></a>  

***
<br><br>[$chatInviteAlready](../constructors/chatInviteAlready.md) = \['chat' => [Chat](../types/Chat.md), \];<a name="chatInviteAlready"></a>  

***
<br><br>[$chatInviteExported](../constructors/chatInviteExported.md) = \['revoked' => [Bool](../types/Bool.md), 'permanent' => [Bool](../types/Bool.md), 'request_needed' => [Bool](../types/Bool.md), 'link' => [string](../types/string.md), 'admin_id' => [long](../types/long.md), 'date' => [int](../types/int.md), 'start_date' => [int](../types/int.md), 'expire_date' => [int](../types/int.md), 'usage_limit' => [int](../types/int.md), 'usage' => [int](../types/int.md), 'requested' => [int](../types/int.md), 'title' => [string](../types/string.md), \];<a name="chatInviteExported"></a>  

***
<br><br>[$chatInviteImporter](../constructors/chatInviteImporter.md) = \['requested' => [Bool](../types/Bool.md), 'user_id' => [long](../types/long.md), 'date' => [int](../types/int.md), 'about' => [string](../types/string.md), 'approved_by' => [long](../types/long.md), \];<a name="chatInviteImporter"></a>  

***
<br><br>[$chatInvitePeek](../constructors/chatInvitePeek.md) = \['chat' => [Chat](../types/Chat.md), 'expires' => [int](../types/int.md), \];<a name="chatInvitePeek"></a>  

***
<br><br>[$chatOnlines](../constructors/chatOnlines.md) = \['onlines' => [int](../types/int.md), \];<a name="chatOnlines"></a>  

***
<br><br>[$chatParticipant](../constructors/chatParticipant.md) = \['user_id' => [long](../types/long.md), 'inviter_id' => [long](../types/long.md), 'date' => [int](../types/int.md), \];<a name="chatParticipant"></a>  

***
<br><br>[$chatParticipantAdmin](../constructors/chatParticipantAdmin.md) = \['user_id' => [long](../types/long.md), 'inviter_id' => [long](../types/long.md), 'date' => [int](../types/int.md), \];<a name="chatParticipantAdmin"></a>  

***
<br><br>[$chatParticipantCreator](../constructors/chatParticipantCreator.md) = \['user_id' => [long](../types/long.md), \];<a name="chatParticipantCreator"></a>  

***
<br><br>[$chatParticipants](../constructors/chatParticipants.md) = \['chat_id' => [long](../types/long.md), 'participants' => \[[ChatParticipant](../types/ChatParticipant.md)\], 'version' => [int](../types/int.md), \];<a name="chatParticipants"></a>  

***
<br><br>[$chatParticipantsForbidden](../constructors/chatParticipantsForbidden.md) = \['chat_id' => [long](../types/long.md), 'self_participant' => [ChatParticipant](../types/ChatParticipant.md), \];<a name="chatParticipantsForbidden"></a>  

***
<br><br>[$chatPhoto](../constructors/chatPhoto.md) = \['has_video' => [Bool](../types/Bool.md), 'photo_id' => [long](../types/long.md), 'stripped_thumb' => [bytes](../types/bytes.md), 'dc_id' => [int](../types/int.md), \];<a name="chatPhoto"></a>  

***
<br><br>[$chatPhotoEmpty](../constructors/chatPhotoEmpty.md) = \[\];<a name="chatPhotoEmpty"></a>  

***
<br><br>[$codeSettings](../constructors/codeSettings.md) = \['allow_flashcall' => [Bool](../types/Bool.md), 'current_number' => [Bool](../types/Bool.md), 'allow_app_hash' => [Bool](../types/Bool.md), 'allow_missed_call' => [Bool](../types/Bool.md), 'logout_tokens' => \[[bytes](../types/bytes.md)\], \];<a name="codeSettings"></a>  

***
<br><br>[$config](../constructors/config.md) = \['phonecalls_enabled' => [Bool](../types/Bool.md), 'default_p2p_contacts' => [Bool](../types/Bool.md), 'preload_featured_stickers' => [Bool](../types/Bool.md), 'ignore_phone_entities' => [Bool](../types/Bool.md), 'revoke_pm_inbox' => [Bool](../types/Bool.md), 'blocked_mode' => [Bool](../types/Bool.md), 'pfs_enabled' => [Bool](../types/Bool.md), 'date' => [int](../types/int.md), 'expires' => [int](../types/int.md), 'test_mode' => [Bool](../types/Bool.md), 'this_dc' => [int](../types/int.md), 'dc_options' => \[[DcOption](../types/DcOption.md)\], 'dc_txt_domain_name' => [string](../types/string.md), 'chat_size_max' => [int](../types/int.md), 'megagroup_size_max' => [int](../types/int.md), 'forwarded_count_max' => [int](../types/int.md), 'online_update_period_ms' => [int](../types/int.md), 'offline_blur_timeout_ms' => [int](../types/int.md), 'offline_idle_timeout_ms' => [int](../types/int.md), 'online_cloud_timeout_ms' => [int](../types/int.md), 'notify_cloud_delay_ms' => [int](../types/int.md), 'notify_default_delay_ms' => [int](../types/int.md), 'push_chat_period_ms' => [int](../types/int.md), 'push_chat_limit' => [int](../types/int.md), 'saved_gifs_limit' => [int](../types/int.md), 'edit_time_limit' => [int](../types/int.md), 'revoke_time_limit' => [int](../types/int.md), 'revoke_pm_time_limit' => [int](../types/int.md), 'rating_e_decay' => [int](../types/int.md), 'stickers_recent_limit' => [int](../types/int.md), 'stickers_faved_limit' => [int](../types/int.md), 'channels_read_media_period' => [int](../types/int.md), 'tmp_sessions' => [int](../types/int.md), 'pinned_dialogs_count_max' => [int](../types/int.md), 'pinned_infolder_count_max' => [int](../types/int.md), 'call_receive_timeout_ms' => [int](../types/int.md), 'call_ring_timeout_ms' => [int](../types/int.md), 'call_connect_timeout_ms' => [int](../types/int.md), 'call_packet_timeout_ms' => [int](../types/int.md), 'me_url_prefix' => [string](../types/string.md), 'autoupdate_url_prefix' => [string](../types/string.md), 'gif_search_username' => [string](../types/string.md), 'venue_search_username' => [string](../types/string.md), 'img_search_username' => [string](../types/string.md), 'static_maps_provider' => [string](../types/string.md), 'caption_length_max' => [int](../types/int.md), 'message_length_max' => [int](../types/int.md), 'webfile_dc_id' => [int](../types/int.md), 'suggested_lang_code' => [string](../types/string.md), 'lang_pack_version' => [int](../types/int.md), 'base_lang_pack_version' => [int](../types/int.md), \];<a name="config"></a>  

***
<br><br>[$contact](../constructors/contact.md) = \['user_id' => [long](../types/long.md), 'mutual' => [Bool](../types/Bool.md), \];<a name="contact"></a>  

***
<br><br>[$contactStatus](../constructors/contactStatus.md) = \['user_id' => [long](../types/long.md), 'status' => [UserStatus](../types/UserStatus.md), \];<a name="contactStatus"></a>  

***
<br><br>[$contacts.blocked](../constructors/contacts.blocked.md) = \['blocked' => \[[PeerBlocked](../types/PeerBlocked.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts.blocked"></a>  

***
<br><br>[$contacts.blockedSlice](../constructors/contacts.blockedSlice.md) = \['count' => [int](../types/int.md), 'blocked' => \[[PeerBlocked](../types/PeerBlocked.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts.blockedSlice"></a>  

***
<br><br>[$contacts.contacts](../constructors/contacts.contacts.md) = \['contacts' => \[[Contact](../types/Contact.md)\], 'saved_count' => [int](../types/int.md), 'users' => \[[User](../types/User.md)\], \];<a name="contacts.contacts"></a>  

***
<br><br>[$contacts.contactsNotModified](../constructors/contacts.contactsNotModified.md) = \[\];<a name="contacts.contactsNotModified"></a>  

***
<br><br>[$contacts.found](../constructors/contacts.found.md) = \['my_results' => \[[Peer](../types/Peer.md)\], 'results' => \[[Peer](../types/Peer.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts.found"></a>  

***
<br><br>[$contacts.importedContacts](../constructors/contacts.importedContacts.md) = \['imported' => \[[ImportedContact](../types/ImportedContact.md)\], 'popular_invites' => \[[PopularContact](../types/PopularContact.md)\], 'retry_contacts' => \[[long](../types/long.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts.importedContacts"></a>  

***
<br><br>[$contacts.resolvedPeer](../constructors/contacts.resolvedPeer.md) = \['peer' => [Peer](../types/Peer.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts.resolvedPeer"></a>  

***
<br><br>[$contacts.topPeers](../constructors/contacts.topPeers.md) = \['categories' => \[[TopPeerCategoryPeers](../types/TopPeerCategoryPeers.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="contacts.topPeers"></a>  

***
<br><br>[$contacts.topPeersDisabled](../constructors/contacts.topPeersDisabled.md) = \[\];<a name="contacts.topPeersDisabled"></a>  

***
<br><br>[$contacts.topPeersNotModified](../constructors/contacts.topPeersNotModified.md) = \[\];<a name="contacts.topPeersNotModified"></a>  

***
<br><br>[$dataJSON](../constructors/dataJSON.md) = \['data' => [string](../types/string.md), \];<a name="dataJSON"></a>  

***
<br><br>[$dcOption](../constructors/dcOption.md) = \['ipv6' => [Bool](../types/Bool.md), 'media_only' => [Bool](../types/Bool.md), 'tcpo_only' => [Bool](../types/Bool.md), 'cdn' => [Bool](../types/Bool.md), 'static' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'ip_address' => [string](../types/string.md), 'port' => [int](../types/int.md), 'secret' => [bytes](../types/bytes.md), \];<a name="dcOption"></a>  

***
<br><br>[$decryptedMessage\_73](../constructors/decryptedMessage_73.md) = \['ttl' => [int](../types/int.md), 'message' => [string](../types/string.md), 'media' => [DecryptedMessageMedia](../types/DecryptedMessageMedia.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'via_bot_name' => [string](../types/string.md), 'reply_to_random_id' => [long](../types/long.md), 'grouped_id' => [long](../types/long.md), \];<a name="decryptedMessage_73"></a>  

***
<br><br>[$decryptedMessageActionAbortKey\_20](../constructors/decryptedMessageActionAbortKey_20.md) = \['exchange_id' => [long](../types/long.md), \];<a name="decryptedMessageActionAbortKey_20"></a>  

***
<br><br>[$decryptedMessageActionAcceptKey\_20](../constructors/decryptedMessageActionAcceptKey_20.md) = \['exchange_id' => [long](../types/long.md), 'g_b' => [bytes](../types/bytes.md), 'key_fingerprint' => [long](../types/long.md), \];<a name="decryptedMessageActionAcceptKey_20"></a>  

***
<br><br>[$decryptedMessageActionCommitKey\_20](../constructors/decryptedMessageActionCommitKey_20.md) = \['exchange_id' => [long](../types/long.md), 'key_fingerprint' => [long](../types/long.md), \];<a name="decryptedMessageActionCommitKey_20"></a>  

***
<br><br>[$decryptedMessageActionDeleteMessages\_8](../constructors/decryptedMessageActionDeleteMessages_8.md) = \['random_ids' => \[[long](../types/long.md)\], \];<a name="decryptedMessageActionDeleteMessages_8"></a>  

***
<br><br>[$decryptedMessageActionFlushHistory\_8](../constructors/decryptedMessageActionFlushHistory_8.md) = \[\];<a name="decryptedMessageActionFlushHistory_8"></a>  

***
<br><br>[$decryptedMessageActionNoop\_20](../constructors/decryptedMessageActionNoop_20.md) = \[\];<a name="decryptedMessageActionNoop_20"></a>  

***
<br><br>[$decryptedMessageActionNotifyLayer\_17](../constructors/decryptedMessageActionNotifyLayer_17.md) = \['layer' => [int](../types/int.md), \];<a name="decryptedMessageActionNotifyLayer_17"></a>  

***
<br><br>[$decryptedMessageActionReadMessages\_8](../constructors/decryptedMessageActionReadMessages_8.md) = \['random_ids' => \[[long](../types/long.md)\], \];<a name="decryptedMessageActionReadMessages_8"></a>  

***
<br><br>[$decryptedMessageActionRequestKey\_20](../constructors/decryptedMessageActionRequestKey_20.md) = \['exchange_id' => [long](../types/long.md), 'g_a' => [bytes](../types/bytes.md), \];<a name="decryptedMessageActionRequestKey_20"></a>  

***
<br><br>[$decryptedMessageActionResend\_17](../constructors/decryptedMessageActionResend_17.md) = \['start_seq_no' => [int](../types/int.md), 'end_seq_no' => [int](../types/int.md), \];<a name="decryptedMessageActionResend_17"></a>  

***
<br><br>[$decryptedMessageActionScreenshotMessages\_8](../constructors/decryptedMessageActionScreenshotMessages_8.md) = \['random_ids' => \[[long](../types/long.md)\], \];<a name="decryptedMessageActionScreenshotMessages_8"></a>  

***
<br><br>[$decryptedMessageActionSetMessageTTL\_8](../constructors/decryptedMessageActionSetMessageTTL_8.md) = \['ttl_seconds' => [int](../types/int.md), \];<a name="decryptedMessageActionSetMessageTTL_8"></a>  

***
<br><br>[$decryptedMessageActionTyping\_17](../constructors/decryptedMessageActionTyping_17.md) = \['action' => [SendMessageAction](../types/SendMessageAction.md), \];<a name="decryptedMessageActionTyping_17"></a>  

***
<br><br>[$decryptedMessageLayer\_17](../constructors/decryptedMessageLayer_17.md) = \['layer' => [int](../types/int.md), 'in_seq_no' => [int](../types/int.md), 'out_seq_no' => [int](../types/int.md), 'message' => [DecryptedMessage](../types/DecryptedMessage.md), \];<a name="decryptedMessageLayer_17"></a>  

***
<br><br>[$decryptedMessageMediaAudio\_17](../constructors/decryptedMessageMediaAudio_17.md) = \['duration' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'size' => [int](../types/int.md), 'key' => [bytes](../types/bytes.md), 'iv' => [bytes](../types/bytes.md), \];<a name="decryptedMessageMediaAudio_17"></a>  

***
<br><br>[$decryptedMessageMediaContact\_8](../constructors/decryptedMessageMediaContact_8.md) = \['phone_number' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'user_id' => [int](../types/int.md), \];<a name="decryptedMessageMediaContact_8"></a>  

***
<br><br>[$decryptedMessageMediaDocument\_45](../constructors/decryptedMessageMediaDocument_45.md) = \['thumb' => [bytes](../types/bytes.md), 'thumb_w' => [int](../types/int.md), 'thumb_h' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'size' => [int](../types/int.md), 'key' => [bytes](../types/bytes.md), 'iv' => [bytes](../types/bytes.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], 'caption' => [string](../types/string.md), \];<a name="decryptedMessageMediaDocument_45"></a>  

***
<br><br>[$decryptedMessageMediaEmpty\_8](../constructors/decryptedMessageMediaEmpty_8.md) = \[\];<a name="decryptedMessageMediaEmpty_8"></a>  

***
<br><br>[$decryptedMessageMediaExternalDocument\_23](../constructors/decryptedMessageMediaExternalDocument_23.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'size' => [int](../types/int.md), 'thumb' => [PhotoSize](../types/PhotoSize.md), 'dc_id' => [int](../types/int.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], \];<a name="decryptedMessageMediaExternalDocument_23"></a>  

***
<br><br>[$decryptedMessageMediaGeoPoint\_8](../constructors/decryptedMessageMediaGeoPoint_8.md) = \['lat' => [double](../types/double.md), 'long' => [double](../types/double.md), \];<a name="decryptedMessageMediaGeoPoint_8"></a>  

***
<br><br>[$decryptedMessageMediaPhoto\_45](../constructors/decryptedMessageMediaPhoto_45.md) = \['thumb' => [bytes](../types/bytes.md), 'thumb_w' => [int](../types/int.md), 'thumb_h' => [int](../types/int.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'size' => [int](../types/int.md), 'key' => [bytes](../types/bytes.md), 'iv' => [bytes](../types/bytes.md), 'caption' => [string](../types/string.md), \];<a name="decryptedMessageMediaPhoto_45"></a>  

***
<br><br>[$decryptedMessageMediaVenue\_46](../constructors/decryptedMessageMediaVenue_46.md) = \['lat' => [double](../types/double.md), 'long' => [double](../types/double.md), 'title' => [string](../types/string.md), 'address' => [string](../types/string.md), 'provider' => [string](../types/string.md), 'venue_id' => [string](../types/string.md), \];<a name="decryptedMessageMediaVenue_46"></a>  

***
<br><br>[$decryptedMessageMediaVideo\_45](../constructors/decryptedMessageMediaVideo_45.md) = \['thumb' => [bytes](../types/bytes.md), 'thumb_w' => [int](../types/int.md), 'thumb_h' => [int](../types/int.md), 'duration' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'size' => [int](../types/int.md), 'key' => [bytes](../types/bytes.md), 'iv' => [bytes](../types/bytes.md), 'caption' => [string](../types/string.md), \];<a name="decryptedMessageMediaVideo_45"></a>  

***
<br><br>[$decryptedMessageMediaWebPage\_46](../constructors/decryptedMessageMediaWebPage_46.md) = \['url' => [string](../types/string.md), \];<a name="decryptedMessageMediaWebPage_46"></a>  

***
<br><br>[$decryptedMessageService\_17](../constructors/decryptedMessageService_17.md) = \['action' => [DecryptedMessageAction](../types/DecryptedMessageAction.md), \];<a name="decryptedMessageService_17"></a>  

***
<br><br>[$dialog](../constructors/dialog.md) = \['pinned' => [Bool](../types/Bool.md), 'unread_mark' => [Bool](../types/Bool.md), 'peer' => [Peer](../types/Peer.md), 'top_message' => [int](../types/int.md), 'read_inbox_max_id' => [int](../types/int.md), 'read_outbox_max_id' => [int](../types/int.md), 'unread_count' => [int](../types/int.md), 'unread_mentions_count' => [int](../types/int.md), 'notify_settings' => [PeerNotifySettings](../types/PeerNotifySettings.md), 'pts' => [int](../types/int.md), 'draft' => [DraftMessage](../types/DraftMessage.md), 'folder_id' => [int](../types/int.md), \];<a name="dialog"></a>  

***
<br><br>[$dialogFilter](../constructors/dialogFilter.md) = \['contacts' => [Bool](../types/Bool.md), 'non_contacts' => [Bool](../types/Bool.md), 'groups' => [Bool](../types/Bool.md), 'broadcasts' => [Bool](../types/Bool.md), 'bots' => [Bool](../types/Bool.md), 'exclude_muted' => [Bool](../types/Bool.md), 'exclude_read' => [Bool](../types/Bool.md), 'exclude_archived' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'title' => [string](../types/string.md), 'emoticon' => [string](../types/string.md), 'pinned_peers' => \[[InputPeer](../types/InputPeer.md)\], 'include_peers' => \[[InputPeer](../types/InputPeer.md)\], 'exclude_peers' => \[[InputPeer](../types/InputPeer.md)\], \];<a name="dialogFilter"></a>  

***
<br><br>[$dialogFilterSuggested](../constructors/dialogFilterSuggested.md) = \['filter' => [DialogFilter](../types/DialogFilter.md), 'description' => [string](../types/string.md), \];<a name="dialogFilterSuggested"></a>  

***
<br><br>[$dialogFolder](../constructors/dialogFolder.md) = \['pinned' => [Bool](../types/Bool.md), 'folder' => [Folder](../types/Folder.md), 'peer' => [Peer](../types/Peer.md), 'top_message' => [int](../types/int.md), 'unread_muted_peers_count' => [int](../types/int.md), 'unread_unmuted_peers_count' => [int](../types/int.md), 'unread_muted_messages_count' => [int](../types/int.md), 'unread_unmuted_messages_count' => [int](../types/int.md), \];<a name="dialogFolder"></a>  

***
<br><br>[$dialogPeer](../constructors/dialogPeer.md) = \['peer' => [Peer](../types/Peer.md), \];<a name="dialogPeer"></a>  

***
<br><br>[$dialogPeerFolder](../constructors/dialogPeerFolder.md) = \['folder_id' => [int](../types/int.md), \];<a name="dialogPeerFolder"></a>  

***
<br><br>[$document](../constructors/document.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'file_reference' => [bytes](../types/bytes.md), 'date' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'size' => [int](../types/int.md), 'thumbs' => \[[PhotoSize](../types/PhotoSize.md)\], 'video_thumbs' => \[[VideoSize](../types/VideoSize.md)\], 'dc_id' => [int](../types/int.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], \];<a name="document"></a>  

***
<br><br>[$documentAttributeAnimated](../constructors/documentAttributeAnimated.md) = \[\];<a name="documentAttributeAnimated"></a>  

***
<br><br>[$documentAttributeAudio\_46](../constructors/documentAttributeAudio_46.md) = \['duration' => [int](../types/int.md), 'title' => [string](../types/string.md), 'performer' => [string](../types/string.md), \];<a name="documentAttributeAudio_46"></a>  

***
<br><br>[$documentAttributeFilename](../constructors/documentAttributeFilename.md) = \['file_name' => [string](../types/string.md), \];<a name="documentAttributeFilename"></a>  

***
<br><br>[$documentAttributeHasStickers](../constructors/documentAttributeHasStickers.md) = \[\];<a name="documentAttributeHasStickers"></a>  

***
<br><br>[$documentAttributeImageSize](../constructors/documentAttributeImageSize.md) = \['w' => [int](../types/int.md), 'h' => [int](../types/int.md), \];<a name="documentAttributeImageSize"></a>  

***
<br><br>[$documentAttributeSticker\_55](../constructors/documentAttributeSticker_55.md) = \['alt' => [string](../types/string.md), 'stickerset' => [InputStickerSet](../types/InputStickerSet.md), \];<a name="documentAttributeSticker_55"></a>  

***
<br><br>[$documentAttributeVideo\_23](../constructors/documentAttributeVideo_23.md) = \['duration' => [int](../types/int.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), \];<a name="documentAttributeVideo_23"></a>  

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
<br><br>[$encryptedChat](../constructors/encryptedChat.md) = \['id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [long](../types/long.md), 'participant_id' => [long](../types/long.md), 'g_a_or_b' => [bytes](../types/bytes.md), 'key_fingerprint' => [long](../types/long.md), \];<a name="encryptedChat"></a>  

***
<br><br>[$encryptedChatDiscarded](../constructors/encryptedChatDiscarded.md) = \['history_deleted' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), \];<a name="encryptedChatDiscarded"></a>  

***
<br><br>[$encryptedChatEmpty](../constructors/encryptedChatEmpty.md) = \['id' => [int](../types/int.md), \];<a name="encryptedChatEmpty"></a>  

***
<br><br>[$encryptedChatRequested](../constructors/encryptedChatRequested.md) = \['folder_id' => [int](../types/int.md), 'id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [long](../types/long.md), 'participant_id' => [long](../types/long.md), 'g_a' => [bytes](../types/bytes.md), \];<a name="encryptedChatRequested"></a>  

***
<br><br>[$encryptedChatWaiting](../constructors/encryptedChatWaiting.md) = \['id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [long](../types/long.md), 'participant_id' => [long](../types/long.md), \];<a name="encryptedChatWaiting"></a>  

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
<br><br>[$fileLocation\_23](../constructors/fileLocation_23.md) = \['dc_id' => [int](../types/int.md), 'volume_id' => [long](../types/long.md), 'local_id' => [int](../types/int.md), 'secret' => [long](../types/long.md), \];<a name="fileLocation_23"></a>  

***
<br><br>[$fileLocationUnavailable\_23](../constructors/fileLocationUnavailable_23.md) = \['volume_id' => [long](../types/long.md), 'local_id' => [int](../types/int.md), 'secret' => [long](../types/long.md), \];<a name="fileLocationUnavailable_23"></a>  

***
<br><br>[$folder](../constructors/folder.md) = \['autofill_new_broadcasts' => [Bool](../types/Bool.md), 'autofill_public_groups' => [Bool](../types/Bool.md), 'autofill_new_correspondents' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'title' => [string](../types/string.md), 'photo' => [ChatPhoto](../types/ChatPhoto.md), \];<a name="folder"></a>  

***
<br><br>[$folderPeer](../constructors/folderPeer.md) = \['peer' => [Peer](../types/Peer.md), 'folder_id' => [int](../types/int.md), \];<a name="folderPeer"></a>  

***
<br><br>[$game](../constructors/game.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'short_name' => [string](../types/string.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'photo' => [Photo](../types/Photo.md), 'document' => [Document](../types/Document.md), \];<a name="game"></a>  

***
<br><br>[$geoPoint](../constructors/geoPoint.md) = \['long' => [double](../types/double.md), 'lat' => [double](../types/double.md), 'access_hash' => [long](../types/long.md), 'accuracy_radius' => [int](../types/int.md), \];<a name="geoPoint"></a>  

***
<br><br>[$geoPointEmpty](../constructors/geoPointEmpty.md) = \[\];<a name="geoPointEmpty"></a>  

***
<br><br>[$globalPrivacySettings](../constructors/globalPrivacySettings.md) = \['archive_and_mute_new_noncontact_peers' => [Bool](../types/Bool.md), \];<a name="globalPrivacySettings"></a>  

***
<br><br>[$groupCall](../constructors/groupCall.md) = \['join_muted' => [Bool](../types/Bool.md), 'can_change_join_muted' => [Bool](../types/Bool.md), 'join_date_asc' => [Bool](../types/Bool.md), 'schedule_start_subscribed' => [Bool](../types/Bool.md), 'can_start_video' => [Bool](../types/Bool.md), 'record_video_active' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'participants_count' => [int](../types/int.md), 'title' => [string](../types/string.md), 'stream_dc_id' => [int](../types/int.md), 'record_start_date' => [int](../types/int.md), 'schedule_date' => [int](../types/int.md), 'unmuted_video_count' => [int](../types/int.md), 'unmuted_video_limit' => [int](../types/int.md), 'version' => [int](../types/int.md), \];<a name="groupCall"></a>  

***
<br><br>[$groupCallDiscarded](../constructors/groupCallDiscarded.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'duration' => [int](../types/int.md), \];<a name="groupCallDiscarded"></a>  

***
<br><br>[$groupCallParticipant](../constructors/groupCallParticipant.md) = \['muted' => [Bool](../types/Bool.md), 'left' => [Bool](../types/Bool.md), 'can_self_unmute' => [Bool](../types/Bool.md), 'just_joined' => [Bool](../types/Bool.md), 'versioned' => [Bool](../types/Bool.md), 'min' => [Bool](../types/Bool.md), 'muted_by_you' => [Bool](../types/Bool.md), 'volume_by_admin' => [Bool](../types/Bool.md), 'self' => [Bool](../types/Bool.md), 'video_joined' => [Bool](../types/Bool.md), 'peer' => [Peer](../types/Peer.md), 'date' => [int](../types/int.md), 'active_date' => [int](../types/int.md), 'source' => [int](../types/int.md), 'volume' => [int](../types/int.md), 'about' => [string](../types/string.md), 'raise_hand_rating' => [long](../types/long.md), 'video' => [GroupCallParticipantVideo](../types/GroupCallParticipantVideo.md), 'presentation' => [GroupCallParticipantVideo](../types/GroupCallParticipantVideo.md), \];<a name="groupCallParticipant"></a>  

***
<br><br>[$groupCallParticipantVideo](../constructors/groupCallParticipantVideo.md) = \['paused' => [Bool](../types/Bool.md), 'endpoint' => [string](../types/string.md), 'source_groups' => \[[GroupCallParticipantVideoSourceGroup](../types/GroupCallParticipantVideoSourceGroup.md)\], 'audio_source' => [int](../types/int.md), \];<a name="groupCallParticipantVideo"></a>  

***
<br><br>[$groupCallParticipantVideoSourceGroup](../constructors/groupCallParticipantVideoSourceGroup.md) = \['semantics' => [string](../types/string.md), 'sources' => \[[int](../types/int.md)\], \];<a name="groupCallParticipantVideoSourceGroup"></a>  

***
<br><br>[$help.appUpdate](../constructors/help.appUpdate.md) = \['can_not_skip' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'version' => [string](../types/string.md), 'text' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'document' => [Document](../types/Document.md), 'url' => [string](../types/string.md), 'sticker' => [Document](../types/Document.md), \];<a name="help.appUpdate"></a>  

***
<br><br>[$help.countriesList](../constructors/help.countriesList.md) = \['countries' => \[[help.Country](../types/help.Country.md)\], 'hash' => [int](../types/int.md), \];<a name="help.countriesList"></a>  

***
<br><br>[$help.countriesListNotModified](../constructors/help.countriesListNotModified.md) = \[\];<a name="help.countriesListNotModified"></a>  

***
<br><br>[$help.country](../constructors/help.country.md) = \['hidden' => [Bool](../types/Bool.md), 'iso2' => [string](../types/string.md), 'default_name' => [string](../types/string.md), 'name' => [string](../types/string.md), 'country_codes' => \[[help.CountryCode](../types/help.CountryCode.md)\], \];<a name="help.country"></a>  

***
<br><br>[$help.countryCode](../constructors/help.countryCode.md) = \['country_code' => [string](../types/string.md), 'prefixes' => \[[string](../types/string.md)\], 'patterns' => \[[string](../types/string.md)\], \];<a name="help.countryCode"></a>  

***
<br><br>[$help.deepLinkInfo](../constructors/help.deepLinkInfo.md) = \['update_app' => [Bool](../types/Bool.md), 'message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \];<a name="help.deepLinkInfo"></a>  

***
<br><br>[$help.deepLinkInfoEmpty](../constructors/help.deepLinkInfoEmpty.md) = \[\];<a name="help.deepLinkInfoEmpty"></a>  

***
<br><br>[$help.inviteText](../constructors/help.inviteText.md) = \['message' => [string](../types/string.md), \];<a name="help.inviteText"></a>  

***
<br><br>[$help.noAppUpdate](../constructors/help.noAppUpdate.md) = \[\];<a name="help.noAppUpdate"></a>  

***
<br><br>[$help.passportConfig](../constructors/help.passportConfig.md) = \['hash' => [int](../types/int.md), 'countries_langs' => [DataJSON](../types/DataJSON.md), \];<a name="help.passportConfig"></a>  

***
<br><br>[$help.passportConfigNotModified](../constructors/help.passportConfigNotModified.md) = \[\];<a name="help.passportConfigNotModified"></a>  

***
<br><br>[$help.promoData](../constructors/help.promoData.md) = \['proxy' => [Bool](../types/Bool.md), 'expires' => [int](../types/int.md), 'peer' => [Peer](../types/Peer.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], 'psa_type' => [string](../types/string.md), 'psa_message' => [string](../types/string.md), \];<a name="help.promoData"></a>  

***
<br><br>[$help.promoDataEmpty](../constructors/help.promoDataEmpty.md) = \['expires' => [int](../types/int.md), \];<a name="help.promoDataEmpty"></a>  

***
<br><br>[$help.recentMeUrls](../constructors/help.recentMeUrls.md) = \['urls' => \[[RecentMeUrl](../types/RecentMeUrl.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="help.recentMeUrls"></a>  

***
<br><br>[$help.support](../constructors/help.support.md) = \['phone_number' => [string](../types/string.md), 'user' => [User](../types/User.md), \];<a name="help.support"></a>  

***
<br><br>[$help.supportName](../constructors/help.supportName.md) = \['name' => [string](../types/string.md), \];<a name="help.supportName"></a>  

***
<br><br>[$help.termsOfService](../constructors/help.termsOfService.md) = \['popup' => [Bool](../types/Bool.md), 'id' => [DataJSON](../types/DataJSON.md), 'text' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'min_age_confirm' => [int](../types/int.md), \];<a name="help.termsOfService"></a>  

***
<br><br>[$help.termsOfServiceUpdate](../constructors/help.termsOfServiceUpdate.md) = \['expires' => [int](../types/int.md), 'terms_of_service' => [help.TermsOfService](../types/help.TermsOfService.md), \];<a name="help.termsOfServiceUpdate"></a>  

***
<br><br>[$help.termsOfServiceUpdateEmpty](../constructors/help.termsOfServiceUpdateEmpty.md) = \['expires' => [int](../types/int.md), \];<a name="help.termsOfServiceUpdateEmpty"></a>  

***
<br><br>[$help.userInfo](../constructors/help.userInfo.md) = \['message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'author' => [string](../types/string.md), 'date' => [int](../types/int.md), \];<a name="help.userInfo"></a>  

***
<br><br>[$help.userInfoEmpty](../constructors/help.userInfoEmpty.md) = \[\];<a name="help.userInfoEmpty"></a>  

***
<br><br>[$highScore](../constructors/highScore.md) = \['pos' => [int](../types/int.md), 'user_id' => [long](../types/long.md), 'score' => [int](../types/int.md), \];<a name="highScore"></a>  

***
<br><br>[$importedContact](../constructors/importedContact.md) = \['user_id' => [long](../types/long.md), 'client_id' => [long](../types/long.md), \];<a name="importedContact"></a>  

***
<br><br>[$inlineBotSwitchPM](../constructors/inlineBotSwitchPM.md) = \['text' => [string](../types/string.md), 'start_param' => [string](../types/string.md), \];<a name="inlineBotSwitchPM"></a>  

***
<br><br>[$inlineQueryPeerTypeBroadcast](../constructors/inlineQueryPeerTypeBroadcast.md) = \[\];<a name="inlineQueryPeerTypeBroadcast"></a>  

***
<br><br>[$inlineQueryPeerTypeChat](../constructors/inlineQueryPeerTypeChat.md) = \[\];<a name="inlineQueryPeerTypeChat"></a>  

***
<br><br>[$inlineQueryPeerTypeMegagroup](../constructors/inlineQueryPeerTypeMegagroup.md) = \[\];<a name="inlineQueryPeerTypeMegagroup"></a>  

***
<br><br>[$inlineQueryPeerTypePM](../constructors/inlineQueryPeerTypePM.md) = \[\];<a name="inlineQueryPeerTypePM"></a>  

***
<br><br>[$inlineQueryPeerTypeSameBotPM](../constructors/inlineQueryPeerTypeSameBotPM.md) = \[\];<a name="inlineQueryPeerTypeSameBotPM"></a>  

***
<br><br>[$inputAppEvent](../constructors/inputAppEvent.md) = \['time' => [double](../types/double.md), 'type' => [string](../types/string.md), 'peer' => [long](../types/long.md), 'data' => [JSONValue](../types/JSONValue.md), \];<a name="inputAppEvent"></a>  

***
<br><br>[$inputBotInlineMessageGame](../constructors/inputBotInlineMessageGame.md) = \['reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="inputBotInlineMessageGame"></a>  

***
<br><br>[$inputBotInlineMessageID](../constructors/inputBotInlineMessageID.md) = \['dc_id' => [int](../types/int.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputBotInlineMessageID"></a>  

***
<br><br>[$inputBotInlineMessageID64](../constructors/inputBotInlineMessageID64.md) = \['dc_id' => [int](../types/int.md), 'owner_id' => [long](../types/long.md), 'id' => [int](../types/int.md), 'access_hash' => [long](../types/long.md), \];<a name="inputBotInlineMessageID64"></a>  

***
<br><br>[$inputBotInlineMessageMediaAuto](../constructors/inputBotInlineMessageMediaAuto.md) = \['message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaAuto"></a>  

***
<br><br>[$inputBotInlineMessageMediaContact](../constructors/inputBotInlineMessageMediaContact.md) = \['phone_number' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'vcard' => [string](../types/string.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaContact"></a>  

***
<br><br>[$inputBotInlineMessageMediaGeo](../constructors/inputBotInlineMessageMediaGeo.md) = \['geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'heading' => [int](../types/int.md), 'period' => [int](../types/int.md), 'proximity_notification_radius' => [int](../types/int.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaGeo"></a>  

***
<br><br>[$inputBotInlineMessageMediaInvoice](../constructors/inputBotInlineMessageMediaInvoice.md) = \['title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'photo' => [InputWebDocument](../types/InputWebDocument.md), 'invoice' => [Invoice](../types/Invoice.md), 'payload' => [bytes](../types/bytes.md), 'provider' => [string](../types/string.md), 'provider_data' => [DataJSON](../types/DataJSON.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaInvoice"></a>  

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
<br><br>[$inputChannel](../constructors/inputChannel.md) = \['channel_id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputChannel"></a>  

***
<br><br>[$inputChannelEmpty](../constructors/inputChannelEmpty.md) = \[\];<a name="inputChannelEmpty"></a>  

***
<br><br>[$inputChannelFromMessage](../constructors/inputChannelFromMessage.md) = \['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'channel_id' => [long](../types/long.md), \];<a name="inputChannelFromMessage"></a>  

***
<br><br>[$inputChatPhoto](../constructors/inputChatPhoto.md) = \['id' => [InputPhoto](../types/InputPhoto.md), \];<a name="inputChatPhoto"></a>  

***
<br><br>[$inputChatPhotoEmpty](../constructors/inputChatPhotoEmpty.md) = \[\];<a name="inputChatPhotoEmpty"></a>  

***
<br><br>[$inputChatUploadedPhoto](../constructors/inputChatUploadedPhoto.md) = \['file' => [InputFile](../types/InputFile.md), 'video' => [InputFile](../types/InputFile.md), 'video_start_ts' => [double](../types/double.md), \];<a name="inputChatUploadedPhoto"></a>  

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
<br><br>[$inputGeoPoint](../constructors/inputGeoPoint.md) = \['lat' => [double](../types/double.md), 'long' => [double](../types/double.md), 'accuracy_radius' => [int](../types/int.md), \];<a name="inputGeoPoint"></a>  

***
<br><br>[$inputGeoPointEmpty](../constructors/inputGeoPointEmpty.md) = \[\];<a name="inputGeoPointEmpty"></a>  

***
<br><br>[$inputGroupCall](../constructors/inputGroupCall.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputGroupCall"></a>  

***
<br><br>[$inputGroupCallStream](../constructors/inputGroupCallStream.md) = \['call' => [InputGroupCall](../types/InputGroupCall.md), 'time_ms' => [long](../types/long.md), 'scale' => [int](../types/int.md), 'video_channel' => [int](../types/int.md), 'video_quality' => [int](../types/int.md), \];<a name="inputGroupCallStream"></a>  

***
<br><br>[$inputKeyboardButtonUrlAuth](../constructors/inputKeyboardButtonUrlAuth.md) = \['request_write_access' => [Bool](../types/Bool.md), 'text' => [string](../types/string.md), 'fwd_text' => [string](../types/string.md), 'url' => [string](../types/string.md), 'bot' => [InputUser](../types/InputUser.md), \];<a name="inputKeyboardButtonUrlAuth"></a>  

***
<br><br>[$inputKeyboardButtonUserProfile](../constructors/inputKeyboardButtonUserProfile.md) = \['text' => [string](../types/string.md), 'user_id' => [InputUser](../types/InputUser.md), \];<a name="inputKeyboardButtonUserProfile"></a>  

***
<br><br>[$inputMediaContact](../constructors/inputMediaContact.md) = \['phone_number' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'vcard' => [string](../types/string.md), \];<a name="inputMediaContact"></a>  

***
<br><br>[$inputMediaDice](../constructors/inputMediaDice.md) = \['emoticon' => [string](../types/string.md), \];<a name="inputMediaDice"></a>  

***
<br><br>[$inputMediaDocument](../constructors/inputMediaDocument.md) = \['id' => [InputDocument](../types/InputDocument.md), 'ttl_seconds' => [int](../types/int.md), 'query' => [string](../types/string.md), \];<a name="inputMediaDocument"></a>  

***
<br><br>[$inputMediaDocumentExternal](../constructors/inputMediaDocumentExternal.md) = \['url' => [string](../types/string.md), 'ttl_seconds' => [int](../types/int.md), \];<a name="inputMediaDocumentExternal"></a>  

***
<br><br>[$inputMediaEmpty](../constructors/inputMediaEmpty.md) = \[\];<a name="inputMediaEmpty"></a>  

***
<br><br>[$inputMediaGame](../constructors/inputMediaGame.md) = \['id' => [InputGame](../types/InputGame.md), \];<a name="inputMediaGame"></a>  

***
<br><br>[$inputMediaGeoLive](../constructors/inputMediaGeoLive.md) = \['stopped' => [Bool](../types/Bool.md), 'geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'heading' => [int](../types/int.md), 'period' => [int](../types/int.md), 'proximity_notification_radius' => [int](../types/int.md), \];<a name="inputMediaGeoLive"></a>  

***
<br><br>[$inputMediaGeoPoint](../constructors/inputMediaGeoPoint.md) = \['geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), \];<a name="inputMediaGeoPoint"></a>  

***
<br><br>[$inputMediaInvoice](../constructors/inputMediaInvoice.md) = \['title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'photo' => [InputWebDocument](../types/InputWebDocument.md), 'invoice' => [Invoice](../types/Invoice.md), 'payload' => [bytes](../types/bytes.md), 'provider' => [string](../types/string.md), 'provider_data' => [DataJSON](../types/DataJSON.md), 'start_param' => [string](../types/string.md), \];<a name="inputMediaInvoice"></a>  

***
<br><br>[$inputMediaPhoto](../constructors/inputMediaPhoto.md) = \['id' => [InputPhoto](../types/InputPhoto.md), 'ttl_seconds' => [int](../types/int.md), \];<a name="inputMediaPhoto"></a>  

***
<br><br>[$inputMediaPhotoExternal](../constructors/inputMediaPhotoExternal.md) = \['url' => [string](../types/string.md), 'ttl_seconds' => [int](../types/int.md), \];<a name="inputMediaPhotoExternal"></a>  

***
<br><br>[$inputMediaPoll](../constructors/inputMediaPoll.md) = \['poll' => [Poll](../types/Poll.md), 'correct_answers' => \[[bytes](../types/bytes.md)\], 'solution' => [string](../types/string.md), 'solution_entities' => \[[MessageEntity](../types/MessageEntity.md)\], \];<a name="inputMediaPoll"></a>  

***
<br><br>[$inputMediaUploadedDocument](../constructors/inputMediaUploadedDocument.md) = \['nosound_video' => [Bool](../types/Bool.md), 'force_file' => [Bool](../types/Bool.md), 'file' => [InputFile](../types/InputFile.md), 'thumb' => [InputFile](../types/InputFile.md), 'mime_type' => [string](../types/string.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], 'stickers' => \[[InputDocument](../types/InputDocument.md)\], 'ttl_seconds' => [int](../types/int.md), \];<a name="inputMediaUploadedDocument"></a>  

***
<br><br>[$inputMediaUploadedPhoto](../constructors/inputMediaUploadedPhoto.md) = \['file' => [InputFile](../types/InputFile.md), 'stickers' => \[[InputDocument](../types/InputDocument.md)\], 'ttl_seconds' => [int](../types/int.md), \];<a name="inputMediaUploadedPhoto"></a>  

***
<br><br>[$inputMediaVenue](../constructors/inputMediaVenue.md) = \['geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'title' => [string](../types/string.md), 'address' => [string](../types/string.md), 'provider' => [string](../types/string.md), 'venue_id' => [string](../types/string.md), 'venue_type' => [string](../types/string.md), \];<a name="inputMediaVenue"></a>  

***
<br><br>[$inputMessageCallbackQuery](../constructors/inputMessageCallbackQuery.md) = \['id' => [int](../types/int.md), 'query_id' => [long](../types/long.md), \];<a name="inputMessageCallbackQuery"></a>  

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
<br><br>[$inputMessagesFilterPinned](../constructors/inputMessagesFilterPinned.md) = \[\];<a name="inputMessagesFilterPinned"></a>  

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
<br><br>[$inputPaymentCredentialsApplePay](../constructors/inputPaymentCredentialsApplePay.md) = \['payment_data' => [DataJSON](../types/DataJSON.md), \];<a name="inputPaymentCredentialsApplePay"></a>  

***
<br><br>[$inputPaymentCredentialsGooglePay](../constructors/inputPaymentCredentialsGooglePay.md) = \['payment_token' => [DataJSON](../types/DataJSON.md), \];<a name="inputPaymentCredentialsGooglePay"></a>  

***
<br><br>[$inputPaymentCredentialsSaved](../constructors/inputPaymentCredentialsSaved.md) = \['id' => [string](../types/string.md), 'tmp_password' => [bytes](../types/bytes.md), \];<a name="inputPaymentCredentialsSaved"></a>  

***
<br><br>[$inputPeerChannel](../constructors/inputPeerChannel.md) = \['channel_id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputPeerChannel"></a>  

***
<br><br>[$inputPeerChannelFromMessage](../constructors/inputPeerChannelFromMessage.md) = \['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'channel_id' => [long](../types/long.md), \];<a name="inputPeerChannelFromMessage"></a>  

***
<br><br>[$inputPeerChat](../constructors/inputPeerChat.md) = \['chat_id' => [long](../types/long.md), \];<a name="inputPeerChat"></a>  

***
<br><br>[$inputPeerEmpty](../constructors/inputPeerEmpty.md) = \[\];<a name="inputPeerEmpty"></a>  

***
<br><br>[$inputPeerNotifySettings](../constructors/inputPeerNotifySettings.md) = \['show_previews' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'mute_until' => [int](../types/int.md), 'sound' => [string](../types/string.md), \];<a name="inputPeerNotifySettings"></a>  

***
<br><br>[$inputPeerPhotoFileLocation](../constructors/inputPeerPhotoFileLocation.md) = \['big' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'photo_id' => [long](../types/long.md), \];<a name="inputPeerPhotoFileLocation"></a>  

***
<br><br>[$inputPeerSelf](../constructors/inputPeerSelf.md) = \[\];<a name="inputPeerSelf"></a>  

***
<br><br>[$inputPeerUser](../constructors/inputPeerUser.md) = \['user_id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputPeerUser"></a>  

***
<br><br>[$inputPeerUserFromMessage](../constructors/inputPeerUserFromMessage.md) = \['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'user_id' => [long](../types/long.md), \];<a name="inputPeerUserFromMessage"></a>  

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
<br><br>[$inputPhotoLegacyFileLocation](../constructors/inputPhotoLegacyFileLocation.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'file_reference' => [bytes](../types/bytes.md), 'volume_id' => [long](../types/long.md), 'local_id' => [int](../types/int.md), 'secret' => [long](../types/long.md), \];<a name="inputPhotoLegacyFileLocation"></a>  

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
<br><br>[$inputPrivacyValueAllowChatParticipants](../constructors/inputPrivacyValueAllowChatParticipants.md) = \['chats' => \[[long](../types/long.md)\], \];<a name="inputPrivacyValueAllowChatParticipants"></a>  

***
<br><br>[$inputPrivacyValueAllowContacts](../constructors/inputPrivacyValueAllowContacts.md) = \[\];<a name="inputPrivacyValueAllowContacts"></a>  

***
<br><br>[$inputPrivacyValueAllowUsers](../constructors/inputPrivacyValueAllowUsers.md) = \['users' => \[[InputUser](../types/InputUser.md)\], \];<a name="inputPrivacyValueAllowUsers"></a>  

***
<br><br>[$inputPrivacyValueDisallowAll](../constructors/inputPrivacyValueDisallowAll.md) = \[\];<a name="inputPrivacyValueDisallowAll"></a>  

***
<br><br>[$inputPrivacyValueDisallowChatParticipants](../constructors/inputPrivacyValueDisallowChatParticipants.md) = \['chats' => \[[long](../types/long.md)\], \];<a name="inputPrivacyValueDisallowChatParticipants"></a>  

***
<br><br>[$inputPrivacyValueDisallowContacts](../constructors/inputPrivacyValueDisallowContacts.md) = \[\];<a name="inputPrivacyValueDisallowContacts"></a>  

***
<br><br>[$inputPrivacyValueDisallowUsers](../constructors/inputPrivacyValueDisallowUsers.md) = \['users' => \[[InputUser](../types/InputUser.md)\], \];<a name="inputPrivacyValueDisallowUsers"></a>  

***
<br><br>[$inputReportReasonChildAbuse](../constructors/inputReportReasonChildAbuse.md) = \[\];<a name="inputReportReasonChildAbuse"></a>  

***
<br><br>[$inputReportReasonCopyright](../constructors/inputReportReasonCopyright.md) = \[\];<a name="inputReportReasonCopyright"></a>  

***
<br><br>[$inputReportReasonFake](../constructors/inputReportReasonFake.md) = \[\];<a name="inputReportReasonFake"></a>  

***
<br><br>[$inputReportReasonGeoIrrelevant](../constructors/inputReportReasonGeoIrrelevant.md) = \[\];<a name="inputReportReasonGeoIrrelevant"></a>  

***
<br><br>[$inputReportReasonOther](../constructors/inputReportReasonOther.md) = \[\];<a name="inputReportReasonOther"></a>  

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
<br><br>[$inputStickerSetAnimatedEmojiAnimations](../constructors/inputStickerSetAnimatedEmojiAnimations.md) = \[\];<a name="inputStickerSetAnimatedEmojiAnimations"></a>  

***
<br><br>[$inputStickerSetDice](../constructors/inputStickerSetDice.md) = \['emoticon' => [string](../types/string.md), \];<a name="inputStickerSetDice"></a>  

***
<br><br>[$inputStickerSetEmpty](../constructors/inputStickerSetEmpty.md) = \[\];<a name="inputStickerSetEmpty"></a>  

***
<br><br>[$inputStickerSetID](../constructors/inputStickerSetID.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputStickerSetID"></a>  

***
<br><br>[$inputStickerSetItem](../constructors/inputStickerSetItem.md) = \['document' => [InputDocument](../types/InputDocument.md), 'emoji' => [string](../types/string.md), 'mask_coords' => [MaskCoords](../types/MaskCoords.md), \];<a name="inputStickerSetItem"></a>  

***
<br><br>[$inputStickerSetShortName](../constructors/inputStickerSetShortName.md) = \['short_name' => [string](../types/string.md), \];<a name="inputStickerSetShortName"></a>  

***
<br><br>[$inputStickerSetThumb](../constructors/inputStickerSetThumb.md) = \['stickerset' => [InputStickerSet](../types/InputStickerSet.md), 'thumb_version' => [int](../types/int.md), \];<a name="inputStickerSetThumb"></a>  

***
<br><br>[$inputStickeredMediaDocument](../constructors/inputStickeredMediaDocument.md) = \['id' => [InputDocument](../types/InputDocument.md), \];<a name="inputStickeredMediaDocument"></a>  

***
<br><br>[$inputStickeredMediaPhoto](../constructors/inputStickeredMediaPhoto.md) = \['id' => [InputPhoto](../types/InputPhoto.md), \];<a name="inputStickeredMediaPhoto"></a>  

***
<br><br>[$inputTakeoutFileLocation](../constructors/inputTakeoutFileLocation.md) = \[\];<a name="inputTakeoutFileLocation"></a>  

***
<br><br>[$inputTheme](../constructors/inputTheme.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputTheme"></a>  

***
<br><br>[$inputThemeSettings](../constructors/inputThemeSettings.md) = \['message_colors_animated' => [Bool](../types/Bool.md), 'base_theme' => [BaseTheme](../types/BaseTheme.md), 'accent_color' => [int](../types/int.md), 'outbox_accent_color' => [int](../types/int.md), 'message_colors' => \[[int](../types/int.md)\], 'wallpaper' => [InputWallPaper](../types/InputWallPaper.md), 'wallpaper_settings' => [WallPaperSettings](../types/WallPaperSettings.md), \];<a name="inputThemeSettings"></a>  

***
<br><br>[$inputThemeSlug](../constructors/inputThemeSlug.md) = \['slug' => [string](../types/string.md), \];<a name="inputThemeSlug"></a>  

***
<br><br>[$inputUser](../constructors/inputUser.md) = \['user_id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputUser"></a>  

***
<br><br>[$inputUserEmpty](../constructors/inputUserEmpty.md) = \[\];<a name="inputUserEmpty"></a>  

***
<br><br>[$inputUserFromMessage](../constructors/inputUserFromMessage.md) = \['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'user_id' => [long](../types/long.md), \];<a name="inputUserFromMessage"></a>  

***
<br><br>[$inputUserSelf](../constructors/inputUserSelf.md) = \[\];<a name="inputUserSelf"></a>  

***
<br><br>[$inputWallPaper](../constructors/inputWallPaper.md) = \['id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), \];<a name="inputWallPaper"></a>  

***
<br><br>[$inputWallPaperNoFile](../constructors/inputWallPaperNoFile.md) = \['id' => [long](../types/long.md), \];<a name="inputWallPaperNoFile"></a>  

***
<br><br>[$inputWallPaperSlug](../constructors/inputWallPaperSlug.md) = \['slug' => [string](../types/string.md), \];<a name="inputWallPaperSlug"></a>  

***
<br><br>[$inputWebDocument](../constructors/inputWebDocument.md) = \['url' => [string](../types/string.md), 'size' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], \];<a name="inputWebDocument"></a>  

***
<br><br>[$inputWebFileGeoPointLocation](../constructors/inputWebFileGeoPointLocation.md) = \['geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'access_hash' => [long](../types/long.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'zoom' => [int](../types/int.md), 'scale' => [int](../types/int.md), \];<a name="inputWebFileGeoPointLocation"></a>  

***
<br><br>[$inputWebFileLocation](../constructors/inputWebFileLocation.md) = \['url' => [string](../types/string.md), 'access_hash' => [long](../types/long.md), \];<a name="inputWebFileLocation"></a>  

***
<br><br>[$invoice](../constructors/invoice.md) = \['test' => [Bool](../types/Bool.md), 'name_requested' => [Bool](../types/Bool.md), 'phone_requested' => [Bool](../types/Bool.md), 'email_requested' => [Bool](../types/Bool.md), 'shipping_address_requested' => [Bool](../types/Bool.md), 'flexible' => [Bool](../types/Bool.md), 'phone_to_provider' => [Bool](../types/Bool.md), 'email_to_provider' => [Bool](../types/Bool.md), 'currency' => [string](../types/string.md), 'prices' => \[[LabeledPrice](../types/LabeledPrice.md)\], 'max_tip_amount' => [long](../types/long.md), 'suggested_tip_amounts' => \[[long](../types/long.md)\], \];<a name="invoice"></a>  

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
<br><br>[$keyboardButtonCallback](../constructors/keyboardButtonCallback.md) = \['requires_password' => [Bool](../types/Bool.md), 'text' => [string](../types/string.md), 'data' => [bytes](../types/bytes.md), \];<a name="keyboardButtonCallback"></a>  

***
<br><br>[$keyboardButtonGame](../constructors/keyboardButtonGame.md) = \['text' => [string](../types/string.md), \];<a name="keyboardButtonGame"></a>  

***
<br><br>[$keyboardButtonRequestGeoLocation](../constructors/keyboardButtonRequestGeoLocation.md) = \['text' => [string](../types/string.md), \];<a name="keyboardButtonRequestGeoLocation"></a>  

***
<br><br>[$keyboardButtonRequestPhone](../constructors/keyboardButtonRequestPhone.md) = \['text' => [string](../types/string.md), \];<a name="keyboardButtonRequestPhone"></a>  

***
<br><br>[$keyboardButtonRequestPoll](../constructors/keyboardButtonRequestPoll.md) = \['quiz' => [Bool](../types/Bool.md), 'text' => [string](../types/string.md), \];<a name="keyboardButtonRequestPoll"></a>  

***
<br><br>[$keyboardButtonRow](../constructors/keyboardButtonRow.md) = \['buttons' => \[[KeyboardButton](../types/KeyboardButton.md)\], \];<a name="keyboardButtonRow"></a>  

***
<br><br>[$keyboardButtonSwitchInline](../constructors/keyboardButtonSwitchInline.md) = \['same_peer' => [Bool](../types/Bool.md), 'text' => [string](../types/string.md), 'query' => [string](../types/string.md), \];<a name="keyboardButtonSwitchInline"></a>  

***
<br><br>[$keyboardButtonUrl](../constructors/keyboardButtonUrl.md) = \['text' => [string](../types/string.md), 'url' => [string](../types/string.md), \];<a name="keyboardButtonUrl"></a>  

***
<br><br>[$keyboardButtonUrlAuth](../constructors/keyboardButtonUrlAuth.md) = \['text' => [string](../types/string.md), 'fwd_text' => [string](../types/string.md), 'url' => [string](../types/string.md), 'button_id' => [int](../types/int.md), \];<a name="keyboardButtonUrlAuth"></a>  

***
<br><br>[$keyboardButtonUserProfile](../constructors/keyboardButtonUserProfile.md) = \['text' => [string](../types/string.md), 'user_id' => [long](../types/long.md), \];<a name="keyboardButtonUserProfile"></a>  

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
<br><br>[$message](../constructors/message.md) = \['out' => [Bool](../types/Bool.md), 'mentioned' => [Bool](../types/Bool.md), 'media_unread' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'post' => [Bool](../types/Bool.md), 'from_scheduled' => [Bool](../types/Bool.md), 'legacy' => [Bool](../types/Bool.md), 'edit_hide' => [Bool](../types/Bool.md), 'pinned' => [Bool](../types/Bool.md), 'noforwards' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'from_id' => [Peer](../types/Peer.md), 'peer_id' => [Peer](../types/Peer.md), 'fwd_from' => [MessageFwdHeader](../types/MessageFwdHeader.md), 'via_bot_id' => [long](../types/long.md), 'reply_to' => [MessageReplyHeader](../types/MessageReplyHeader.md), 'date' => [int](../types/int.md), 'message' => [string](../types/string.md), 'media' => [MessageMedia](../types/MessageMedia.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'views' => [int](../types/int.md), 'forwards' => [int](../types/int.md), 'replies' => [MessageReplies](../types/MessageReplies.md), 'edit_date' => [int](../types/int.md), 'post_author' => [string](../types/string.md), 'grouped_id' => [long](../types/long.md), 'reactions' => [MessageReactions](../types/MessageReactions.md), 'restriction_reason' => \[[RestrictionReason](../types/RestrictionReason.md)\], 'ttl_period' => [int](../types/int.md), \];<a name="message"></a>  

***
<br><br>[$messageActionBotAllowed](../constructors/messageActionBotAllowed.md) = \['domain' => [string](../types/string.md), \];<a name="messageActionBotAllowed"></a>  

***
<br><br>[$messageActionChannelCreate](../constructors/messageActionChannelCreate.md) = \['title' => [string](../types/string.md), \];<a name="messageActionChannelCreate"></a>  

***
<br><br>[$messageActionChannelMigrateFrom](../constructors/messageActionChannelMigrateFrom.md) = \['title' => [string](../types/string.md), 'chat_id' => [long](../types/long.md), \];<a name="messageActionChannelMigrateFrom"></a>  

***
<br><br>[$messageActionChatAddUser](../constructors/messageActionChatAddUser.md) = \['users' => \[[long](../types/long.md)\], \];<a name="messageActionChatAddUser"></a>  

***
<br><br>[$messageActionChatCreate](../constructors/messageActionChatCreate.md) = \['title' => [string](../types/string.md), 'users' => \[[long](../types/long.md)\], \];<a name="messageActionChatCreate"></a>  

***
<br><br>[$messageActionChatDeletePhoto](../constructors/messageActionChatDeletePhoto.md) = \[\];<a name="messageActionChatDeletePhoto"></a>  

***
<br><br>[$messageActionChatDeleteUser](../constructors/messageActionChatDeleteUser.md) = \['user_id' => [long](../types/long.md), \];<a name="messageActionChatDeleteUser"></a>  

***
<br><br>[$messageActionChatEditPhoto](../constructors/messageActionChatEditPhoto.md) = \['photo' => [Photo](../types/Photo.md), \];<a name="messageActionChatEditPhoto"></a>  

***
<br><br>[$messageActionChatEditTitle](../constructors/messageActionChatEditTitle.md) = \['title' => [string](../types/string.md), \];<a name="messageActionChatEditTitle"></a>  

***
<br><br>[$messageActionChatJoinedByLink](../constructors/messageActionChatJoinedByLink.md) = \['inviter_id' => [long](../types/long.md), \];<a name="messageActionChatJoinedByLink"></a>  

***
<br><br>[$messageActionChatJoinedByRequest](../constructors/messageActionChatJoinedByRequest.md) = \[\];<a name="messageActionChatJoinedByRequest"></a>  

***
<br><br>[$messageActionChatMigrateTo](../constructors/messageActionChatMigrateTo.md) = \['channel_id' => [long](../types/long.md), \];<a name="messageActionChatMigrateTo"></a>  

***
<br><br>[$messageActionContactSignUp](../constructors/messageActionContactSignUp.md) = \[\];<a name="messageActionContactSignUp"></a>  

***
<br><br>[$messageActionCustomAction](../constructors/messageActionCustomAction.md) = \['message' => [string](../types/string.md), \];<a name="messageActionCustomAction"></a>  

***
<br><br>[$messageActionEmpty](../constructors/messageActionEmpty.md) = \[\];<a name="messageActionEmpty"></a>  

***
<br><br>[$messageActionGameScore](../constructors/messageActionGameScore.md) = \['game_id' => [long](../types/long.md), 'score' => [int](../types/int.md), \];<a name="messageActionGameScore"></a>  

***
<br><br>[$messageActionGeoProximityReached](../constructors/messageActionGeoProximityReached.md) = \['from_id' => [Peer](../types/Peer.md), 'to_id' => [Peer](../types/Peer.md), 'distance' => [int](../types/int.md), \];<a name="messageActionGeoProximityReached"></a>  

***
<br><br>[$messageActionGroupCall](../constructors/messageActionGroupCall.md) = \['call' => [InputGroupCall](../types/InputGroupCall.md), 'duration' => [int](../types/int.md), \];<a name="messageActionGroupCall"></a>  

***
<br><br>[$messageActionGroupCallScheduled](../constructors/messageActionGroupCallScheduled.md) = \['call' => [InputGroupCall](../types/InputGroupCall.md), 'schedule_date' => [int](../types/int.md), \];<a name="messageActionGroupCallScheduled"></a>  

***
<br><br>[$messageActionHistoryClear](../constructors/messageActionHistoryClear.md) = \[\];<a name="messageActionHistoryClear"></a>  

***
<br><br>[$messageActionInviteToGroupCall](../constructors/messageActionInviteToGroupCall.md) = \['call' => [InputGroupCall](../types/InputGroupCall.md), 'users' => \[[long](../types/long.md)\], \];<a name="messageActionInviteToGroupCall"></a>  

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
<br><br>[$messageActionSetChatTheme](../constructors/messageActionSetChatTheme.md) = \['emoticon' => [string](../types/string.md), \];<a name="messageActionSetChatTheme"></a>  

***
<br><br>[$messageActionSetMessagesTTL](../constructors/messageActionSetMessagesTTL.md) = \['period' => [int](../types/int.md), \];<a name="messageActionSetMessagesTTL"></a>  

***
<br><br>[$messageEmpty](../constructors/messageEmpty.md) = \['id' => [int](../types/int.md), 'peer_id' => [Peer](../types/Peer.md), \];<a name="messageEmpty"></a>  

***
<br><br>[$messageEntityBankCard](../constructors/messageEntityBankCard.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityBankCard"></a>  

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
<br><br>[$messageEntityMentionName](../constructors/messageEntityMentionName.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), 'user_id' => [long](../types/long.md), \];<a name="messageEntityMentionName"></a>  

***
<br><br>[$messageEntityPhone](../constructors/messageEntityPhone.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntityPhone"></a>  

***
<br><br>[$messageEntityPre](../constructors/messageEntityPre.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), 'language' => [string](../types/string.md), \];<a name="messageEntityPre"></a>  

***
<br><br>[$messageEntitySpoiler](../constructors/messageEntitySpoiler.md) = \['offset' => [int](../types/int.md), 'length' => [int](../types/int.md), \];<a name="messageEntitySpoiler"></a>  

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
<br><br>[$messageFwdHeader](../constructors/messageFwdHeader.md) = \['imported' => [Bool](../types/Bool.md), 'from_id' => [Peer](../types/Peer.md), 'from_name' => [string](../types/string.md), 'date' => [int](../types/int.md), 'channel_post' => [int](../types/int.md), 'post_author' => [string](../types/string.md), 'saved_from_peer' => [Peer](../types/Peer.md), 'saved_from_msg_id' => [int](../types/int.md), 'psa_type' => [string](../types/string.md), \];<a name="messageFwdHeader"></a>  

***
<br><br>[$messageInteractionCounters](../constructors/messageInteractionCounters.md) = \['msg_id' => [int](../types/int.md), 'views' => [int](../types/int.md), 'forwards' => [int](../types/int.md), \];<a name="messageInteractionCounters"></a>  

***
<br><br>[$messageMediaContact](../constructors/messageMediaContact.md) = \['phone_number' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'vcard' => [string](../types/string.md), 'user_id' => [long](../types/long.md), \];<a name="messageMediaContact"></a>  

***
<br><br>[$messageMediaDice](../constructors/messageMediaDice.md) = \['value' => [int](../types/int.md), 'emoticon' => [string](../types/string.md), \];<a name="messageMediaDice"></a>  

***
<br><br>[$messageMediaDocument](../constructors/messageMediaDocument.md) = \['document' => [Document](../types/Document.md), 'ttl_seconds' => [int](../types/int.md), \];<a name="messageMediaDocument"></a>  

***
<br><br>[$messageMediaEmpty](../constructors/messageMediaEmpty.md) = \[\];<a name="messageMediaEmpty"></a>  

***
<br><br>[$messageMediaGame](../constructors/messageMediaGame.md) = \['game' => [Game](../types/Game.md), \];<a name="messageMediaGame"></a>  

***
<br><br>[$messageMediaGeo](../constructors/messageMediaGeo.md) = \['geo' => [GeoPoint](../types/GeoPoint.md), \];<a name="messageMediaGeo"></a>  

***
<br><br>[$messageMediaGeoLive](../constructors/messageMediaGeoLive.md) = \['geo' => [GeoPoint](../types/GeoPoint.md), 'heading' => [int](../types/int.md), 'period' => [int](../types/int.md), 'proximity_notification_radius' => [int](../types/int.md), \];<a name="messageMediaGeoLive"></a>  

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
<br><br>[$messageReactions](../constructors/messageReactions.md) = \['min' => [Bool](../types/Bool.md), 'can_see_list' => [Bool](../types/Bool.md), 'results' => \[[ReactionCount](../types/ReactionCount.md)\], 'recent_reactons' => \[[MessageUserReaction](../types/MessageUserReaction.md)\], \];<a name="messageReactions"></a>  

***
<br><br>[$messageReplies](../constructors/messageReplies.md) = \['comments' => [Bool](../types/Bool.md), 'replies' => [int](../types/int.md), 'replies_pts' => [int](../types/int.md), 'recent_repliers' => \[[Peer](../types/Peer.md)\], 'channel_id' => [long](../types/long.md), 'max_id' => [int](../types/int.md), 'read_max_id' => [int](../types/int.md), \];<a name="messageReplies"></a>  

***
<br><br>[$messageReplyHeader](../constructors/messageReplyHeader.md) = \['reply_to_msg_id' => [int](../types/int.md), 'reply_to_peer_id' => [Peer](../types/Peer.md), 'reply_to_top_id' => [int](../types/int.md), \];<a name="messageReplyHeader"></a>  

***
<br><br>[$messageService](../constructors/messageService.md) = \['out' => [Bool](../types/Bool.md), 'mentioned' => [Bool](../types/Bool.md), 'media_unread' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'post' => [Bool](../types/Bool.md), 'legacy' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'from_id' => [Peer](../types/Peer.md), 'peer_id' => [Peer](../types/Peer.md), 'reply_to' => [MessageReplyHeader](../types/MessageReplyHeader.md), 'date' => [int](../types/int.md), 'action' => [MessageAction](../types/MessageAction.md), 'ttl_period' => [int](../types/int.md), \];<a name="messageService"></a>  

***
<br><br>[$messageUserReaction](../constructors/messageUserReaction.md) = \['user_id' => [long](../types/long.md), 'reaction' => [string](../types/string.md), \];<a name="messageUserReaction"></a>  

***
<br><br>[$messageUserVote](../constructors/messageUserVote.md) = \['user_id' => [long](../types/long.md), 'option' => [bytes](../types/bytes.md), 'date' => [int](../types/int.md), \];<a name="messageUserVote"></a>  

***
<br><br>[$messageUserVoteInputOption](../constructors/messageUserVoteInputOption.md) = \['user_id' => [long](../types/long.md), 'date' => [int](../types/int.md), \];<a name="messageUserVoteInputOption"></a>  

***
<br><br>[$messageUserVoteMultiple](../constructors/messageUserVoteMultiple.md) = \['user_id' => [long](../types/long.md), 'options' => \[[bytes](../types/bytes.md)\], 'date' => [int](../types/int.md), \];<a name="messageUserVoteMultiple"></a>  

***
<br><br>[$messageViews](../constructors/messageViews.md) = \['views' => [int](../types/int.md), 'forwards' => [int](../types/int.md), 'replies' => [MessageReplies](../types/MessageReplies.md), \];<a name="messageViews"></a>  

***
<br><br>[$messages.affectedFoundMessages](../constructors/messages.affectedFoundMessages.md) = \['pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), 'offset' => [int](../types/int.md), 'messages' => \[[int](../types/int.md)\], \];<a name="messages.affectedFoundMessages"></a>  

***
<br><br>[$messages.affectedHistory](../constructors/messages.affectedHistory.md) = \['pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), 'offset' => [int](../types/int.md), \];<a name="messages.affectedHistory"></a>  

***
<br><br>[$messages.affectedMessages](../constructors/messages.affectedMessages.md) = \['pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="messages.affectedMessages"></a>  

***
<br><br>[$messages.allStickers](../constructors/messages.allStickers.md) = \['hash' => [long](../types/long.md), 'sets' => \[[StickerSet](../types/StickerSet.md)\], \];<a name="messages.allStickers"></a>  

***
<br><br>[$messages.allStickersNotModified](../constructors/messages.allStickersNotModified.md) = \[\];<a name="messages.allStickersNotModified"></a>  

***
<br><br>[$messages.archivedStickers](../constructors/messages.archivedStickers.md) = \['count' => [int](../types/int.md), 'sets' => \[[StickerSetCovered](../types/StickerSetCovered.md)\], \];<a name="messages.archivedStickers"></a>  

***
<br><br>[$messages.availableReactions](../constructors/messages.availableReactions.md) = \['hash' => [int](../types/int.md), 'reactions' => \[[AvailableReaction](../types/AvailableReaction.md)\], \];<a name="messages.availableReactions"></a>  

***
<br><br>[$messages.availableReactionsNotModified](../constructors/messages.availableReactionsNotModified.md) = \[\];<a name="messages.availableReactionsNotModified"></a>  

***
<br><br>[$messages.botCallbackAnswer](../constructors/messages.botCallbackAnswer.md) = \['alert' => [Bool](../types/Bool.md), 'has_url' => [Bool](../types/Bool.md), 'native_ui' => [Bool](../types/Bool.md), 'message' => [string](../types/string.md), 'url' => [string](../types/string.md), 'cache_time' => [int](../types/int.md), \];<a name="messages.botCallbackAnswer"></a>  

***
<br><br>[$messages.botResults](../constructors/messages.botResults.md) = \['gallery' => [Bool](../types/Bool.md), 'query_id' => [long](../types/long.md), 'next_offset' => [string](../types/string.md), 'switch_pm' => [InlineBotSwitchPM](../types/InlineBotSwitchPM.md), 'results' => \[[BotInlineResult](../types/BotInlineResult.md)\], 'cache_time' => [int](../types/int.md), 'users' => \[[User](../types/User.md)\], \];<a name="messages.botResults"></a>  

***
<br><br>[$messages.channelMessages](../constructors/messages.channelMessages.md) = \['inexact' => [Bool](../types/Bool.md), 'pts' => [int](../types/int.md), 'count' => [int](../types/int.md), 'offset_id_offset' => [int](../types/int.md), 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.channelMessages"></a>  

***
<br><br>[$messages.chatAdminsWithInvites](../constructors/messages.chatAdminsWithInvites.md) = \['admins' => \[[ChatAdminWithInvites](../types/ChatAdminWithInvites.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.chatAdminsWithInvites"></a>  

***
<br><br>[$messages.chatFull](../constructors/messages.chatFull.md) = \['full_chat' => [ChatFull](../types/ChatFull.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.chatFull"></a>  

***
<br><br>[$messages.chatInviteImporters](../constructors/messages.chatInviteImporters.md) = \['count' => [int](../types/int.md), 'importers' => \[[ChatInviteImporter](../types/ChatInviteImporter.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.chatInviteImporters"></a>  

***
<br><br>[$messages.chats](../constructors/messages.chats.md) = \['chats' => \[[Chat](../types/Chat.md)\], \];<a name="messages.chats"></a>  

***
<br><br>[$messages.chatsSlice](../constructors/messages.chatsSlice.md) = \['count' => [int](../types/int.md), 'chats' => \[[Chat](../types/Chat.md)\], \];<a name="messages.chatsSlice"></a>  

***
<br><br>[$messages.checkedHistoryImportPeer](../constructors/messages.checkedHistoryImportPeer.md) = \['confirm_text' => [string](../types/string.md), \];<a name="messages.checkedHistoryImportPeer"></a>  

***
<br><br>[$messages.dhConfig](../constructors/messages.dhConfig.md) = \['g' => [int](../types/int.md), 'p' => [bytes](../types/bytes.md), 'version' => [int](../types/int.md), 'random' => [bytes](../types/bytes.md), \];<a name="messages.dhConfig"></a>  

***
<br><br>[$messages.dhConfigNotModified](../constructors/messages.dhConfigNotModified.md) = \['random' => [bytes](../types/bytes.md), \];<a name="messages.dhConfigNotModified"></a>  

***
<br><br>[$messages.dialogs](../constructors/messages.dialogs.md) = \['dialogs' => \[[Dialog](../types/Dialog.md)\], 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.dialogs"></a>  

***
<br><br>[$messages.dialogsNotModified](../constructors/messages.dialogsNotModified.md) = \['count' => [int](../types/int.md), \];<a name="messages.dialogsNotModified"></a>  

***
<br><br>[$messages.dialogsSlice](../constructors/messages.dialogsSlice.md) = \['count' => [int](../types/int.md), 'dialogs' => \[[Dialog](../types/Dialog.md)\], 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.dialogsSlice"></a>  

***
<br><br>[$messages.discussionMessage](../constructors/messages.discussionMessage.md) = \['messages' => \[[Message](../types/Message.md)\], 'max_id' => [int](../types/int.md), 'read_inbox_max_id' => [int](../types/int.md), 'read_outbox_max_id' => [int](../types/int.md), 'unread_count' => [int](../types/int.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.discussionMessage"></a>  

***
<br><br>[$messages.exportedChatInvite](../constructors/messages.exportedChatInvite.md) = \['invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'users' => \[[User](../types/User.md)\], \];<a name="messages.exportedChatInvite"></a>  

***
<br><br>[$messages.exportedChatInviteReplaced](../constructors/messages.exportedChatInviteReplaced.md) = \['invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'new_invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'users' => \[[User](../types/User.md)\], \];<a name="messages.exportedChatInviteReplaced"></a>  

***
<br><br>[$messages.exportedChatInvites](../constructors/messages.exportedChatInvites.md) = \['count' => [int](../types/int.md), 'invites' => \[[ExportedChatInvite](../types/ExportedChatInvite.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.exportedChatInvites"></a>  

***
<br><br>[$messages.favedStickers](../constructors/messages.favedStickers.md) = \['hash' => [long](../types/long.md), 'packs' => \[[StickerPack](../types/StickerPack.md)\], 'stickers' => \[[Document](../types/Document.md)\], \];<a name="messages.favedStickers"></a>  

***
<br><br>[$messages.favedStickersNotModified](../constructors/messages.favedStickersNotModified.md) = \[\];<a name="messages.favedStickersNotModified"></a>  

***
<br><br>[$messages.featuredStickers](../constructors/messages.featuredStickers.md) = \['hash' => [long](../types/long.md), 'count' => [int](../types/int.md), 'sets' => \[[StickerSetCovered](../types/StickerSetCovered.md)\], 'unread' => \[[long](../types/long.md)\], \];<a name="messages.featuredStickers"></a>  

***
<br><br>[$messages.featuredStickersNotModified](../constructors/messages.featuredStickersNotModified.md) = \['count' => [int](../types/int.md), \];<a name="messages.featuredStickersNotModified"></a>  

***
<br><br>[$messages.foundStickerSets](../constructors/messages.foundStickerSets.md) = \['hash' => [long](../types/long.md), 'sets' => \[[StickerSetCovered](../types/StickerSetCovered.md)\], \];<a name="messages.foundStickerSets"></a>  

***
<br><br>[$messages.foundStickerSetsNotModified](../constructors/messages.foundStickerSetsNotModified.md) = \[\];<a name="messages.foundStickerSetsNotModified"></a>  

***
<br><br>[$messages.highScores](../constructors/messages.highScores.md) = \['scores' => \[[HighScore](../types/HighScore.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.highScores"></a>  

***
<br><br>[$messages.historyImport](../constructors/messages.historyImport.md) = \['id' => [long](../types/long.md), \];<a name="messages.historyImport"></a>  

***
<br><br>[$messages.historyImportParsed](../constructors/messages.historyImportParsed.md) = \['pm' => [Bool](../types/Bool.md), 'group' => [Bool](../types/Bool.md), 'title' => [string](../types/string.md), \];<a name="messages.historyImportParsed"></a>  

***
<br><br>[$messages.inactiveChats](../constructors/messages.inactiveChats.md) = \['dates' => \[[int](../types/int.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.inactiveChats"></a>  

***
<br><br>[$messages.messageEditData](../constructors/messages.messageEditData.md) = \['caption' => [Bool](../types/Bool.md), \];<a name="messages.messageEditData"></a>  

***
<br><br>[$messages.messageReactionsList](../constructors/messages.messageReactionsList.md) = \['count' => [int](../types/int.md), 'reactions' => \[[MessageUserReaction](../types/MessageUserReaction.md)\], 'users' => \[[User](../types/User.md)\], 'next_offset' => [string](../types/string.md), \];<a name="messages.messageReactionsList"></a>  

***
<br><br>[$messages.messageViews](../constructors/messages.messageViews.md) = \['views' => \[[MessageViews](../types/MessageViews.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.messageViews"></a>  

***
<br><br>[$messages.messages](../constructors/messages.messages.md) = \['messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.messages"></a>  

***
<br><br>[$messages.messagesNotModified](../constructors/messages.messagesNotModified.md) = \['count' => [int](../types/int.md), \];<a name="messages.messagesNotModified"></a>  

***
<br><br>[$messages.messagesSlice](../constructors/messages.messagesSlice.md) = \['inexact' => [Bool](../types/Bool.md), 'count' => [int](../types/int.md), 'next_rate' => [int](../types/int.md), 'offset_id_offset' => [int](../types/int.md), 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.messagesSlice"></a>  

***
<br><br>[$messages.peerDialogs](../constructors/messages.peerDialogs.md) = \['dialogs' => \[[Dialog](../types/Dialog.md)\], 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], 'state' => [updates.State](../types/updates.State.md), \];<a name="messages.peerDialogs"></a>  

***
<br><br>[$messages.peerSettings](../constructors/messages.peerSettings.md) = \['settings' => [PeerSettings](../types/PeerSettings.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.peerSettings"></a>  

***
<br><br>[$messages.recentStickers](../constructors/messages.recentStickers.md) = \['hash' => [long](../types/long.md), 'packs' => \[[StickerPack](../types/StickerPack.md)\], 'stickers' => \[[Document](../types/Document.md)\], 'dates' => \[[int](../types/int.md)\], \];<a name="messages.recentStickers"></a>  

***
<br><br>[$messages.recentStickersNotModified](../constructors/messages.recentStickersNotModified.md) = \[\];<a name="messages.recentStickersNotModified"></a>  

***
<br><br>[$messages.savedGifs](../constructors/messages.savedGifs.md) = \['hash' => [long](../types/long.md), 'gifs' => \[[Document](../types/Document.md)\], \];<a name="messages.savedGifs"></a>  

***
<br><br>[$messages.savedGifsNotModified](../constructors/messages.savedGifsNotModified.md) = \[\];<a name="messages.savedGifsNotModified"></a>  

***
<br><br>[$messages.searchCounter](../constructors/messages.searchCounter.md) = \['inexact' => [Bool](../types/Bool.md), 'filter' => [MessagesFilter](../types/MessagesFilter.md), 'count' => [int](../types/int.md), \];<a name="messages.searchCounter"></a>  

***
<br><br>[$messages.searchResultsCalendar](../constructors/messages.searchResultsCalendar.md) = \['inexact' => [Bool](../types/Bool.md), 'count' => [int](../types/int.md), 'min_date' => [int](../types/int.md), 'min_msg_id' => [int](../types/int.md), 'offset_id_offset' => [int](../types/int.md), 'periods' => \[[SearchResultsCalendarPeriod](../types/SearchResultsCalendarPeriod.md)\], 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.searchResultsCalendar"></a>  

***
<br><br>[$messages.searchResultsPositions](../constructors/messages.searchResultsPositions.md) = \['count' => [int](../types/int.md), 'positions' => \[[SearchResultsPosition](../types/SearchResultsPosition.md)\], \];<a name="messages.searchResultsPositions"></a>  

***
<br><br>[$messages.sentEncryptedFile](../constructors/messages.sentEncryptedFile.md) = \['date' => [int](../types/int.md), 'file' => [EncryptedFile](../types/EncryptedFile.md), \];<a name="messages.sentEncryptedFile"></a>  

***
<br><br>[$messages.sentEncryptedMessage](../constructors/messages.sentEncryptedMessage.md) = \['date' => [int](../types/int.md), \];<a name="messages.sentEncryptedMessage"></a>  

***
<br><br>[$messages.sponsoredMessages](../constructors/messages.sponsoredMessages.md) = \['messages' => \[[SponsoredMessage](../types/SponsoredMessage.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="messages.sponsoredMessages"></a>  

***
<br><br>[$messages.stickerSet](../constructors/messages.stickerSet.md) = \['set' => [StickerSet](../types/StickerSet.md), 'packs' => \[[StickerPack](../types/StickerPack.md)\], 'documents' => \[[Document](../types/Document.md)\], \];<a name="messages.stickerSet"></a>  

***
<br><br>[$messages.stickerSetInstallResultArchive](../constructors/messages.stickerSetInstallResultArchive.md) = \['sets' => \[[StickerSetCovered](../types/StickerSetCovered.md)\], \];<a name="messages.stickerSetInstallResultArchive"></a>  

***
<br><br>[$messages.stickerSetInstallResultSuccess](../constructors/messages.stickerSetInstallResultSuccess.md) = \[\];<a name="messages.stickerSetInstallResultSuccess"></a>  

***
<br><br>[$messages.stickerSetNotModified](../constructors/messages.stickerSetNotModified.md) = \[\];<a name="messages.stickerSetNotModified"></a>  

***
<br><br>[$messages.stickers](../constructors/messages.stickers.md) = \['hash' => [long](../types/long.md), 'stickers' => \[[Document](../types/Document.md)\], \];<a name="messages.stickers"></a>  

***
<br><br>[$messages.stickersNotModified](../constructors/messages.stickersNotModified.md) = \[\];<a name="messages.stickersNotModified"></a>  

***
<br><br>[$messages.votesList](../constructors/messages.votesList.md) = \['count' => [int](../types/int.md), 'votes' => \[[MessageUserVote](../types/MessageUserVote.md)\], 'users' => \[[User](../types/User.md)\], 'next_offset' => [string](../types/string.md), \];<a name="messages.votesList"></a>  

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
<br><br>[$page](../constructors/page.md) = \['part' => [Bool](../types/Bool.md), 'rtl' => [Bool](../types/Bool.md), 'v2' => [Bool](../types/Bool.md), 'url' => [string](../types/string.md), 'blocks' => \[[PageBlock](../types/PageBlock.md)\], 'photos' => \[[Photo](../types/Photo.md)\], 'documents' => \[[Document](../types/Document.md)\], 'views' => [int](../types/int.md), \];<a name="page"></a>  

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
<br><br>[$payments.bankCardData](../constructors/payments.bankCardData.md) = \['title' => [string](../types/string.md), 'open_urls' => \[[BankCardOpenUrl](../types/BankCardOpenUrl.md)\], \];<a name="payments.bankCardData"></a>  

***
<br><br>[$payments.paymentForm](../constructors/payments.paymentForm.md) = \['can_save_credentials' => [Bool](../types/Bool.md), 'password_missing' => [Bool](../types/Bool.md), 'form_id' => [long](../types/long.md), 'bot_id' => [long](../types/long.md), 'invoice' => [Invoice](../types/Invoice.md), 'provider_id' => [long](../types/long.md), 'url' => [string](../types/string.md), 'native_provider' => [string](../types/string.md), 'native_params' => [DataJSON](../types/DataJSON.md), 'saved_info' => [PaymentRequestedInfo](../types/PaymentRequestedInfo.md), 'saved_credentials' => [PaymentSavedCredentials](../types/PaymentSavedCredentials.md), 'users' => \[[User](../types/User.md)\], \];<a name="payments.paymentForm"></a>  

***
<br><br>[$payments.paymentReceipt](../constructors/payments.paymentReceipt.md) = \['date' => [int](../types/int.md), 'bot_id' => [long](../types/long.md), 'provider_id' => [long](../types/long.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'photo' => [WebDocument](../types/WebDocument.md), 'invoice' => [Invoice](../types/Invoice.md), 'info' => [PaymentRequestedInfo](../types/PaymentRequestedInfo.md), 'shipping' => [ShippingOption](../types/ShippingOption.md), 'tip_amount' => [long](../types/long.md), 'currency' => [string](../types/string.md), 'total_amount' => [long](../types/long.md), 'credentials_title' => [string](../types/string.md), 'users' => \[[User](../types/User.md)\], \];<a name="payments.paymentReceipt"></a>  

***
<br><br>[$payments.paymentResult](../constructors/payments.paymentResult.md) = \['updates' => [Updates](../types/Updates.md), \];<a name="payments.paymentResult"></a>  

***
<br><br>[$payments.paymentVerificationNeeded](../constructors/payments.paymentVerificationNeeded.md) = \['url' => [string](../types/string.md), \];<a name="payments.paymentVerificationNeeded"></a>  

***
<br><br>[$payments.savedInfo](../constructors/payments.savedInfo.md) = \['has_saved_credentials' => [Bool](../types/Bool.md), 'saved_info' => [PaymentRequestedInfo](../types/PaymentRequestedInfo.md), \];<a name="payments.savedInfo"></a>  

***
<br><br>[$payments.validatedRequestedInfo](../constructors/payments.validatedRequestedInfo.md) = \['id' => [string](../types/string.md), 'shipping_options' => \[[ShippingOption](../types/ShippingOption.md)\], \];<a name="payments.validatedRequestedInfo"></a>  

***
<br><br>[$peerBlocked](../constructors/peerBlocked.md) = \['peer_id' => [Peer](../types/Peer.md), 'date' => [int](../types/int.md), \];<a name="peerBlocked"></a>  

***
<br><br>[$peerChannel](../constructors/peerChannel.md) = \['channel_id' => [long](../types/long.md), \];<a name="peerChannel"></a>  

***
<br><br>[$peerChat](../constructors/peerChat.md) = \['chat_id' => [long](../types/long.md), \];<a name="peerChat"></a>  

***
<br><br>[$peerLocated](../constructors/peerLocated.md) = \['peer' => [Peer](../types/Peer.md), 'expires' => [int](../types/int.md), 'distance' => [int](../types/int.md), \];<a name="peerLocated"></a>  

***
<br><br>[$peerNotifySettings](../constructors/peerNotifySettings.md) = \['show_previews' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'mute_until' => [int](../types/int.md), 'sound' => [string](../types/string.md), \];<a name="peerNotifySettings"></a>  

***
<br><br>[$peerSelfLocated](../constructors/peerSelfLocated.md) = \['expires' => [int](../types/int.md), \];<a name="peerSelfLocated"></a>  

***
<br><br>[$peerSettings](../constructors/peerSettings.md) = \['report_spam' => [Bool](../types/Bool.md), 'add_contact' => [Bool](../types/Bool.md), 'block_contact' => [Bool](../types/Bool.md), 'share_contact' => [Bool](../types/Bool.md), 'need_contacts_exception' => [Bool](../types/Bool.md), 'report_geo' => [Bool](../types/Bool.md), 'autoarchived' => [Bool](../types/Bool.md), 'invite_members' => [Bool](../types/Bool.md), 'request_chat_broadcast' => [Bool](../types/Bool.md), 'geo_distance' => [int](../types/int.md), 'request_chat_title' => [string](../types/string.md), 'request_chat_date' => [int](../types/int.md), \];<a name="peerSettings"></a>  

***
<br><br>[$peerUser](../constructors/peerUser.md) = \['user_id' => [long](../types/long.md), \];<a name="peerUser"></a>  

***
<br><br>[$phone.exportedGroupCallInvite](../constructors/phone.exportedGroupCallInvite.md) = \['link' => [string](../types/string.md), \];<a name="phone.exportedGroupCallInvite"></a>  

***
<br><br>[$phone.groupCall](../constructors/phone.groupCall.md) = \['call' => [GroupCall](../types/GroupCall.md), 'participants' => \[[GroupCallParticipant](../types/GroupCallParticipant.md)\], 'participants_next_offset' => [string](../types/string.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="phone.groupCall"></a>  

***
<br><br>[$phone.groupParticipants](../constructors/phone.groupParticipants.md) = \['count' => [int](../types/int.md), 'participants' => \[[GroupCallParticipant](../types/GroupCallParticipant.md)\], 'next_offset' => [string](../types/string.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], 'version' => [int](../types/int.md), \];<a name="phone.groupParticipants"></a>  

***
<br><br>[$phone.joinAsPeers](../constructors/phone.joinAsPeers.md) = \['peers' => \[[Peer](../types/Peer.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="phone.joinAsPeers"></a>  

***
<br><br>[$phone.phoneCall](../constructors/phone.phoneCall.md) = \['phone_call' => [PhoneCall](../types/PhoneCall.md), 'users' => \[[User](../types/User.md)\], \];<a name="phone.phoneCall"></a>  

***
<br><br>[$phoneCall](../constructors/phoneCall.md) = \['p2p_allowed' => [Bool](../types/Bool.md), 'video' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [long](../types/long.md), 'participant_id' => [long](../types/long.md), 'g_a_or_b' => [bytes](../types/bytes.md), 'key_fingerprint' => [long](../types/long.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), 'connections' => \[[PhoneConnection](../types/PhoneConnection.md)\], 'start_date' => [int](../types/int.md), \];<a name="phoneCall"></a>  

***
<br><br>[$phoneCallAccepted](../constructors/phoneCallAccepted.md) = \['video' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [long](../types/long.md), 'participant_id' => [long](../types/long.md), 'g_b' => [bytes](../types/bytes.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), \];<a name="phoneCallAccepted"></a>  

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
<br><br>[$phoneCallProtocol](../constructors/phoneCallProtocol.md) = \['udp_p2p' => [Bool](../types/Bool.md), 'udp_reflector' => [Bool](../types/Bool.md), 'min_layer' => [int](../types/int.md), 'max_layer' => [int](../types/int.md), 'library_versions' => \[[string](../types/string.md)\], \];<a name="phoneCallProtocol"></a>  

***
<br><br>[$phoneCallRequested](../constructors/phoneCallRequested.md) = \['video' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [long](../types/long.md), 'participant_id' => [long](../types/long.md), 'g_a_hash' => [bytes](../types/bytes.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), \];<a name="phoneCallRequested"></a>  

***
<br><br>[$phoneCallWaiting](../constructors/phoneCallWaiting.md) = \['video' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'date' => [int](../types/int.md), 'admin_id' => [long](../types/long.md), 'participant_id' => [long](../types/long.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), 'receive_date' => [int](../types/int.md), \];<a name="phoneCallWaiting"></a>  

***
<br><br>[$phoneConnection](../constructors/phoneConnection.md) = \['id' => [long](../types/long.md), 'ip' => [string](../types/string.md), 'ipv6' => [string](../types/string.md), 'port' => [int](../types/int.md), 'peer_tag' => [bytes](../types/bytes.md), \];<a name="phoneConnection"></a>  

***
<br><br>[$phoneConnectionWebrtc](../constructors/phoneConnectionWebrtc.md) = \['turn' => [Bool](../types/Bool.md), 'stun' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'ip' => [string](../types/string.md), 'ipv6' => [string](../types/string.md), 'port' => [int](../types/int.md), 'username' => [string](../types/string.md), 'password' => [string](../types/string.md), \];<a name="phoneConnectionWebrtc"></a>  

***
<br><br>[$photo](../constructors/photo.md) = \['has_stickers' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'file_reference' => [bytes](../types/bytes.md), 'date' => [int](../types/int.md), 'sizes' => \[[PhotoSize](../types/PhotoSize.md)\], 'video_sizes' => \[[VideoSize](../types/VideoSize.md)\], 'dc_id' => [int](../types/int.md), \];<a name="photo"></a>  

***
<br><br>[$photoCachedSize\_23](../constructors/photoCachedSize_23.md) = \['type' => [string](../types/string.md), 'location' => [FileLocation](../types/FileLocation.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \];<a name="photoCachedSize_23"></a>  

***
<br><br>[$photoEmpty](../constructors/photoEmpty.md) = \['id' => [long](../types/long.md), \];<a name="photoEmpty"></a>  

***
<br><br>[$photoPathSize](../constructors/photoPathSize.md) = \['type' => [string](../types/string.md), 'bytes' => [bytes](../types/bytes.md), \];<a name="photoPathSize"></a>  

***
<br><br>[$photoSize\_23](../constructors/photoSize_23.md) = \['type' => [string](../types/string.md), 'location' => [FileLocation](../types/FileLocation.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'size' => [int](../types/int.md), \];<a name="photoSize_23"></a>  

***
<br><br>[$photoSizeEmpty](../constructors/photoSizeEmpty.md) = \['type' => [string](../types/string.md), \];<a name="photoSizeEmpty"></a>  

***
<br><br>[$photoSizeProgressive](../constructors/photoSizeProgressive.md) = \['type' => [string](../types/string.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'sizes' => \[[int](../types/int.md)\], \];<a name="photoSizeProgressive"></a>  

***
<br><br>[$photoStrippedSize](../constructors/photoStrippedSize.md) = \['type' => [string](../types/string.md), 'bytes' => [bytes](../types/bytes.md), \];<a name="photoStrippedSize"></a>  

***
<br><br>[$photos.photo](../constructors/photos.photo.md) = \['photo' => [Photo](../types/Photo.md), 'users' => \[[User](../types/User.md)\], \];<a name="photos.photo"></a>  

***
<br><br>[$photos.photos](../constructors/photos.photos.md) = \['photos' => \[[Photo](../types/Photo.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="photos.photos"></a>  

***
<br><br>[$photos.photosSlice](../constructors/photos.photosSlice.md) = \['count' => [int](../types/int.md), 'photos' => \[[Photo](../types/Photo.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="photos.photosSlice"></a>  

***
<br><br>[$poll](../constructors/poll.md) = \['id' => [long](../types/long.md), 'closed' => [Bool](../types/Bool.md), 'public_voters' => [Bool](../types/Bool.md), 'multiple_choice' => [Bool](../types/Bool.md), 'quiz' => [Bool](../types/Bool.md), 'question' => [string](../types/string.md), 'answers' => \[[PollAnswer](../types/PollAnswer.md)\], 'close_period' => [int](../types/int.md), 'close_date' => [int](../types/int.md), \];<a name="poll"></a>  

***
<br><br>[$pollAnswer](../constructors/pollAnswer.md) = \['text' => [string](../types/string.md), 'option' => [bytes](../types/bytes.md), \];<a name="pollAnswer"></a>  

***
<br><br>[$pollAnswerVoters](../constructors/pollAnswerVoters.md) = \['chosen' => [Bool](../types/Bool.md), 'correct' => [Bool](../types/Bool.md), 'option' => [bytes](../types/bytes.md), 'voters' => [int](../types/int.md), \];<a name="pollAnswerVoters"></a>  

***
<br><br>[$pollResults](../constructors/pollResults.md) = \['min' => [Bool](../types/Bool.md), 'results' => \[[PollAnswerVoters](../types/PollAnswerVoters.md)\], 'total_voters' => [int](../types/int.md), 'recent_voters' => \[[long](../types/long.md)\], 'solution' => [string](../types/string.md), 'solution_entities' => \[[MessageEntity](../types/MessageEntity.md)\], \];<a name="pollResults"></a>  

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
<br><br>[$privacyValueAllowChatParticipants](../constructors/privacyValueAllowChatParticipants.md) = \['chats' => \[[long](../types/long.md)\], \];<a name="privacyValueAllowChatParticipants"></a>  

***
<br><br>[$privacyValueAllowContacts](../constructors/privacyValueAllowContacts.md) = \[\];<a name="privacyValueAllowContacts"></a>  

***
<br><br>[$privacyValueAllowUsers](../constructors/privacyValueAllowUsers.md) = \['users' => \[[long](../types/long.md)\], \];<a name="privacyValueAllowUsers"></a>  

***
<br><br>[$privacyValueDisallowAll](../constructors/privacyValueDisallowAll.md) = \[\];<a name="privacyValueDisallowAll"></a>  

***
<br><br>[$privacyValueDisallowChatParticipants](../constructors/privacyValueDisallowChatParticipants.md) = \['chats' => \[[long](../types/long.md)\], \];<a name="privacyValueDisallowChatParticipants"></a>  

***
<br><br>[$privacyValueDisallowContacts](../constructors/privacyValueDisallowContacts.md) = \[\];<a name="privacyValueDisallowContacts"></a>  

***
<br><br>[$privacyValueDisallowUsers](../constructors/privacyValueDisallowUsers.md) = \['users' => \[[long](../types/long.md)\], \];<a name="privacyValueDisallowUsers"></a>  

***
<br><br>[$reactionCount](../constructors/reactionCount.md) = \['chosen' => [Bool](../types/Bool.md), 'reaction' => [string](../types/string.md), 'count' => [int](../types/int.md), \];<a name="reactionCount"></a>  

***
<br><br>[$receivedNotifyMessage](../constructors/receivedNotifyMessage.md) = \['id' => [int](../types/int.md), \];<a name="receivedNotifyMessage"></a>  

***
<br><br>[$recentMeUrlChat](../constructors/recentMeUrlChat.md) = \['url' => [string](../types/string.md), 'chat_id' => [long](../types/long.md), \];<a name="recentMeUrlChat"></a>  

***
<br><br>[$recentMeUrlChatInvite](../constructors/recentMeUrlChatInvite.md) = \['url' => [string](../types/string.md), 'chat_invite' => [ChatInvite](../types/ChatInvite.md), \];<a name="recentMeUrlChatInvite"></a>  

***
<br><br>[$recentMeUrlStickerSet](../constructors/recentMeUrlStickerSet.md) = \['url' => [string](../types/string.md), 'set' => [StickerSetCovered](../types/StickerSetCovered.md), \];<a name="recentMeUrlStickerSet"></a>  

***
<br><br>[$recentMeUrlUnknown](../constructors/recentMeUrlUnknown.md) = \['url' => [string](../types/string.md), \];<a name="recentMeUrlUnknown"></a>  

***
<br><br>[$recentMeUrlUser](../constructors/recentMeUrlUser.md) = \['url' => [string](../types/string.md), 'user_id' => [long](../types/long.md), \];<a name="recentMeUrlUser"></a>  

***
<br><br>[$replyInlineMarkup](../constructors/replyInlineMarkup.md) = \['rows' => \[[KeyboardButtonRow](../types/KeyboardButtonRow.md)\], \];<a name="replyInlineMarkup"></a>  

***
<br><br>[$replyKeyboardForceReply](../constructors/replyKeyboardForceReply.md) = \['single_use' => [Bool](../types/Bool.md), 'selective' => [Bool](../types/Bool.md), 'placeholder' => [string](../types/string.md), \];<a name="replyKeyboardForceReply"></a>  

***
<br><br>[$replyKeyboardHide](../constructors/replyKeyboardHide.md) = \['selective' => [Bool](../types/Bool.md), \];<a name="replyKeyboardHide"></a>  

***
<br><br>[$replyKeyboardMarkup](../constructors/replyKeyboardMarkup.md) = \['resize' => [Bool](../types/Bool.md), 'single_use' => [Bool](../types/Bool.md), 'selective' => [Bool](../types/Bool.md), 'rows' => \[[KeyboardButtonRow](../types/KeyboardButtonRow.md)\], 'placeholder' => [string](../types/string.md), \];<a name="replyKeyboardMarkup"></a>  

***
<br><br>[$restrictionReason](../constructors/restrictionReason.md) = \['platform' => [string](../types/string.md), 'reason' => [string](../types/string.md), 'text' => [string](../types/string.md), \];<a name="restrictionReason"></a>  

***
<br><br>[$savedPhoneContact](../constructors/savedPhoneContact.md) = \['phone' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'date' => [int](../types/int.md), \];<a name="savedPhoneContact"></a>  

***
<br><br>[$searchResultPosition](../constructors/searchResultPosition.md) = \['msg_id' => [int](../types/int.md), 'date' => [int](../types/int.md), 'offset' => [int](../types/int.md), \];<a name="searchResultPosition"></a>  

***
<br><br>[$searchResultsCalendarPeriod](../constructors/searchResultsCalendarPeriod.md) = \['date' => [int](../types/int.md), 'min_msg_id' => [int](../types/int.md), 'max_msg_id' => [int](../types/int.md), 'count' => [int](../types/int.md), \];<a name="searchResultsCalendarPeriod"></a>  

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
<br><br>[$sendMessageChooseStickerAction](../constructors/sendMessageChooseStickerAction.md) = \[\];<a name="sendMessageChooseStickerAction"></a>  

***
<br><br>[$sendMessageEmojiInteraction](../constructors/sendMessageEmojiInteraction.md) = \['emoticon' => [string](../types/string.md), 'msg_id' => [int](../types/int.md), 'interaction' => [DataJSON](../types/DataJSON.md), \];<a name="sendMessageEmojiInteraction"></a>  

***
<br><br>[$sendMessageEmojiInteractionSeen](../constructors/sendMessageEmojiInteractionSeen.md) = \['emoticon' => [string](../types/string.md), \];<a name="sendMessageEmojiInteractionSeen"></a>  

***
<br><br>[$sendMessageGamePlayAction](../constructors/sendMessageGamePlayAction.md) = \[\];<a name="sendMessageGamePlayAction"></a>  

***
<br><br>[$sendMessageGeoLocationAction](../constructors/sendMessageGeoLocationAction.md) = \[\];<a name="sendMessageGeoLocationAction"></a>  

***
<br><br>[$sendMessageHistoryImportAction](../constructors/sendMessageHistoryImportAction.md) = \['progress' => [int](../types/int.md), \];<a name="sendMessageHistoryImportAction"></a>  

***
<br><br>[$sendMessageRecordAudioAction](../constructors/sendMessageRecordAudioAction.md) = \[\];<a name="sendMessageRecordAudioAction"></a>  

***
<br><br>[$sendMessageRecordRoundAction](../constructors/sendMessageRecordRoundAction.md) = \[\];<a name="sendMessageRecordRoundAction"></a>  

***
<br><br>[$sendMessageRecordVideoAction](../constructors/sendMessageRecordVideoAction.md) = \[\];<a name="sendMessageRecordVideoAction"></a>  

***
<br><br>[$sendMessageTypingAction](../constructors/sendMessageTypingAction.md) = \[\];<a name="sendMessageTypingAction"></a>  

***
<br><br>[$sendMessageUploadAudioAction\_17](../constructors/sendMessageUploadAudioAction_17.md) = \[\];<a name="sendMessageUploadAudioAction_17"></a>  

***
<br><br>[$sendMessageUploadDocumentAction\_17](../constructors/sendMessageUploadDocumentAction_17.md) = \[\];<a name="sendMessageUploadDocumentAction_17"></a>  

***
<br><br>[$sendMessageUploadPhotoAction\_17](../constructors/sendMessageUploadPhotoAction_17.md) = \[\];<a name="sendMessageUploadPhotoAction_17"></a>  

***
<br><br>[$sendMessageUploadRoundAction](../constructors/sendMessageUploadRoundAction.md) = \['progress' => [int](../types/int.md), \];<a name="sendMessageUploadRoundAction"></a>  

***
<br><br>[$sendMessageUploadVideoAction\_17](../constructors/sendMessageUploadVideoAction_17.md) = \[\];<a name="sendMessageUploadVideoAction_17"></a>  

***
<br><br>[$shippingOption](../constructors/shippingOption.md) = \['id' => [string](../types/string.md), 'title' => [string](../types/string.md), 'prices' => \[[LabeledPrice](../types/LabeledPrice.md)\], \];<a name="shippingOption"></a>  

***
<br><br>[$speakingInGroupCallAction](../constructors/speakingInGroupCallAction.md) = \[\];<a name="speakingInGroupCallAction"></a>  

***
<br><br>[$sponsoredMessage](../constructors/sponsoredMessage.md) = \['from_id' => [Peer](../types/Peer.md), 'chat_invite' => [ChatInvite](../types/ChatInvite.md), 'chat_invite_hash' => [string](../types/string.md), 'channel_post' => [int](../types/int.md), 'start_param' => [string](../types/string.md), 'message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \];<a name="sponsoredMessage"></a>  

***
<br><br>[$stats.broadcastStats](../constructors/stats.broadcastStats.md) = \['period' => [StatsDateRangeDays](../types/StatsDateRangeDays.md), 'followers' => [StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md), 'views_per_post' => [StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md), 'shares_per_post' => [StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md), 'enabled_notifications' => [StatsPercentValue](../types/StatsPercentValue.md), 'growth_graph' => [StatsGraph](../types/StatsGraph.md), 'followers_graph' => [StatsGraph](../types/StatsGraph.md), 'mute_graph' => [StatsGraph](../types/StatsGraph.md), 'top_hours_graph' => [StatsGraph](../types/StatsGraph.md), 'interactions_graph' => [StatsGraph](../types/StatsGraph.md), 'iv_interactions_graph' => [StatsGraph](../types/StatsGraph.md), 'views_by_source_graph' => [StatsGraph](../types/StatsGraph.md), 'new_followers_by_source_graph' => [StatsGraph](../types/StatsGraph.md), 'languages_graph' => [StatsGraph](../types/StatsGraph.md), 'recent_message_interactions' => \[[MessageInteractionCounters](../types/MessageInteractionCounters.md)\], \];<a name="stats.broadcastStats"></a>  

***
<br><br>[$stats.megagroupStats](../constructors/stats.megagroupStats.md) = \['period' => [StatsDateRangeDays](../types/StatsDateRangeDays.md), 'members' => [StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md), 'messages' => [StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md), 'viewers' => [StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md), 'posters' => [StatsAbsValueAndPrev](../types/StatsAbsValueAndPrev.md), 'growth_graph' => [StatsGraph](../types/StatsGraph.md), 'members_graph' => [StatsGraph](../types/StatsGraph.md), 'new_members_by_source_graph' => [StatsGraph](../types/StatsGraph.md), 'languages_graph' => [StatsGraph](../types/StatsGraph.md), 'messages_graph' => [StatsGraph](../types/StatsGraph.md), 'actions_graph' => [StatsGraph](../types/StatsGraph.md), 'top_hours_graph' => [StatsGraph](../types/StatsGraph.md), 'weekdays_graph' => [StatsGraph](../types/StatsGraph.md), 'top_posters' => \[[StatsGroupTopPoster](../types/StatsGroupTopPoster.md)\], 'top_admins' => \[[StatsGroupTopAdmin](../types/StatsGroupTopAdmin.md)\], 'top_inviters' => \[[StatsGroupTopInviter](../types/StatsGroupTopInviter.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="stats.megagroupStats"></a>  

***
<br><br>[$stats.messageStats](../constructors/stats.messageStats.md) = \['views_graph' => [StatsGraph](../types/StatsGraph.md), \];<a name="stats.messageStats"></a>  

***
<br><br>[$statsAbsValueAndPrev](../constructors/statsAbsValueAndPrev.md) = \['current' => [double](../types/double.md), 'previous' => [double](../types/double.md), \];<a name="statsAbsValueAndPrev"></a>  

***
<br><br>[$statsDateRangeDays](../constructors/statsDateRangeDays.md) = \['min_date' => [int](../types/int.md), 'max_date' => [int](../types/int.md), \];<a name="statsDateRangeDays"></a>  

***
<br><br>[$statsGraph](../constructors/statsGraph.md) = \['json' => [DataJSON](../types/DataJSON.md), 'zoom_token' => [string](../types/string.md), \];<a name="statsGraph"></a>  

***
<br><br>[$statsGraphAsync](../constructors/statsGraphAsync.md) = \['token' => [string](../types/string.md), \];<a name="statsGraphAsync"></a>  

***
<br><br>[$statsGraphError](../constructors/statsGraphError.md) = \['error' => [string](../types/string.md), \];<a name="statsGraphError"></a>  

***
<br><br>[$statsGroupTopAdmin](../constructors/statsGroupTopAdmin.md) = \['user_id' => [long](../types/long.md), 'deleted' => [int](../types/int.md), 'kicked' => [int](../types/int.md), 'banned' => [int](../types/int.md), \];<a name="statsGroupTopAdmin"></a>  

***
<br><br>[$statsGroupTopInviter](../constructors/statsGroupTopInviter.md) = \['user_id' => [long](../types/long.md), 'invitations' => [int](../types/int.md), \];<a name="statsGroupTopInviter"></a>  

***
<br><br>[$statsGroupTopPoster](../constructors/statsGroupTopPoster.md) = \['user_id' => [long](../types/long.md), 'messages' => [int](../types/int.md), 'avg_chars' => [int](../types/int.md), \];<a name="statsGroupTopPoster"></a>  

***
<br><br>[$statsPercentValue](../constructors/statsPercentValue.md) = \['part' => [double](../types/double.md), 'total' => [double](../types/double.md), \];<a name="statsPercentValue"></a>  

***
<br><br>[$statsURL](../constructors/statsURL.md) = \['url' => [string](../types/string.md), \];<a name="statsURL"></a>  

***
<br><br>[$stickerPack](../constructors/stickerPack.md) = \['emoticon' => [string](../types/string.md), 'documents' => \[[long](../types/long.md)\], \];<a name="stickerPack"></a>  

***
<br><br>[$stickerSet](../constructors/stickerSet.md) = \['archived' => [Bool](../types/Bool.md), 'official' => [Bool](../types/Bool.md), 'masks' => [Bool](../types/Bool.md), 'animated' => [Bool](../types/Bool.md), 'installed_date' => [int](../types/int.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'title' => [string](../types/string.md), 'short_name' => [string](../types/string.md), 'thumbs' => \[[PhotoSize](../types/PhotoSize.md)\], 'thumb_dc_id' => [int](../types/int.md), 'thumb_version' => [int](../types/int.md), 'count' => [int](../types/int.md), 'hash' => [int](../types/int.md), \];<a name="stickerSet"></a>  

***
<br><br>[$stickerSetCovered](../constructors/stickerSetCovered.md) = \['set' => [StickerSet](../types/StickerSet.md), 'cover' => [Document](../types/Document.md), \];<a name="stickerSetCovered"></a>  

***
<br><br>[$stickerSetMultiCovered](../constructors/stickerSetMultiCovered.md) = \['set' => [StickerSet](../types/StickerSet.md), 'covers' => \[[Document](../types/Document.md)\], \];<a name="stickerSetMultiCovered"></a>  

***
<br><br>[$stickers.suggestedShortName](../constructors/stickers.suggestedShortName.md) = \['short_name' => [string](../types/string.md), \];<a name="stickers.suggestedShortName"></a>  

***
<br><br>[$storage.fileGif](../constructors/storage.fileGif.md) = \[\];<a name="storage.fileGif"></a>  

***
<br><br>[$storage.fileJpeg](../constructors/storage.fileJpeg.md) = \[\];<a name="storage.fileJpeg"></a>  

***
<br><br>[$storage.fileMov](../constructors/storage.fileMov.md) = \[\];<a name="storage.fileMov"></a>  

***
<br><br>[$storage.fileMp3](../constructors/storage.fileMp3.md) = \[\];<a name="storage.fileMp3"></a>  

***
<br><br>[$storage.fileMp4](../constructors/storage.fileMp4.md) = \[\];<a name="storage.fileMp4"></a>  

***
<br><br>[$storage.filePartial](../constructors/storage.filePartial.md) = \[\];<a name="storage.filePartial"></a>  

***
<br><br>[$storage.filePdf](../constructors/storage.filePdf.md) = \[\];<a name="storage.filePdf"></a>  

***
<br><br>[$storage.filePng](../constructors/storage.filePng.md) = \[\];<a name="storage.filePng"></a>  

***
<br><br>[$storage.fileUnknown](../constructors/storage.fileUnknown.md) = \[\];<a name="storage.fileUnknown"></a>  

***
<br><br>[$storage.fileWebp](../constructors/storage.fileWebp.md) = \[\];<a name="storage.fileWebp"></a>  

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
<br><br>[$theme](../constructors/theme.md) = \['creator' => [Bool](../types/Bool.md), 'default' => [Bool](../types/Bool.md), 'for_chat' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'slug' => [string](../types/string.md), 'title' => [string](../types/string.md), 'document' => [Document](../types/Document.md), 'settings' => \[[ThemeSettings](../types/ThemeSettings.md)\], 'emoticon' => [string](../types/string.md), 'installs_count' => [int](../types/int.md), \];<a name="theme"></a>  

***
<br><br>[$themeSettings](../constructors/themeSettings.md) = \['message_colors_animated' => [Bool](../types/Bool.md), 'base_theme' => [BaseTheme](../types/BaseTheme.md), 'accent_color' => [int](../types/int.md), 'outbox_accent_color' => [int](../types/int.md), 'message_colors' => \[[int](../types/int.md)\], 'wallpaper' => [WallPaper](../types/WallPaper.md), \];<a name="themeSettings"></a>  

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
<br><br>[$updateBotCallbackQuery](../constructors/updateBotCallbackQuery.md) = \['query_id' => [long](../types/long.md), 'user_id' => [long](../types/long.md), 'peer' => [Peer](../types/Peer.md), 'msg_id' => [int](../types/int.md), 'chat_instance' => [long](../types/long.md), 'data' => [bytes](../types/bytes.md), 'game_short_name' => [string](../types/string.md), \];<a name="updateBotCallbackQuery"></a>  

***
<br><br>[$updateBotChatInviteRequester](../constructors/updateBotChatInviteRequester.md) = \['peer' => [Peer](../types/Peer.md), 'date' => [int](../types/int.md), 'user_id' => [long](../types/long.md), 'about' => [string](../types/string.md), 'invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'qts' => [int](../types/int.md), \];<a name="updateBotChatInviteRequester"></a>  

***
<br><br>[$updateBotCommands](../constructors/updateBotCommands.md) = \['peer' => [Peer](../types/Peer.md), 'bot_id' => [long](../types/long.md), 'commands' => \[[BotCommand](../types/BotCommand.md)\], \];<a name="updateBotCommands"></a>  

***
<br><br>[$updateBotInlineQuery](../constructors/updateBotInlineQuery.md) = \['query_id' => [long](../types/long.md), 'user_id' => [long](../types/long.md), 'query' => [string](../types/string.md), 'geo' => [GeoPoint](../types/GeoPoint.md), 'peer_type' => [InlineQueryPeerType](../types/InlineQueryPeerType.md), 'offset' => [string](../types/string.md), \];<a name="updateBotInlineQuery"></a>  

***
<br><br>[$updateBotInlineSend](../constructors/updateBotInlineSend.md) = \['user_id' => [long](../types/long.md), 'query' => [string](../types/string.md), 'geo' => [GeoPoint](../types/GeoPoint.md), 'id' => [string](../types/string.md), 'msg_id' => [InputBotInlineMessageID](../types/InputBotInlineMessageID.md), \];<a name="updateBotInlineSend"></a>  

***
<br><br>[$updateBotPrecheckoutQuery](../constructors/updateBotPrecheckoutQuery.md) = \['query_id' => [long](../types/long.md), 'user_id' => [long](../types/long.md), 'payload' => [bytes](../types/bytes.md), 'info' => [PaymentRequestedInfo](../types/PaymentRequestedInfo.md), 'shipping_option_id' => [string](../types/string.md), 'currency' => [string](../types/string.md), 'total_amount' => [long](../types/long.md), \];<a name="updateBotPrecheckoutQuery"></a>  

***
<br><br>[$updateBotShippingQuery](../constructors/updateBotShippingQuery.md) = \['query_id' => [long](../types/long.md), 'user_id' => [long](../types/long.md), 'payload' => [bytes](../types/bytes.md), 'shipping_address' => [PostAddress](../types/PostAddress.md), \];<a name="updateBotShippingQuery"></a>  

***
<br><br>[$updateBotStopped](../constructors/updateBotStopped.md) = \['user_id' => [long](../types/long.md), 'date' => [int](../types/int.md), 'stopped' => [Bool](../types/Bool.md), 'qts' => [int](../types/int.md), \];<a name="updateBotStopped"></a>  

***
<br><br>[$updateBotWebhookJSON](../constructors/updateBotWebhookJSON.md) = \['data' => [DataJSON](../types/DataJSON.md), \];<a name="updateBotWebhookJSON"></a>  

***
<br><br>[$updateBotWebhookJSONQuery](../constructors/updateBotWebhookJSONQuery.md) = \['query_id' => [long](../types/long.md), 'data' => [DataJSON](../types/DataJSON.md), 'timeout' => [int](../types/int.md), \];<a name="updateBotWebhookJSONQuery"></a>  

***
<br><br>[$updateChannel](../constructors/updateChannel.md) = \['channel_id' => [long](../types/long.md), \];<a name="updateChannel"></a>  

***
<br><br>[$updateChannelAvailableMessages](../constructors/updateChannelAvailableMessages.md) = \['channel_id' => [long](../types/long.md), 'available_min_id' => [int](../types/int.md), \];<a name="updateChannelAvailableMessages"></a>  

***
<br><br>[$updateChannelMessageForwards](../constructors/updateChannelMessageForwards.md) = \['channel_id' => [long](../types/long.md), 'id' => [int](../types/int.md), 'forwards' => [int](../types/int.md), \];<a name="updateChannelMessageForwards"></a>  

***
<br><br>[$updateChannelMessageViews](../constructors/updateChannelMessageViews.md) = \['channel_id' => [long](../types/long.md), 'id' => [int](../types/int.md), 'views' => [int](../types/int.md), \];<a name="updateChannelMessageViews"></a>  

***
<br><br>[$updateChannelParticipant](../constructors/updateChannelParticipant.md) = \['channel_id' => [long](../types/long.md), 'date' => [int](../types/int.md), 'actor_id' => [long](../types/long.md), 'user_id' => [long](../types/long.md), 'prev_participant' => [ChannelParticipant](../types/ChannelParticipant.md), 'new_participant' => [ChannelParticipant](../types/ChannelParticipant.md), 'invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'qts' => [int](../types/int.md), \];<a name="updateChannelParticipant"></a>  

***
<br><br>[$updateChannelReadMessagesContents](../constructors/updateChannelReadMessagesContents.md) = \['channel_id' => [long](../types/long.md), 'messages' => \[[int](../types/int.md)\], \];<a name="updateChannelReadMessagesContents"></a>  

***
<br><br>[$updateChannelTooLong](../constructors/updateChannelTooLong.md) = \['channel_id' => [long](../types/long.md), 'pts' => [int](../types/int.md), \];<a name="updateChannelTooLong"></a>  

***
<br><br>[$updateChannelUserTyping](../constructors/updateChannelUserTyping.md) = \['channel_id' => [long](../types/long.md), 'top_msg_id' => [int](../types/int.md), 'from_id' => [Peer](../types/Peer.md), 'action' => [SendMessageAction](../types/SendMessageAction.md), \];<a name="updateChannelUserTyping"></a>  

***
<br><br>[$updateChannelWebPage](../constructors/updateChannelWebPage.md) = \['channel_id' => [long](../types/long.md), 'webpage' => [WebPage](../types/WebPage.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateChannelWebPage"></a>  

***
<br><br>[$updateChat](../constructors/updateChat.md) = \['chat_id' => [long](../types/long.md), \];<a name="updateChat"></a>  

***
<br><br>[$updateChatDefaultBannedRights](../constructors/updateChatDefaultBannedRights.md) = \['peer' => [Peer](../types/Peer.md), 'default_banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), 'version' => [int](../types/int.md), \];<a name="updateChatDefaultBannedRights"></a>  

***
<br><br>[$updateChatParticipant](../constructors/updateChatParticipant.md) = \['chat_id' => [long](../types/long.md), 'date' => [int](../types/int.md), 'actor_id' => [long](../types/long.md), 'user_id' => [long](../types/long.md), 'prev_participant' => [ChatParticipant](../types/ChatParticipant.md), 'new_participant' => [ChatParticipant](../types/ChatParticipant.md), 'invite' => [ExportedChatInvite](../types/ExportedChatInvite.md), 'qts' => [int](../types/int.md), \];<a name="updateChatParticipant"></a>  

***
<br><br>[$updateChatParticipantAdd](../constructors/updateChatParticipantAdd.md) = \['chat_id' => [long](../types/long.md), 'user_id' => [long](../types/long.md), 'inviter_id' => [long](../types/long.md), 'date' => [int](../types/int.md), 'version' => [int](../types/int.md), \];<a name="updateChatParticipantAdd"></a>  

***
<br><br>[$updateChatParticipantAdmin](../constructors/updateChatParticipantAdmin.md) = \['chat_id' => [long](../types/long.md), 'user_id' => [long](../types/long.md), 'is_admin' => [Bool](../types/Bool.md), 'version' => [int](../types/int.md), \];<a name="updateChatParticipantAdmin"></a>  

***
<br><br>[$updateChatParticipantDelete](../constructors/updateChatParticipantDelete.md) = \['chat_id' => [long](../types/long.md), 'user_id' => [long](../types/long.md), 'version' => [int](../types/int.md), \];<a name="updateChatParticipantDelete"></a>  

***
<br><br>[$updateChatParticipants](../constructors/updateChatParticipants.md) = \['participants' => [ChatParticipants](../types/ChatParticipants.md), \];<a name="updateChatParticipants"></a>  

***
<br><br>[$updateChatUserTyping](../constructors/updateChatUserTyping.md) = \['chat_id' => [long](../types/long.md), 'from_id' => [Peer](../types/Peer.md), 'action' => [SendMessageAction](../types/SendMessageAction.md), \];<a name="updateChatUserTyping"></a>  

***
<br><br>[$updateConfig](../constructors/updateConfig.md) = \[\];<a name="updateConfig"></a>  

***
<br><br>[$updateContactsReset](../constructors/updateContactsReset.md) = \[\];<a name="updateContactsReset"></a>  

***
<br><br>[$updateDcOptions](../constructors/updateDcOptions.md) = \['dc_options' => \[[DcOption](../types/DcOption.md)\], \];<a name="updateDcOptions"></a>  

***
<br><br>[$updateDeleteChannelMessages](../constructors/updateDeleteChannelMessages.md) = \['channel_id' => [long](../types/long.md), 'messages' => \[[int](../types/int.md)\], 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateDeleteChannelMessages"></a>  

***
<br><br>[$updateDeleteMessages](../constructors/updateDeleteMessages.md) = \['messages' => \[[int](../types/int.md)\], 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateDeleteMessages"></a>  

***
<br><br>[$updateDeleteScheduledMessages](../constructors/updateDeleteScheduledMessages.md) = \['peer' => [Peer](../types/Peer.md), 'messages' => \[[int](../types/int.md)\], \];<a name="updateDeleteScheduledMessages"></a>  

***
<br><br>[$updateDialogFilter](../constructors/updateDialogFilter.md) = \['id' => [int](../types/int.md), 'filter' => [DialogFilter](../types/DialogFilter.md), \];<a name="updateDialogFilter"></a>  

***
<br><br>[$updateDialogFilterOrder](../constructors/updateDialogFilterOrder.md) = \['order' => \[[int](../types/int.md)\], \];<a name="updateDialogFilterOrder"></a>  

***
<br><br>[$updateDialogFilters](../constructors/updateDialogFilters.md) = \[\];<a name="updateDialogFilters"></a>  

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
<br><br>[$updateGeoLiveViewed](../constructors/updateGeoLiveViewed.md) = \['peer' => [Peer](../types/Peer.md), 'msg_id' => [int](../types/int.md), \];<a name="updateGeoLiveViewed"></a>  

***
<br><br>[$updateGroupCall](../constructors/updateGroupCall.md) = \['chat_id' => [long](../types/long.md), 'call' => [GroupCall](../types/GroupCall.md), \];<a name="updateGroupCall"></a>  

***
<br><br>[$updateGroupCallConnection](../constructors/updateGroupCallConnection.md) = \['presentation' => [Bool](../types/Bool.md), 'params' => [DataJSON](../types/DataJSON.md), \];<a name="updateGroupCallConnection"></a>  

***
<br><br>[$updateGroupCallParticipants](../constructors/updateGroupCallParticipants.md) = \['call' => [InputGroupCall](../types/InputGroupCall.md), 'participants' => \[[GroupCallParticipant](../types/GroupCallParticipant.md)\], 'version' => [int](../types/int.md), \];<a name="updateGroupCallParticipants"></a>  

***
<br><br>[$updateInlineBotCallbackQuery](../constructors/updateInlineBotCallbackQuery.md) = \['query_id' => [long](../types/long.md), 'user_id' => [long](../types/long.md), 'msg_id' => [InputBotInlineMessageID](../types/InputBotInlineMessageID.md), 'chat_instance' => [long](../types/long.md), 'data' => [bytes](../types/bytes.md), 'game_short_name' => [string](../types/string.md), \];<a name="updateInlineBotCallbackQuery"></a>  

***
<br><br>[$updateLangPack](../constructors/updateLangPack.md) = \['difference' => [LangPackDifference](../types/LangPackDifference.md), \];<a name="updateLangPack"></a>  

***
<br><br>[$updateLangPackTooLong](../constructors/updateLangPackTooLong.md) = \['lang_code' => [string](../types/string.md), \];<a name="updateLangPackTooLong"></a>  

***
<br><br>[$updateLoginToken](../constructors/updateLoginToken.md) = \[\];<a name="updateLoginToken"></a>  

***
<br><br>[$updateMessageID](../constructors/updateMessageID.md) = \['id' => [int](../types/int.md), \];<a name="updateMessageID"></a>  

***
<br><br>[$updateMessagePoll](../constructors/updateMessagePoll.md) = \['poll_id' => [long](../types/long.md), 'poll' => [Poll](../types/Poll.md), 'results' => [PollResults](../types/PollResults.md), \];<a name="updateMessagePoll"></a>  

***
<br><br>[$updateMessagePollVote](../constructors/updateMessagePollVote.md) = \['poll_id' => [long](../types/long.md), 'user_id' => [long](../types/long.md), 'options' => \[[bytes](../types/bytes.md)\], 'qts' => [int](../types/int.md), \];<a name="updateMessagePollVote"></a>  

***
<br><br>[$updateMessageReactions](../constructors/updateMessageReactions.md) = \['peer' => [Peer](../types/Peer.md), 'msg_id' => [int](../types/int.md), 'reactions' => [MessageReactions](../types/MessageReactions.md), \];<a name="updateMessageReactions"></a>  

***
<br><br>[$updateNewChannelMessage](../constructors/updateNewChannelMessage.md) = \['message' => [Message](../types/Message.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateNewChannelMessage"></a>  

***
<br><br>[$updateNewEncryptedMessage](../constructors/updateNewEncryptedMessage.md) = \['message' => [EncryptedMessage](../types/EncryptedMessage.md), 'qts' => [int](../types/int.md), \];<a name="updateNewEncryptedMessage"></a>  

***
<br><br>[$updateNewMessage](../constructors/updateNewMessage.md) = \['message' => [Message](../types/Message.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateNewMessage"></a>  

***
<br><br>[$updateNewScheduledMessage](../constructors/updateNewScheduledMessage.md) = \['message' => [Message](../types/Message.md), \];<a name="updateNewScheduledMessage"></a>  

***
<br><br>[$updateNewStickerSet](../constructors/updateNewStickerSet.md) = \['stickerset' => [messages.StickerSet](../types/messages.StickerSet.md), \];<a name="updateNewStickerSet"></a>  

***
<br><br>[$updateNotifySettings](../constructors/updateNotifySettings.md) = \['peer' => [NotifyPeer](../types/NotifyPeer.md), 'notify_settings' => [PeerNotifySettings](../types/PeerNotifySettings.md), \];<a name="updateNotifySettings"></a>  

***
<br><br>[$updatePeerBlocked](../constructors/updatePeerBlocked.md) = \['peer_id' => [Peer](../types/Peer.md), 'blocked' => [Bool](../types/Bool.md), \];<a name="updatePeerBlocked"></a>  

***
<br><br>[$updatePeerHistoryTTL](../constructors/updatePeerHistoryTTL.md) = \['peer' => [Peer](../types/Peer.md), 'ttl_period' => [int](../types/int.md), \];<a name="updatePeerHistoryTTL"></a>  

***
<br><br>[$updatePeerLocated](../constructors/updatePeerLocated.md) = \['peers' => \[[PeerLocated](../types/PeerLocated.md)\], \];<a name="updatePeerLocated"></a>  

***
<br><br>[$updatePeerSettings](../constructors/updatePeerSettings.md) = \['peer' => [Peer](../types/Peer.md), 'settings' => [PeerSettings](../types/PeerSettings.md), \];<a name="updatePeerSettings"></a>  

***
<br><br>[$updatePendingJoinRequests](../constructors/updatePendingJoinRequests.md) = \['peer' => [Peer](../types/Peer.md), 'requests_pending' => [int](../types/int.md), 'recent_requesters' => \[[long](../types/long.md)\], \];<a name="updatePendingJoinRequests"></a>  

***
<br><br>[$updatePhoneCall](../constructors/updatePhoneCall.md) = \['phone_call' => [PhoneCall](../types/PhoneCall.md), \];<a name="updatePhoneCall"></a>  

***
<br><br>[$updatePhoneCallSignalingData](../constructors/updatePhoneCallSignalingData.md) = \['phone_call_id' => [long](../types/long.md), 'data' => [bytes](../types/bytes.md), \];<a name="updatePhoneCallSignalingData"></a>  

***
<br><br>[$updatePinnedChannelMessages](../constructors/updatePinnedChannelMessages.md) = \['pinned' => [Bool](../types/Bool.md), 'channel_id' => [long](../types/long.md), 'messages' => \[[int](../types/int.md)\], 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updatePinnedChannelMessages"></a>  

***
<br><br>[$updatePinnedDialogs](../constructors/updatePinnedDialogs.md) = \['folder_id' => [int](../types/int.md), 'order' => \[[DialogPeer](../types/DialogPeer.md)\], \];<a name="updatePinnedDialogs"></a>  

***
<br><br>[$updatePinnedMessages](../constructors/updatePinnedMessages.md) = \['pinned' => [Bool](../types/Bool.md), 'peer' => [Peer](../types/Peer.md), 'messages' => \[[int](../types/int.md)\], 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updatePinnedMessages"></a>  

***
<br><br>[$updatePrivacy](../constructors/updatePrivacy.md) = \['key' => [PrivacyKey](../types/PrivacyKey.md), 'rules' => \[[PrivacyRule](../types/PrivacyRule.md)\], \];<a name="updatePrivacy"></a>  

***
<br><br>[$updatePtsChanged](../constructors/updatePtsChanged.md) = \[\];<a name="updatePtsChanged"></a>  

***
<br><br>[$updateReadChannelDiscussionInbox](../constructors/updateReadChannelDiscussionInbox.md) = \['channel_id' => [long](../types/long.md), 'top_msg_id' => [int](../types/int.md), 'read_max_id' => [int](../types/int.md), 'broadcast_id' => [long](../types/long.md), 'broadcast_post' => [int](../types/int.md), \];<a name="updateReadChannelDiscussionInbox"></a>  

***
<br><br>[$updateReadChannelDiscussionOutbox](../constructors/updateReadChannelDiscussionOutbox.md) = \['channel_id' => [long](../types/long.md), 'top_msg_id' => [int](../types/int.md), 'read_max_id' => [int](../types/int.md), \];<a name="updateReadChannelDiscussionOutbox"></a>  

***
<br><br>[$updateReadChannelInbox](../constructors/updateReadChannelInbox.md) = \['folder_id' => [int](../types/int.md), 'channel_id' => [long](../types/long.md), 'max_id' => [int](../types/int.md), 'still_unread_count' => [int](../types/int.md), 'pts' => [int](../types/int.md), \];<a name="updateReadChannelInbox"></a>  

***
<br><br>[$updateReadChannelOutbox](../constructors/updateReadChannelOutbox.md) = \['channel_id' => [long](../types/long.md), 'max_id' => [int](../types/int.md), \];<a name="updateReadChannelOutbox"></a>  

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
<br><br>[$updateShortChatMessage](../constructors/updateShortChatMessage.md) = \['out' => [Bool](../types/Bool.md), 'mentioned' => [Bool](../types/Bool.md), 'media_unread' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'from_id' => [long](../types/long.md), 'chat_id' => [long](../types/long.md), 'message' => [string](../types/string.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), 'date' => [int](../types/int.md), 'fwd_from' => [MessageFwdHeader](../types/MessageFwdHeader.md), 'via_bot_id' => [long](../types/long.md), 'reply_to' => [MessageReplyHeader](../types/MessageReplyHeader.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'ttl_period' => [int](../types/int.md), \];<a name="updateShortChatMessage"></a>  

***
<br><br>[$updateShortMessage](../constructors/updateShortMessage.md) = \['out' => [Bool](../types/Bool.md), 'mentioned' => [Bool](../types/Bool.md), 'media_unread' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'user_id' => [long](../types/long.md), 'message' => [string](../types/string.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), 'date' => [int](../types/int.md), 'fwd_from' => [MessageFwdHeader](../types/MessageFwdHeader.md), 'via_bot_id' => [long](../types/long.md), 'reply_to' => [MessageReplyHeader](../types/MessageReplyHeader.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'ttl_period' => [int](../types/int.md), \];<a name="updateShortMessage"></a>  

***
<br><br>[$updateShortSentMessage](../constructors/updateShortSentMessage.md) = \['out' => [Bool](../types/Bool.md), 'id' => [int](../types/int.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), 'date' => [int](../types/int.md), 'media' => [MessageMedia](../types/MessageMedia.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'ttl_period' => [int](../types/int.md), \];<a name="updateShortSentMessage"></a>  

***
<br><br>[$updateStickerSets](../constructors/updateStickerSets.md) = \[\];<a name="updateStickerSets"></a>  

***
<br><br>[$updateStickerSetsOrder](../constructors/updateStickerSetsOrder.md) = \['masks' => [Bool](../types/Bool.md), 'order' => \[[long](../types/long.md)\], \];<a name="updateStickerSetsOrder"></a>  

***
<br><br>[$updateTheme](../constructors/updateTheme.md) = \['theme' => [Theme](../types/Theme.md), \];<a name="updateTheme"></a>  

***
<br><br>[$updateUserName](../constructors/updateUserName.md) = \['user_id' => [long](../types/long.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'username' => [string](../types/string.md), \];<a name="updateUserName"></a>  

***
<br><br>[$updateUserPhone](../constructors/updateUserPhone.md) = \['user_id' => [long](../types/long.md), 'phone' => [string](../types/string.md), \];<a name="updateUserPhone"></a>  

***
<br><br>[$updateUserPhoto](../constructors/updateUserPhoto.md) = \['user_id' => [long](../types/long.md), 'date' => [int](../types/int.md), 'photo' => [UserProfilePhoto](../types/UserProfilePhoto.md), 'previous' => [Bool](../types/Bool.md), \];<a name="updateUserPhoto"></a>  

***
<br><br>[$updateUserStatus](../constructors/updateUserStatus.md) = \['user_id' => [long](../types/long.md), 'status' => [UserStatus](../types/UserStatus.md), \];<a name="updateUserStatus"></a>  

***
<br><br>[$updateUserTyping](../constructors/updateUserTyping.md) = \['user_id' => [long](../types/long.md), 'action' => [SendMessageAction](../types/SendMessageAction.md), \];<a name="updateUserTyping"></a>  

***
<br><br>[$updateWebPage](../constructors/updateWebPage.md) = \['webpage' => [WebPage](../types/WebPage.md), 'pts' => [int](../types/int.md), 'pts_count' => [int](../types/int.md), \];<a name="updateWebPage"></a>  

***
<br><br>[$updates](../constructors/updates.md) = \['updates' => \[[Update](../types/Update.md)\], 'users' => \[[User](../types/User.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'date' => [int](../types/int.md), 'seq' => [int](../types/int.md), \];<a name="updates"></a>  

***
<br><br>[$updates.channelDifference](../constructors/updates.channelDifference.md) = \['final' => [Bool](../types/Bool.md), 'pts' => [int](../types/int.md), 'timeout' => [int](../types/int.md), 'new_messages' => \[[Message](../types/Message.md)\], 'other_updates' => \[[Update](../types/Update.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="updates.channelDifference"></a>  

***
<br><br>[$updates.channelDifferenceEmpty](../constructors/updates.channelDifferenceEmpty.md) = \['final' => [Bool](../types/Bool.md), 'pts' => [int](../types/int.md), 'timeout' => [int](../types/int.md), \];<a name="updates.channelDifferenceEmpty"></a>  

***
<br><br>[$updates.channelDifferenceTooLong](../constructors/updates.channelDifferenceTooLong.md) = \['final' => [Bool](../types/Bool.md), 'timeout' => [int](../types/int.md), 'dialog' => [Dialog](../types/Dialog.md), 'messages' => \[[Message](../types/Message.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="updates.channelDifferenceTooLong"></a>  

***
<br><br>[$updates.difference](../constructors/updates.difference.md) = \['new_messages' => \[[Message](../types/Message.md)\], 'new_encrypted_messages' => \[[EncryptedMessage](../types/EncryptedMessage.md)\], 'other_updates' => \[[Update](../types/Update.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], 'state' => [updates.State](../types/updates.State.md), \];<a name="updates.difference"></a>  

***
<br><br>[$updates.differenceEmpty](../constructors/updates.differenceEmpty.md) = \['date' => [int](../types/int.md), 'seq' => [int](../types/int.md), \];<a name="updates.differenceEmpty"></a>  

***
<br><br>[$updates.differenceSlice](../constructors/updates.differenceSlice.md) = \['new_messages' => \[[Message](../types/Message.md)\], 'new_encrypted_messages' => \[[EncryptedMessage](../types/EncryptedMessage.md)\], 'other_updates' => \[[Update](../types/Update.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], 'intermediate_state' => [updates.State](../types/updates.State.md), \];<a name="updates.differenceSlice"></a>  

***
<br><br>[$updates.differenceTooLong](../constructors/updates.differenceTooLong.md) = \['pts' => [int](../types/int.md), \];<a name="updates.differenceTooLong"></a>  

***
<br><br>[$updates.state](../constructors/updates.state.md) = \['pts' => [int](../types/int.md), 'qts' => [int](../types/int.md), 'date' => [int](../types/int.md), 'seq' => [int](../types/int.md), 'unread_count' => [int](../types/int.md), \];<a name="updates.state"></a>  

***
<br><br>[$updatesCombined](../constructors/updatesCombined.md) = \['updates' => \[[Update](../types/Update.md)\], 'users' => \[[User](../types/User.md)\], 'chats' => \[[Chat](../types/Chat.md)\], 'date' => [int](../types/int.md), 'seq_start' => [int](../types/int.md), 'seq' => [int](../types/int.md), \];<a name="updatesCombined"></a>  

***
<br><br>[$updatesTooLong](../constructors/updatesTooLong.md) = \[\];<a name="updatesTooLong"></a>  

***
<br><br>[$upload.cdnFile](../constructors/upload.cdnFile.md) = \['bytes' => [bytes](../types/bytes.md), \];<a name="upload.cdnFile"></a>  

***
<br><br>[$upload.cdnFileReuploadNeeded](../constructors/upload.cdnFileReuploadNeeded.md) = \['request_token' => [bytes](../types/bytes.md), \];<a name="upload.cdnFileReuploadNeeded"></a>  

***
<br><br>[$upload.file](../constructors/upload.file.md) = \['type' => [storage.FileType](../types/storage.FileType.md), 'mtime' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \];<a name="upload.file"></a>  

***
<br><br>[$upload.fileCdnRedirect](../constructors/upload.fileCdnRedirect.md) = \['dc_id' => [int](../types/int.md), 'file_token' => [bytes](../types/bytes.md), 'encryption_key' => [bytes](../types/bytes.md), 'encryption_iv' => [bytes](../types/bytes.md), 'file_hashes' => \[[FileHash](../types/FileHash.md)\], \];<a name="upload.fileCdnRedirect"></a>  

***
<br><br>[$upload.webFile](../constructors/upload.webFile.md) = \['size' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'file_type' => [storage.FileType](../types/storage.FileType.md), 'mtime' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \];<a name="upload.webFile"></a>  

***
<br><br>[$urlAuthResultAccepted](../constructors/urlAuthResultAccepted.md) = \['url' => [string](../types/string.md), \];<a name="urlAuthResultAccepted"></a>  

***
<br><br>[$urlAuthResultDefault](../constructors/urlAuthResultDefault.md) = \[\];<a name="urlAuthResultDefault"></a>  

***
<br><br>[$urlAuthResultRequest](../constructors/urlAuthResultRequest.md) = \['request_write_access' => [Bool](../types/Bool.md), 'bot' => [User](../types/User.md), 'domain' => [string](../types/string.md), \];<a name="urlAuthResultRequest"></a>  

***
<br><br>[$user](../constructors/user.md) = \['self' => [Bool](../types/Bool.md), 'contact' => [Bool](../types/Bool.md), 'mutual_contact' => [Bool](../types/Bool.md), 'deleted' => [Bool](../types/Bool.md), 'bot' => [Bool](../types/Bool.md), 'bot_chat_history' => [Bool](../types/Bool.md), 'bot_nochats' => [Bool](../types/Bool.md), 'verified' => [Bool](../types/Bool.md), 'restricted' => [Bool](../types/Bool.md), 'min' => [Bool](../types/Bool.md), 'bot_inline_geo' => [Bool](../types/Bool.md), 'support' => [Bool](../types/Bool.md), 'scam' => [Bool](../types/Bool.md), 'apply_min_photo' => [Bool](../types/Bool.md), 'fake' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'access_hash' => [long](../types/long.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'username' => [string](../types/string.md), 'phone' => [string](../types/string.md), 'photo' => [UserProfilePhoto](../types/UserProfilePhoto.md), 'status' => [UserStatus](../types/UserStatus.md), 'bot_info_version' => [int](../types/int.md), 'restriction_reason' => \[[RestrictionReason](../types/RestrictionReason.md)\], 'bot_inline_placeholder' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), \];<a name="user"></a>  

***
<br><br>[$userEmpty](../constructors/userEmpty.md) = \['id' => [long](../types/long.md), \];<a name="userEmpty"></a>  

***
<br><br>[$userFull](../constructors/userFull.md) = \['blocked' => [Bool](../types/Bool.md), 'phone_calls_available' => [Bool](../types/Bool.md), 'phone_calls_private' => [Bool](../types/Bool.md), 'can_pin_message' => [Bool](../types/Bool.md), 'has_scheduled' => [Bool](../types/Bool.md), 'video_calls_available' => [Bool](../types/Bool.md), 'id' => [long](../types/long.md), 'about' => [string](../types/string.md), 'settings' => [PeerSettings](../types/PeerSettings.md), 'profile_photo' => [Photo](../types/Photo.md), 'notify_settings' => [PeerNotifySettings](../types/PeerNotifySettings.md), 'bot_info' => [BotInfo](../types/BotInfo.md), 'pinned_msg_id' => [int](../types/int.md), 'common_chats_count' => [int](../types/int.md), 'folder_id' => [int](../types/int.md), 'ttl_period' => [int](../types/int.md), 'theme_emoticon' => [string](../types/string.md), 'private_forward_name' => [string](../types/string.md), \];<a name="userFull"></a>  

***
<br><br>[$userProfilePhoto](../constructors/userProfilePhoto.md) = \['has_video' => [Bool](../types/Bool.md), 'photo_id' => [long](../types/long.md), 'stripped_thumb' => [bytes](../types/bytes.md), 'dc_id' => [int](../types/int.md), \];<a name="userProfilePhoto"></a>  

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
<br><br>[$users.userFull](../constructors/users.userFull.md) = \['full_user' => [UserFull](../types/UserFull.md), 'chats' => \[[Chat](../types/Chat.md)\], 'users' => \[[User](../types/User.md)\], \];<a name="users.userFull"></a>  

***
<br><br>[$videoSize](../constructors/videoSize.md) = \['type' => [string](../types/string.md), 'w' => [int](../types/int.md), 'h' => [int](../types/int.md), 'size' => [int](../types/int.md), 'video_start_ts' => [double](../types/double.md), \];<a name="videoSize"></a>  

***
<br><br>[$wallPaper](../constructors/wallPaper.md) = \['id' => [long](../types/long.md), 'creator' => [Bool](../types/Bool.md), 'default' => [Bool](../types/Bool.md), 'pattern' => [Bool](../types/Bool.md), 'dark' => [Bool](../types/Bool.md), 'access_hash' => [long](../types/long.md), 'slug' => [string](../types/string.md), 'document' => [Document](../types/Document.md), 'settings' => [WallPaperSettings](../types/WallPaperSettings.md), \];<a name="wallPaper"></a>  

***
<br><br>[$wallPaperNoFile](../constructors/wallPaperNoFile.md) = \['id' => [long](../types/long.md), 'default' => [Bool](../types/Bool.md), 'dark' => [Bool](../types/Bool.md), 'settings' => [WallPaperSettings](../types/WallPaperSettings.md), \];<a name="wallPaperNoFile"></a>  

***
<br><br>[$wallPaperSettings](../constructors/wallPaperSettings.md) = \['blur' => [Bool](../types/Bool.md), 'motion' => [Bool](../types/Bool.md), 'background_color' => [int](../types/int.md), 'second_background_color' => [int](../types/int.md), 'third_background_color' => [int](../types/int.md), 'fourth_background_color' => [int](../types/int.md), 'intensity' => [int](../types/int.md), 'rotation' => [int](../types/int.md), \];<a name="wallPaperSettings"></a>  

***
<br><br>[$webAuthorization](../constructors/webAuthorization.md) = \['hash' => [long](../types/long.md), 'bot_id' => [long](../types/long.md), 'domain' => [string](../types/string.md), 'browser' => [string](../types/string.md), 'platform' => [string](../types/string.md), 'date_created' => [int](../types/int.md), 'date_active' => [int](../types/int.md), 'ip' => [string](../types/string.md), 'region' => [string](../types/string.md), \];<a name="webAuthorization"></a>  

***
<br><br>[$webDocument](../constructors/webDocument.md) = \['url' => [string](../types/string.md), 'access_hash' => [long](../types/long.md), 'size' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], \];<a name="webDocument"></a>  

***
<br><br>[$webDocumentNoProxy](../constructors/webDocumentNoProxy.md) = \['url' => [string](../types/string.md), 'size' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), 'attributes' => \[[DocumentAttribute](../types/DocumentAttribute.md)\], \];<a name="webDocumentNoProxy"></a>  

***
<br><br>[$webPage](../constructors/webPage.md) = \['id' => [long](../types/long.md), 'url' => [string](../types/string.md), 'display_url' => [string](../types/string.md), 'hash' => [int](../types/int.md), 'type' => [string](../types/string.md), 'site_name' => [string](../types/string.md), 'title' => [string](../types/string.md), 'description' => [string](../types/string.md), 'photo' => [Photo](../types/Photo.md), 'embed_url' => [string](../types/string.md), 'embed_type' => [string](../types/string.md), 'embed_width' => [int](../types/int.md), 'embed_height' => [int](../types/int.md), 'duration' => [int](../types/int.md), 'author' => [string](../types/string.md), 'document' => [Document](../types/Document.md), 'cached_page' => [Page](../types/Page.md), 'attributes' => \[[WebPageAttribute](../types/WebPageAttribute.md)\], \];<a name="webPage"></a>  

***
<br><br>[$webPageAttributeTheme](../constructors/webPageAttributeTheme.md) = \['documents' => \[[Document](../types/Document.md)\], 'settings' => [ThemeSettings](../types/ThemeSettings.md), \];<a name="webPageAttributeTheme"></a>  

***
<br><br>[$webPageEmpty](../constructors/webPageEmpty.md) = \['id' => [long](../types/long.md), \];<a name="webPageEmpty"></a>  

***
<br><br>[$webPageNotModified](../constructors/webPageNotModified.md) = \['cached_page_views' => [int](../types/int.md), \];<a name="webPageNotModified"></a>  

***
<br><br>[$webPagePending](../constructors/webPagePending.md) = \['id' => [long](../types/long.md), 'date' => [int](../types/int.md), \];<a name="webPagePending"></a>  


