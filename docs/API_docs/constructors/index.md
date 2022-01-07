---
title: Constructors
description: List of constructors
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructors  
[Back to API documentation index](..)

***
<br><br>[$account.authorizationForm](/API_docs/constructors/account.authorizationForm.md) = \['required_types' => \[[SecureRequiredType](/API_docs/types/SecureRequiredType.md)\], 'values' => \[[SecureValue](/API_docs/types/SecureValue.md)\], 'errors' => \[[SecureValueError](/API_docs/types/SecureValueError.md)\], 'users' => \[[User](/API_docs/types/User.md)\], 'privacy_policy_url' => [string](/API_docs/types/string.md), \];<a name="account.authorizationForm"></a>  

***
<br><br>[$account.authorizations](/API_docs/constructors/account.authorizations.md) = \['authorization_ttl_days' => [int](/API_docs/types/int.md), 'authorizations' => \[[Authorization](/API_docs/types/Authorization.md)\], \];<a name="account.authorizations"></a>  

***
<br><br>[$account.autoDownloadSettings](/API_docs/constructors/account.autoDownloadSettings.md) = \['low' => [AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.md), 'medium' => [AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.md), 'high' => [AutoDownloadSettings](/API_docs/types/AutoDownloadSettings.md), \];<a name="account.autoDownloadSettings"></a>  

***
<br><br>[$account.contentSettings](/API_docs/constructors/account.contentSettings.md) = \['sensitive_enabled' => [Bool](/API_docs/types/Bool.md), 'sensitive_can_change' => [Bool](/API_docs/types/Bool.md), \];<a name="account.contentSettings"></a>  

***
<br><br>[$account.password](/API_docs/constructors/account.password.md) = \['has_recovery' => [Bool](/API_docs/types/Bool.md), 'has_secure_values' => [Bool](/API_docs/types/Bool.md), 'has_password' => [Bool](/API_docs/types/Bool.md), 'current_algo' => [PasswordKdfAlgo](/API_docs/types/PasswordKdfAlgo.md), 'srp_B' => [bytes](/API_docs/types/bytes.md), 'srp_id' => [long](/API_docs/types/long.md), 'hint' => [string](/API_docs/types/string.md), 'email_unconfirmed_pattern' => [string](/API_docs/types/string.md), 'new_algo' => [PasswordKdfAlgo](/API_docs/types/PasswordKdfAlgo.md), 'new_secure_algo' => [SecurePasswordKdfAlgo](/API_docs/types/SecurePasswordKdfAlgo.md), 'secure_random' => [bytes](/API_docs/types/bytes.md), 'pending_reset_date' => [int](/API_docs/types/int.md), \];<a name="account.password"></a>  

***
<br><br>[$account.passwordInputSettings](/API_docs/constructors/account.passwordInputSettings.md) = \['new_algo' => [PasswordKdfAlgo](/API_docs/types/PasswordKdfAlgo.md), 'new_password_hash' => [bytes](/API_docs/types/bytes.md), 'hint' => [string](/API_docs/types/string.md), 'email' => [string](/API_docs/types/string.md), 'new_secure_settings' => [SecureSecretSettings](/API_docs/types/SecureSecretSettings.md), \];<a name="account.passwordInputSettings"></a>  

***
<br><br>[$account.passwordSettings](/API_docs/constructors/account.passwordSettings.md) = \['email' => [string](/API_docs/types/string.md), 'secure_settings' => [SecureSecretSettings](/API_docs/types/SecureSecretSettings.md), \];<a name="account.passwordSettings"></a>  

***
<br><br>[$account.privacyRules](/API_docs/constructors/account.privacyRules.md) = \['rules' => \[[PrivacyRule](/API_docs/types/PrivacyRule.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="account.privacyRules"></a>  

***
<br><br>[$account.resetPasswordFailedWait](/API_docs/constructors/account.resetPasswordFailedWait.md) = \['retry_date' => [int](/API_docs/types/int.md), \];<a name="account.resetPasswordFailedWait"></a>  

***
<br><br>[$account.resetPasswordOk](/API_docs/constructors/account.resetPasswordOk.md) = \[\];<a name="account.resetPasswordOk"></a>  

***
<br><br>[$account.resetPasswordRequestedWait](/API_docs/constructors/account.resetPasswordRequestedWait.md) = \['until_date' => [int](/API_docs/types/int.md), \];<a name="account.resetPasswordRequestedWait"></a>  

***
<br><br>[$account.sentEmailCode](/API_docs/constructors/account.sentEmailCode.md) = \['email_pattern' => [string](/API_docs/types/string.md), 'length' => [int](/API_docs/types/int.md), \];<a name="account.sentEmailCode"></a>  

***
<br><br>[$account.takeout](/API_docs/constructors/account.takeout.md) = \['id' => [long](/API_docs/types/long.md), \];<a name="account.takeout"></a>  

***
<br><br>[$account.themes](/API_docs/constructors/account.themes.md) = \['hash' => [long](/API_docs/types/long.md), 'themes' => \[[Theme](/API_docs/types/Theme.md)\], \];<a name="account.themes"></a>  

***
<br><br>[$account.themesNotModified](/API_docs/constructors/account.themesNotModified.md) = \[\];<a name="account.themesNotModified"></a>  

***
<br><br>[$account.tmpPassword](/API_docs/constructors/account.tmpPassword.md) = \['tmp_password' => [bytes](/API_docs/types/bytes.md), 'valid_until' => [int](/API_docs/types/int.md), \];<a name="account.tmpPassword"></a>  

***
<br><br>[$account.wallPapers](/API_docs/constructors/account.wallPapers.md) = \['hash' => [long](/API_docs/types/long.md), 'wallpapers' => \[[WallPaper](/API_docs/types/WallPaper.md)\], \];<a name="account.wallPapers"></a>  

***
<br><br>[$account.wallPapersNotModified](/API_docs/constructors/account.wallPapersNotModified.md) = \[\];<a name="account.wallPapersNotModified"></a>  

***
<br><br>[$account.webAuthorizations](/API_docs/constructors/account.webAuthorizations.md) = \['authorizations' => \[[WebAuthorization](/API_docs/types/WebAuthorization.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="account.webAuthorizations"></a>  

***
<br><br>[$accountDaysTTL](/API_docs/constructors/accountDaysTTL.md) = \['days' => [int](/API_docs/types/int.md), \];<a name="accountDaysTTL"></a>  

***
<br><br>[$auth.authorization](/API_docs/constructors/auth.authorization.md) = \['setup_password_required' => [Bool](/API_docs/types/Bool.md), 'otherwise_relogin_days' => [int](/API_docs/types/int.md), 'tmp_sessions' => [int](/API_docs/types/int.md), 'user' => [User](/API_docs/types/User.md), \];<a name="auth.authorization"></a>  

***
<br><br>[$auth.authorizationSignUpRequired](/API_docs/constructors/auth.authorizationSignUpRequired.md) = \['terms_of_service' => [help.TermsOfService](/API_docs/types/help.TermsOfService.md), \];<a name="auth.authorizationSignUpRequired"></a>  

***
<br><br>[$auth.codeTypeCall](/API_docs/constructors/auth.codeTypeCall.md) = \[\];<a name="auth.codeTypeCall"></a>  

***
<br><br>[$auth.codeTypeFlashCall](/API_docs/constructors/auth.codeTypeFlashCall.md) = \[\];<a name="auth.codeTypeFlashCall"></a>  

***
<br><br>[$auth.codeTypeMissedCall](/API_docs/constructors/auth.codeTypeMissedCall.md) = \[\];<a name="auth.codeTypeMissedCall"></a>  

***
<br><br>[$auth.codeTypeSms](/API_docs/constructors/auth.codeTypeSms.md) = \[\];<a name="auth.codeTypeSms"></a>  

***
<br><br>[$auth.exportedAuthorization](/API_docs/constructors/auth.exportedAuthorization.md) = \['id' => [long](/API_docs/types/long.md), 'bytes' => [bytes](/API_docs/types/bytes.md), \];<a name="auth.exportedAuthorization"></a>  

***
<br><br>[$auth.loggedOut](/API_docs/constructors/auth.loggedOut.md) = \['future_auth_token' => [bytes](/API_docs/types/bytes.md), \];<a name="auth.loggedOut"></a>  

***
<br><br>[$auth.loginToken](/API_docs/constructors/auth.loginToken.md) = \['expires' => [int](/API_docs/types/int.md), 'token' => [bytes](/API_docs/types/bytes.md), \];<a name="auth.loginToken"></a>  

***
<br><br>[$auth.loginTokenMigrateTo](/API_docs/constructors/auth.loginTokenMigrateTo.md) = \['dc_id' => [int](/API_docs/types/int.md), 'token' => [bytes](/API_docs/types/bytes.md), \];<a name="auth.loginTokenMigrateTo"></a>  

***
<br><br>[$auth.loginTokenSuccess](/API_docs/constructors/auth.loginTokenSuccess.md) = \['authorization' => [auth.Authorization](/API_docs/types/auth.Authorization.md), \];<a name="auth.loginTokenSuccess"></a>  

***
<br><br>[$auth.passwordRecovery](/API_docs/constructors/auth.passwordRecovery.md) = \['email_pattern' => [string](/API_docs/types/string.md), \];<a name="auth.passwordRecovery"></a>  

***
<br><br>[$auth.sentCode](/API_docs/constructors/auth.sentCode.md) = \['type' => [auth.SentCodeType](/API_docs/types/auth.SentCodeType.md), 'phone_code_hash' => [string](/API_docs/types/string.md), 'next_type' => [auth.CodeType](/API_docs/types/auth.CodeType.md), 'timeout' => [int](/API_docs/types/int.md), \];<a name="auth.sentCode"></a>  

***
<br><br>[$auth.sentCodeTypeApp](/API_docs/constructors/auth.sentCodeTypeApp.md) = \['length' => [int](/API_docs/types/int.md), \];<a name="auth.sentCodeTypeApp"></a>  

***
<br><br>[$auth.sentCodeTypeCall](/API_docs/constructors/auth.sentCodeTypeCall.md) = \['length' => [int](/API_docs/types/int.md), \];<a name="auth.sentCodeTypeCall"></a>  

***
<br><br>[$auth.sentCodeTypeFlashCall](/API_docs/constructors/auth.sentCodeTypeFlashCall.md) = \['pattern' => [string](/API_docs/types/string.md), \];<a name="auth.sentCodeTypeFlashCall"></a>  

***
<br><br>[$auth.sentCodeTypeMissedCall](/API_docs/constructors/auth.sentCodeTypeMissedCall.md) = \['prefix' => [string](/API_docs/types/string.md), 'length' => [int](/API_docs/types/int.md), \];<a name="auth.sentCodeTypeMissedCall"></a>  

***
<br><br>[$auth.sentCodeTypeSms](/API_docs/constructors/auth.sentCodeTypeSms.md) = \['length' => [int](/API_docs/types/int.md), \];<a name="auth.sentCodeTypeSms"></a>  

***
<br><br>[$authorization](/API_docs/constructors/authorization.md) = \['current' => [Bool](/API_docs/types/Bool.md), 'official_app' => [Bool](/API_docs/types/Bool.md), 'password_pending' => [Bool](/API_docs/types/Bool.md), 'encrypted_requests_disabled' => [Bool](/API_docs/types/Bool.md), 'call_requests_disabled' => [Bool](/API_docs/types/Bool.md), 'hash' => [long](/API_docs/types/long.md), 'device_model' => [string](/API_docs/types/string.md), 'platform' => [string](/API_docs/types/string.md), 'system_version' => [string](/API_docs/types/string.md), 'api_id' => [int](/API_docs/types/int.md), 'app_name' => [string](/API_docs/types/string.md), 'app_version' => [string](/API_docs/types/string.md), 'date_created' => [int](/API_docs/types/int.md), 'date_active' => [int](/API_docs/types/int.md), 'ip' => [string](/API_docs/types/string.md), 'country' => [string](/API_docs/types/string.md), 'region' => [string](/API_docs/types/string.md), \];<a name="authorization"></a>  

***
<br><br>[$autoDownloadSettings](/API_docs/constructors/autoDownloadSettings.md) = \['disabled' => [Bool](/API_docs/types/Bool.md), 'video_preload_large' => [Bool](/API_docs/types/Bool.md), 'audio_preload_next' => [Bool](/API_docs/types/Bool.md), 'phonecalls_less_data' => [Bool](/API_docs/types/Bool.md), 'photo_size_max' => [int](/API_docs/types/int.md), 'video_size_max' => [int](/API_docs/types/int.md), 'file_size_max' => [int](/API_docs/types/int.md), 'video_upload_maxbitrate' => [int](/API_docs/types/int.md), \];<a name="autoDownloadSettings"></a>  

***
<br><br>[$availableReaction](/API_docs/constructors/availableReaction.md) = \['inactive' => [Bool](/API_docs/types/Bool.md), 'reaction' => [string](/API_docs/types/string.md), 'title' => [string](/API_docs/types/string.md), 'static_icon' => [Document](/API_docs/types/Document.md), 'appear_animation' => [Document](/API_docs/types/Document.md), 'select_animation' => [Document](/API_docs/types/Document.md), 'activate_animation' => [Document](/API_docs/types/Document.md), 'effect_animation' => [Document](/API_docs/types/Document.md), \];<a name="availableReaction"></a>  

***
<br><br>[$bankCardOpenUrl](/API_docs/constructors/bankCardOpenUrl.md) = \['url' => [string](/API_docs/types/string.md), 'name' => [string](/API_docs/types/string.md), \];<a name="bankCardOpenUrl"></a>  

***
<br><br>[$baseThemeArctic](/API_docs/constructors/baseThemeArctic.md) = \[\];<a name="baseThemeArctic"></a>  

***
<br><br>[$baseThemeClassic](/API_docs/constructors/baseThemeClassic.md) = \[\];<a name="baseThemeClassic"></a>  

***
<br><br>[$baseThemeDay](/API_docs/constructors/baseThemeDay.md) = \[\];<a name="baseThemeDay"></a>  

***
<br><br>[$baseThemeNight](/API_docs/constructors/baseThemeNight.md) = \[\];<a name="baseThemeNight"></a>  

***
<br><br>[$baseThemeTinted](/API_docs/constructors/baseThemeTinted.md) = \[\];<a name="baseThemeTinted"></a>  

***
<br><br>[$boolFalse](/API_docs/constructors/boolFalse.md) = \[\];<a name="boolFalse"></a>  

***
<br><br>[$boolTrue](/API_docs/constructors/boolTrue.md) = \[\];<a name="boolTrue"></a>  

***
<br><br>[$botCommand](/API_docs/constructors/botCommand.md) = \['command' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), \];<a name="botCommand"></a>  

***
<br><br>[$botCommandScopeChatAdmins](/API_docs/constructors/botCommandScopeChatAdmins.md) = \[\];<a name="botCommandScopeChatAdmins"></a>  

***
<br><br>[$botCommandScopeChats](/API_docs/constructors/botCommandScopeChats.md) = \[\];<a name="botCommandScopeChats"></a>  

***
<br><br>[$botCommandScopeDefault](/API_docs/constructors/botCommandScopeDefault.md) = \[\];<a name="botCommandScopeDefault"></a>  

***
<br><br>[$botCommandScopePeer](/API_docs/constructors/botCommandScopePeer.md) = \['peer' => [InputPeer](/API_docs/types/InputPeer.md), \];<a name="botCommandScopePeer"></a>  

***
<br><br>[$botCommandScopePeerAdmins](/API_docs/constructors/botCommandScopePeerAdmins.md) = \['peer' => [InputPeer](/API_docs/types/InputPeer.md), \];<a name="botCommandScopePeerAdmins"></a>  

***
<br><br>[$botCommandScopePeerUser](/API_docs/constructors/botCommandScopePeerUser.md) = \['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), \];<a name="botCommandScopePeerUser"></a>  

***
<br><br>[$botCommandScopeUsers](/API_docs/constructors/botCommandScopeUsers.md) = \[\];<a name="botCommandScopeUsers"></a>  

***
<br><br>[$botInfo](/API_docs/constructors/botInfo.md) = \['user_id' => [long](/API_docs/types/long.md), 'description' => [string](/API_docs/types/string.md), 'commands' => \[[BotCommand](/API_docs/types/BotCommand.md)\], \];<a name="botInfo"></a>  

***
<br><br>[$botInlineMediaResult](/API_docs/constructors/botInlineMediaResult.md) = \['id' => [string](/API_docs/types/string.md), 'type' => [string](/API_docs/types/string.md), 'photo' => [Photo](/API_docs/types/Photo.md), 'document' => [Document](/API_docs/types/Document.md), 'title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'send_message' => [BotInlineMessage](/API_docs/types/BotInlineMessage.md), \];<a name="botInlineMediaResult"></a>  

***
<br><br>[$botInlineMessageMediaAuto](/API_docs/constructors/botInlineMessageMediaAuto.md) = \['message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="botInlineMessageMediaAuto"></a>  

***
<br><br>[$botInlineMessageMediaContact](/API_docs/constructors/botInlineMessageMediaContact.md) = \['phone_number' => [string](/API_docs/types/string.md), 'first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), 'vcard' => [string](/API_docs/types/string.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="botInlineMessageMediaContact"></a>  

***
<br><br>[$botInlineMessageMediaGeo](/API_docs/constructors/botInlineMessageMediaGeo.md) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.md), 'heading' => [int](/API_docs/types/int.md), 'period' => [int](/API_docs/types/int.md), 'proximity_notification_radius' => [int](/API_docs/types/int.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="botInlineMessageMediaGeo"></a>  

***
<br><br>[$botInlineMessageMediaInvoice](/API_docs/constructors/botInlineMessageMediaInvoice.md) = \['shipping_address_requested' => [Bool](/API_docs/types/Bool.md), 'test' => [Bool](/API_docs/types/Bool.md), 'title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'photo' => [WebDocument](/API_docs/types/WebDocument.md), 'currency' => [string](/API_docs/types/string.md), 'total_amount' => [long](/API_docs/types/long.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="botInlineMessageMediaInvoice"></a>  

***
<br><br>[$botInlineMessageMediaVenue](/API_docs/constructors/botInlineMessageMediaVenue.md) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.md), 'title' => [string](/API_docs/types/string.md), 'address' => [string](/API_docs/types/string.md), 'provider' => [string](/API_docs/types/string.md), 'venue_id' => [string](/API_docs/types/string.md), 'venue_type' => [string](/API_docs/types/string.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="botInlineMessageMediaVenue"></a>  

***
<br><br>[$botInlineMessageText](/API_docs/constructors/botInlineMessageText.md) = \['no_webpage' => [Bool](/API_docs/types/Bool.md), 'message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="botInlineMessageText"></a>  

***
<br><br>[$botInlineResult](/API_docs/constructors/botInlineResult.md) = \['id' => [string](/API_docs/types/string.md), 'type' => [string](/API_docs/types/string.md), 'title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'url' => [string](/API_docs/types/string.md), 'thumb' => [WebDocument](/API_docs/types/WebDocument.md), 'content' => [WebDocument](/API_docs/types/WebDocument.md), 'send_message' => [BotInlineMessage](/API_docs/types/BotInlineMessage.md), \];<a name="botInlineResult"></a>  

***
<br><br>[$cdnConfig](/API_docs/constructors/cdnConfig.md) = \['public_keys' => \[[CdnPublicKey](/API_docs/types/CdnPublicKey.md)\], \];<a name="cdnConfig"></a>  

***
<br><br>[$cdnPublicKey](/API_docs/constructors/cdnPublicKey.md) = \['dc_id' => [int](/API_docs/types/int.md), 'public_key' => [string](/API_docs/types/string.md), \];<a name="cdnPublicKey"></a>  

***
<br><br>[$channel](/API_docs/constructors/channel.md) = \['creator' => [Bool](/API_docs/types/Bool.md), 'left' => [Bool](/API_docs/types/Bool.md), 'broadcast' => [Bool](/API_docs/types/Bool.md), 'verified' => [Bool](/API_docs/types/Bool.md), 'megagroup' => [Bool](/API_docs/types/Bool.md), 'restricted' => [Bool](/API_docs/types/Bool.md), 'signatures' => [Bool](/API_docs/types/Bool.md), 'min' => [Bool](/API_docs/types/Bool.md), 'scam' => [Bool](/API_docs/types/Bool.md), 'has_link' => [Bool](/API_docs/types/Bool.md), 'has_geo' => [Bool](/API_docs/types/Bool.md), 'slowmode_enabled' => [Bool](/API_docs/types/Bool.md), 'call_active' => [Bool](/API_docs/types/Bool.md), 'call_not_empty' => [Bool](/API_docs/types/Bool.md), 'fake' => [Bool](/API_docs/types/Bool.md), 'gigagroup' => [Bool](/API_docs/types/Bool.md), 'noforwards' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'title' => [string](/API_docs/types/string.md), 'username' => [string](/API_docs/types/string.md), 'photo' => [ChatPhoto](/API_docs/types/ChatPhoto.md), 'date' => [int](/API_docs/types/int.md), 'restriction_reason' => \[[RestrictionReason](/API_docs/types/RestrictionReason.md)\], 'admin_rights' => [ChatAdminRights](/API_docs/types/ChatAdminRights.md), 'banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.md), 'default_banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.md), 'participants_count' => [int](/API_docs/types/int.md), \];<a name="channel"></a>  

***
<br><br>[$channelAdminLogEvent](/API_docs/constructors/channelAdminLogEvent.md) = \['id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'user_id' => [long](/API_docs/types/long.md), 'action' => [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.md), \];<a name="channelAdminLogEvent"></a>  

***
<br><br>[$channelAdminLogEventActionChangeAbout](/API_docs/constructors/channelAdminLogEventActionChangeAbout.md) = \['prev_value' => [string](/API_docs/types/string.md), 'new_value' => [string](/API_docs/types/string.md), \];<a name="channelAdminLogEventActionChangeAbout"></a>  

***
<br><br>[$channelAdminLogEventActionChangeAvailableReactions](/API_docs/constructors/channelAdminLogEventActionChangeAvailableReactions.md) = \['prev_value' => \[[string](/API_docs/types/string.md)\], 'new_value' => \[[string](/API_docs/types/string.md)\], \];<a name="channelAdminLogEventActionChangeAvailableReactions"></a>  

***
<br><br>[$channelAdminLogEventActionChangeHistoryTTL](/API_docs/constructors/channelAdminLogEventActionChangeHistoryTTL.md) = \['prev_value' => [int](/API_docs/types/int.md), 'new_value' => [int](/API_docs/types/int.md), \];<a name="channelAdminLogEventActionChangeHistoryTTL"></a>  

***
<br><br>[$channelAdminLogEventActionChangeLinkedChat](/API_docs/constructors/channelAdminLogEventActionChangeLinkedChat.md) = \['prev_value' => [long](/API_docs/types/long.md), 'new_value' => [long](/API_docs/types/long.md), \];<a name="channelAdminLogEventActionChangeLinkedChat"></a>  

***
<br><br>[$channelAdminLogEventActionChangeLocation](/API_docs/constructors/channelAdminLogEventActionChangeLocation.md) = \['prev_value' => [ChannelLocation](/API_docs/types/ChannelLocation.md), 'new_value' => [ChannelLocation](/API_docs/types/ChannelLocation.md), \];<a name="channelAdminLogEventActionChangeLocation"></a>  

***
<br><br>[$channelAdminLogEventActionChangePhoto](/API_docs/constructors/channelAdminLogEventActionChangePhoto.md) = \['prev_photo' => [Photo](/API_docs/types/Photo.md), 'new_photo' => [Photo](/API_docs/types/Photo.md), \];<a name="channelAdminLogEventActionChangePhoto"></a>  

***
<br><br>[$channelAdminLogEventActionChangeStickerSet](/API_docs/constructors/channelAdminLogEventActionChangeStickerSet.md) = \['prev_stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.md), 'new_stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.md), \];<a name="channelAdminLogEventActionChangeStickerSet"></a>  

***
<br><br>[$channelAdminLogEventActionChangeTitle](/API_docs/constructors/channelAdminLogEventActionChangeTitle.md) = \['prev_value' => [string](/API_docs/types/string.md), 'new_value' => [string](/API_docs/types/string.md), \];<a name="channelAdminLogEventActionChangeTitle"></a>  

***
<br><br>[$channelAdminLogEventActionChangeUsername](/API_docs/constructors/channelAdminLogEventActionChangeUsername.md) = \['prev_value' => [string](/API_docs/types/string.md), 'new_value' => [string](/API_docs/types/string.md), \];<a name="channelAdminLogEventActionChangeUsername"></a>  

***
<br><br>[$channelAdminLogEventActionDefaultBannedRights](/API_docs/constructors/channelAdminLogEventActionDefaultBannedRights.md) = \['prev_banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.md), 'new_banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.md), \];<a name="channelAdminLogEventActionDefaultBannedRights"></a>  

***
<br><br>[$channelAdminLogEventActionDeleteMessage](/API_docs/constructors/channelAdminLogEventActionDeleteMessage.md) = \['message' => [Message](/API_docs/types/Message.md), \];<a name="channelAdminLogEventActionDeleteMessage"></a>  

***
<br><br>[$channelAdminLogEventActionDiscardGroupCall](/API_docs/constructors/channelAdminLogEventActionDiscardGroupCall.md) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), \];<a name="channelAdminLogEventActionDiscardGroupCall"></a>  

***
<br><br>[$channelAdminLogEventActionEditMessage](/API_docs/constructors/channelAdminLogEventActionEditMessage.md) = \['prev_message' => [Message](/API_docs/types/Message.md), 'new_message' => [Message](/API_docs/types/Message.md), \];<a name="channelAdminLogEventActionEditMessage"></a>  

***
<br><br>[$channelAdminLogEventActionExportedInviteDelete](/API_docs/constructors/channelAdminLogEventActionExportedInviteDelete.md) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), \];<a name="channelAdminLogEventActionExportedInviteDelete"></a>  

***
<br><br>[$channelAdminLogEventActionExportedInviteEdit](/API_docs/constructors/channelAdminLogEventActionExportedInviteEdit.md) = \['prev_invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), 'new_invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), \];<a name="channelAdminLogEventActionExportedInviteEdit"></a>  

***
<br><br>[$channelAdminLogEventActionExportedInviteRevoke](/API_docs/constructors/channelAdminLogEventActionExportedInviteRevoke.md) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), \];<a name="channelAdminLogEventActionExportedInviteRevoke"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantInvite](/API_docs/constructors/channelAdminLogEventActionParticipantInvite.md) = \['participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.md), \];<a name="channelAdminLogEventActionParticipantInvite"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantJoin](/API_docs/constructors/channelAdminLogEventActionParticipantJoin.md) = \[\];<a name="channelAdminLogEventActionParticipantJoin"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantJoinByInvite](/API_docs/constructors/channelAdminLogEventActionParticipantJoinByInvite.md) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), \];<a name="channelAdminLogEventActionParticipantJoinByInvite"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantJoinByRequest](/API_docs/constructors/channelAdminLogEventActionParticipantJoinByRequest.md) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), 'approved_by' => [long](/API_docs/types/long.md), \];<a name="channelAdminLogEventActionParticipantJoinByRequest"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantLeave](/API_docs/constructors/channelAdminLogEventActionParticipantLeave.md) = \[\];<a name="channelAdminLogEventActionParticipantLeave"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantMute](/API_docs/constructors/channelAdminLogEventActionParticipantMute.md) = \['participant' => [GroupCallParticipant](/API_docs/types/GroupCallParticipant.md), \];<a name="channelAdminLogEventActionParticipantMute"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantToggleAdmin](/API_docs/constructors/channelAdminLogEventActionParticipantToggleAdmin.md) = \['prev_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.md), 'new_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.md), \];<a name="channelAdminLogEventActionParticipantToggleAdmin"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantToggleBan](/API_docs/constructors/channelAdminLogEventActionParticipantToggleBan.md) = \['prev_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.md), 'new_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.md), \];<a name="channelAdminLogEventActionParticipantToggleBan"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantUnmute](/API_docs/constructors/channelAdminLogEventActionParticipantUnmute.md) = \['participant' => [GroupCallParticipant](/API_docs/types/GroupCallParticipant.md), \];<a name="channelAdminLogEventActionParticipantUnmute"></a>  

***
<br><br>[$channelAdminLogEventActionParticipantVolume](/API_docs/constructors/channelAdminLogEventActionParticipantVolume.md) = \['participant' => [GroupCallParticipant](/API_docs/types/GroupCallParticipant.md), \];<a name="channelAdminLogEventActionParticipantVolume"></a>  

***
<br><br>[$channelAdminLogEventActionSendMessage](/API_docs/constructors/channelAdminLogEventActionSendMessage.md) = \['message' => [Message](/API_docs/types/Message.md), \];<a name="channelAdminLogEventActionSendMessage"></a>  

***
<br><br>[$channelAdminLogEventActionStartGroupCall](/API_docs/constructors/channelAdminLogEventActionStartGroupCall.md) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), \];<a name="channelAdminLogEventActionStartGroupCall"></a>  

***
<br><br>[$channelAdminLogEventActionStopPoll](/API_docs/constructors/channelAdminLogEventActionStopPoll.md) = \['message' => [Message](/API_docs/types/Message.md), \];<a name="channelAdminLogEventActionStopPoll"></a>  

***
<br><br>[$channelAdminLogEventActionToggleGroupCallSetting](/API_docs/constructors/channelAdminLogEventActionToggleGroupCallSetting.md) = \['join_muted' => [Bool](/API_docs/types/Bool.md), \];<a name="channelAdminLogEventActionToggleGroupCallSetting"></a>  

***
<br><br>[$channelAdminLogEventActionToggleInvites](/API_docs/constructors/channelAdminLogEventActionToggleInvites.md) = \['new_value' => [Bool](/API_docs/types/Bool.md), \];<a name="channelAdminLogEventActionToggleInvites"></a>  

***
<br><br>[$channelAdminLogEventActionToggleNoForwards](/API_docs/constructors/channelAdminLogEventActionToggleNoForwards.md) = \['new_value' => [Bool](/API_docs/types/Bool.md), \];<a name="channelAdminLogEventActionToggleNoForwards"></a>  

***
<br><br>[$channelAdminLogEventActionTogglePreHistoryHidden](/API_docs/constructors/channelAdminLogEventActionTogglePreHistoryHidden.md) = \['new_value' => [Bool](/API_docs/types/Bool.md), \];<a name="channelAdminLogEventActionTogglePreHistoryHidden"></a>  

***
<br><br>[$channelAdminLogEventActionToggleSignatures](/API_docs/constructors/channelAdminLogEventActionToggleSignatures.md) = \['new_value' => [Bool](/API_docs/types/Bool.md), \];<a name="channelAdminLogEventActionToggleSignatures"></a>  

***
<br><br>[$channelAdminLogEventActionToggleSlowMode](/API_docs/constructors/channelAdminLogEventActionToggleSlowMode.md) = \['prev_value' => [int](/API_docs/types/int.md), 'new_value' => [int](/API_docs/types/int.md), \];<a name="channelAdminLogEventActionToggleSlowMode"></a>  

***
<br><br>[$channelAdminLogEventActionUpdatePinned](/API_docs/constructors/channelAdminLogEventActionUpdatePinned.md) = \['message' => [Message](/API_docs/types/Message.md), \];<a name="channelAdminLogEventActionUpdatePinned"></a>  

***
<br><br>[$channelAdminLogEventsFilter](/API_docs/constructors/channelAdminLogEventsFilter.md) = \['join' => [Bool](/API_docs/types/Bool.md), 'leave' => [Bool](/API_docs/types/Bool.md), 'invite' => [Bool](/API_docs/types/Bool.md), 'ban' => [Bool](/API_docs/types/Bool.md), 'unban' => [Bool](/API_docs/types/Bool.md), 'kick' => [Bool](/API_docs/types/Bool.md), 'unkick' => [Bool](/API_docs/types/Bool.md), 'promote' => [Bool](/API_docs/types/Bool.md), 'demote' => [Bool](/API_docs/types/Bool.md), 'info' => [Bool](/API_docs/types/Bool.md), 'settings' => [Bool](/API_docs/types/Bool.md), 'pinned' => [Bool](/API_docs/types/Bool.md), 'edit' => [Bool](/API_docs/types/Bool.md), 'delete' => [Bool](/API_docs/types/Bool.md), 'group_call' => [Bool](/API_docs/types/Bool.md), 'invites' => [Bool](/API_docs/types/Bool.md), 'send' => [Bool](/API_docs/types/Bool.md), \];<a name="channelAdminLogEventsFilter"></a>  

***
<br><br>[$channelForbidden](/API_docs/constructors/channelForbidden.md) = \['broadcast' => [Bool](/API_docs/types/Bool.md), 'megagroup' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'title' => [string](/API_docs/types/string.md), 'until_date' => [int](/API_docs/types/int.md), \];<a name="channelForbidden"></a>  

***
<br><br>[$channelFull](/API_docs/constructors/channelFull.md) = \['can_view_participants' => [Bool](/API_docs/types/Bool.md), 'can_set_username' => [Bool](/API_docs/types/Bool.md), 'can_set_stickers' => [Bool](/API_docs/types/Bool.md), 'hidden_prehistory' => [Bool](/API_docs/types/Bool.md), 'can_set_location' => [Bool](/API_docs/types/Bool.md), 'has_scheduled' => [Bool](/API_docs/types/Bool.md), 'can_view_stats' => [Bool](/API_docs/types/Bool.md), 'blocked' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'about' => [string](/API_docs/types/string.md), 'participants_count' => [int](/API_docs/types/int.md), 'admins_count' => [int](/API_docs/types/int.md), 'kicked_count' => [int](/API_docs/types/int.md), 'banned_count' => [int](/API_docs/types/int.md), 'online_count' => [int](/API_docs/types/int.md), 'read_inbox_max_id' => [int](/API_docs/types/int.md), 'read_outbox_max_id' => [int](/API_docs/types/int.md), 'unread_count' => [int](/API_docs/types/int.md), 'chat_photo' => [Photo](/API_docs/types/Photo.md), 'notify_settings' => [PeerNotifySettings](/API_docs/types/PeerNotifySettings.md), 'exported_invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), 'bot_info' => \[[BotInfo](/API_docs/types/BotInfo.md)\], 'migrated_from_chat_id' => [long](/API_docs/types/long.md), 'migrated_from_max_id' => [int](/API_docs/types/int.md), 'pinned_msg_id' => [int](/API_docs/types/int.md), 'stickerset' => [StickerSet](/API_docs/types/StickerSet.md), 'available_min_id' => [int](/API_docs/types/int.md), 'folder_id' => [int](/API_docs/types/int.md), 'linked_chat_id' => [long](/API_docs/types/long.md), 'location' => [ChannelLocation](/API_docs/types/ChannelLocation.md), 'slowmode_seconds' => [int](/API_docs/types/int.md), 'slowmode_next_send_date' => [int](/API_docs/types/int.md), 'stats_dc' => [int](/API_docs/types/int.md), 'pts' => [int](/API_docs/types/int.md), 'call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'ttl_period' => [int](/API_docs/types/int.md), 'pending_suggestions' => \[[string](/API_docs/types/string.md)\], 'groupcall_default_join_as' => [Peer](/API_docs/types/Peer.md), 'theme_emoticon' => [string](/API_docs/types/string.md), 'requests_pending' => [int](/API_docs/types/int.md), 'recent_requesters' => \[[long](/API_docs/types/long.md)\], 'default_send_as' => [Peer](/API_docs/types/Peer.md), 'available_reactions' => \[[string](/API_docs/types/string.md)\], \];<a name="channelFull"></a>  

***
<br><br>[$channelLocation](/API_docs/constructors/channelLocation.md) = \['geo_point' => [GeoPoint](/API_docs/types/GeoPoint.md), 'address' => [string](/API_docs/types/string.md), \];<a name="channelLocation"></a>  

***
<br><br>[$channelLocationEmpty](/API_docs/constructors/channelLocationEmpty.md) = \[\];<a name="channelLocationEmpty"></a>  

***
<br><br>[$channelMessagesFilter](/API_docs/constructors/channelMessagesFilter.md) = \['exclude_new_messages' => [Bool](/API_docs/types/Bool.md), 'ranges' => \[[MessageRange](/API_docs/types/MessageRange.md)\], \];<a name="channelMessagesFilter"></a>  

***
<br><br>[$channelMessagesFilterEmpty](/API_docs/constructors/channelMessagesFilterEmpty.md) = \[\];<a name="channelMessagesFilterEmpty"></a>  

***
<br><br>[$channelParticipant](/API_docs/constructors/channelParticipant.md) = \['user_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), \];<a name="channelParticipant"></a>  

***
<br><br>[$channelParticipantAdmin](/API_docs/constructors/channelParticipantAdmin.md) = \['can_edit' => [Bool](/API_docs/types/Bool.md), 'self' => [Bool](/API_docs/types/Bool.md), 'user_id' => [long](/API_docs/types/long.md), 'inviter_id' => [long](/API_docs/types/long.md), 'promoted_by' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'admin_rights' => [ChatAdminRights](/API_docs/types/ChatAdminRights.md), 'rank' => [string](/API_docs/types/string.md), \];<a name="channelParticipantAdmin"></a>  

***
<br><br>[$channelParticipantBanned](/API_docs/constructors/channelParticipantBanned.md) = \['left' => [Bool](/API_docs/types/Bool.md), 'peer' => [Peer](/API_docs/types/Peer.md), 'kicked_by' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.md), \];<a name="channelParticipantBanned"></a>  

***
<br><br>[$channelParticipantCreator](/API_docs/constructors/channelParticipantCreator.md) = \['user_id' => [long](/API_docs/types/long.md), 'admin_rights' => [ChatAdminRights](/API_docs/types/ChatAdminRights.md), 'rank' => [string](/API_docs/types/string.md), \];<a name="channelParticipantCreator"></a>  

***
<br><br>[$channelParticipantLeft](/API_docs/constructors/channelParticipantLeft.md) = \['peer' => [Peer](/API_docs/types/Peer.md), \];<a name="channelParticipantLeft"></a>  

***
<br><br>[$channelParticipantSelf](/API_docs/constructors/channelParticipantSelf.md) = \['via_request' => [Bool](/API_docs/types/Bool.md), 'user_id' => [long](/API_docs/types/long.md), 'inviter_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), \];<a name="channelParticipantSelf"></a>  

***
<br><br>[$channelParticipantsAdmins](/API_docs/constructors/channelParticipantsAdmins.md) = \[\];<a name="channelParticipantsAdmins"></a>  

***
<br><br>[$channelParticipantsBanned](/API_docs/constructors/channelParticipantsBanned.md) = \['q' => [string](/API_docs/types/string.md), \];<a name="channelParticipantsBanned"></a>  

***
<br><br>[$channelParticipantsBots](/API_docs/constructors/channelParticipantsBots.md) = \[\];<a name="channelParticipantsBots"></a>  

***
<br><br>[$channelParticipantsContacts](/API_docs/constructors/channelParticipantsContacts.md) = \['q' => [string](/API_docs/types/string.md), \];<a name="channelParticipantsContacts"></a>  

***
<br><br>[$channelParticipantsKicked](/API_docs/constructors/channelParticipantsKicked.md) = \['q' => [string](/API_docs/types/string.md), \];<a name="channelParticipantsKicked"></a>  

***
<br><br>[$channelParticipantsMentions](/API_docs/constructors/channelParticipantsMentions.md) = \['q' => [string](/API_docs/types/string.md), 'top_msg_id' => [int](/API_docs/types/int.md), \];<a name="channelParticipantsMentions"></a>  

***
<br><br>[$channelParticipantsRecent](/API_docs/constructors/channelParticipantsRecent.md) = \[\];<a name="channelParticipantsRecent"></a>  

***
<br><br>[$channelParticipantsSearch](/API_docs/constructors/channelParticipantsSearch.md) = \['q' => [string](/API_docs/types/string.md), \];<a name="channelParticipantsSearch"></a>  

***
<br><br>[$channels.adminLogResults](/API_docs/constructors/channels.adminLogResults.md) = \['events' => \[[ChannelAdminLogEvent](/API_docs/types/ChannelAdminLogEvent.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="channels.adminLogResults"></a>  

***
<br><br>[$channels.channelParticipant](/API_docs/constructors/channels.channelParticipant.md) = \['participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.md), 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="channels.channelParticipant"></a>  

***
<br><br>[$channels.channelParticipants](/API_docs/constructors/channels.channelParticipants.md) = \['count' => [int](/API_docs/types/int.md), 'participants' => \[[ChannelParticipant](/API_docs/types/ChannelParticipant.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="channels.channelParticipants"></a>  

***
<br><br>[$channels.channelParticipantsNotModified](/API_docs/constructors/channels.channelParticipantsNotModified.md) = \[\];<a name="channels.channelParticipantsNotModified"></a>  

***
<br><br>[$channels.sendAsPeers](/API_docs/constructors/channels.sendAsPeers.md) = \['peers' => \[[Peer](/API_docs/types/Peer.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="channels.sendAsPeers"></a>  

***
<br><br>[$chat](/API_docs/constructors/chat.md) = \['creator' => [Bool](/API_docs/types/Bool.md), 'kicked' => [Bool](/API_docs/types/Bool.md), 'left' => [Bool](/API_docs/types/Bool.md), 'deactivated' => [Bool](/API_docs/types/Bool.md), 'call_active' => [Bool](/API_docs/types/Bool.md), 'call_not_empty' => [Bool](/API_docs/types/Bool.md), 'noforwards' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'title' => [string](/API_docs/types/string.md), 'photo' => [ChatPhoto](/API_docs/types/ChatPhoto.md), 'participants_count' => [int](/API_docs/types/int.md), 'date' => [int](/API_docs/types/int.md), 'version' => [int](/API_docs/types/int.md), 'migrated_to' => [InputChannel](/API_docs/types/InputChannel.md), 'admin_rights' => [ChatAdminRights](/API_docs/types/ChatAdminRights.md), 'default_banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.md), \];<a name="chat"></a>  

***
<br><br>[$chatAdminRights](/API_docs/constructors/chatAdminRights.md) = \['change_info' => [Bool](/API_docs/types/Bool.md), 'post_messages' => [Bool](/API_docs/types/Bool.md), 'edit_messages' => [Bool](/API_docs/types/Bool.md), 'delete_messages' => [Bool](/API_docs/types/Bool.md), 'ban_users' => [Bool](/API_docs/types/Bool.md), 'invite_users' => [Bool](/API_docs/types/Bool.md), 'pin_messages' => [Bool](/API_docs/types/Bool.md), 'add_admins' => [Bool](/API_docs/types/Bool.md), 'anonymous' => [Bool](/API_docs/types/Bool.md), 'manage_call' => [Bool](/API_docs/types/Bool.md), 'other' => [Bool](/API_docs/types/Bool.md), \];<a name="chatAdminRights"></a>  

***
<br><br>[$chatAdminWithInvites](/API_docs/constructors/chatAdminWithInvites.md) = \['admin_id' => [long](/API_docs/types/long.md), 'invites_count' => [int](/API_docs/types/int.md), 'revoked_invites_count' => [int](/API_docs/types/int.md), \];<a name="chatAdminWithInvites"></a>  

***
<br><br>[$chatBannedRights](/API_docs/constructors/chatBannedRights.md) = \['view_messages' => [Bool](/API_docs/types/Bool.md), 'send_messages' => [Bool](/API_docs/types/Bool.md), 'send_media' => [Bool](/API_docs/types/Bool.md), 'send_stickers' => [Bool](/API_docs/types/Bool.md), 'send_gifs' => [Bool](/API_docs/types/Bool.md), 'send_games' => [Bool](/API_docs/types/Bool.md), 'send_inline' => [Bool](/API_docs/types/Bool.md), 'embed_links' => [Bool](/API_docs/types/Bool.md), 'send_polls' => [Bool](/API_docs/types/Bool.md), 'change_info' => [Bool](/API_docs/types/Bool.md), 'invite_users' => [Bool](/API_docs/types/Bool.md), 'pin_messages' => [Bool](/API_docs/types/Bool.md), 'until_date' => [int](/API_docs/types/int.md), \];<a name="chatBannedRights"></a>  

***
<br><br>[$chatEmpty](/API_docs/constructors/chatEmpty.md) = \['id' => [long](/API_docs/types/long.md), \];<a name="chatEmpty"></a>  

***
<br><br>[$chatForbidden](/API_docs/constructors/chatForbidden.md) = \['id' => [long](/API_docs/types/long.md), 'title' => [string](/API_docs/types/string.md), \];<a name="chatForbidden"></a>  

***
<br><br>[$chatFull](/API_docs/constructors/chatFull.md) = \['can_set_username' => [Bool](/API_docs/types/Bool.md), 'has_scheduled' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'about' => [string](/API_docs/types/string.md), 'participants' => [ChatParticipants](/API_docs/types/ChatParticipants.md), 'chat_photo' => [Photo](/API_docs/types/Photo.md), 'notify_settings' => [PeerNotifySettings](/API_docs/types/PeerNotifySettings.md), 'exported_invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), 'bot_info' => \[[BotInfo](/API_docs/types/BotInfo.md)\], 'pinned_msg_id' => [int](/API_docs/types/int.md), 'folder_id' => [int](/API_docs/types/int.md), 'call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'ttl_period' => [int](/API_docs/types/int.md), 'groupcall_default_join_as' => [Peer](/API_docs/types/Peer.md), 'theme_emoticon' => [string](/API_docs/types/string.md), 'requests_pending' => [int](/API_docs/types/int.md), 'recent_requesters' => \[[long](/API_docs/types/long.md)\], 'available_reactions' => \[[string](/API_docs/types/string.md)\], \];<a name="chatFull"></a>  

***
<br><br>[$chatInvite](/API_docs/constructors/chatInvite.md) = \['channel' => [Bool](/API_docs/types/Bool.md), 'broadcast' => [Bool](/API_docs/types/Bool.md), 'public' => [Bool](/API_docs/types/Bool.md), 'megagroup' => [Bool](/API_docs/types/Bool.md), 'request_needed' => [Bool](/API_docs/types/Bool.md), 'title' => [string](/API_docs/types/string.md), 'about' => [string](/API_docs/types/string.md), 'photo' => [Photo](/API_docs/types/Photo.md), 'participants_count' => [int](/API_docs/types/int.md), 'participants' => \[[User](/API_docs/types/User.md)\], \];<a name="chatInvite"></a>  

***
<br><br>[$chatInviteAlready](/API_docs/constructors/chatInviteAlready.md) = \['chat' => [Chat](/API_docs/types/Chat.md), \];<a name="chatInviteAlready"></a>  

***
<br><br>[$chatInviteExported](/API_docs/constructors/chatInviteExported.md) = \['revoked' => [Bool](/API_docs/types/Bool.md), 'permanent' => [Bool](/API_docs/types/Bool.md), 'request_needed' => [Bool](/API_docs/types/Bool.md), 'link' => [string](/API_docs/types/string.md), 'admin_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'start_date' => [int](/API_docs/types/int.md), 'expire_date' => [int](/API_docs/types/int.md), 'usage_limit' => [int](/API_docs/types/int.md), 'usage' => [int](/API_docs/types/int.md), 'requested' => [int](/API_docs/types/int.md), 'title' => [string](/API_docs/types/string.md), \];<a name="chatInviteExported"></a>  

***
<br><br>[$chatInviteImporter](/API_docs/constructors/chatInviteImporter.md) = \['requested' => [Bool](/API_docs/types/Bool.md), 'user_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'about' => [string](/API_docs/types/string.md), 'approved_by' => [long](/API_docs/types/long.md), \];<a name="chatInviteImporter"></a>  

***
<br><br>[$chatInvitePeek](/API_docs/constructors/chatInvitePeek.md) = \['chat' => [Chat](/API_docs/types/Chat.md), 'expires' => [int](/API_docs/types/int.md), \];<a name="chatInvitePeek"></a>  

***
<br><br>[$chatOnlines](/API_docs/constructors/chatOnlines.md) = \['onlines' => [int](/API_docs/types/int.md), \];<a name="chatOnlines"></a>  

***
<br><br>[$chatParticipant](/API_docs/constructors/chatParticipant.md) = \['user_id' => [long](/API_docs/types/long.md), 'inviter_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), \];<a name="chatParticipant"></a>  

***
<br><br>[$chatParticipantAdmin](/API_docs/constructors/chatParticipantAdmin.md) = \['user_id' => [long](/API_docs/types/long.md), 'inviter_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), \];<a name="chatParticipantAdmin"></a>  

***
<br><br>[$chatParticipantCreator](/API_docs/constructors/chatParticipantCreator.md) = \['user_id' => [long](/API_docs/types/long.md), \];<a name="chatParticipantCreator"></a>  

***
<br><br>[$chatParticipants](/API_docs/constructors/chatParticipants.md) = \['chat_id' => [long](/API_docs/types/long.md), 'participants' => \[[ChatParticipant](/API_docs/types/ChatParticipant.md)\], 'version' => [int](/API_docs/types/int.md), \];<a name="chatParticipants"></a>  

***
<br><br>[$chatParticipantsForbidden](/API_docs/constructors/chatParticipantsForbidden.md) = \['chat_id' => [long](/API_docs/types/long.md), 'self_participant' => [ChatParticipant](/API_docs/types/ChatParticipant.md), \];<a name="chatParticipantsForbidden"></a>  

***
<br><br>[$chatPhoto](/API_docs/constructors/chatPhoto.md) = \['has_video' => [Bool](/API_docs/types/Bool.md), 'photo_id' => [long](/API_docs/types/long.md), 'stripped_thumb' => [bytes](/API_docs/types/bytes.md), 'dc_id' => [int](/API_docs/types/int.md), \];<a name="chatPhoto"></a>  

***
<br><br>[$chatPhotoEmpty](/API_docs/constructors/chatPhotoEmpty.md) = \[\];<a name="chatPhotoEmpty"></a>  

***
<br><br>[$codeSettings](/API_docs/constructors/codeSettings.md) = \['allow_flashcall' => [Bool](/API_docs/types/Bool.md), 'current_number' => [Bool](/API_docs/types/Bool.md), 'allow_app_hash' => [Bool](/API_docs/types/Bool.md), 'allow_missed_call' => [Bool](/API_docs/types/Bool.md), 'logout_tokens' => \[[bytes](/API_docs/types/bytes.md)\], \];<a name="codeSettings"></a>  

***
<br><br>[$config](/API_docs/constructors/config.md) = \['phonecalls_enabled' => [Bool](/API_docs/types/Bool.md), 'default_p2p_contacts' => [Bool](/API_docs/types/Bool.md), 'preload_featured_stickers' => [Bool](/API_docs/types/Bool.md), 'ignore_phone_entities' => [Bool](/API_docs/types/Bool.md), 'revoke_pm_inbox' => [Bool](/API_docs/types/Bool.md), 'blocked_mode' => [Bool](/API_docs/types/Bool.md), 'pfs_enabled' => [Bool](/API_docs/types/Bool.md), 'date' => [int](/API_docs/types/int.md), 'expires' => [int](/API_docs/types/int.md), 'test_mode' => [Bool](/API_docs/types/Bool.md), 'this_dc' => [int](/API_docs/types/int.md), 'dc_options' => \[[DcOption](/API_docs/types/DcOption.md)\], 'dc_txt_domain_name' => [string](/API_docs/types/string.md), 'chat_size_max' => [int](/API_docs/types/int.md), 'megagroup_size_max' => [int](/API_docs/types/int.md), 'forwarded_count_max' => [int](/API_docs/types/int.md), 'online_update_period_ms' => [int](/API_docs/types/int.md), 'offline_blur_timeout_ms' => [int](/API_docs/types/int.md), 'offline_idle_timeout_ms' => [int](/API_docs/types/int.md), 'online_cloud_timeout_ms' => [int](/API_docs/types/int.md), 'notify_cloud_delay_ms' => [int](/API_docs/types/int.md), 'notify_default_delay_ms' => [int](/API_docs/types/int.md), 'push_chat_period_ms' => [int](/API_docs/types/int.md), 'push_chat_limit' => [int](/API_docs/types/int.md), 'saved_gifs_limit' => [int](/API_docs/types/int.md), 'edit_time_limit' => [int](/API_docs/types/int.md), 'revoke_time_limit' => [int](/API_docs/types/int.md), 'revoke_pm_time_limit' => [int](/API_docs/types/int.md), 'rating_e_decay' => [int](/API_docs/types/int.md), 'stickers_recent_limit' => [int](/API_docs/types/int.md), 'stickers_faved_limit' => [int](/API_docs/types/int.md), 'channels_read_media_period' => [int](/API_docs/types/int.md), 'tmp_sessions' => [int](/API_docs/types/int.md), 'pinned_dialogs_count_max' => [int](/API_docs/types/int.md), 'pinned_infolder_count_max' => [int](/API_docs/types/int.md), 'call_receive_timeout_ms' => [int](/API_docs/types/int.md), 'call_ring_timeout_ms' => [int](/API_docs/types/int.md), 'call_connect_timeout_ms' => [int](/API_docs/types/int.md), 'call_packet_timeout_ms' => [int](/API_docs/types/int.md), 'me_url_prefix' => [string](/API_docs/types/string.md), 'autoupdate_url_prefix' => [string](/API_docs/types/string.md), 'gif_search_username' => [string](/API_docs/types/string.md), 'venue_search_username' => [string](/API_docs/types/string.md), 'img_search_username' => [string](/API_docs/types/string.md), 'static_maps_provider' => [string](/API_docs/types/string.md), 'caption_length_max' => [int](/API_docs/types/int.md), 'message_length_max' => [int](/API_docs/types/int.md), 'webfile_dc_id' => [int](/API_docs/types/int.md), 'suggested_lang_code' => [string](/API_docs/types/string.md), 'lang_pack_version' => [int](/API_docs/types/int.md), 'base_lang_pack_version' => [int](/API_docs/types/int.md), \];<a name="config"></a>  

***
<br><br>[$contact](/API_docs/constructors/contact.md) = \['user_id' => [long](/API_docs/types/long.md), 'mutual' => [Bool](/API_docs/types/Bool.md), \];<a name="contact"></a>  

***
<br><br>[$contactStatus](/API_docs/constructors/contactStatus.md) = \['user_id' => [long](/API_docs/types/long.md), 'status' => [UserStatus](/API_docs/types/UserStatus.md), \];<a name="contactStatus"></a>  

***
<br><br>[$contacts.blocked](/API_docs/constructors/contacts.blocked.md) = \['blocked' => \[[PeerBlocked](/API_docs/types/PeerBlocked.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="contacts.blocked"></a>  

***
<br><br>[$contacts.blockedSlice](/API_docs/constructors/contacts.blockedSlice.md) = \['count' => [int](/API_docs/types/int.md), 'blocked' => \[[PeerBlocked](/API_docs/types/PeerBlocked.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="contacts.blockedSlice"></a>  

***
<br><br>[$contacts.contacts](/API_docs/constructors/contacts.contacts.md) = \['contacts' => \[[Contact](/API_docs/types/Contact.md)\], 'saved_count' => [int](/API_docs/types/int.md), 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="contacts.contacts"></a>  

***
<br><br>[$contacts.contactsNotModified](/API_docs/constructors/contacts.contactsNotModified.md) = \[\];<a name="contacts.contactsNotModified"></a>  

***
<br><br>[$contacts.found](/API_docs/constructors/contacts.found.md) = \['my_results' => \[[Peer](/API_docs/types/Peer.md)\], 'results' => \[[Peer](/API_docs/types/Peer.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="contacts.found"></a>  

***
<br><br>[$contacts.importedContacts](/API_docs/constructors/contacts.importedContacts.md) = \['imported' => \[[ImportedContact](/API_docs/types/ImportedContact.md)\], 'popular_invites' => \[[PopularContact](/API_docs/types/PopularContact.md)\], 'retry_contacts' => \[[long](/API_docs/types/long.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="contacts.importedContacts"></a>  

***
<br><br>[$contacts.resolvedPeer](/API_docs/constructors/contacts.resolvedPeer.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="contacts.resolvedPeer"></a>  

***
<br><br>[$contacts.topPeers](/API_docs/constructors/contacts.topPeers.md) = \['categories' => \[[TopPeerCategoryPeers](/API_docs/types/TopPeerCategoryPeers.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="contacts.topPeers"></a>  

***
<br><br>[$contacts.topPeersDisabled](/API_docs/constructors/contacts.topPeersDisabled.md) = \[\];<a name="contacts.topPeersDisabled"></a>  

***
<br><br>[$contacts.topPeersNotModified](/API_docs/constructors/contacts.topPeersNotModified.md) = \[\];<a name="contacts.topPeersNotModified"></a>  

***
<br><br>[$dataJSON](/API_docs/constructors/dataJSON.md) = \['data' => [string](/API_docs/types/string.md), \];<a name="dataJSON"></a>  

***
<br><br>[$dcOption](/API_docs/constructors/dcOption.md) = \['ipv6' => [Bool](/API_docs/types/Bool.md), 'media_only' => [Bool](/API_docs/types/Bool.md), 'tcpo_only' => [Bool](/API_docs/types/Bool.md), 'cdn' => [Bool](/API_docs/types/Bool.md), 'static' => [Bool](/API_docs/types/Bool.md), 'id' => [int](/API_docs/types/int.md), 'ip_address' => [string](/API_docs/types/string.md), 'port' => [int](/API_docs/types/int.md), 'secret' => [bytes](/API_docs/types/bytes.md), \];<a name="dcOption"></a>  

***
<br><br>[$decryptedMessage\_73](/API_docs/constructors/decryptedMessage_73.md) = \['ttl' => [int](/API_docs/types/int.md), 'message' => [string](/API_docs/types/string.md), 'media' => [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'via_bot_name' => [string](/API_docs/types/string.md), 'reply_to_random_id' => [long](/API_docs/types/long.md), 'grouped_id' => [long](/API_docs/types/long.md), \];<a name="decryptedMessage_73"></a>  

***
<br><br>[$decryptedMessageActionAbortKey\_20](/API_docs/constructors/decryptedMessageActionAbortKey_20.md) = \['exchange_id' => [long](/API_docs/types/long.md), \];<a name="decryptedMessageActionAbortKey_20"></a>  

***
<br><br>[$decryptedMessageActionAcceptKey\_20](/API_docs/constructors/decryptedMessageActionAcceptKey_20.md) = \['exchange_id' => [long](/API_docs/types/long.md), 'g_b' => [bytes](/API_docs/types/bytes.md), 'key_fingerprint' => [long](/API_docs/types/long.md), \];<a name="decryptedMessageActionAcceptKey_20"></a>  

***
<br><br>[$decryptedMessageActionCommitKey\_20](/API_docs/constructors/decryptedMessageActionCommitKey_20.md) = \['exchange_id' => [long](/API_docs/types/long.md), 'key_fingerprint' => [long](/API_docs/types/long.md), \];<a name="decryptedMessageActionCommitKey_20"></a>  

***
<br><br>[$decryptedMessageActionDeleteMessages\_8](/API_docs/constructors/decryptedMessageActionDeleteMessages_8.md) = \['random_ids' => \[[long](/API_docs/types/long.md)\], \];<a name="decryptedMessageActionDeleteMessages_8"></a>  

***
<br><br>[$decryptedMessageActionFlushHistory\_8](/API_docs/constructors/decryptedMessageActionFlushHistory_8.md) = \[\];<a name="decryptedMessageActionFlushHistory_8"></a>  

***
<br><br>[$decryptedMessageActionNoop\_20](/API_docs/constructors/decryptedMessageActionNoop_20.md) = \[\];<a name="decryptedMessageActionNoop_20"></a>  

***
<br><br>[$decryptedMessageActionNotifyLayer\_17](/API_docs/constructors/decryptedMessageActionNotifyLayer_17.md) = \['layer' => [int](/API_docs/types/int.md), \];<a name="decryptedMessageActionNotifyLayer_17"></a>  

***
<br><br>[$decryptedMessageActionReadMessages\_8](/API_docs/constructors/decryptedMessageActionReadMessages_8.md) = \['random_ids' => \[[long](/API_docs/types/long.md)\], \];<a name="decryptedMessageActionReadMessages_8"></a>  

***
<br><br>[$decryptedMessageActionRequestKey\_20](/API_docs/constructors/decryptedMessageActionRequestKey_20.md) = \['exchange_id' => [long](/API_docs/types/long.md), 'g_a' => [bytes](/API_docs/types/bytes.md), \];<a name="decryptedMessageActionRequestKey_20"></a>  

***
<br><br>[$decryptedMessageActionResend\_17](/API_docs/constructors/decryptedMessageActionResend_17.md) = \['start_seq_no' => [int](/API_docs/types/int.md), 'end_seq_no' => [int](/API_docs/types/int.md), \];<a name="decryptedMessageActionResend_17"></a>  

***
<br><br>[$decryptedMessageActionScreenshotMessages\_8](/API_docs/constructors/decryptedMessageActionScreenshotMessages_8.md) = \['random_ids' => \[[long](/API_docs/types/long.md)\], \];<a name="decryptedMessageActionScreenshotMessages_8"></a>  

***
<br><br>[$decryptedMessageActionSetMessageTTL\_8](/API_docs/constructors/decryptedMessageActionSetMessageTTL_8.md) = \['ttl_seconds' => [int](/API_docs/types/int.md), \];<a name="decryptedMessageActionSetMessageTTL_8"></a>  

***
<br><br>[$decryptedMessageActionTyping\_17](/API_docs/constructors/decryptedMessageActionTyping_17.md) = \['action' => [SendMessageAction](/API_docs/types/SendMessageAction.md), \];<a name="decryptedMessageActionTyping_17"></a>  

***
<br><br>[$decryptedMessageLayer\_17](/API_docs/constructors/decryptedMessageLayer_17.md) = \['layer' => [int](/API_docs/types/int.md), 'in_seq_no' => [int](/API_docs/types/int.md), 'out_seq_no' => [int](/API_docs/types/int.md), 'message' => [DecryptedMessage](/API_docs/types/DecryptedMessage.md), \];<a name="decryptedMessageLayer_17"></a>  

***
<br><br>[$decryptedMessageMediaAudio\_17](/API_docs/constructors/decryptedMessageMediaAudio_17.md) = \['duration' => [int](/API_docs/types/int.md), 'mime_type' => [string](/API_docs/types/string.md), 'size' => [int](/API_docs/types/int.md), 'key' => [bytes](/API_docs/types/bytes.md), 'iv' => [bytes](/API_docs/types/bytes.md), \];<a name="decryptedMessageMediaAudio_17"></a>  

***
<br><br>[$decryptedMessageMediaContact\_8](/API_docs/constructors/decryptedMessageMediaContact_8.md) = \['phone_number' => [string](/API_docs/types/string.md), 'first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), 'user_id' => [int](/API_docs/types/int.md), \];<a name="decryptedMessageMediaContact_8"></a>  

***
<br><br>[$decryptedMessageMediaDocument\_45](/API_docs/constructors/decryptedMessageMediaDocument_45.md) = \['thumb' => [bytes](/API_docs/types/bytes.md), 'thumb_w' => [int](/API_docs/types/int.md), 'thumb_h' => [int](/API_docs/types/int.md), 'mime_type' => [string](/API_docs/types/string.md), 'size' => [int](/API_docs/types/int.md), 'key' => [bytes](/API_docs/types/bytes.md), 'iv' => [bytes](/API_docs/types/bytes.md), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.md)\], 'caption' => [string](/API_docs/types/string.md), \];<a name="decryptedMessageMediaDocument_45"></a>  

***
<br><br>[$decryptedMessageMediaEmpty\_8](/API_docs/constructors/decryptedMessageMediaEmpty_8.md) = \[\];<a name="decryptedMessageMediaEmpty_8"></a>  

***
<br><br>[$decryptedMessageMediaExternalDocument\_23](/API_docs/constructors/decryptedMessageMediaExternalDocument_23.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'mime_type' => [string](/API_docs/types/string.md), 'size' => [int](/API_docs/types/int.md), 'thumb' => [PhotoSize](/API_docs/types/PhotoSize.md), 'dc_id' => [int](/API_docs/types/int.md), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.md)\], \];<a name="decryptedMessageMediaExternalDocument_23"></a>  

***
<br><br>[$decryptedMessageMediaGeoPoint\_8](/API_docs/constructors/decryptedMessageMediaGeoPoint_8.md) = \['lat' => [double](/API_docs/types/double.md), 'long' => [double](/API_docs/types/double.md), \];<a name="decryptedMessageMediaGeoPoint_8"></a>  

***
<br><br>[$decryptedMessageMediaPhoto\_45](/API_docs/constructors/decryptedMessageMediaPhoto_45.md) = \['thumb' => [bytes](/API_docs/types/bytes.md), 'thumb_w' => [int](/API_docs/types/int.md), 'thumb_h' => [int](/API_docs/types/int.md), 'w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), 'size' => [int](/API_docs/types/int.md), 'key' => [bytes](/API_docs/types/bytes.md), 'iv' => [bytes](/API_docs/types/bytes.md), 'caption' => [string](/API_docs/types/string.md), \];<a name="decryptedMessageMediaPhoto_45"></a>  

***
<br><br>[$decryptedMessageMediaVenue\_46](/API_docs/constructors/decryptedMessageMediaVenue_46.md) = \['lat' => [double](/API_docs/types/double.md), 'long' => [double](/API_docs/types/double.md), 'title' => [string](/API_docs/types/string.md), 'address' => [string](/API_docs/types/string.md), 'provider' => [string](/API_docs/types/string.md), 'venue_id' => [string](/API_docs/types/string.md), \];<a name="decryptedMessageMediaVenue_46"></a>  

***
<br><br>[$decryptedMessageMediaVideo\_45](/API_docs/constructors/decryptedMessageMediaVideo_45.md) = \['thumb' => [bytes](/API_docs/types/bytes.md), 'thumb_w' => [int](/API_docs/types/int.md), 'thumb_h' => [int](/API_docs/types/int.md), 'duration' => [int](/API_docs/types/int.md), 'mime_type' => [string](/API_docs/types/string.md), 'w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), 'size' => [int](/API_docs/types/int.md), 'key' => [bytes](/API_docs/types/bytes.md), 'iv' => [bytes](/API_docs/types/bytes.md), 'caption' => [string](/API_docs/types/string.md), \];<a name="decryptedMessageMediaVideo_45"></a>  

***
<br><br>[$decryptedMessageMediaWebPage\_46](/API_docs/constructors/decryptedMessageMediaWebPage_46.md) = \['url' => [string](/API_docs/types/string.md), \];<a name="decryptedMessageMediaWebPage_46"></a>  

***
<br><br>[$decryptedMessageService\_17](/API_docs/constructors/decryptedMessageService_17.md) = \['action' => [DecryptedMessageAction](/API_docs/types/DecryptedMessageAction.md), \];<a name="decryptedMessageService_17"></a>  

***
<br><br>[$dialog](/API_docs/constructors/dialog.md) = \['pinned' => [Bool](/API_docs/types/Bool.md), 'unread_mark' => [Bool](/API_docs/types/Bool.md), 'peer' => [Peer](/API_docs/types/Peer.md), 'top_message' => [int](/API_docs/types/int.md), 'read_inbox_max_id' => [int](/API_docs/types/int.md), 'read_outbox_max_id' => [int](/API_docs/types/int.md), 'unread_count' => [int](/API_docs/types/int.md), 'unread_mentions_count' => [int](/API_docs/types/int.md), 'notify_settings' => [PeerNotifySettings](/API_docs/types/PeerNotifySettings.md), 'pts' => [int](/API_docs/types/int.md), 'draft' => [DraftMessage](/API_docs/types/DraftMessage.md), 'folder_id' => [int](/API_docs/types/int.md), \];<a name="dialog"></a>  

***
<br><br>[$dialogFilter](/API_docs/constructors/dialogFilter.md) = \['contacts' => [Bool](/API_docs/types/Bool.md), 'non_contacts' => [Bool](/API_docs/types/Bool.md), 'groups' => [Bool](/API_docs/types/Bool.md), 'broadcasts' => [Bool](/API_docs/types/Bool.md), 'bots' => [Bool](/API_docs/types/Bool.md), 'exclude_muted' => [Bool](/API_docs/types/Bool.md), 'exclude_read' => [Bool](/API_docs/types/Bool.md), 'exclude_archived' => [Bool](/API_docs/types/Bool.md), 'id' => [int](/API_docs/types/int.md), 'title' => [string](/API_docs/types/string.md), 'emoticon' => [string](/API_docs/types/string.md), 'pinned_peers' => \[[InputPeer](/API_docs/types/InputPeer.md)\], 'include_peers' => \[[InputPeer](/API_docs/types/InputPeer.md)\], 'exclude_peers' => \[[InputPeer](/API_docs/types/InputPeer.md)\], \];<a name="dialogFilter"></a>  

***
<br><br>[$dialogFilterSuggested](/API_docs/constructors/dialogFilterSuggested.md) = \['filter' => [DialogFilter](/API_docs/types/DialogFilter.md), 'description' => [string](/API_docs/types/string.md), \];<a name="dialogFilterSuggested"></a>  

***
<br><br>[$dialogFolder](/API_docs/constructors/dialogFolder.md) = \['pinned' => [Bool](/API_docs/types/Bool.md), 'folder' => [Folder](/API_docs/types/Folder.md), 'peer' => [Peer](/API_docs/types/Peer.md), 'top_message' => [int](/API_docs/types/int.md), 'unread_muted_peers_count' => [int](/API_docs/types/int.md), 'unread_unmuted_peers_count' => [int](/API_docs/types/int.md), 'unread_muted_messages_count' => [int](/API_docs/types/int.md), 'unread_unmuted_messages_count' => [int](/API_docs/types/int.md), \];<a name="dialogFolder"></a>  

***
<br><br>[$dialogPeer](/API_docs/constructors/dialogPeer.md) = \['peer' => [Peer](/API_docs/types/Peer.md), \];<a name="dialogPeer"></a>  

***
<br><br>[$dialogPeerFolder](/API_docs/constructors/dialogPeerFolder.md) = \['folder_id' => [int](/API_docs/types/int.md), \];<a name="dialogPeerFolder"></a>  

***
<br><br>[$document](/API_docs/constructors/document.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'file_reference' => [bytes](/API_docs/types/bytes.md), 'date' => [int](/API_docs/types/int.md), 'mime_type' => [string](/API_docs/types/string.md), 'size' => [int](/API_docs/types/int.md), 'thumbs' => \[[PhotoSize](/API_docs/types/PhotoSize.md)\], 'video_thumbs' => \[[VideoSize](/API_docs/types/VideoSize.md)\], 'dc_id' => [int](/API_docs/types/int.md), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.md)\], \];<a name="document"></a>  

***
<br><br>[$documentAttributeAnimated](/API_docs/constructors/documentAttributeAnimated.md) = \[\];<a name="documentAttributeAnimated"></a>  

***
<br><br>[$documentAttributeAudio\_46](/API_docs/constructors/documentAttributeAudio_46.md) = \['duration' => [int](/API_docs/types/int.md), 'title' => [string](/API_docs/types/string.md), 'performer' => [string](/API_docs/types/string.md), \];<a name="documentAttributeAudio_46"></a>  

***
<br><br>[$documentAttributeFilename](/API_docs/constructors/documentAttributeFilename.md) = \['file_name' => [string](/API_docs/types/string.md), \];<a name="documentAttributeFilename"></a>  

***
<br><br>[$documentAttributeHasStickers](/API_docs/constructors/documentAttributeHasStickers.md) = \[\];<a name="documentAttributeHasStickers"></a>  

***
<br><br>[$documentAttributeImageSize](/API_docs/constructors/documentAttributeImageSize.md) = \['w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), \];<a name="documentAttributeImageSize"></a>  

***
<br><br>[$documentAttributeSticker\_55](/API_docs/constructors/documentAttributeSticker_55.md) = \['alt' => [string](/API_docs/types/string.md), 'stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.md), \];<a name="documentAttributeSticker_55"></a>  

***
<br><br>[$documentAttributeVideo\_23](/API_docs/constructors/documentAttributeVideo_23.md) = \['duration' => [int](/API_docs/types/int.md), 'w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), \];<a name="documentAttributeVideo_23"></a>  

***
<br><br>[$documentEmpty](/API_docs/constructors/documentEmpty.md) = \['id' => [long](/API_docs/types/long.md), \];<a name="documentEmpty"></a>  

***
<br><br>[$draftMessage](/API_docs/constructors/draftMessage.md) = \['no_webpage' => [Bool](/API_docs/types/Bool.md), 'reply_to_msg_id' => [int](/API_docs/types/int.md), 'message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'date' => [int](/API_docs/types/int.md), \];<a name="draftMessage"></a>  

***
<br><br>[$draftMessageEmpty](/API_docs/constructors/draftMessageEmpty.md) = \['date' => [int](/API_docs/types/int.md), \];<a name="draftMessageEmpty"></a>  

***
<br><br>[$emojiKeyword](/API_docs/constructors/emojiKeyword.md) = \['keyword' => [string](/API_docs/types/string.md), 'emoticons' => \[[string](/API_docs/types/string.md)\], \];<a name="emojiKeyword"></a>  

***
<br><br>[$emojiKeywordDeleted](/API_docs/constructors/emojiKeywordDeleted.md) = \['keyword' => [string](/API_docs/types/string.md), 'emoticons' => \[[string](/API_docs/types/string.md)\], \];<a name="emojiKeywordDeleted"></a>  

***
<br><br>[$emojiKeywordsDifference](/API_docs/constructors/emojiKeywordsDifference.md) = \['lang_code' => [string](/API_docs/types/string.md), 'from_version' => [int](/API_docs/types/int.md), 'version' => [int](/API_docs/types/int.md), 'keywords' => \[[EmojiKeyword](/API_docs/types/EmojiKeyword.md)\], \];<a name="emojiKeywordsDifference"></a>  

***
<br><br>[$emojiLanguage](/API_docs/constructors/emojiLanguage.md) = \['lang_code' => [string](/API_docs/types/string.md), \];<a name="emojiLanguage"></a>  

***
<br><br>[$emojiURL](/API_docs/constructors/emojiURL.md) = \['url' => [string](/API_docs/types/string.md), \];<a name="emojiURL"></a>  

***
<br><br>[$encryptedChat](/API_docs/constructors/encryptedChat.md) = \['id' => [int](/API_docs/types/int.md), 'access_hash' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'admin_id' => [long](/API_docs/types/long.md), 'participant_id' => [long](/API_docs/types/long.md), 'g_a_or_b' => [bytes](/API_docs/types/bytes.md), 'key_fingerprint' => [long](/API_docs/types/long.md), \];<a name="encryptedChat"></a>  

***
<br><br>[$encryptedChatDiscarded](/API_docs/constructors/encryptedChatDiscarded.md) = \['history_deleted' => [Bool](/API_docs/types/Bool.md), 'id' => [int](/API_docs/types/int.md), \];<a name="encryptedChatDiscarded"></a>  

***
<br><br>[$encryptedChatEmpty](/API_docs/constructors/encryptedChatEmpty.md) = \['id' => [int](/API_docs/types/int.md), \];<a name="encryptedChatEmpty"></a>  

***
<br><br>[$encryptedChatRequested](/API_docs/constructors/encryptedChatRequested.md) = \['folder_id' => [int](/API_docs/types/int.md), 'id' => [int](/API_docs/types/int.md), 'access_hash' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'admin_id' => [long](/API_docs/types/long.md), 'participant_id' => [long](/API_docs/types/long.md), 'g_a' => [bytes](/API_docs/types/bytes.md), \];<a name="encryptedChatRequested"></a>  

***
<br><br>[$encryptedChatWaiting](/API_docs/constructors/encryptedChatWaiting.md) = \['id' => [int](/API_docs/types/int.md), 'access_hash' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'admin_id' => [long](/API_docs/types/long.md), 'participant_id' => [long](/API_docs/types/long.md), \];<a name="encryptedChatWaiting"></a>  

***
<br><br>[$encryptedFile](/API_docs/constructors/encryptedFile.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'size' => [int](/API_docs/types/int.md), 'dc_id' => [int](/API_docs/types/int.md), 'key_fingerprint' => [int](/API_docs/types/int.md), \];<a name="encryptedFile"></a>  

***
<br><br>[$encryptedFileEmpty](/API_docs/constructors/encryptedFileEmpty.md) = \[\];<a name="encryptedFileEmpty"></a>  

***
<br><br>[$encryptedMessage](/API_docs/constructors/encryptedMessage.md) = \['chat_id' => [int](/API_docs/types/int.md), 'date' => [int](/API_docs/types/int.md), 'decrypted_message' => [DecryptedMessage](/API_docs/types/DecryptedMessage.md), 'file' => [EncryptedFile](/API_docs/types/EncryptedFile.md), \];<a name="encryptedMessage"></a>  

***
<br><br>[$encryptedMessageService](/API_docs/constructors/encryptedMessageService.md) = \['chat_id' => [int](/API_docs/types/int.md), 'date' => [int](/API_docs/types/int.md), 'decrypted_message' => [DecryptedMessage](/API_docs/types/DecryptedMessage.md), \];<a name="encryptedMessageService"></a>  

***
<br><br>[$error](/API_docs/constructors/error.md) = \['code' => [int](/API_docs/types/int.md), 'text' => [string](/API_docs/types/string.md), \];<a name="error"></a>  

***
<br><br>[$exportedMessageLink](/API_docs/constructors/exportedMessageLink.md) = \['link' => [string](/API_docs/types/string.md), 'html' => [string](/API_docs/types/string.md), \];<a name="exportedMessageLink"></a>  

***
<br><br>[$fileHash](/API_docs/constructors/fileHash.md) = \['offset' => [int](/API_docs/types/int.md), 'limit' => [int](/API_docs/types/int.md), 'hash' => [bytes](/API_docs/types/bytes.md), \];<a name="fileHash"></a>  

***
<br><br>[$fileLocation\_23](/API_docs/constructors/fileLocation_23.md) = \['dc_id' => [int](/API_docs/types/int.md), 'volume_id' => [long](/API_docs/types/long.md), 'local_id' => [int](/API_docs/types/int.md), 'secret' => [long](/API_docs/types/long.md), \];<a name="fileLocation_23"></a>  

***
<br><br>[$fileLocationUnavailable\_23](/API_docs/constructors/fileLocationUnavailable_23.md) = \['volume_id' => [long](/API_docs/types/long.md), 'local_id' => [int](/API_docs/types/int.md), 'secret' => [long](/API_docs/types/long.md), \];<a name="fileLocationUnavailable_23"></a>  

***
<br><br>[$folder](/API_docs/constructors/folder.md) = \['autofill_new_broadcasts' => [Bool](/API_docs/types/Bool.md), 'autofill_public_groups' => [Bool](/API_docs/types/Bool.md), 'autofill_new_correspondents' => [Bool](/API_docs/types/Bool.md), 'id' => [int](/API_docs/types/int.md), 'title' => [string](/API_docs/types/string.md), 'photo' => [ChatPhoto](/API_docs/types/ChatPhoto.md), \];<a name="folder"></a>  

***
<br><br>[$folderPeer](/API_docs/constructors/folderPeer.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'folder_id' => [int](/API_docs/types/int.md), \];<a name="folderPeer"></a>  

***
<br><br>[$game](/API_docs/constructors/game.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'short_name' => [string](/API_docs/types/string.md), 'title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'photo' => [Photo](/API_docs/types/Photo.md), 'document' => [Document](/API_docs/types/Document.md), \];<a name="game"></a>  

***
<br><br>[$geoPoint](/API_docs/constructors/geoPoint.md) = \['long' => [double](/API_docs/types/double.md), 'lat' => [double](/API_docs/types/double.md), 'access_hash' => [long](/API_docs/types/long.md), 'accuracy_radius' => [int](/API_docs/types/int.md), \];<a name="geoPoint"></a>  

***
<br><br>[$geoPointEmpty](/API_docs/constructors/geoPointEmpty.md) = \[\];<a name="geoPointEmpty"></a>  

***
<br><br>[$globalPrivacySettings](/API_docs/constructors/globalPrivacySettings.md) = \['archive_and_mute_new_noncontact_peers' => [Bool](/API_docs/types/Bool.md), \];<a name="globalPrivacySettings"></a>  

***
<br><br>[$groupCall](/API_docs/constructors/groupCall.md) = \['join_muted' => [Bool](/API_docs/types/Bool.md), 'can_change_join_muted' => [Bool](/API_docs/types/Bool.md), 'join_date_asc' => [Bool](/API_docs/types/Bool.md), 'schedule_start_subscribed' => [Bool](/API_docs/types/Bool.md), 'can_start_video' => [Bool](/API_docs/types/Bool.md), 'record_video_active' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'participants_count' => [int](/API_docs/types/int.md), 'title' => [string](/API_docs/types/string.md), 'stream_dc_id' => [int](/API_docs/types/int.md), 'record_start_date' => [int](/API_docs/types/int.md), 'schedule_date' => [int](/API_docs/types/int.md), 'unmuted_video_count' => [int](/API_docs/types/int.md), 'unmuted_video_limit' => [int](/API_docs/types/int.md), 'version' => [int](/API_docs/types/int.md), \];<a name="groupCall"></a>  

***
<br><br>[$groupCallDiscarded](/API_docs/constructors/groupCallDiscarded.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'duration' => [int](/API_docs/types/int.md), \];<a name="groupCallDiscarded"></a>  

***
<br><br>[$groupCallParticipant](/API_docs/constructors/groupCallParticipant.md) = \['muted' => [Bool](/API_docs/types/Bool.md), 'left' => [Bool](/API_docs/types/Bool.md), 'can_self_unmute' => [Bool](/API_docs/types/Bool.md), 'just_joined' => [Bool](/API_docs/types/Bool.md), 'versioned' => [Bool](/API_docs/types/Bool.md), 'min' => [Bool](/API_docs/types/Bool.md), 'muted_by_you' => [Bool](/API_docs/types/Bool.md), 'volume_by_admin' => [Bool](/API_docs/types/Bool.md), 'self' => [Bool](/API_docs/types/Bool.md), 'video_joined' => [Bool](/API_docs/types/Bool.md), 'peer' => [Peer](/API_docs/types/Peer.md), 'date' => [int](/API_docs/types/int.md), 'active_date' => [int](/API_docs/types/int.md), 'source' => [int](/API_docs/types/int.md), 'volume' => [int](/API_docs/types/int.md), 'about' => [string](/API_docs/types/string.md), 'raise_hand_rating' => [long](/API_docs/types/long.md), 'video' => [GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.md), 'presentation' => [GroupCallParticipantVideo](/API_docs/types/GroupCallParticipantVideo.md), \];<a name="groupCallParticipant"></a>  

***
<br><br>[$groupCallParticipantVideo](/API_docs/constructors/groupCallParticipantVideo.md) = \['paused' => [Bool](/API_docs/types/Bool.md), 'endpoint' => [string](/API_docs/types/string.md), 'source_groups' => \[[GroupCallParticipantVideoSourceGroup](/API_docs/types/GroupCallParticipantVideoSourceGroup.md)\], 'audio_source' => [int](/API_docs/types/int.md), \];<a name="groupCallParticipantVideo"></a>  

***
<br><br>[$groupCallParticipantVideoSourceGroup](/API_docs/constructors/groupCallParticipantVideoSourceGroup.md) = \['semantics' => [string](/API_docs/types/string.md), 'sources' => \[[int](/API_docs/types/int.md)\], \];<a name="groupCallParticipantVideoSourceGroup"></a>  

***
<br><br>[$help.appUpdate](/API_docs/constructors/help.appUpdate.md) = \['can_not_skip' => [Bool](/API_docs/types/Bool.md), 'id' => [int](/API_docs/types/int.md), 'version' => [string](/API_docs/types/string.md), 'text' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'document' => [Document](/API_docs/types/Document.md), 'url' => [string](/API_docs/types/string.md), 'sticker' => [Document](/API_docs/types/Document.md), \];<a name="help.appUpdate"></a>  

***
<br><br>[$help.countriesList](/API_docs/constructors/help.countriesList.md) = \['countries' => \[[help.Country](/API_docs/types/help.Country.md)\], 'hash' => [int](/API_docs/types/int.md), \];<a name="help.countriesList"></a>  

***
<br><br>[$help.countriesListNotModified](/API_docs/constructors/help.countriesListNotModified.md) = \[\];<a name="help.countriesListNotModified"></a>  

***
<br><br>[$help.country](/API_docs/constructors/help.country.md) = \['hidden' => [Bool](/API_docs/types/Bool.md), 'iso2' => [string](/API_docs/types/string.md), 'default_name' => [string](/API_docs/types/string.md), 'name' => [string](/API_docs/types/string.md), 'country_codes' => \[[help.CountryCode](/API_docs/types/help.CountryCode.md)\], \];<a name="help.country"></a>  

***
<br><br>[$help.countryCode](/API_docs/constructors/help.countryCode.md) = \['country_code' => [string](/API_docs/types/string.md), 'prefixes' => \[[string](/API_docs/types/string.md)\], 'patterns' => \[[string](/API_docs/types/string.md)\], \];<a name="help.countryCode"></a>  

***
<br><br>[$help.deepLinkInfo](/API_docs/constructors/help.deepLinkInfo.md) = \['update_app' => [Bool](/API_docs/types/Bool.md), 'message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], \];<a name="help.deepLinkInfo"></a>  

***
<br><br>[$help.deepLinkInfoEmpty](/API_docs/constructors/help.deepLinkInfoEmpty.md) = \[\];<a name="help.deepLinkInfoEmpty"></a>  

***
<br><br>[$help.inviteText](/API_docs/constructors/help.inviteText.md) = \['message' => [string](/API_docs/types/string.md), \];<a name="help.inviteText"></a>  

***
<br><br>[$help.noAppUpdate](/API_docs/constructors/help.noAppUpdate.md) = \[\];<a name="help.noAppUpdate"></a>  

***
<br><br>[$help.passportConfig](/API_docs/constructors/help.passportConfig.md) = \['hash' => [int](/API_docs/types/int.md), 'countries_langs' => [DataJSON](/API_docs/types/DataJSON.md), \];<a name="help.passportConfig"></a>  

***
<br><br>[$help.passportConfigNotModified](/API_docs/constructors/help.passportConfigNotModified.md) = \[\];<a name="help.passportConfigNotModified"></a>  

***
<br><br>[$help.promoData](/API_docs/constructors/help.promoData.md) = \['proxy' => [Bool](/API_docs/types/Bool.md), 'expires' => [int](/API_docs/types/int.md), 'peer' => [Peer](/API_docs/types/Peer.md), 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], 'psa_type' => [string](/API_docs/types/string.md), 'psa_message' => [string](/API_docs/types/string.md), \];<a name="help.promoData"></a>  

***
<br><br>[$help.promoDataEmpty](/API_docs/constructors/help.promoDataEmpty.md) = \['expires' => [int](/API_docs/types/int.md), \];<a name="help.promoDataEmpty"></a>  

***
<br><br>[$help.recentMeUrls](/API_docs/constructors/help.recentMeUrls.md) = \['urls' => \[[RecentMeUrl](/API_docs/types/RecentMeUrl.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="help.recentMeUrls"></a>  

***
<br><br>[$help.support](/API_docs/constructors/help.support.md) = \['phone_number' => [string](/API_docs/types/string.md), 'user' => [User](/API_docs/types/User.md), \];<a name="help.support"></a>  

***
<br><br>[$help.supportName](/API_docs/constructors/help.supportName.md) = \['name' => [string](/API_docs/types/string.md), \];<a name="help.supportName"></a>  

***
<br><br>[$help.termsOfService](/API_docs/constructors/help.termsOfService.md) = \['popup' => [Bool](/API_docs/types/Bool.md), 'id' => [DataJSON](/API_docs/types/DataJSON.md), 'text' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'min_age_confirm' => [int](/API_docs/types/int.md), \];<a name="help.termsOfService"></a>  

***
<br><br>[$help.termsOfServiceUpdate](/API_docs/constructors/help.termsOfServiceUpdate.md) = \['expires' => [int](/API_docs/types/int.md), 'terms_of_service' => [help.TermsOfService](/API_docs/types/help.TermsOfService.md), \];<a name="help.termsOfServiceUpdate"></a>  

***
<br><br>[$help.termsOfServiceUpdateEmpty](/API_docs/constructors/help.termsOfServiceUpdateEmpty.md) = \['expires' => [int](/API_docs/types/int.md), \];<a name="help.termsOfServiceUpdateEmpty"></a>  

***
<br><br>[$help.userInfo](/API_docs/constructors/help.userInfo.md) = \['message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'author' => [string](/API_docs/types/string.md), 'date' => [int](/API_docs/types/int.md), \];<a name="help.userInfo"></a>  

***
<br><br>[$help.userInfoEmpty](/API_docs/constructors/help.userInfoEmpty.md) = \[\];<a name="help.userInfoEmpty"></a>  

***
<br><br>[$highScore](/API_docs/constructors/highScore.md) = \['pos' => [int](/API_docs/types/int.md), 'user_id' => [long](/API_docs/types/long.md), 'score' => [int](/API_docs/types/int.md), \];<a name="highScore"></a>  

***
<br><br>[$importedContact](/API_docs/constructors/importedContact.md) = \['user_id' => [long](/API_docs/types/long.md), 'client_id' => [long](/API_docs/types/long.md), \];<a name="importedContact"></a>  

***
<br><br>[$inlineBotSwitchPM](/API_docs/constructors/inlineBotSwitchPM.md) = \['text' => [string](/API_docs/types/string.md), 'start_param' => [string](/API_docs/types/string.md), \];<a name="inlineBotSwitchPM"></a>  

***
<br><br>[$inlineQueryPeerTypeBroadcast](/API_docs/constructors/inlineQueryPeerTypeBroadcast.md) = \[\];<a name="inlineQueryPeerTypeBroadcast"></a>  

***
<br><br>[$inlineQueryPeerTypeChat](/API_docs/constructors/inlineQueryPeerTypeChat.md) = \[\];<a name="inlineQueryPeerTypeChat"></a>  

***
<br><br>[$inlineQueryPeerTypeMegagroup](/API_docs/constructors/inlineQueryPeerTypeMegagroup.md) = \[\];<a name="inlineQueryPeerTypeMegagroup"></a>  

***
<br><br>[$inlineQueryPeerTypePM](/API_docs/constructors/inlineQueryPeerTypePM.md) = \[\];<a name="inlineQueryPeerTypePM"></a>  

***
<br><br>[$inlineQueryPeerTypeSameBotPM](/API_docs/constructors/inlineQueryPeerTypeSameBotPM.md) = \[\];<a name="inlineQueryPeerTypeSameBotPM"></a>  

***
<br><br>[$inputAppEvent](/API_docs/constructors/inputAppEvent.md) = \['time' => [double](/API_docs/types/double.md), 'type' => [string](/API_docs/types/string.md), 'peer' => [long](/API_docs/types/long.md), 'data' => [JSONValue](/API_docs/types/JSONValue.md), \];<a name="inputAppEvent"></a>  

***
<br><br>[$inputBotInlineMessageGame](/API_docs/constructors/inputBotInlineMessageGame.md) = \['reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="inputBotInlineMessageGame"></a>  

***
<br><br>[$inputBotInlineMessageID](/API_docs/constructors/inputBotInlineMessageID.md) = \['dc_id' => [int](/API_docs/types/int.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputBotInlineMessageID"></a>  

***
<br><br>[$inputBotInlineMessageID64](/API_docs/constructors/inputBotInlineMessageID64.md) = \['dc_id' => [int](/API_docs/types/int.md), 'owner_id' => [long](/API_docs/types/long.md), 'id' => [int](/API_docs/types/int.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputBotInlineMessageID64"></a>  

***
<br><br>[$inputBotInlineMessageMediaAuto](/API_docs/constructors/inputBotInlineMessageMediaAuto.md) = \['message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaAuto"></a>  

***
<br><br>[$inputBotInlineMessageMediaContact](/API_docs/constructors/inputBotInlineMessageMediaContact.md) = \['phone_number' => [string](/API_docs/types/string.md), 'first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), 'vcard' => [string](/API_docs/types/string.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaContact"></a>  

***
<br><br>[$inputBotInlineMessageMediaGeo](/API_docs/constructors/inputBotInlineMessageMediaGeo.md) = \['geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.md), 'heading' => [int](/API_docs/types/int.md), 'period' => [int](/API_docs/types/int.md), 'proximity_notification_radius' => [int](/API_docs/types/int.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaGeo"></a>  

***
<br><br>[$inputBotInlineMessageMediaInvoice](/API_docs/constructors/inputBotInlineMessageMediaInvoice.md) = \['title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'photo' => [InputWebDocument](/API_docs/types/InputWebDocument.md), 'invoice' => [Invoice](/API_docs/types/Invoice.md), 'payload' => [bytes](/API_docs/types/bytes.md), 'provider' => [string](/API_docs/types/string.md), 'provider_data' => [DataJSON](/API_docs/types/DataJSON.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaInvoice"></a>  

***
<br><br>[$inputBotInlineMessageMediaVenue](/API_docs/constructors/inputBotInlineMessageMediaVenue.md) = \['geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.md), 'title' => [string](/API_docs/types/string.md), 'address' => [string](/API_docs/types/string.md), 'provider' => [string](/API_docs/types/string.md), 'venue_id' => [string](/API_docs/types/string.md), 'venue_type' => [string](/API_docs/types/string.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="inputBotInlineMessageMediaVenue"></a>  

***
<br><br>[$inputBotInlineMessageText](/API_docs/constructors/inputBotInlineMessageText.md) = \['no_webpage' => [Bool](/API_docs/types/Bool.md), 'message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), \];<a name="inputBotInlineMessageText"></a>  

***
<br><br>[$inputBotInlineResult](/API_docs/constructors/inputBotInlineResult.md) = \['id' => [string](/API_docs/types/string.md), 'type' => [string](/API_docs/types/string.md), 'title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'url' => [string](/API_docs/types/string.md), 'thumb' => [InputWebDocument](/API_docs/types/InputWebDocument.md), 'content' => [InputWebDocument](/API_docs/types/InputWebDocument.md), 'send_message' => [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.md), \];<a name="inputBotInlineResult"></a>  

***
<br><br>[$inputBotInlineResultDocument](/API_docs/constructors/inputBotInlineResultDocument.md) = \['id' => [string](/API_docs/types/string.md), 'type' => [string](/API_docs/types/string.md), 'title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'document' => [InputDocument](/API_docs/types/InputDocument.md), 'send_message' => [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.md), \];<a name="inputBotInlineResultDocument"></a>  

***
<br><br>[$inputBotInlineResultGame](/API_docs/constructors/inputBotInlineResultGame.md) = \['id' => [string](/API_docs/types/string.md), 'short_name' => [string](/API_docs/types/string.md), 'send_message' => [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.md), \];<a name="inputBotInlineResultGame"></a>  

***
<br><br>[$inputBotInlineResultPhoto](/API_docs/constructors/inputBotInlineResultPhoto.md) = \['id' => [string](/API_docs/types/string.md), 'type' => [string](/API_docs/types/string.md), 'photo' => [InputPhoto](/API_docs/types/InputPhoto.md), 'send_message' => [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.md), \];<a name="inputBotInlineResultPhoto"></a>  

***
<br><br>[$inputChannel](/API_docs/constructors/inputChannel.md) = \['channel_id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputChannel"></a>  

***
<br><br>[$inputChannelEmpty](/API_docs/constructors/inputChannelEmpty.md) = \[\];<a name="inputChannelEmpty"></a>  

***
<br><br>[$inputChannelFromMessage](/API_docs/constructors/inputChannelFromMessage.md) = \['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'channel_id' => [long](/API_docs/types/long.md), \];<a name="inputChannelFromMessage"></a>  

***
<br><br>[$inputChatPhoto](/API_docs/constructors/inputChatPhoto.md) = \['id' => [InputPhoto](/API_docs/types/InputPhoto.md), \];<a name="inputChatPhoto"></a>  

***
<br><br>[$inputChatPhotoEmpty](/API_docs/constructors/inputChatPhotoEmpty.md) = \[\];<a name="inputChatPhotoEmpty"></a>  

***
<br><br>[$inputChatUploadedPhoto](/API_docs/constructors/inputChatUploadedPhoto.md) = \['file' => [InputFile](/API_docs/types/InputFile.md), 'video' => [InputFile](/API_docs/types/InputFile.md), 'video_start_ts' => [double](/API_docs/types/double.md), \];<a name="inputChatUploadedPhoto"></a>  

***
<br><br>[$inputCheckPasswordEmpty](/API_docs/constructors/inputCheckPasswordEmpty.md) = \[\];<a name="inputCheckPasswordEmpty"></a>  

***
<br><br>[$inputCheckPasswordSRP](/API_docs/constructors/inputCheckPasswordSRP.md) = \['srp_id' => [long](/API_docs/types/long.md), 'A' => [bytes](/API_docs/types/bytes.md), 'M1' => [bytes](/API_docs/types/bytes.md), \];<a name="inputCheckPasswordSRP"></a>  

***
<br><br>[$inputClientProxy](/API_docs/constructors/inputClientProxy.md) = \['address' => [string](/API_docs/types/string.md), 'port' => [int](/API_docs/types/int.md), \];<a name="inputClientProxy"></a>  

***
<br><br>[$inputDialogPeer](/API_docs/constructors/inputDialogPeer.md) = \['peer' => [InputPeer](/API_docs/types/InputPeer.md), \];<a name="inputDialogPeer"></a>  

***
<br><br>[$inputDialogPeerFolder](/API_docs/constructors/inputDialogPeerFolder.md) = \['folder_id' => [int](/API_docs/types/int.md), \];<a name="inputDialogPeerFolder"></a>  

***
<br><br>[$inputDocument](/API_docs/constructors/inputDocument.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'file_reference' => [bytes](/API_docs/types/bytes.md), \];<a name="inputDocument"></a>  

***
<br><br>[$inputDocumentEmpty](/API_docs/constructors/inputDocumentEmpty.md) = \[\];<a name="inputDocumentEmpty"></a>  

***
<br><br>[$inputDocumentFileLocation](/API_docs/constructors/inputDocumentFileLocation.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'file_reference' => [bytes](/API_docs/types/bytes.md), 'thumb_size' => [string](/API_docs/types/string.md), \];<a name="inputDocumentFileLocation"></a>  

***
<br><br>[$inputEncryptedChat](/API_docs/constructors/inputEncryptedChat.md) = \['chat_id' => [int](/API_docs/types/int.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputEncryptedChat"></a>  

***
<br><br>[$inputEncryptedFile](/API_docs/constructors/inputEncryptedFile.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputEncryptedFile"></a>  

***
<br><br>[$inputEncryptedFileBigUploaded](/API_docs/constructors/inputEncryptedFileBigUploaded.md) = \['id' => [long](/API_docs/types/long.md), 'parts' => [int](/API_docs/types/int.md), 'key_fingerprint' => [int](/API_docs/types/int.md), \];<a name="inputEncryptedFileBigUploaded"></a>  

***
<br><br>[$inputEncryptedFileEmpty](/API_docs/constructors/inputEncryptedFileEmpty.md) = \[\];<a name="inputEncryptedFileEmpty"></a>  

***
<br><br>[$inputEncryptedFileLocation](/API_docs/constructors/inputEncryptedFileLocation.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputEncryptedFileLocation"></a>  

***
<br><br>[$inputEncryptedFileUploaded](/API_docs/constructors/inputEncryptedFileUploaded.md) = \['id' => [long](/API_docs/types/long.md), 'parts' => [int](/API_docs/types/int.md), 'md5_checksum' => [string](/API_docs/types/string.md), 'key_fingerprint' => [int](/API_docs/types/int.md), \];<a name="inputEncryptedFileUploaded"></a>  

***
<br><br>[$inputFile](/API_docs/constructors/inputFile.md) = \['id' => [long](/API_docs/types/long.md), 'parts' => [int](/API_docs/types/int.md), 'name' => [string](/API_docs/types/string.md), 'md5_checksum' => [string](/API_docs/types/string.md), \];<a name="inputFile"></a>  

***
<br><br>[$inputFileBig](/API_docs/constructors/inputFileBig.md) = \['id' => [long](/API_docs/types/long.md), 'parts' => [int](/API_docs/types/int.md), 'name' => [string](/API_docs/types/string.md), \];<a name="inputFileBig"></a>  

***
<br><br>[$inputFileLocation](/API_docs/constructors/inputFileLocation.md) = \['volume_id' => [long](/API_docs/types/long.md), 'local_id' => [int](/API_docs/types/int.md), 'secret' => [long](/API_docs/types/long.md), 'file_reference' => [bytes](/API_docs/types/bytes.md), \];<a name="inputFileLocation"></a>  

***
<br><br>[$inputFolderPeer](/API_docs/constructors/inputFolderPeer.md) = \['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'folder_id' => [int](/API_docs/types/int.md), \];<a name="inputFolderPeer"></a>  

***
<br><br>[$inputGameID](/API_docs/constructors/inputGameID.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputGameID"></a>  

***
<br><br>[$inputGameShortName](/API_docs/constructors/inputGameShortName.md) = \['bot_id' => [InputUser](/API_docs/types/InputUser.md), 'short_name' => [string](/API_docs/types/string.md), \];<a name="inputGameShortName"></a>  

***
<br><br>[$inputGeoPoint](/API_docs/constructors/inputGeoPoint.md) = \['lat' => [double](/API_docs/types/double.md), 'long' => [double](/API_docs/types/double.md), 'accuracy_radius' => [int](/API_docs/types/int.md), \];<a name="inputGeoPoint"></a>  

***
<br><br>[$inputGeoPointEmpty](/API_docs/constructors/inputGeoPointEmpty.md) = \[\];<a name="inputGeoPointEmpty"></a>  

***
<br><br>[$inputGroupCall](/API_docs/constructors/inputGroupCall.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputGroupCall"></a>  

***
<br><br>[$inputGroupCallStream](/API_docs/constructors/inputGroupCallStream.md) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'time_ms' => [long](/API_docs/types/long.md), 'scale' => [int](/API_docs/types/int.md), 'video_channel' => [int](/API_docs/types/int.md), 'video_quality' => [int](/API_docs/types/int.md), \];<a name="inputGroupCallStream"></a>  

***
<br><br>[$inputKeyboardButtonUrlAuth](/API_docs/constructors/inputKeyboardButtonUrlAuth.md) = \['request_write_access' => [Bool](/API_docs/types/Bool.md), 'text' => [string](/API_docs/types/string.md), 'fwd_text' => [string](/API_docs/types/string.md), 'url' => [string](/API_docs/types/string.md), 'bot' => [InputUser](/API_docs/types/InputUser.md), \];<a name="inputKeyboardButtonUrlAuth"></a>  

***
<br><br>[$inputKeyboardButtonUserProfile](/API_docs/constructors/inputKeyboardButtonUserProfile.md) = \['text' => [string](/API_docs/types/string.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), \];<a name="inputKeyboardButtonUserProfile"></a>  

***
<br><br>[$inputMediaContact](/API_docs/constructors/inputMediaContact.md) = \['phone_number' => [string](/API_docs/types/string.md), 'first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), 'vcard' => [string](/API_docs/types/string.md), \];<a name="inputMediaContact"></a>  

***
<br><br>[$inputMediaDice](/API_docs/constructors/inputMediaDice.md) = \['emoticon' => [string](/API_docs/types/string.md), \];<a name="inputMediaDice"></a>  

***
<br><br>[$inputMediaDocument](/API_docs/constructors/inputMediaDocument.md) = \['id' => [InputDocument](/API_docs/types/InputDocument.md), 'ttl_seconds' => [int](/API_docs/types/int.md), 'query' => [string](/API_docs/types/string.md), \];<a name="inputMediaDocument"></a>  

***
<br><br>[$inputMediaDocumentExternal](/API_docs/constructors/inputMediaDocumentExternal.md) = \['url' => [string](/API_docs/types/string.md), 'ttl_seconds' => [int](/API_docs/types/int.md), \];<a name="inputMediaDocumentExternal"></a>  

***
<br><br>[$inputMediaEmpty](/API_docs/constructors/inputMediaEmpty.md) = \[\];<a name="inputMediaEmpty"></a>  

***
<br><br>[$inputMediaGame](/API_docs/constructors/inputMediaGame.md) = \['id' => [InputGame](/API_docs/types/InputGame.md), \];<a name="inputMediaGame"></a>  

***
<br><br>[$inputMediaGeoLive](/API_docs/constructors/inputMediaGeoLive.md) = \['stopped' => [Bool](/API_docs/types/Bool.md), 'geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.md), 'heading' => [int](/API_docs/types/int.md), 'period' => [int](/API_docs/types/int.md), 'proximity_notification_radius' => [int](/API_docs/types/int.md), \];<a name="inputMediaGeoLive"></a>  

***
<br><br>[$inputMediaGeoPoint](/API_docs/constructors/inputMediaGeoPoint.md) = \['geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.md), \];<a name="inputMediaGeoPoint"></a>  

***
<br><br>[$inputMediaInvoice](/API_docs/constructors/inputMediaInvoice.md) = \['title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'photo' => [InputWebDocument](/API_docs/types/InputWebDocument.md), 'invoice' => [Invoice](/API_docs/types/Invoice.md), 'payload' => [bytes](/API_docs/types/bytes.md), 'provider' => [string](/API_docs/types/string.md), 'provider_data' => [DataJSON](/API_docs/types/DataJSON.md), 'start_param' => [string](/API_docs/types/string.md), \];<a name="inputMediaInvoice"></a>  

***
<br><br>[$inputMediaPhoto](/API_docs/constructors/inputMediaPhoto.md) = \['id' => [InputPhoto](/API_docs/types/InputPhoto.md), 'ttl_seconds' => [int](/API_docs/types/int.md), \];<a name="inputMediaPhoto"></a>  

***
<br><br>[$inputMediaPhotoExternal](/API_docs/constructors/inputMediaPhotoExternal.md) = \['url' => [string](/API_docs/types/string.md), 'ttl_seconds' => [int](/API_docs/types/int.md), \];<a name="inputMediaPhotoExternal"></a>  

***
<br><br>[$inputMediaPoll](/API_docs/constructors/inputMediaPoll.md) = \['poll' => [Poll](/API_docs/types/Poll.md), 'correct_answers' => \[[bytes](/API_docs/types/bytes.md)\], 'solution' => [string](/API_docs/types/string.md), 'solution_entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], \];<a name="inputMediaPoll"></a>  

***
<br><br>[$inputMediaUploadedDocument](/API_docs/constructors/inputMediaUploadedDocument.md) = \['nosound_video' => [Bool](/API_docs/types/Bool.md), 'force_file' => [Bool](/API_docs/types/Bool.md), 'file' => [InputFile](/API_docs/types/InputFile.md), 'thumb' => [InputFile](/API_docs/types/InputFile.md), 'mime_type' => [string](/API_docs/types/string.md), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.md)\], 'stickers' => \[[InputDocument](/API_docs/types/InputDocument.md)\], 'ttl_seconds' => [int](/API_docs/types/int.md), \];<a name="inputMediaUploadedDocument"></a>  

***
<br><br>[$inputMediaUploadedPhoto](/API_docs/constructors/inputMediaUploadedPhoto.md) = \['file' => [InputFile](/API_docs/types/InputFile.md), 'stickers' => \[[InputDocument](/API_docs/types/InputDocument.md)\], 'ttl_seconds' => [int](/API_docs/types/int.md), \];<a name="inputMediaUploadedPhoto"></a>  

***
<br><br>[$inputMediaVenue](/API_docs/constructors/inputMediaVenue.md) = \['geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.md), 'title' => [string](/API_docs/types/string.md), 'address' => [string](/API_docs/types/string.md), 'provider' => [string](/API_docs/types/string.md), 'venue_id' => [string](/API_docs/types/string.md), 'venue_type' => [string](/API_docs/types/string.md), \];<a name="inputMediaVenue"></a>  

***
<br><br>[$inputMessageCallbackQuery](/API_docs/constructors/inputMessageCallbackQuery.md) = \['id' => [int](/API_docs/types/int.md), 'query_id' => [long](/API_docs/types/long.md), \];<a name="inputMessageCallbackQuery"></a>  

***
<br><br>[$inputMessageEntityMentionName](/API_docs/constructors/inputMessageEntityMentionName.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), 'user_id' => [InputUser](/API_docs/types/InputUser.md), \];<a name="inputMessageEntityMentionName"></a>  

***
<br><br>[$inputMessageID](/API_docs/constructors/inputMessageID.md) = \['id' => [int](/API_docs/types/int.md), \];<a name="inputMessageID"></a>  

***
<br><br>[$inputMessagePinned](/API_docs/constructors/inputMessagePinned.md) = \[\];<a name="inputMessagePinned"></a>  

***
<br><br>[$inputMessageReplyTo](/API_docs/constructors/inputMessageReplyTo.md) = \['id' => [int](/API_docs/types/int.md), \];<a name="inputMessageReplyTo"></a>  

***
<br><br>[$inputMessagesFilterChatPhotos](/API_docs/constructors/inputMessagesFilterChatPhotos.md) = \[\];<a name="inputMessagesFilterChatPhotos"></a>  

***
<br><br>[$inputMessagesFilterContacts](/API_docs/constructors/inputMessagesFilterContacts.md) = \[\];<a name="inputMessagesFilterContacts"></a>  

***
<br><br>[$inputMessagesFilterDocument](/API_docs/constructors/inputMessagesFilterDocument.md) = \[\];<a name="inputMessagesFilterDocument"></a>  

***
<br><br>[$inputMessagesFilterEmpty](/API_docs/constructors/inputMessagesFilterEmpty.md) = \[\];<a name="inputMessagesFilterEmpty"></a>  

***
<br><br>[$inputMessagesFilterGeo](/API_docs/constructors/inputMessagesFilterGeo.md) = \[\];<a name="inputMessagesFilterGeo"></a>  

***
<br><br>[$inputMessagesFilterGif](/API_docs/constructors/inputMessagesFilterGif.md) = \[\];<a name="inputMessagesFilterGif"></a>  

***
<br><br>[$inputMessagesFilterMusic](/API_docs/constructors/inputMessagesFilterMusic.md) = \[\];<a name="inputMessagesFilterMusic"></a>  

***
<br><br>[$inputMessagesFilterMyMentions](/API_docs/constructors/inputMessagesFilterMyMentions.md) = \[\];<a name="inputMessagesFilterMyMentions"></a>  

***
<br><br>[$inputMessagesFilterPhoneCalls](/API_docs/constructors/inputMessagesFilterPhoneCalls.md) = \['missed' => [Bool](/API_docs/types/Bool.md), \];<a name="inputMessagesFilterPhoneCalls"></a>  

***
<br><br>[$inputMessagesFilterPhotoVideo](/API_docs/constructors/inputMessagesFilterPhotoVideo.md) = \[\];<a name="inputMessagesFilterPhotoVideo"></a>  

***
<br><br>[$inputMessagesFilterPhotos](/API_docs/constructors/inputMessagesFilterPhotos.md) = \[\];<a name="inputMessagesFilterPhotos"></a>  

***
<br><br>[$inputMessagesFilterPinned](/API_docs/constructors/inputMessagesFilterPinned.md) = \[\];<a name="inputMessagesFilterPinned"></a>  

***
<br><br>[$inputMessagesFilterRoundVideo](/API_docs/constructors/inputMessagesFilterRoundVideo.md) = \[\];<a name="inputMessagesFilterRoundVideo"></a>  

***
<br><br>[$inputMessagesFilterRoundVoice](/API_docs/constructors/inputMessagesFilterRoundVoice.md) = \[\];<a name="inputMessagesFilterRoundVoice"></a>  

***
<br><br>[$inputMessagesFilterUrl](/API_docs/constructors/inputMessagesFilterUrl.md) = \[\];<a name="inputMessagesFilterUrl"></a>  

***
<br><br>[$inputMessagesFilterVideo](/API_docs/constructors/inputMessagesFilterVideo.md) = \[\];<a name="inputMessagesFilterVideo"></a>  

***
<br><br>[$inputMessagesFilterVoice](/API_docs/constructors/inputMessagesFilterVoice.md) = \[\];<a name="inputMessagesFilterVoice"></a>  

***
<br><br>[$inputNotifyBroadcasts](/API_docs/constructors/inputNotifyBroadcasts.md) = \[\];<a name="inputNotifyBroadcasts"></a>  

***
<br><br>[$inputNotifyChats](/API_docs/constructors/inputNotifyChats.md) = \[\];<a name="inputNotifyChats"></a>  

***
<br><br>[$inputNotifyPeer](/API_docs/constructors/inputNotifyPeer.md) = \['peer' => [InputPeer](/API_docs/types/InputPeer.md), \];<a name="inputNotifyPeer"></a>  

***
<br><br>[$inputNotifyUsers](/API_docs/constructors/inputNotifyUsers.md) = \[\];<a name="inputNotifyUsers"></a>  

***
<br><br>[$inputPaymentCredentials](/API_docs/constructors/inputPaymentCredentials.md) = \['save' => [Bool](/API_docs/types/Bool.md), 'data' => [DataJSON](/API_docs/types/DataJSON.md), \];<a name="inputPaymentCredentials"></a>  

***
<br><br>[$inputPaymentCredentialsApplePay](/API_docs/constructors/inputPaymentCredentialsApplePay.md) = \['payment_data' => [DataJSON](/API_docs/types/DataJSON.md), \];<a name="inputPaymentCredentialsApplePay"></a>  

***
<br><br>[$inputPaymentCredentialsGooglePay](/API_docs/constructors/inputPaymentCredentialsGooglePay.md) = \['payment_token' => [DataJSON](/API_docs/types/DataJSON.md), \];<a name="inputPaymentCredentialsGooglePay"></a>  

***
<br><br>[$inputPaymentCredentialsSaved](/API_docs/constructors/inputPaymentCredentialsSaved.md) = \['id' => [string](/API_docs/types/string.md), 'tmp_password' => [bytes](/API_docs/types/bytes.md), \];<a name="inputPaymentCredentialsSaved"></a>  

***
<br><br>[$inputPeerChannel](/API_docs/constructors/inputPeerChannel.md) = \['channel_id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputPeerChannel"></a>  

***
<br><br>[$inputPeerChannelFromMessage](/API_docs/constructors/inputPeerChannelFromMessage.md) = \['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'channel_id' => [long](/API_docs/types/long.md), \];<a name="inputPeerChannelFromMessage"></a>  

***
<br><br>[$inputPeerChat](/API_docs/constructors/inputPeerChat.md) = \['chat_id' => [long](/API_docs/types/long.md), \];<a name="inputPeerChat"></a>  

***
<br><br>[$inputPeerEmpty](/API_docs/constructors/inputPeerEmpty.md) = \[\];<a name="inputPeerEmpty"></a>  

***
<br><br>[$inputPeerNotifySettings](/API_docs/constructors/inputPeerNotifySettings.md) = \['show_previews' => [Bool](/API_docs/types/Bool.md), 'silent' => [Bool](/API_docs/types/Bool.md), 'mute_until' => [int](/API_docs/types/int.md), 'sound' => [string](/API_docs/types/string.md), \];<a name="inputPeerNotifySettings"></a>  

***
<br><br>[$inputPeerPhotoFileLocation](/API_docs/constructors/inputPeerPhotoFileLocation.md) = \['big' => [Bool](/API_docs/types/Bool.md), 'peer' => [InputPeer](/API_docs/types/InputPeer.md), 'photo_id' => [long](/API_docs/types/long.md), \];<a name="inputPeerPhotoFileLocation"></a>  

***
<br><br>[$inputPeerSelf](/API_docs/constructors/inputPeerSelf.md) = \[\];<a name="inputPeerSelf"></a>  

***
<br><br>[$inputPeerUser](/API_docs/constructors/inputPeerUser.md) = \['user_id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputPeerUser"></a>  

***
<br><br>[$inputPeerUserFromMessage](/API_docs/constructors/inputPeerUserFromMessage.md) = \['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'user_id' => [long](/API_docs/types/long.md), \];<a name="inputPeerUserFromMessage"></a>  

***
<br><br>[$inputPhoneCall](/API_docs/constructors/inputPhoneCall.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputPhoneCall"></a>  

***
<br><br>[$inputPhoneContact](/API_docs/constructors/inputPhoneContact.md) = \['client_id' => [long](/API_docs/types/long.md), 'phone' => [string](/API_docs/types/string.md), 'first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), \];<a name="inputPhoneContact"></a>  

***
<br><br>[$inputPhoto](/API_docs/constructors/inputPhoto.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'file_reference' => [bytes](/API_docs/types/bytes.md), \];<a name="inputPhoto"></a>  

***
<br><br>[$inputPhotoEmpty](/API_docs/constructors/inputPhotoEmpty.md) = \[\];<a name="inputPhotoEmpty"></a>  

***
<br><br>[$inputPhotoFileLocation](/API_docs/constructors/inputPhotoFileLocation.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'file_reference' => [bytes](/API_docs/types/bytes.md), 'thumb_size' => [string](/API_docs/types/string.md), \];<a name="inputPhotoFileLocation"></a>  

***
<br><br>[$inputPhotoLegacyFileLocation](/API_docs/constructors/inputPhotoLegacyFileLocation.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'file_reference' => [bytes](/API_docs/types/bytes.md), 'volume_id' => [long](/API_docs/types/long.md), 'local_id' => [int](/API_docs/types/int.md), 'secret' => [long](/API_docs/types/long.md), \];<a name="inputPhotoLegacyFileLocation"></a>  

***
<br><br>[$inputPrivacyKeyAddedByPhone](/API_docs/constructors/inputPrivacyKeyAddedByPhone.md) = \[\];<a name="inputPrivacyKeyAddedByPhone"></a>  

***
<br><br>[$inputPrivacyKeyChatInvite](/API_docs/constructors/inputPrivacyKeyChatInvite.md) = \[\];<a name="inputPrivacyKeyChatInvite"></a>  

***
<br><br>[$inputPrivacyKeyForwards](/API_docs/constructors/inputPrivacyKeyForwards.md) = \[\];<a name="inputPrivacyKeyForwards"></a>  

***
<br><br>[$inputPrivacyKeyPhoneCall](/API_docs/constructors/inputPrivacyKeyPhoneCall.md) = \[\];<a name="inputPrivacyKeyPhoneCall"></a>  

***
<br><br>[$inputPrivacyKeyPhoneNumber](/API_docs/constructors/inputPrivacyKeyPhoneNumber.md) = \[\];<a name="inputPrivacyKeyPhoneNumber"></a>  

***
<br><br>[$inputPrivacyKeyPhoneP2P](/API_docs/constructors/inputPrivacyKeyPhoneP2P.md) = \[\];<a name="inputPrivacyKeyPhoneP2P"></a>  

***
<br><br>[$inputPrivacyKeyProfilePhoto](/API_docs/constructors/inputPrivacyKeyProfilePhoto.md) = \[\];<a name="inputPrivacyKeyProfilePhoto"></a>  

***
<br><br>[$inputPrivacyKeyStatusTimestamp](/API_docs/constructors/inputPrivacyKeyStatusTimestamp.md) = \[\];<a name="inputPrivacyKeyStatusTimestamp"></a>  

***
<br><br>[$inputPrivacyValueAllowAll](/API_docs/constructors/inputPrivacyValueAllowAll.md) = \[\];<a name="inputPrivacyValueAllowAll"></a>  

***
<br><br>[$inputPrivacyValueAllowChatParticipants](/API_docs/constructors/inputPrivacyValueAllowChatParticipants.md) = \['chats' => \[[long](/API_docs/types/long.md)\], \];<a name="inputPrivacyValueAllowChatParticipants"></a>  

***
<br><br>[$inputPrivacyValueAllowContacts](/API_docs/constructors/inputPrivacyValueAllowContacts.md) = \[\];<a name="inputPrivacyValueAllowContacts"></a>  

***
<br><br>[$inputPrivacyValueAllowUsers](/API_docs/constructors/inputPrivacyValueAllowUsers.md) = \['users' => \[[InputUser](/API_docs/types/InputUser.md)\], \];<a name="inputPrivacyValueAllowUsers"></a>  

***
<br><br>[$inputPrivacyValueDisallowAll](/API_docs/constructors/inputPrivacyValueDisallowAll.md) = \[\];<a name="inputPrivacyValueDisallowAll"></a>  

***
<br><br>[$inputPrivacyValueDisallowChatParticipants](/API_docs/constructors/inputPrivacyValueDisallowChatParticipants.md) = \['chats' => \[[long](/API_docs/types/long.md)\], \];<a name="inputPrivacyValueDisallowChatParticipants"></a>  

***
<br><br>[$inputPrivacyValueDisallowContacts](/API_docs/constructors/inputPrivacyValueDisallowContacts.md) = \[\];<a name="inputPrivacyValueDisallowContacts"></a>  

***
<br><br>[$inputPrivacyValueDisallowUsers](/API_docs/constructors/inputPrivacyValueDisallowUsers.md) = \['users' => \[[InputUser](/API_docs/types/InputUser.md)\], \];<a name="inputPrivacyValueDisallowUsers"></a>  

***
<br><br>[$inputReportReasonChildAbuse](/API_docs/constructors/inputReportReasonChildAbuse.md) = \[\];<a name="inputReportReasonChildAbuse"></a>  

***
<br><br>[$inputReportReasonCopyright](/API_docs/constructors/inputReportReasonCopyright.md) = \[\];<a name="inputReportReasonCopyright"></a>  

***
<br><br>[$inputReportReasonFake](/API_docs/constructors/inputReportReasonFake.md) = \[\];<a name="inputReportReasonFake"></a>  

***
<br><br>[$inputReportReasonGeoIrrelevant](/API_docs/constructors/inputReportReasonGeoIrrelevant.md) = \[\];<a name="inputReportReasonGeoIrrelevant"></a>  

***
<br><br>[$inputReportReasonOther](/API_docs/constructors/inputReportReasonOther.md) = \[\];<a name="inputReportReasonOther"></a>  

***
<br><br>[$inputReportReasonPornography](/API_docs/constructors/inputReportReasonPornography.md) = \[\];<a name="inputReportReasonPornography"></a>  

***
<br><br>[$inputReportReasonSpam](/API_docs/constructors/inputReportReasonSpam.md) = \[\];<a name="inputReportReasonSpam"></a>  

***
<br><br>[$inputReportReasonViolence](/API_docs/constructors/inputReportReasonViolence.md) = \[\];<a name="inputReportReasonViolence"></a>  

***
<br><br>[$inputSecureFile](/API_docs/constructors/inputSecureFile.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputSecureFile"></a>  

***
<br><br>[$inputSecureFileLocation](/API_docs/constructors/inputSecureFileLocation.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputSecureFileLocation"></a>  

***
<br><br>[$inputSecureFileUploaded](/API_docs/constructors/inputSecureFileUploaded.md) = \['id' => [long](/API_docs/types/long.md), 'parts' => [int](/API_docs/types/int.md), 'md5_checksum' => [string](/API_docs/types/string.md), 'file_hash' => [bytes](/API_docs/types/bytes.md), 'secret' => [bytes](/API_docs/types/bytes.md), \];<a name="inputSecureFileUploaded"></a>  

***
<br><br>[$inputSecureValue](/API_docs/constructors/inputSecureValue.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'data' => [SecureData](/API_docs/types/SecureData.md), 'front_side' => [InputSecureFile](/API_docs/types/InputSecureFile.md), 'reverse_side' => [InputSecureFile](/API_docs/types/InputSecureFile.md), 'selfie' => [InputSecureFile](/API_docs/types/InputSecureFile.md), 'translation' => \[[InputSecureFile](/API_docs/types/InputSecureFile.md)\], 'files' => \[[InputSecureFile](/API_docs/types/InputSecureFile.md)\], 'plain_data' => [SecurePlainData](/API_docs/types/SecurePlainData.md), \];<a name="inputSecureValue"></a>  

***
<br><br>[$inputSingleMedia](/API_docs/constructors/inputSingleMedia.md) = \['media' => [InputMedia](/API_docs/types/InputMedia.md), 'message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], \];<a name="inputSingleMedia"></a>  

***
<br><br>[$inputStickerSetAnimatedEmoji](/API_docs/constructors/inputStickerSetAnimatedEmoji.md) = \[\];<a name="inputStickerSetAnimatedEmoji"></a>  

***
<br><br>[$inputStickerSetAnimatedEmojiAnimations](/API_docs/constructors/inputStickerSetAnimatedEmojiAnimations.md) = \[\];<a name="inputStickerSetAnimatedEmojiAnimations"></a>  

***
<br><br>[$inputStickerSetDice](/API_docs/constructors/inputStickerSetDice.md) = \['emoticon' => [string](/API_docs/types/string.md), \];<a name="inputStickerSetDice"></a>  

***
<br><br>[$inputStickerSetEmpty](/API_docs/constructors/inputStickerSetEmpty.md) = \[\];<a name="inputStickerSetEmpty"></a>  

***
<br><br>[$inputStickerSetID](/API_docs/constructors/inputStickerSetID.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputStickerSetID"></a>  

***
<br><br>[$inputStickerSetItem](/API_docs/constructors/inputStickerSetItem.md) = \['document' => [InputDocument](/API_docs/types/InputDocument.md), 'emoji' => [string](/API_docs/types/string.md), 'mask_coords' => [MaskCoords](/API_docs/types/MaskCoords.md), \];<a name="inputStickerSetItem"></a>  

***
<br><br>[$inputStickerSetShortName](/API_docs/constructors/inputStickerSetShortName.md) = \['short_name' => [string](/API_docs/types/string.md), \];<a name="inputStickerSetShortName"></a>  

***
<br><br>[$inputStickerSetThumb](/API_docs/constructors/inputStickerSetThumb.md) = \['stickerset' => [InputStickerSet](/API_docs/types/InputStickerSet.md), 'thumb_version' => [int](/API_docs/types/int.md), \];<a name="inputStickerSetThumb"></a>  

***
<br><br>[$inputStickeredMediaDocument](/API_docs/constructors/inputStickeredMediaDocument.md) = \['id' => [InputDocument](/API_docs/types/InputDocument.md), \];<a name="inputStickeredMediaDocument"></a>  

***
<br><br>[$inputStickeredMediaPhoto](/API_docs/constructors/inputStickeredMediaPhoto.md) = \['id' => [InputPhoto](/API_docs/types/InputPhoto.md), \];<a name="inputStickeredMediaPhoto"></a>  

***
<br><br>[$inputTakeoutFileLocation](/API_docs/constructors/inputTakeoutFileLocation.md) = \[\];<a name="inputTakeoutFileLocation"></a>  

***
<br><br>[$inputTheme](/API_docs/constructors/inputTheme.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputTheme"></a>  

***
<br><br>[$inputThemeSettings](/API_docs/constructors/inputThemeSettings.md) = \['message_colors_animated' => [Bool](/API_docs/types/Bool.md), 'base_theme' => [BaseTheme](/API_docs/types/BaseTheme.md), 'accent_color' => [int](/API_docs/types/int.md), 'outbox_accent_color' => [int](/API_docs/types/int.md), 'message_colors' => \[[int](/API_docs/types/int.md)\], 'wallpaper' => [InputWallPaper](/API_docs/types/InputWallPaper.md), 'wallpaper_settings' => [WallPaperSettings](/API_docs/types/WallPaperSettings.md), \];<a name="inputThemeSettings"></a>  

***
<br><br>[$inputThemeSlug](/API_docs/constructors/inputThemeSlug.md) = \['slug' => [string](/API_docs/types/string.md), \];<a name="inputThemeSlug"></a>  

***
<br><br>[$inputUser](/API_docs/constructors/inputUser.md) = \['user_id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputUser"></a>  

***
<br><br>[$inputUserEmpty](/API_docs/constructors/inputUserEmpty.md) = \[\];<a name="inputUserEmpty"></a>  

***
<br><br>[$inputUserFromMessage](/API_docs/constructors/inputUserFromMessage.md) = \['peer' => [InputPeer](/API_docs/types/InputPeer.md), 'msg_id' => [int](/API_docs/types/int.md), 'user_id' => [long](/API_docs/types/long.md), \];<a name="inputUserFromMessage"></a>  

***
<br><br>[$inputUserSelf](/API_docs/constructors/inputUserSelf.md) = \[\];<a name="inputUserSelf"></a>  

***
<br><br>[$inputWallPaper](/API_docs/constructors/inputWallPaper.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputWallPaper"></a>  

***
<br><br>[$inputWallPaperNoFile](/API_docs/constructors/inputWallPaperNoFile.md) = \['id' => [long](/API_docs/types/long.md), \];<a name="inputWallPaperNoFile"></a>  

***
<br><br>[$inputWallPaperSlug](/API_docs/constructors/inputWallPaperSlug.md) = \['slug' => [string](/API_docs/types/string.md), \];<a name="inputWallPaperSlug"></a>  

***
<br><br>[$inputWebDocument](/API_docs/constructors/inputWebDocument.md) = \['url' => [string](/API_docs/types/string.md), 'size' => [int](/API_docs/types/int.md), 'mime_type' => [string](/API_docs/types/string.md), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.md)\], \];<a name="inputWebDocument"></a>  

***
<br><br>[$inputWebFileGeoPointLocation](/API_docs/constructors/inputWebFileGeoPointLocation.md) = \['geo_point' => [InputGeoPoint](/API_docs/types/InputGeoPoint.md), 'access_hash' => [long](/API_docs/types/long.md), 'w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), 'zoom' => [int](/API_docs/types/int.md), 'scale' => [int](/API_docs/types/int.md), \];<a name="inputWebFileGeoPointLocation"></a>  

***
<br><br>[$inputWebFileLocation](/API_docs/constructors/inputWebFileLocation.md) = \['url' => [string](/API_docs/types/string.md), 'access_hash' => [long](/API_docs/types/long.md), \];<a name="inputWebFileLocation"></a>  

***
<br><br>[$invoice](/API_docs/constructors/invoice.md) = \['test' => [Bool](/API_docs/types/Bool.md), 'name_requested' => [Bool](/API_docs/types/Bool.md), 'phone_requested' => [Bool](/API_docs/types/Bool.md), 'email_requested' => [Bool](/API_docs/types/Bool.md), 'shipping_address_requested' => [Bool](/API_docs/types/Bool.md), 'flexible' => [Bool](/API_docs/types/Bool.md), 'phone_to_provider' => [Bool](/API_docs/types/Bool.md), 'email_to_provider' => [Bool](/API_docs/types/Bool.md), 'currency' => [string](/API_docs/types/string.md), 'prices' => \[[LabeledPrice](/API_docs/types/LabeledPrice.md)\], 'max_tip_amount' => [long](/API_docs/types/long.md), 'suggested_tip_amounts' => \[[long](/API_docs/types/long.md)\], \];<a name="invoice"></a>  

***
<br><br>[$jsonArray](/API_docs/constructors/jsonArray.md) = \['value' => \[[JSONValue](/API_docs/types/JSONValue.md)\], \];<a name="jsonArray"></a>  

***
<br><br>[$jsonBool](/API_docs/constructors/jsonBool.md) = \['value' => [Bool](/API_docs/types/Bool.md), \];<a name="jsonBool"></a>  

***
<br><br>[$jsonNull](/API_docs/constructors/jsonNull.md) = \[\];<a name="jsonNull"></a>  

***
<br><br>[$jsonNumber](/API_docs/constructors/jsonNumber.md) = \['value' => [double](/API_docs/types/double.md), \];<a name="jsonNumber"></a>  

***
<br><br>[$jsonObject](/API_docs/constructors/jsonObject.md) = \['value' => \[[JSONObjectValue](/API_docs/types/JSONObjectValue.md)\], \];<a name="jsonObject"></a>  

***
<br><br>[$jsonObjectValue](/API_docs/constructors/jsonObjectValue.md) = \['key' => [string](/API_docs/types/string.md), 'value' => [JSONValue](/API_docs/types/JSONValue.md), \];<a name="jsonObjectValue"></a>  

***
<br><br>[$jsonString](/API_docs/constructors/jsonString.md) = \['value' => [string](/API_docs/types/string.md), \];<a name="jsonString"></a>  

***
<br><br>[$keyboardButton](/API_docs/constructors/keyboardButton.md) = \['text' => [string](/API_docs/types/string.md), \];<a name="keyboardButton"></a>  

***
<br><br>[$keyboardButtonBuy](/API_docs/constructors/keyboardButtonBuy.md) = \['text' => [string](/API_docs/types/string.md), \];<a name="keyboardButtonBuy"></a>  

***
<br><br>[$keyboardButtonCallback](/API_docs/constructors/keyboardButtonCallback.md) = \['requires_password' => [Bool](/API_docs/types/Bool.md), 'text' => [string](/API_docs/types/string.md), 'data' => [bytes](/API_docs/types/bytes.md), \];<a name="keyboardButtonCallback"></a>  

***
<br><br>[$keyboardButtonGame](/API_docs/constructors/keyboardButtonGame.md) = \['text' => [string](/API_docs/types/string.md), \];<a name="keyboardButtonGame"></a>  

***
<br><br>[$keyboardButtonRequestGeoLocation](/API_docs/constructors/keyboardButtonRequestGeoLocation.md) = \['text' => [string](/API_docs/types/string.md), \];<a name="keyboardButtonRequestGeoLocation"></a>  

***
<br><br>[$keyboardButtonRequestPhone](/API_docs/constructors/keyboardButtonRequestPhone.md) = \['text' => [string](/API_docs/types/string.md), \];<a name="keyboardButtonRequestPhone"></a>  

***
<br><br>[$keyboardButtonRequestPoll](/API_docs/constructors/keyboardButtonRequestPoll.md) = \['quiz' => [Bool](/API_docs/types/Bool.md), 'text' => [string](/API_docs/types/string.md), \];<a name="keyboardButtonRequestPoll"></a>  

***
<br><br>[$keyboardButtonRow](/API_docs/constructors/keyboardButtonRow.md) = \['buttons' => \[[KeyboardButton](/API_docs/types/KeyboardButton.md)\], \];<a name="keyboardButtonRow"></a>  

***
<br><br>[$keyboardButtonSwitchInline](/API_docs/constructors/keyboardButtonSwitchInline.md) = \['same_peer' => [Bool](/API_docs/types/Bool.md), 'text' => [string](/API_docs/types/string.md), 'query' => [string](/API_docs/types/string.md), \];<a name="keyboardButtonSwitchInline"></a>  

***
<br><br>[$keyboardButtonUrl](/API_docs/constructors/keyboardButtonUrl.md) = \['text' => [string](/API_docs/types/string.md), 'url' => [string](/API_docs/types/string.md), \];<a name="keyboardButtonUrl"></a>  

***
<br><br>[$keyboardButtonUrlAuth](/API_docs/constructors/keyboardButtonUrlAuth.md) = \['text' => [string](/API_docs/types/string.md), 'fwd_text' => [string](/API_docs/types/string.md), 'url' => [string](/API_docs/types/string.md), 'button_id' => [int](/API_docs/types/int.md), \];<a name="keyboardButtonUrlAuth"></a>  

***
<br><br>[$keyboardButtonUserProfile](/API_docs/constructors/keyboardButtonUserProfile.md) = \['text' => [string](/API_docs/types/string.md), 'user_id' => [long](/API_docs/types/long.md), \];<a name="keyboardButtonUserProfile"></a>  

***
<br><br>[$labeledPrice](/API_docs/constructors/labeledPrice.md) = \['label' => [string](/API_docs/types/string.md), 'amount' => [long](/API_docs/types/long.md), \];<a name="labeledPrice"></a>  

***
<br><br>[$langPackDifference](/API_docs/constructors/langPackDifference.md) = \['lang_code' => [string](/API_docs/types/string.md), 'from_version' => [int](/API_docs/types/int.md), 'version' => [int](/API_docs/types/int.md), 'strings' => \[[LangPackString](/API_docs/types/LangPackString.md)\], \];<a name="langPackDifference"></a>  

***
<br><br>[$langPackLanguage](/API_docs/constructors/langPackLanguage.md) = \['official' => [Bool](/API_docs/types/Bool.md), 'rtl' => [Bool](/API_docs/types/Bool.md), 'beta' => [Bool](/API_docs/types/Bool.md), 'name' => [string](/API_docs/types/string.md), 'native_name' => [string](/API_docs/types/string.md), 'lang_code' => [string](/API_docs/types/string.md), 'base_lang_code' => [string](/API_docs/types/string.md), 'plural_code' => [string](/API_docs/types/string.md), 'strings_count' => [int](/API_docs/types/int.md), 'translated_count' => [int](/API_docs/types/int.md), 'translations_url' => [string](/API_docs/types/string.md), \];<a name="langPackLanguage"></a>  

***
<br><br>[$langPackString](/API_docs/constructors/langPackString.md) = \['key' => [string](/API_docs/types/string.md), 'value' => [string](/API_docs/types/string.md), \];<a name="langPackString"></a>  

***
<br><br>[$langPackStringDeleted](/API_docs/constructors/langPackStringDeleted.md) = \['key' => [string](/API_docs/types/string.md), \];<a name="langPackStringDeleted"></a>  

***
<br><br>[$langPackStringPluralized](/API_docs/constructors/langPackStringPluralized.md) = \['key' => [string](/API_docs/types/string.md), 'zero_value' => [string](/API_docs/types/string.md), 'one_value' => [string](/API_docs/types/string.md), 'two_value' => [string](/API_docs/types/string.md), 'few_value' => [string](/API_docs/types/string.md), 'many_value' => [string](/API_docs/types/string.md), 'other_value' => [string](/API_docs/types/string.md), \];<a name="langPackStringPluralized"></a>  

***
<br><br>[$maskCoords](/API_docs/constructors/maskCoords.md) = \['n' => [int](/API_docs/types/int.md), 'x' => [double](/API_docs/types/double.md), 'y' => [double](/API_docs/types/double.md), 'zoom' => [double](/API_docs/types/double.md), \];<a name="maskCoords"></a>  

***
<br><br>[$message](/API_docs/constructors/message.md) = \['out' => [Bool](/API_docs/types/Bool.md), 'mentioned' => [Bool](/API_docs/types/Bool.md), 'media_unread' => [Bool](/API_docs/types/Bool.md), 'silent' => [Bool](/API_docs/types/Bool.md), 'post' => [Bool](/API_docs/types/Bool.md), 'from_scheduled' => [Bool](/API_docs/types/Bool.md), 'legacy' => [Bool](/API_docs/types/Bool.md), 'edit_hide' => [Bool](/API_docs/types/Bool.md), 'pinned' => [Bool](/API_docs/types/Bool.md), 'noforwards' => [Bool](/API_docs/types/Bool.md), 'id' => [int](/API_docs/types/int.md), 'from_id' => [Peer](/API_docs/types/Peer.md), 'peer_id' => [Peer](/API_docs/types/Peer.md), 'fwd_from' => [MessageFwdHeader](/API_docs/types/MessageFwdHeader.md), 'via_bot_id' => [long](/API_docs/types/long.md), 'reply_to' => [MessageReplyHeader](/API_docs/types/MessageReplyHeader.md), 'date' => [int](/API_docs/types/int.md), 'message' => [string](/API_docs/types/string.md), 'media' => [MessageMedia](/API_docs/types/MessageMedia.md), 'reply_markup' => [ReplyMarkup](/API_docs/types/ReplyMarkup.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'views' => [int](/API_docs/types/int.md), 'forwards' => [int](/API_docs/types/int.md), 'replies' => [MessageReplies](/API_docs/types/MessageReplies.md), 'edit_date' => [int](/API_docs/types/int.md), 'post_author' => [string](/API_docs/types/string.md), 'grouped_id' => [long](/API_docs/types/long.md), 'reactions' => [MessageReactions](/API_docs/types/MessageReactions.md), 'restriction_reason' => \[[RestrictionReason](/API_docs/types/RestrictionReason.md)\], 'ttl_period' => [int](/API_docs/types/int.md), \];<a name="message"></a>  

***
<br><br>[$messageActionBotAllowed](/API_docs/constructors/messageActionBotAllowed.md) = \['domain' => [string](/API_docs/types/string.md), \];<a name="messageActionBotAllowed"></a>  

***
<br><br>[$messageActionChannelCreate](/API_docs/constructors/messageActionChannelCreate.md) = \['title' => [string](/API_docs/types/string.md), \];<a name="messageActionChannelCreate"></a>  

***
<br><br>[$messageActionChannelMigrateFrom](/API_docs/constructors/messageActionChannelMigrateFrom.md) = \['title' => [string](/API_docs/types/string.md), 'chat_id' => [long](/API_docs/types/long.md), \];<a name="messageActionChannelMigrateFrom"></a>  

***
<br><br>[$messageActionChatAddUser](/API_docs/constructors/messageActionChatAddUser.md) = \['users' => \[[long](/API_docs/types/long.md)\], \];<a name="messageActionChatAddUser"></a>  

***
<br><br>[$messageActionChatCreate](/API_docs/constructors/messageActionChatCreate.md) = \['title' => [string](/API_docs/types/string.md), 'users' => \[[long](/API_docs/types/long.md)\], \];<a name="messageActionChatCreate"></a>  

***
<br><br>[$messageActionChatDeletePhoto](/API_docs/constructors/messageActionChatDeletePhoto.md) = \[\];<a name="messageActionChatDeletePhoto"></a>  

***
<br><br>[$messageActionChatDeleteUser](/API_docs/constructors/messageActionChatDeleteUser.md) = \['user_id' => [long](/API_docs/types/long.md), \];<a name="messageActionChatDeleteUser"></a>  

***
<br><br>[$messageActionChatEditPhoto](/API_docs/constructors/messageActionChatEditPhoto.md) = \['photo' => [Photo](/API_docs/types/Photo.md), \];<a name="messageActionChatEditPhoto"></a>  

***
<br><br>[$messageActionChatEditTitle](/API_docs/constructors/messageActionChatEditTitle.md) = \['title' => [string](/API_docs/types/string.md), \];<a name="messageActionChatEditTitle"></a>  

***
<br><br>[$messageActionChatJoinedByLink](/API_docs/constructors/messageActionChatJoinedByLink.md) = \['inviter_id' => [long](/API_docs/types/long.md), \];<a name="messageActionChatJoinedByLink"></a>  

***
<br><br>[$messageActionChatJoinedByRequest](/API_docs/constructors/messageActionChatJoinedByRequest.md) = \[\];<a name="messageActionChatJoinedByRequest"></a>  

***
<br><br>[$messageActionChatMigrateTo](/API_docs/constructors/messageActionChatMigrateTo.md) = \['channel_id' => [long](/API_docs/types/long.md), \];<a name="messageActionChatMigrateTo"></a>  

***
<br><br>[$messageActionContactSignUp](/API_docs/constructors/messageActionContactSignUp.md) = \[\];<a name="messageActionContactSignUp"></a>  

***
<br><br>[$messageActionCustomAction](/API_docs/constructors/messageActionCustomAction.md) = \['message' => [string](/API_docs/types/string.md), \];<a name="messageActionCustomAction"></a>  

***
<br><br>[$messageActionEmpty](/API_docs/constructors/messageActionEmpty.md) = \[\];<a name="messageActionEmpty"></a>  

***
<br><br>[$messageActionGameScore](/API_docs/constructors/messageActionGameScore.md) = \['game_id' => [long](/API_docs/types/long.md), 'score' => [int](/API_docs/types/int.md), \];<a name="messageActionGameScore"></a>  

***
<br><br>[$messageActionGeoProximityReached](/API_docs/constructors/messageActionGeoProximityReached.md) = \['from_id' => [Peer](/API_docs/types/Peer.md), 'to_id' => [Peer](/API_docs/types/Peer.md), 'distance' => [int](/API_docs/types/int.md), \];<a name="messageActionGeoProximityReached"></a>  

***
<br><br>[$messageActionGroupCall](/API_docs/constructors/messageActionGroupCall.md) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'duration' => [int](/API_docs/types/int.md), \];<a name="messageActionGroupCall"></a>  

***
<br><br>[$messageActionGroupCallScheduled](/API_docs/constructors/messageActionGroupCallScheduled.md) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'schedule_date' => [int](/API_docs/types/int.md), \];<a name="messageActionGroupCallScheduled"></a>  

***
<br><br>[$messageActionHistoryClear](/API_docs/constructors/messageActionHistoryClear.md) = \[\];<a name="messageActionHistoryClear"></a>  

***
<br><br>[$messageActionInviteToGroupCall](/API_docs/constructors/messageActionInviteToGroupCall.md) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'users' => \[[long](/API_docs/types/long.md)\], \];<a name="messageActionInviteToGroupCall"></a>  

***
<br><br>[$messageActionPaymentSent](/API_docs/constructors/messageActionPaymentSent.md) = \['currency' => [string](/API_docs/types/string.md), 'total_amount' => [long](/API_docs/types/long.md), \];<a name="messageActionPaymentSent"></a>  

***
<br><br>[$messageActionPaymentSentMe](/API_docs/constructors/messageActionPaymentSentMe.md) = \['currency' => [string](/API_docs/types/string.md), 'total_amount' => [long](/API_docs/types/long.md), 'payload' => [bytes](/API_docs/types/bytes.md), 'info' => [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.md), 'shipping_option_id' => [string](/API_docs/types/string.md), 'charge' => [PaymentCharge](/API_docs/types/PaymentCharge.md), \];<a name="messageActionPaymentSentMe"></a>  

***
<br><br>[$messageActionPhoneCall](/API_docs/constructors/messageActionPhoneCall.md) = \['video' => [Bool](/API_docs/types/Bool.md), 'call_id' => [long](/API_docs/types/long.md), 'reason' => [PhoneCallDiscardReason](/API_docs/types/PhoneCallDiscardReason.md), 'duration' => [int](/API_docs/types/int.md), \];<a name="messageActionPhoneCall"></a>  

***
<br><br>[$messageActionPinMessage](/API_docs/constructors/messageActionPinMessage.md) = \[\];<a name="messageActionPinMessage"></a>  

***
<br><br>[$messageActionScreenshotTaken](/API_docs/constructors/messageActionScreenshotTaken.md) = \[\];<a name="messageActionScreenshotTaken"></a>  

***
<br><br>[$messageActionSecureValuesSent](/API_docs/constructors/messageActionSecureValuesSent.md) = \['types' => \[[SecureValueType](/API_docs/types/SecureValueType.md)\], \];<a name="messageActionSecureValuesSent"></a>  

***
<br><br>[$messageActionSecureValuesSentMe](/API_docs/constructors/messageActionSecureValuesSentMe.md) = \['values' => \[[SecureValue](/API_docs/types/SecureValue.md)\], 'credentials' => [SecureCredentialsEncrypted](/API_docs/types/SecureCredentialsEncrypted.md), \];<a name="messageActionSecureValuesSentMe"></a>  

***
<br><br>[$messageActionSetChatTheme](/API_docs/constructors/messageActionSetChatTheme.md) = \['emoticon' => [string](/API_docs/types/string.md), \];<a name="messageActionSetChatTheme"></a>  

***
<br><br>[$messageActionSetMessagesTTL](/API_docs/constructors/messageActionSetMessagesTTL.md) = \['period' => [int](/API_docs/types/int.md), \];<a name="messageActionSetMessagesTTL"></a>  

***
<br><br>[$messageEmpty](/API_docs/constructors/messageEmpty.md) = \['id' => [int](/API_docs/types/int.md), 'peer_id' => [Peer](/API_docs/types/Peer.md), \];<a name="messageEmpty"></a>  

***
<br><br>[$messageEntityBankCard](/API_docs/constructors/messageEntityBankCard.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityBankCard"></a>  

***
<br><br>[$messageEntityBlockquote](/API_docs/constructors/messageEntityBlockquote.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityBlockquote"></a>  

***
<br><br>[$messageEntityBold](/API_docs/constructors/messageEntityBold.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityBold"></a>  

***
<br><br>[$messageEntityBotCommand](/API_docs/constructors/messageEntityBotCommand.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityBotCommand"></a>  

***
<br><br>[$messageEntityCashtag](/API_docs/constructors/messageEntityCashtag.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityCashtag"></a>  

***
<br><br>[$messageEntityCode](/API_docs/constructors/messageEntityCode.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityCode"></a>  

***
<br><br>[$messageEntityEmail](/API_docs/constructors/messageEntityEmail.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityEmail"></a>  

***
<br><br>[$messageEntityHashtag](/API_docs/constructors/messageEntityHashtag.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityHashtag"></a>  

***
<br><br>[$messageEntityItalic](/API_docs/constructors/messageEntityItalic.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityItalic"></a>  

***
<br><br>[$messageEntityMention](/API_docs/constructors/messageEntityMention.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityMention"></a>  

***
<br><br>[$messageEntityMentionName](/API_docs/constructors/messageEntityMentionName.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), 'user_id' => [long](/API_docs/types/long.md), \];<a name="messageEntityMentionName"></a>  

***
<br><br>[$messageEntityPhone](/API_docs/constructors/messageEntityPhone.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityPhone"></a>  

***
<br><br>[$messageEntityPre](/API_docs/constructors/messageEntityPre.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), 'language' => [string](/API_docs/types/string.md), \];<a name="messageEntityPre"></a>  

***
<br><br>[$messageEntitySpoiler](/API_docs/constructors/messageEntitySpoiler.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntitySpoiler"></a>  

***
<br><br>[$messageEntityStrike](/API_docs/constructors/messageEntityStrike.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityStrike"></a>  

***
<br><br>[$messageEntityTextUrl](/API_docs/constructors/messageEntityTextUrl.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), 'url' => [string](/API_docs/types/string.md), \];<a name="messageEntityTextUrl"></a>  

***
<br><br>[$messageEntityUnderline](/API_docs/constructors/messageEntityUnderline.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityUnderline"></a>  

***
<br><br>[$messageEntityUnknown](/API_docs/constructors/messageEntityUnknown.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityUnknown"></a>  

***
<br><br>[$messageEntityUrl](/API_docs/constructors/messageEntityUrl.md) = \['offset' => [int](/API_docs/types/int.md), 'length' => [int](/API_docs/types/int.md), \];<a name="messageEntityUrl"></a>  

***
<br><br>[$messageFwdHeader](/API_docs/constructors/messageFwdHeader.md) = \['imported' => [Bool](/API_docs/types/Bool.md), 'from_id' => [Peer](/API_docs/types/Peer.md), 'from_name' => [string](/API_docs/types/string.md), 'date' => [int](/API_docs/types/int.md), 'channel_post' => [int](/API_docs/types/int.md), 'post_author' => [string](/API_docs/types/string.md), 'saved_from_peer' => [Peer](/API_docs/types/Peer.md), 'saved_from_msg_id' => [int](/API_docs/types/int.md), 'psa_type' => [string](/API_docs/types/string.md), \];<a name="messageFwdHeader"></a>  

***
<br><br>[$messageInteractionCounters](/API_docs/constructors/messageInteractionCounters.md) = \['msg_id' => [int](/API_docs/types/int.md), 'views' => [int](/API_docs/types/int.md), 'forwards' => [int](/API_docs/types/int.md), \];<a name="messageInteractionCounters"></a>  

***
<br><br>[$messageMediaContact](/API_docs/constructors/messageMediaContact.md) = \['phone_number' => [string](/API_docs/types/string.md), 'first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), 'vcard' => [string](/API_docs/types/string.md), 'user_id' => [long](/API_docs/types/long.md), \];<a name="messageMediaContact"></a>  

***
<br><br>[$messageMediaDice](/API_docs/constructors/messageMediaDice.md) = \['value' => [int](/API_docs/types/int.md), 'emoticon' => [string](/API_docs/types/string.md), \];<a name="messageMediaDice"></a>  

***
<br><br>[$messageMediaDocument](/API_docs/constructors/messageMediaDocument.md) = \['document' => [Document](/API_docs/types/Document.md), 'ttl_seconds' => [int](/API_docs/types/int.md), \];<a name="messageMediaDocument"></a>  

***
<br><br>[$messageMediaEmpty](/API_docs/constructors/messageMediaEmpty.md) = \[\];<a name="messageMediaEmpty"></a>  

***
<br><br>[$messageMediaGame](/API_docs/constructors/messageMediaGame.md) = \['game' => [Game](/API_docs/types/Game.md), \];<a name="messageMediaGame"></a>  

***
<br><br>[$messageMediaGeo](/API_docs/constructors/messageMediaGeo.md) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.md), \];<a name="messageMediaGeo"></a>  

***
<br><br>[$messageMediaGeoLive](/API_docs/constructors/messageMediaGeoLive.md) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.md), 'heading' => [int](/API_docs/types/int.md), 'period' => [int](/API_docs/types/int.md), 'proximity_notification_radius' => [int](/API_docs/types/int.md), \];<a name="messageMediaGeoLive"></a>  

***
<br><br>[$messageMediaInvoice](/API_docs/constructors/messageMediaInvoice.md) = \['shipping_address_requested' => [Bool](/API_docs/types/Bool.md), 'test' => [Bool](/API_docs/types/Bool.md), 'title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'photo' => [WebDocument](/API_docs/types/WebDocument.md), 'receipt_msg_id' => [int](/API_docs/types/int.md), 'currency' => [string](/API_docs/types/string.md), 'total_amount' => [long](/API_docs/types/long.md), 'start_param' => [string](/API_docs/types/string.md), \];<a name="messageMediaInvoice"></a>  

***
<br><br>[$messageMediaPhoto](/API_docs/constructors/messageMediaPhoto.md) = \['photo' => [Photo](/API_docs/types/Photo.md), 'ttl_seconds' => [int](/API_docs/types/int.md), \];<a name="messageMediaPhoto"></a>  

***
<br><br>[$messageMediaPoll](/API_docs/constructors/messageMediaPoll.md) = \['poll' => [Poll](/API_docs/types/Poll.md), 'results' => [PollResults](/API_docs/types/PollResults.md), \];<a name="messageMediaPoll"></a>  

***
<br><br>[$messageMediaUnsupported](/API_docs/constructors/messageMediaUnsupported.md) = \[\];<a name="messageMediaUnsupported"></a>  

***
<br><br>[$messageMediaVenue](/API_docs/constructors/messageMediaVenue.md) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.md), 'title' => [string](/API_docs/types/string.md), 'address' => [string](/API_docs/types/string.md), 'provider' => [string](/API_docs/types/string.md), 'venue_id' => [string](/API_docs/types/string.md), 'venue_type' => [string](/API_docs/types/string.md), \];<a name="messageMediaVenue"></a>  

***
<br><br>[$messageMediaWebPage](/API_docs/constructors/messageMediaWebPage.md) = \['webpage' => [WebPage](/API_docs/types/WebPage.md), \];<a name="messageMediaWebPage"></a>  

***
<br><br>[$messageRange](/API_docs/constructors/messageRange.md) = \['min_id' => [int](/API_docs/types/int.md), 'max_id' => [int](/API_docs/types/int.md), \];<a name="messageRange"></a>  

***
<br><br>[$messageReactions](/API_docs/constructors/messageReactions.md) = \['min' => [Bool](/API_docs/types/Bool.md), 'can_see_list' => [Bool](/API_docs/types/Bool.md), 'results' => \[[ReactionCount](/API_docs/types/ReactionCount.md)\], 'recent_reactons' => \[[MessageUserReaction](/API_docs/types/MessageUserReaction.md)\], \];<a name="messageReactions"></a>  

***
<br><br>[$messageReplies](/API_docs/constructors/messageReplies.md) = \['comments' => [Bool](/API_docs/types/Bool.md), 'replies' => [int](/API_docs/types/int.md), 'replies_pts' => [int](/API_docs/types/int.md), 'recent_repliers' => \[[Peer](/API_docs/types/Peer.md)\], 'channel_id' => [long](/API_docs/types/long.md), 'max_id' => [int](/API_docs/types/int.md), 'read_max_id' => [int](/API_docs/types/int.md), \];<a name="messageReplies"></a>  

***
<br><br>[$messageReplyHeader](/API_docs/constructors/messageReplyHeader.md) = \['reply_to_msg_id' => [int](/API_docs/types/int.md), 'reply_to_peer_id' => [Peer](/API_docs/types/Peer.md), 'reply_to_top_id' => [int](/API_docs/types/int.md), \];<a name="messageReplyHeader"></a>  

***
<br><br>[$messageService](/API_docs/constructors/messageService.md) = \['out' => [Bool](/API_docs/types/Bool.md), 'mentioned' => [Bool](/API_docs/types/Bool.md), 'media_unread' => [Bool](/API_docs/types/Bool.md), 'silent' => [Bool](/API_docs/types/Bool.md), 'post' => [Bool](/API_docs/types/Bool.md), 'legacy' => [Bool](/API_docs/types/Bool.md), 'id' => [int](/API_docs/types/int.md), 'from_id' => [Peer](/API_docs/types/Peer.md), 'peer_id' => [Peer](/API_docs/types/Peer.md), 'reply_to' => [MessageReplyHeader](/API_docs/types/MessageReplyHeader.md), 'date' => [int](/API_docs/types/int.md), 'action' => [MessageAction](/API_docs/types/MessageAction.md), 'ttl_period' => [int](/API_docs/types/int.md), \];<a name="messageService"></a>  

***
<br><br>[$messageUserReaction](/API_docs/constructors/messageUserReaction.md) = \['user_id' => [long](/API_docs/types/long.md), 'reaction' => [string](/API_docs/types/string.md), \];<a name="messageUserReaction"></a>  

***
<br><br>[$messageUserVote](/API_docs/constructors/messageUserVote.md) = \['user_id' => [long](/API_docs/types/long.md), 'option' => [bytes](/API_docs/types/bytes.md), 'date' => [int](/API_docs/types/int.md), \];<a name="messageUserVote"></a>  

***
<br><br>[$messageUserVoteInputOption](/API_docs/constructors/messageUserVoteInputOption.md) = \['user_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), \];<a name="messageUserVoteInputOption"></a>  

***
<br><br>[$messageUserVoteMultiple](/API_docs/constructors/messageUserVoteMultiple.md) = \['user_id' => [long](/API_docs/types/long.md), 'options' => \[[bytes](/API_docs/types/bytes.md)\], 'date' => [int](/API_docs/types/int.md), \];<a name="messageUserVoteMultiple"></a>  

***
<br><br>[$messageViews](/API_docs/constructors/messageViews.md) = \['views' => [int](/API_docs/types/int.md), 'forwards' => [int](/API_docs/types/int.md), 'replies' => [MessageReplies](/API_docs/types/MessageReplies.md), \];<a name="messageViews"></a>  

***
<br><br>[$messages.affectedFoundMessages](/API_docs/constructors/messages.affectedFoundMessages.md) = \['pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), 'offset' => [int](/API_docs/types/int.md), 'messages' => \[[int](/API_docs/types/int.md)\], \];<a name="messages.affectedFoundMessages"></a>  

***
<br><br>[$messages.affectedHistory](/API_docs/constructors/messages.affectedHistory.md) = \['pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), 'offset' => [int](/API_docs/types/int.md), \];<a name="messages.affectedHistory"></a>  

***
<br><br>[$messages.affectedMessages](/API_docs/constructors/messages.affectedMessages.md) = \['pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="messages.affectedMessages"></a>  

***
<br><br>[$messages.allStickers](/API_docs/constructors/messages.allStickers.md) = \['hash' => [long](/API_docs/types/long.md), 'sets' => \[[StickerSet](/API_docs/types/StickerSet.md)\], \];<a name="messages.allStickers"></a>  

***
<br><br>[$messages.allStickersNotModified](/API_docs/constructors/messages.allStickersNotModified.md) = \[\];<a name="messages.allStickersNotModified"></a>  

***
<br><br>[$messages.archivedStickers](/API_docs/constructors/messages.archivedStickers.md) = \['count' => [int](/API_docs/types/int.md), 'sets' => \[[StickerSetCovered](/API_docs/types/StickerSetCovered.md)\], \];<a name="messages.archivedStickers"></a>  

***
<br><br>[$messages.availableReactions](/API_docs/constructors/messages.availableReactions.md) = \['hash' => [int](/API_docs/types/int.md), 'reactions' => \[[AvailableReaction](/API_docs/types/AvailableReaction.md)\], \];<a name="messages.availableReactions"></a>  

***
<br><br>[$messages.availableReactionsNotModified](/API_docs/constructors/messages.availableReactionsNotModified.md) = \[\];<a name="messages.availableReactionsNotModified"></a>  

***
<br><br>[$messages.botCallbackAnswer](/API_docs/constructors/messages.botCallbackAnswer.md) = \['alert' => [Bool](/API_docs/types/Bool.md), 'has_url' => [Bool](/API_docs/types/Bool.md), 'native_ui' => [Bool](/API_docs/types/Bool.md), 'message' => [string](/API_docs/types/string.md), 'url' => [string](/API_docs/types/string.md), 'cache_time' => [int](/API_docs/types/int.md), \];<a name="messages.botCallbackAnswer"></a>  

***
<br><br>[$messages.botResults](/API_docs/constructors/messages.botResults.md) = \['gallery' => [Bool](/API_docs/types/Bool.md), 'query_id' => [long](/API_docs/types/long.md), 'next_offset' => [string](/API_docs/types/string.md), 'switch_pm' => [InlineBotSwitchPM](/API_docs/types/InlineBotSwitchPM.md), 'results' => \[[BotInlineResult](/API_docs/types/BotInlineResult.md)\], 'cache_time' => [int](/API_docs/types/int.md), 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.botResults"></a>  

***
<br><br>[$messages.channelMessages](/API_docs/constructors/messages.channelMessages.md) = \['inexact' => [Bool](/API_docs/types/Bool.md), 'pts' => [int](/API_docs/types/int.md), 'count' => [int](/API_docs/types/int.md), 'offset_id_offset' => [int](/API_docs/types/int.md), 'messages' => \[[Message](/API_docs/types/Message.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.channelMessages"></a>  

***
<br><br>[$messages.chatAdminsWithInvites](/API_docs/constructors/messages.chatAdminsWithInvites.md) = \['admins' => \[[ChatAdminWithInvites](/API_docs/types/ChatAdminWithInvites.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.chatAdminsWithInvites"></a>  

***
<br><br>[$messages.chatFull](/API_docs/constructors/messages.chatFull.md) = \['full_chat' => [ChatFull](/API_docs/types/ChatFull.md), 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.chatFull"></a>  

***
<br><br>[$messages.chatInviteImporters](/API_docs/constructors/messages.chatInviteImporters.md) = \['count' => [int](/API_docs/types/int.md), 'importers' => \[[ChatInviteImporter](/API_docs/types/ChatInviteImporter.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.chatInviteImporters"></a>  

***
<br><br>[$messages.chats](/API_docs/constructors/messages.chats.md) = \['chats' => \[[Chat](/API_docs/types/Chat.md)\], \];<a name="messages.chats"></a>  

***
<br><br>[$messages.chatsSlice](/API_docs/constructors/messages.chatsSlice.md) = \['count' => [int](/API_docs/types/int.md), 'chats' => \[[Chat](/API_docs/types/Chat.md)\], \];<a name="messages.chatsSlice"></a>  

***
<br><br>[$messages.checkedHistoryImportPeer](/API_docs/constructors/messages.checkedHistoryImportPeer.md) = \['confirm_text' => [string](/API_docs/types/string.md), \];<a name="messages.checkedHistoryImportPeer"></a>  

***
<br><br>[$messages.dhConfig](/API_docs/constructors/messages.dhConfig.md) = \['g' => [int](/API_docs/types/int.md), 'p' => [bytes](/API_docs/types/bytes.md), 'version' => [int](/API_docs/types/int.md), 'random' => [bytes](/API_docs/types/bytes.md), \];<a name="messages.dhConfig"></a>  

***
<br><br>[$messages.dhConfigNotModified](/API_docs/constructors/messages.dhConfigNotModified.md) = \['random' => [bytes](/API_docs/types/bytes.md), \];<a name="messages.dhConfigNotModified"></a>  

***
<br><br>[$messages.dialogs](/API_docs/constructors/messages.dialogs.md) = \['dialogs' => \[[Dialog](/API_docs/types/Dialog.md)\], 'messages' => \[[Message](/API_docs/types/Message.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.dialogs"></a>  

***
<br><br>[$messages.dialogsNotModified](/API_docs/constructors/messages.dialogsNotModified.md) = \['count' => [int](/API_docs/types/int.md), \];<a name="messages.dialogsNotModified"></a>  

***
<br><br>[$messages.dialogsSlice](/API_docs/constructors/messages.dialogsSlice.md) = \['count' => [int](/API_docs/types/int.md), 'dialogs' => \[[Dialog](/API_docs/types/Dialog.md)\], 'messages' => \[[Message](/API_docs/types/Message.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.dialogsSlice"></a>  

***
<br><br>[$messages.discussionMessage](/API_docs/constructors/messages.discussionMessage.md) = \['messages' => \[[Message](/API_docs/types/Message.md)\], 'max_id' => [int](/API_docs/types/int.md), 'read_inbox_max_id' => [int](/API_docs/types/int.md), 'read_outbox_max_id' => [int](/API_docs/types/int.md), 'unread_count' => [int](/API_docs/types/int.md), 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.discussionMessage"></a>  

***
<br><br>[$messages.exportedChatInvite](/API_docs/constructors/messages.exportedChatInvite.md) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.exportedChatInvite"></a>  

***
<br><br>[$messages.exportedChatInviteReplaced](/API_docs/constructors/messages.exportedChatInviteReplaced.md) = \['invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), 'new_invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.exportedChatInviteReplaced"></a>  

***
<br><br>[$messages.exportedChatInvites](/API_docs/constructors/messages.exportedChatInvites.md) = \['count' => [int](/API_docs/types/int.md), 'invites' => \[[ExportedChatInvite](/API_docs/types/ExportedChatInvite.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.exportedChatInvites"></a>  

***
<br><br>[$messages.favedStickers](/API_docs/constructors/messages.favedStickers.md) = \['hash' => [long](/API_docs/types/long.md), 'packs' => \[[StickerPack](/API_docs/types/StickerPack.md)\], 'stickers' => \[[Document](/API_docs/types/Document.md)\], \];<a name="messages.favedStickers"></a>  

***
<br><br>[$messages.favedStickersNotModified](/API_docs/constructors/messages.favedStickersNotModified.md) = \[\];<a name="messages.favedStickersNotModified"></a>  

***
<br><br>[$messages.featuredStickers](/API_docs/constructors/messages.featuredStickers.md) = \['hash' => [long](/API_docs/types/long.md), 'count' => [int](/API_docs/types/int.md), 'sets' => \[[StickerSetCovered](/API_docs/types/StickerSetCovered.md)\], 'unread' => \[[long](/API_docs/types/long.md)\], \];<a name="messages.featuredStickers"></a>  

***
<br><br>[$messages.featuredStickersNotModified](/API_docs/constructors/messages.featuredStickersNotModified.md) = \['count' => [int](/API_docs/types/int.md), \];<a name="messages.featuredStickersNotModified"></a>  

***
<br><br>[$messages.foundStickerSets](/API_docs/constructors/messages.foundStickerSets.md) = \['hash' => [long](/API_docs/types/long.md), 'sets' => \[[StickerSetCovered](/API_docs/types/StickerSetCovered.md)\], \];<a name="messages.foundStickerSets"></a>  

***
<br><br>[$messages.foundStickerSetsNotModified](/API_docs/constructors/messages.foundStickerSetsNotModified.md) = \[\];<a name="messages.foundStickerSetsNotModified"></a>  

***
<br><br>[$messages.highScores](/API_docs/constructors/messages.highScores.md) = \['scores' => \[[HighScore](/API_docs/types/HighScore.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.highScores"></a>  

***
<br><br>[$messages.historyImport](/API_docs/constructors/messages.historyImport.md) = \['id' => [long](/API_docs/types/long.md), \];<a name="messages.historyImport"></a>  

***
<br><br>[$messages.historyImportParsed](/API_docs/constructors/messages.historyImportParsed.md) = \['pm' => [Bool](/API_docs/types/Bool.md), 'group' => [Bool](/API_docs/types/Bool.md), 'title' => [string](/API_docs/types/string.md), \];<a name="messages.historyImportParsed"></a>  

***
<br><br>[$messages.inactiveChats](/API_docs/constructors/messages.inactiveChats.md) = \['dates' => \[[int](/API_docs/types/int.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.inactiveChats"></a>  

***
<br><br>[$messages.messageEditData](/API_docs/constructors/messages.messageEditData.md) = \['caption' => [Bool](/API_docs/types/Bool.md), \];<a name="messages.messageEditData"></a>  

***
<br><br>[$messages.messageReactionsList](/API_docs/constructors/messages.messageReactionsList.md) = \['count' => [int](/API_docs/types/int.md), 'reactions' => \[[MessageUserReaction](/API_docs/types/MessageUserReaction.md)\], 'users' => \[[User](/API_docs/types/User.md)\], 'next_offset' => [string](/API_docs/types/string.md), \];<a name="messages.messageReactionsList"></a>  

***
<br><br>[$messages.messageViews](/API_docs/constructors/messages.messageViews.md) = \['views' => \[[MessageViews](/API_docs/types/MessageViews.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.messageViews"></a>  

***
<br><br>[$messages.messages](/API_docs/constructors/messages.messages.md) = \['messages' => \[[Message](/API_docs/types/Message.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.messages"></a>  

***
<br><br>[$messages.messagesNotModified](/API_docs/constructors/messages.messagesNotModified.md) = \['count' => [int](/API_docs/types/int.md), \];<a name="messages.messagesNotModified"></a>  

***
<br><br>[$messages.messagesSlice](/API_docs/constructors/messages.messagesSlice.md) = \['inexact' => [Bool](/API_docs/types/Bool.md), 'count' => [int](/API_docs/types/int.md), 'next_rate' => [int](/API_docs/types/int.md), 'offset_id_offset' => [int](/API_docs/types/int.md), 'messages' => \[[Message](/API_docs/types/Message.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.messagesSlice"></a>  

***
<br><br>[$messages.peerDialogs](/API_docs/constructors/messages.peerDialogs.md) = \['dialogs' => \[[Dialog](/API_docs/types/Dialog.md)\], 'messages' => \[[Message](/API_docs/types/Message.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], 'state' => [updates.State](/API_docs/types/updates.State.md), \];<a name="messages.peerDialogs"></a>  

***
<br><br>[$messages.peerSettings](/API_docs/constructors/messages.peerSettings.md) = \['settings' => [PeerSettings](/API_docs/types/PeerSettings.md), 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.peerSettings"></a>  

***
<br><br>[$messages.recentStickers](/API_docs/constructors/messages.recentStickers.md) = \['hash' => [long](/API_docs/types/long.md), 'packs' => \[[StickerPack](/API_docs/types/StickerPack.md)\], 'stickers' => \[[Document](/API_docs/types/Document.md)\], 'dates' => \[[int](/API_docs/types/int.md)\], \];<a name="messages.recentStickers"></a>  

***
<br><br>[$messages.recentStickersNotModified](/API_docs/constructors/messages.recentStickersNotModified.md) = \[\];<a name="messages.recentStickersNotModified"></a>  

***
<br><br>[$messages.savedGifs](/API_docs/constructors/messages.savedGifs.md) = \['hash' => [long](/API_docs/types/long.md), 'gifs' => \[[Document](/API_docs/types/Document.md)\], \];<a name="messages.savedGifs"></a>  

***
<br><br>[$messages.savedGifsNotModified](/API_docs/constructors/messages.savedGifsNotModified.md) = \[\];<a name="messages.savedGifsNotModified"></a>  

***
<br><br>[$messages.searchCounter](/API_docs/constructors/messages.searchCounter.md) = \['inexact' => [Bool](/API_docs/types/Bool.md), 'filter' => [MessagesFilter](/API_docs/types/MessagesFilter.md), 'count' => [int](/API_docs/types/int.md), \];<a name="messages.searchCounter"></a>  

***
<br><br>[$messages.searchResultsCalendar](/API_docs/constructors/messages.searchResultsCalendar.md) = \['inexact' => [Bool](/API_docs/types/Bool.md), 'count' => [int](/API_docs/types/int.md), 'min_date' => [int](/API_docs/types/int.md), 'min_msg_id' => [int](/API_docs/types/int.md), 'offset_id_offset' => [int](/API_docs/types/int.md), 'periods' => \[[SearchResultsCalendarPeriod](/API_docs/types/SearchResultsCalendarPeriod.md)\], 'messages' => \[[Message](/API_docs/types/Message.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.searchResultsCalendar"></a>  

***
<br><br>[$messages.searchResultsPositions](/API_docs/constructors/messages.searchResultsPositions.md) = \['count' => [int](/API_docs/types/int.md), 'positions' => \[[SearchResultsPosition](/API_docs/types/SearchResultsPosition.md)\], \];<a name="messages.searchResultsPositions"></a>  

***
<br><br>[$messages.sentEncryptedFile](/API_docs/constructors/messages.sentEncryptedFile.md) = \['date' => [int](/API_docs/types/int.md), 'file' => [EncryptedFile](/API_docs/types/EncryptedFile.md), \];<a name="messages.sentEncryptedFile"></a>  

***
<br><br>[$messages.sentEncryptedMessage](/API_docs/constructors/messages.sentEncryptedMessage.md) = \['date' => [int](/API_docs/types/int.md), \];<a name="messages.sentEncryptedMessage"></a>  

***
<br><br>[$messages.sponsoredMessages](/API_docs/constructors/messages.sponsoredMessages.md) = \['messages' => \[[SponsoredMessage](/API_docs/types/SponsoredMessage.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="messages.sponsoredMessages"></a>  

***
<br><br>[$messages.stickerSet](/API_docs/constructors/messages.stickerSet.md) = \['set' => [StickerSet](/API_docs/types/StickerSet.md), 'packs' => \[[StickerPack](/API_docs/types/StickerPack.md)\], 'documents' => \[[Document](/API_docs/types/Document.md)\], \];<a name="messages.stickerSet"></a>  

***
<br><br>[$messages.stickerSetInstallResultArchive](/API_docs/constructors/messages.stickerSetInstallResultArchive.md) = \['sets' => \[[StickerSetCovered](/API_docs/types/StickerSetCovered.md)\], \];<a name="messages.stickerSetInstallResultArchive"></a>  

***
<br><br>[$messages.stickerSetInstallResultSuccess](/API_docs/constructors/messages.stickerSetInstallResultSuccess.md) = \[\];<a name="messages.stickerSetInstallResultSuccess"></a>  

***
<br><br>[$messages.stickerSetNotModified](/API_docs/constructors/messages.stickerSetNotModified.md) = \[\];<a name="messages.stickerSetNotModified"></a>  

***
<br><br>[$messages.stickers](/API_docs/constructors/messages.stickers.md) = \['hash' => [long](/API_docs/types/long.md), 'stickers' => \[[Document](/API_docs/types/Document.md)\], \];<a name="messages.stickers"></a>  

***
<br><br>[$messages.stickersNotModified](/API_docs/constructors/messages.stickersNotModified.md) = \[\];<a name="messages.stickersNotModified"></a>  

***
<br><br>[$messages.votesList](/API_docs/constructors/messages.votesList.md) = \['count' => [int](/API_docs/types/int.md), 'votes' => \[[MessageUserVote](/API_docs/types/MessageUserVote.md)\], 'users' => \[[User](/API_docs/types/User.md)\], 'next_offset' => [string](/API_docs/types/string.md), \];<a name="messages.votesList"></a>  

***
<br><br>[$nearestDc](/API_docs/constructors/nearestDc.md) = \['country' => [string](/API_docs/types/string.md), 'this_dc' => [int](/API_docs/types/int.md), 'nearest_dc' => [int](/API_docs/types/int.md), \];<a name="nearestDc"></a>  

***
<br><br>[$notifyBroadcasts](/API_docs/constructors/notifyBroadcasts.md) = \[\];<a name="notifyBroadcasts"></a>  

***
<br><br>[$notifyChats](/API_docs/constructors/notifyChats.md) = \[\];<a name="notifyChats"></a>  

***
<br><br>[$notifyPeer](/API_docs/constructors/notifyPeer.md) = \['peer' => [Peer](/API_docs/types/Peer.md), \];<a name="notifyPeer"></a>  

***
<br><br>[$notifyUsers](/API_docs/constructors/notifyUsers.md) = \[\];<a name="notifyUsers"></a>  

***
<br><br>[$null](/API_docs/constructors/null.md) = \[\];<a name="null"></a>  

***
<br><br>[$page](/API_docs/constructors/page.md) = \['part' => [Bool](/API_docs/types/Bool.md), 'rtl' => [Bool](/API_docs/types/Bool.md), 'v2' => [Bool](/API_docs/types/Bool.md), 'url' => [string](/API_docs/types/string.md), 'blocks' => \[[PageBlock](/API_docs/types/PageBlock.md)\], 'photos' => \[[Photo](/API_docs/types/Photo.md)\], 'documents' => \[[Document](/API_docs/types/Document.md)\], 'views' => [int](/API_docs/types/int.md), \];<a name="page"></a>  

***
<br><br>[$pageBlockAnchor](/API_docs/constructors/pageBlockAnchor.md) = \['name' => [string](/API_docs/types/string.md), \];<a name="pageBlockAnchor"></a>  

***
<br><br>[$pageBlockAudio](/API_docs/constructors/pageBlockAudio.md) = \['audio_id' => [long](/API_docs/types/long.md), 'caption' => [PageCaption](/API_docs/types/PageCaption.md), \];<a name="pageBlockAudio"></a>  

***
<br><br>[$pageBlockAuthorDate](/API_docs/constructors/pageBlockAuthorDate.md) = \['author' => [RichText](/API_docs/types/RichText.md), 'published_date' => [int](/API_docs/types/int.md), \];<a name="pageBlockAuthorDate"></a>  

***
<br><br>[$pageBlockBlockquote](/API_docs/constructors/pageBlockBlockquote.md) = \['text' => [RichText](/API_docs/types/RichText.md), 'caption' => [RichText](/API_docs/types/RichText.md), \];<a name="pageBlockBlockquote"></a>  

***
<br><br>[$pageBlockChannel](/API_docs/constructors/pageBlockChannel.md) = \['channel' => [Chat](/API_docs/types/Chat.md), \];<a name="pageBlockChannel"></a>  

***
<br><br>[$pageBlockCollage](/API_docs/constructors/pageBlockCollage.md) = \['items' => \[[PageBlock](/API_docs/types/PageBlock.md)\], 'caption' => [PageCaption](/API_docs/types/PageCaption.md), \];<a name="pageBlockCollage"></a>  

***
<br><br>[$pageBlockCover](/API_docs/constructors/pageBlockCover.md) = \['cover' => [PageBlock](/API_docs/types/PageBlock.md), \];<a name="pageBlockCover"></a>  

***
<br><br>[$pageBlockDetails](/API_docs/constructors/pageBlockDetails.md) = \['open' => [Bool](/API_docs/types/Bool.md), 'blocks' => \[[PageBlock](/API_docs/types/PageBlock.md)\], 'title' => [RichText](/API_docs/types/RichText.md), \];<a name="pageBlockDetails"></a>  

***
<br><br>[$pageBlockDivider](/API_docs/constructors/pageBlockDivider.md) = \[\];<a name="pageBlockDivider"></a>  

***
<br><br>[$pageBlockEmbed](/API_docs/constructors/pageBlockEmbed.md) = \['full_width' => [Bool](/API_docs/types/Bool.md), 'allow_scrolling' => [Bool](/API_docs/types/Bool.md), 'url' => [string](/API_docs/types/string.md), 'html' => [string](/API_docs/types/string.md), 'poster_photo_id' => [long](/API_docs/types/long.md), 'w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), 'caption' => [PageCaption](/API_docs/types/PageCaption.md), \];<a name="pageBlockEmbed"></a>  

***
<br><br>[$pageBlockEmbedPost](/API_docs/constructors/pageBlockEmbedPost.md) = \['url' => [string](/API_docs/types/string.md), 'webpage_id' => [long](/API_docs/types/long.md), 'author_photo_id' => [long](/API_docs/types/long.md), 'author' => [string](/API_docs/types/string.md), 'date' => [int](/API_docs/types/int.md), 'blocks' => \[[PageBlock](/API_docs/types/PageBlock.md)\], 'caption' => [PageCaption](/API_docs/types/PageCaption.md), \];<a name="pageBlockEmbedPost"></a>  

***
<br><br>[$pageBlockFooter](/API_docs/constructors/pageBlockFooter.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="pageBlockFooter"></a>  

***
<br><br>[$pageBlockHeader](/API_docs/constructors/pageBlockHeader.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="pageBlockHeader"></a>  

***
<br><br>[$pageBlockKicker](/API_docs/constructors/pageBlockKicker.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="pageBlockKicker"></a>  

***
<br><br>[$pageBlockList](/API_docs/constructors/pageBlockList.md) = \['items' => \[[PageListItem](/API_docs/types/PageListItem.md)\], \];<a name="pageBlockList"></a>  

***
<br><br>[$pageBlockMap](/API_docs/constructors/pageBlockMap.md) = \['geo' => [GeoPoint](/API_docs/types/GeoPoint.md), 'zoom' => [int](/API_docs/types/int.md), 'w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), 'caption' => [PageCaption](/API_docs/types/PageCaption.md), \];<a name="pageBlockMap"></a>  

***
<br><br>[$pageBlockOrderedList](/API_docs/constructors/pageBlockOrderedList.md) = \['items' => \[[PageListOrderedItem](/API_docs/types/PageListOrderedItem.md)\], \];<a name="pageBlockOrderedList"></a>  

***
<br><br>[$pageBlockParagraph](/API_docs/constructors/pageBlockParagraph.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="pageBlockParagraph"></a>  

***
<br><br>[$pageBlockPhoto](/API_docs/constructors/pageBlockPhoto.md) = \['photo_id' => [long](/API_docs/types/long.md), 'caption' => [PageCaption](/API_docs/types/PageCaption.md), 'url' => [string](/API_docs/types/string.md), 'webpage_id' => [long](/API_docs/types/long.md), \];<a name="pageBlockPhoto"></a>  

***
<br><br>[$pageBlockPreformatted](/API_docs/constructors/pageBlockPreformatted.md) = \['text' => [RichText](/API_docs/types/RichText.md), 'language' => [string](/API_docs/types/string.md), \];<a name="pageBlockPreformatted"></a>  

***
<br><br>[$pageBlockPullquote](/API_docs/constructors/pageBlockPullquote.md) = \['text' => [RichText](/API_docs/types/RichText.md), 'caption' => [RichText](/API_docs/types/RichText.md), \];<a name="pageBlockPullquote"></a>  

***
<br><br>[$pageBlockRelatedArticles](/API_docs/constructors/pageBlockRelatedArticles.md) = \['title' => [RichText](/API_docs/types/RichText.md), 'articles' => \[[PageRelatedArticle](/API_docs/types/PageRelatedArticle.md)\], \];<a name="pageBlockRelatedArticles"></a>  

***
<br><br>[$pageBlockSlideshow](/API_docs/constructors/pageBlockSlideshow.md) = \['items' => \[[PageBlock](/API_docs/types/PageBlock.md)\], 'caption' => [PageCaption](/API_docs/types/PageCaption.md), \];<a name="pageBlockSlideshow"></a>  

***
<br><br>[$pageBlockSubheader](/API_docs/constructors/pageBlockSubheader.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="pageBlockSubheader"></a>  

***
<br><br>[$pageBlockSubtitle](/API_docs/constructors/pageBlockSubtitle.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="pageBlockSubtitle"></a>  

***
<br><br>[$pageBlockTable](/API_docs/constructors/pageBlockTable.md) = \['bordered' => [Bool](/API_docs/types/Bool.md), 'striped' => [Bool](/API_docs/types/Bool.md), 'title' => [RichText](/API_docs/types/RichText.md), 'rows' => \[[PageTableRow](/API_docs/types/PageTableRow.md)\], \];<a name="pageBlockTable"></a>  

***
<br><br>[$pageBlockTitle](/API_docs/constructors/pageBlockTitle.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="pageBlockTitle"></a>  

***
<br><br>[$pageBlockUnsupported](/API_docs/constructors/pageBlockUnsupported.md) = \[\];<a name="pageBlockUnsupported"></a>  

***
<br><br>[$pageBlockVideo](/API_docs/constructors/pageBlockVideo.md) = \['autoplay' => [Bool](/API_docs/types/Bool.md), 'loop' => [Bool](/API_docs/types/Bool.md), 'video_id' => [long](/API_docs/types/long.md), 'caption' => [PageCaption](/API_docs/types/PageCaption.md), \];<a name="pageBlockVideo"></a>  

***
<br><br>[$pageCaption](/API_docs/constructors/pageCaption.md) = \['text' => [RichText](/API_docs/types/RichText.md), 'credit' => [RichText](/API_docs/types/RichText.md), \];<a name="pageCaption"></a>  

***
<br><br>[$pageListItemBlocks](/API_docs/constructors/pageListItemBlocks.md) = \['blocks' => \[[PageBlock](/API_docs/types/PageBlock.md)\], \];<a name="pageListItemBlocks"></a>  

***
<br><br>[$pageListItemText](/API_docs/constructors/pageListItemText.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="pageListItemText"></a>  

***
<br><br>[$pageListOrderedItemBlocks](/API_docs/constructors/pageListOrderedItemBlocks.md) = \['num' => [string](/API_docs/types/string.md), 'blocks' => \[[PageBlock](/API_docs/types/PageBlock.md)\], \];<a name="pageListOrderedItemBlocks"></a>  

***
<br><br>[$pageListOrderedItemText](/API_docs/constructors/pageListOrderedItemText.md) = \['num' => [string](/API_docs/types/string.md), 'text' => [RichText](/API_docs/types/RichText.md), \];<a name="pageListOrderedItemText"></a>  

***
<br><br>[$pageRelatedArticle](/API_docs/constructors/pageRelatedArticle.md) = \['url' => [string](/API_docs/types/string.md), 'webpage_id' => [long](/API_docs/types/long.md), 'title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'photo_id' => [long](/API_docs/types/long.md), 'author' => [string](/API_docs/types/string.md), 'published_date' => [int](/API_docs/types/int.md), \];<a name="pageRelatedArticle"></a>  

***
<br><br>[$pageTableCell](/API_docs/constructors/pageTableCell.md) = \['header' => [Bool](/API_docs/types/Bool.md), 'align_center' => [Bool](/API_docs/types/Bool.md), 'align_right' => [Bool](/API_docs/types/Bool.md), 'valign_middle' => [Bool](/API_docs/types/Bool.md), 'valign_bottom' => [Bool](/API_docs/types/Bool.md), 'text' => [RichText](/API_docs/types/RichText.md), 'colspan' => [int](/API_docs/types/int.md), 'rowspan' => [int](/API_docs/types/int.md), \];<a name="pageTableCell"></a>  

***
<br><br>[$pageTableRow](/API_docs/constructors/pageTableRow.md) = \['cells' => \[[PageTableCell](/API_docs/types/PageTableCell.md)\], \];<a name="pageTableRow"></a>  

***
<br><br>[$passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow](/API_docs/constructors/passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow.md) = \['salt1' => [bytes](/API_docs/types/bytes.md), 'salt2' => [bytes](/API_docs/types/bytes.md), 'g' => [int](/API_docs/types/int.md), 'p' => [bytes](/API_docs/types/bytes.md), \];<a name="passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow"></a>  

***
<br><br>[$passwordKdfAlgoUnknown](/API_docs/constructors/passwordKdfAlgoUnknown.md) = \[\];<a name="passwordKdfAlgoUnknown"></a>  

***
<br><br>[$paymentCharge](/API_docs/constructors/paymentCharge.md) = \['id' => [string](/API_docs/types/string.md), 'provider_charge_id' => [string](/API_docs/types/string.md), \];<a name="paymentCharge"></a>  

***
<br><br>[$paymentRequestedInfo](/API_docs/constructors/paymentRequestedInfo.md) = \['name' => [string](/API_docs/types/string.md), 'phone' => [string](/API_docs/types/string.md), 'email' => [string](/API_docs/types/string.md), 'shipping_address' => [PostAddress](/API_docs/types/PostAddress.md), \];<a name="paymentRequestedInfo"></a>  

***
<br><br>[$paymentSavedCredentialsCard](/API_docs/constructors/paymentSavedCredentialsCard.md) = \['id' => [string](/API_docs/types/string.md), 'title' => [string](/API_docs/types/string.md), \];<a name="paymentSavedCredentialsCard"></a>  

***
<br><br>[$payments.bankCardData](/API_docs/constructors/payments.bankCardData.md) = \['title' => [string](/API_docs/types/string.md), 'open_urls' => \[[BankCardOpenUrl](/API_docs/types/BankCardOpenUrl.md)\], \];<a name="payments.bankCardData"></a>  

***
<br><br>[$payments.paymentForm](/API_docs/constructors/payments.paymentForm.md) = \['can_save_credentials' => [Bool](/API_docs/types/Bool.md), 'password_missing' => [Bool](/API_docs/types/Bool.md), 'form_id' => [long](/API_docs/types/long.md), 'bot_id' => [long](/API_docs/types/long.md), 'invoice' => [Invoice](/API_docs/types/Invoice.md), 'provider_id' => [long](/API_docs/types/long.md), 'url' => [string](/API_docs/types/string.md), 'native_provider' => [string](/API_docs/types/string.md), 'native_params' => [DataJSON](/API_docs/types/DataJSON.md), 'saved_info' => [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.md), 'saved_credentials' => [PaymentSavedCredentials](/API_docs/types/PaymentSavedCredentials.md), 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="payments.paymentForm"></a>  

***
<br><br>[$payments.paymentReceipt](/API_docs/constructors/payments.paymentReceipt.md) = \['date' => [int](/API_docs/types/int.md), 'bot_id' => [long](/API_docs/types/long.md), 'provider_id' => [long](/API_docs/types/long.md), 'title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'photo' => [WebDocument](/API_docs/types/WebDocument.md), 'invoice' => [Invoice](/API_docs/types/Invoice.md), 'info' => [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.md), 'shipping' => [ShippingOption](/API_docs/types/ShippingOption.md), 'tip_amount' => [long](/API_docs/types/long.md), 'currency' => [string](/API_docs/types/string.md), 'total_amount' => [long](/API_docs/types/long.md), 'credentials_title' => [string](/API_docs/types/string.md), 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="payments.paymentReceipt"></a>  

***
<br><br>[$payments.paymentResult](/API_docs/constructors/payments.paymentResult.md) = \['updates' => [Updates](/API_docs/types/Updates.md), \];<a name="payments.paymentResult"></a>  

***
<br><br>[$payments.paymentVerificationNeeded](/API_docs/constructors/payments.paymentVerificationNeeded.md) = \['url' => [string](/API_docs/types/string.md), \];<a name="payments.paymentVerificationNeeded"></a>  

***
<br><br>[$payments.savedInfo](/API_docs/constructors/payments.savedInfo.md) = \['has_saved_credentials' => [Bool](/API_docs/types/Bool.md), 'saved_info' => [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.md), \];<a name="payments.savedInfo"></a>  

***
<br><br>[$payments.validatedRequestedInfo](/API_docs/constructors/payments.validatedRequestedInfo.md) = \['id' => [string](/API_docs/types/string.md), 'shipping_options' => \[[ShippingOption](/API_docs/types/ShippingOption.md)\], \];<a name="payments.validatedRequestedInfo"></a>  

***
<br><br>[$peerBlocked](/API_docs/constructors/peerBlocked.md) = \['peer_id' => [Peer](/API_docs/types/Peer.md), 'date' => [int](/API_docs/types/int.md), \];<a name="peerBlocked"></a>  

***
<br><br>[$peerChannel](/API_docs/constructors/peerChannel.md) = \['channel_id' => [long](/API_docs/types/long.md), \];<a name="peerChannel"></a>  

***
<br><br>[$peerChat](/API_docs/constructors/peerChat.md) = \['chat_id' => [long](/API_docs/types/long.md), \];<a name="peerChat"></a>  

***
<br><br>[$peerLocated](/API_docs/constructors/peerLocated.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'expires' => [int](/API_docs/types/int.md), 'distance' => [int](/API_docs/types/int.md), \];<a name="peerLocated"></a>  

***
<br><br>[$peerNotifySettings](/API_docs/constructors/peerNotifySettings.md) = \['show_previews' => [Bool](/API_docs/types/Bool.md), 'silent' => [Bool](/API_docs/types/Bool.md), 'mute_until' => [int](/API_docs/types/int.md), 'sound' => [string](/API_docs/types/string.md), \];<a name="peerNotifySettings"></a>  

***
<br><br>[$peerSelfLocated](/API_docs/constructors/peerSelfLocated.md) = \['expires' => [int](/API_docs/types/int.md), \];<a name="peerSelfLocated"></a>  

***
<br><br>[$peerSettings](/API_docs/constructors/peerSettings.md) = \['report_spam' => [Bool](/API_docs/types/Bool.md), 'add_contact' => [Bool](/API_docs/types/Bool.md), 'block_contact' => [Bool](/API_docs/types/Bool.md), 'share_contact' => [Bool](/API_docs/types/Bool.md), 'need_contacts_exception' => [Bool](/API_docs/types/Bool.md), 'report_geo' => [Bool](/API_docs/types/Bool.md), 'autoarchived' => [Bool](/API_docs/types/Bool.md), 'invite_members' => [Bool](/API_docs/types/Bool.md), 'request_chat_broadcast' => [Bool](/API_docs/types/Bool.md), 'geo_distance' => [int](/API_docs/types/int.md), 'request_chat_title' => [string](/API_docs/types/string.md), 'request_chat_date' => [int](/API_docs/types/int.md), \];<a name="peerSettings"></a>  

***
<br><br>[$peerUser](/API_docs/constructors/peerUser.md) = \['user_id' => [long](/API_docs/types/long.md), \];<a name="peerUser"></a>  

***
<br><br>[$phone.exportedGroupCallInvite](/API_docs/constructors/phone.exportedGroupCallInvite.md) = \['link' => [string](/API_docs/types/string.md), \];<a name="phone.exportedGroupCallInvite"></a>  

***
<br><br>[$phone.groupCall](/API_docs/constructors/phone.groupCall.md) = \['call' => [GroupCall](/API_docs/types/GroupCall.md), 'participants' => \[[GroupCallParticipant](/API_docs/types/GroupCallParticipant.md)\], 'participants_next_offset' => [string](/API_docs/types/string.md), 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="phone.groupCall"></a>  

***
<br><br>[$phone.groupParticipants](/API_docs/constructors/phone.groupParticipants.md) = \['count' => [int](/API_docs/types/int.md), 'participants' => \[[GroupCallParticipant](/API_docs/types/GroupCallParticipant.md)\], 'next_offset' => [string](/API_docs/types/string.md), 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], 'version' => [int](/API_docs/types/int.md), \];<a name="phone.groupParticipants"></a>  

***
<br><br>[$phone.joinAsPeers](/API_docs/constructors/phone.joinAsPeers.md) = \['peers' => \[[Peer](/API_docs/types/Peer.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="phone.joinAsPeers"></a>  

***
<br><br>[$phone.phoneCall](/API_docs/constructors/phone.phoneCall.md) = \['phone_call' => [PhoneCall](/API_docs/types/PhoneCall.md), 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="phone.phoneCall"></a>  

***
<br><br>[$phoneCall](/API_docs/constructors/phoneCall.md) = \['p2p_allowed' => [Bool](/API_docs/types/Bool.md), 'video' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'admin_id' => [long](/API_docs/types/long.md), 'participant_id' => [long](/API_docs/types/long.md), 'g_a_or_b' => [bytes](/API_docs/types/bytes.md), 'key_fingerprint' => [long](/API_docs/types/long.md), 'protocol' => [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.md), 'connections' => \[[PhoneConnection](/API_docs/types/PhoneConnection.md)\], 'start_date' => [int](/API_docs/types/int.md), \];<a name="phoneCall"></a>  

***
<br><br>[$phoneCallAccepted](/API_docs/constructors/phoneCallAccepted.md) = \['video' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'admin_id' => [long](/API_docs/types/long.md), 'participant_id' => [long](/API_docs/types/long.md), 'g_b' => [bytes](/API_docs/types/bytes.md), 'protocol' => [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.md), \];<a name="phoneCallAccepted"></a>  

***
<br><br>[$phoneCallDiscardReasonBusy](/API_docs/constructors/phoneCallDiscardReasonBusy.md) = \[\];<a name="phoneCallDiscardReasonBusy"></a>  

***
<br><br>[$phoneCallDiscardReasonDisconnect](/API_docs/constructors/phoneCallDiscardReasonDisconnect.md) = \[\];<a name="phoneCallDiscardReasonDisconnect"></a>  

***
<br><br>[$phoneCallDiscardReasonHangup](/API_docs/constructors/phoneCallDiscardReasonHangup.md) = \[\];<a name="phoneCallDiscardReasonHangup"></a>  

***
<br><br>[$phoneCallDiscardReasonMissed](/API_docs/constructors/phoneCallDiscardReasonMissed.md) = \[\];<a name="phoneCallDiscardReasonMissed"></a>  

***
<br><br>[$phoneCallDiscarded](/API_docs/constructors/phoneCallDiscarded.md) = \['need_rating' => [Bool](/API_docs/types/Bool.md), 'need_debug' => [Bool](/API_docs/types/Bool.md), 'video' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'reason' => [PhoneCallDiscardReason](/API_docs/types/PhoneCallDiscardReason.md), 'duration' => [int](/API_docs/types/int.md), \];<a name="phoneCallDiscarded"></a>  

***
<br><br>[$phoneCallEmpty](/API_docs/constructors/phoneCallEmpty.md) = \['id' => [long](/API_docs/types/long.md), \];<a name="phoneCallEmpty"></a>  

***
<br><br>[$phoneCallProtocol](/API_docs/constructors/phoneCallProtocol.md) = \['udp_p2p' => [Bool](/API_docs/types/Bool.md), 'udp_reflector' => [Bool](/API_docs/types/Bool.md), 'min_layer' => [int](/API_docs/types/int.md), 'max_layer' => [int](/API_docs/types/int.md), 'library_versions' => \[[string](/API_docs/types/string.md)\], \];<a name="phoneCallProtocol"></a>  

***
<br><br>[$phoneCallRequested](/API_docs/constructors/phoneCallRequested.md) = \['video' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'admin_id' => [long](/API_docs/types/long.md), 'participant_id' => [long](/API_docs/types/long.md), 'g_a_hash' => [bytes](/API_docs/types/bytes.md), 'protocol' => [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.md), \];<a name="phoneCallRequested"></a>  

***
<br><br>[$phoneCallWaiting](/API_docs/constructors/phoneCallWaiting.md) = \['video' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'admin_id' => [long](/API_docs/types/long.md), 'participant_id' => [long](/API_docs/types/long.md), 'protocol' => [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.md), 'receive_date' => [int](/API_docs/types/int.md), \];<a name="phoneCallWaiting"></a>  

***
<br><br>[$phoneConnection](/API_docs/constructors/phoneConnection.md) = \['id' => [long](/API_docs/types/long.md), 'ip' => [string](/API_docs/types/string.md), 'ipv6' => [string](/API_docs/types/string.md), 'port' => [int](/API_docs/types/int.md), 'peer_tag' => [bytes](/API_docs/types/bytes.md), \];<a name="phoneConnection"></a>  

***
<br><br>[$phoneConnectionWebrtc](/API_docs/constructors/phoneConnectionWebrtc.md) = \['turn' => [Bool](/API_docs/types/Bool.md), 'stun' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'ip' => [string](/API_docs/types/string.md), 'ipv6' => [string](/API_docs/types/string.md), 'port' => [int](/API_docs/types/int.md), 'username' => [string](/API_docs/types/string.md), 'password' => [string](/API_docs/types/string.md), \];<a name="phoneConnectionWebrtc"></a>  

***
<br><br>[$photo](/API_docs/constructors/photo.md) = \['has_stickers' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'file_reference' => [bytes](/API_docs/types/bytes.md), 'date' => [int](/API_docs/types/int.md), 'sizes' => \[[PhotoSize](/API_docs/types/PhotoSize.md)\], 'video_sizes' => \[[VideoSize](/API_docs/types/VideoSize.md)\], 'dc_id' => [int](/API_docs/types/int.md), \];<a name="photo"></a>  

***
<br><br>[$photoCachedSize\_23](/API_docs/constructors/photoCachedSize_23.md) = \['type' => [string](/API_docs/types/string.md), 'location' => [FileLocation](/API_docs/types/FileLocation.md), 'w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), 'bytes' => [bytes](/API_docs/types/bytes.md), \];<a name="photoCachedSize_23"></a>  

***
<br><br>[$photoEmpty](/API_docs/constructors/photoEmpty.md) = \['id' => [long](/API_docs/types/long.md), \];<a name="photoEmpty"></a>  

***
<br><br>[$photoPathSize](/API_docs/constructors/photoPathSize.md) = \['type' => [string](/API_docs/types/string.md), 'bytes' => [bytes](/API_docs/types/bytes.md), \];<a name="photoPathSize"></a>  

***
<br><br>[$photoSize\_23](/API_docs/constructors/photoSize_23.md) = \['type' => [string](/API_docs/types/string.md), 'location' => [FileLocation](/API_docs/types/FileLocation.md), 'w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), 'size' => [int](/API_docs/types/int.md), \];<a name="photoSize_23"></a>  

***
<br><br>[$photoSizeEmpty](/API_docs/constructors/photoSizeEmpty.md) = \['type' => [string](/API_docs/types/string.md), \];<a name="photoSizeEmpty"></a>  

***
<br><br>[$photoSizeProgressive](/API_docs/constructors/photoSizeProgressive.md) = \['type' => [string](/API_docs/types/string.md), 'w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), 'sizes' => \[[int](/API_docs/types/int.md)\], \];<a name="photoSizeProgressive"></a>  

***
<br><br>[$photoStrippedSize](/API_docs/constructors/photoStrippedSize.md) = \['type' => [string](/API_docs/types/string.md), 'bytes' => [bytes](/API_docs/types/bytes.md), \];<a name="photoStrippedSize"></a>  

***
<br><br>[$photos.photo](/API_docs/constructors/photos.photo.md) = \['photo' => [Photo](/API_docs/types/Photo.md), 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="photos.photo"></a>  

***
<br><br>[$photos.photos](/API_docs/constructors/photos.photos.md) = \['photos' => \[[Photo](/API_docs/types/Photo.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="photos.photos"></a>  

***
<br><br>[$photos.photosSlice](/API_docs/constructors/photos.photosSlice.md) = \['count' => [int](/API_docs/types/int.md), 'photos' => \[[Photo](/API_docs/types/Photo.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="photos.photosSlice"></a>  

***
<br><br>[$poll](/API_docs/constructors/poll.md) = \['id' => [long](/API_docs/types/long.md), 'closed' => [Bool](/API_docs/types/Bool.md), 'public_voters' => [Bool](/API_docs/types/Bool.md), 'multiple_choice' => [Bool](/API_docs/types/Bool.md), 'quiz' => [Bool](/API_docs/types/Bool.md), 'question' => [string](/API_docs/types/string.md), 'answers' => \[[PollAnswer](/API_docs/types/PollAnswer.md)\], 'close_period' => [int](/API_docs/types/int.md), 'close_date' => [int](/API_docs/types/int.md), \];<a name="poll"></a>  

***
<br><br>[$pollAnswer](/API_docs/constructors/pollAnswer.md) = \['text' => [string](/API_docs/types/string.md), 'option' => [bytes](/API_docs/types/bytes.md), \];<a name="pollAnswer"></a>  

***
<br><br>[$pollAnswerVoters](/API_docs/constructors/pollAnswerVoters.md) = \['chosen' => [Bool](/API_docs/types/Bool.md), 'correct' => [Bool](/API_docs/types/Bool.md), 'option' => [bytes](/API_docs/types/bytes.md), 'voters' => [int](/API_docs/types/int.md), \];<a name="pollAnswerVoters"></a>  

***
<br><br>[$pollResults](/API_docs/constructors/pollResults.md) = \['min' => [Bool](/API_docs/types/Bool.md), 'results' => \[[PollAnswerVoters](/API_docs/types/PollAnswerVoters.md)\], 'total_voters' => [int](/API_docs/types/int.md), 'recent_voters' => \[[long](/API_docs/types/long.md)\], 'solution' => [string](/API_docs/types/string.md), 'solution_entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], \];<a name="pollResults"></a>  

***
<br><br>[$popularContact](/API_docs/constructors/popularContact.md) = \['client_id' => [long](/API_docs/types/long.md), 'importers' => [int](/API_docs/types/int.md), \];<a name="popularContact"></a>  

***
<br><br>[$postAddress](/API_docs/constructors/postAddress.md) = \['street_line1' => [string](/API_docs/types/string.md), 'street_line2' => [string](/API_docs/types/string.md), 'city' => [string](/API_docs/types/string.md), 'state' => [string](/API_docs/types/string.md), 'country_iso2' => [string](/API_docs/types/string.md), 'post_code' => [string](/API_docs/types/string.md), \];<a name="postAddress"></a>  

***
<br><br>[$privacyKeyAddedByPhone](/API_docs/constructors/privacyKeyAddedByPhone.md) = \[\];<a name="privacyKeyAddedByPhone"></a>  

***
<br><br>[$privacyKeyChatInvite](/API_docs/constructors/privacyKeyChatInvite.md) = \[\];<a name="privacyKeyChatInvite"></a>  

***
<br><br>[$privacyKeyForwards](/API_docs/constructors/privacyKeyForwards.md) = \[\];<a name="privacyKeyForwards"></a>  

***
<br><br>[$privacyKeyPhoneCall](/API_docs/constructors/privacyKeyPhoneCall.md) = \[\];<a name="privacyKeyPhoneCall"></a>  

***
<br><br>[$privacyKeyPhoneNumber](/API_docs/constructors/privacyKeyPhoneNumber.md) = \[\];<a name="privacyKeyPhoneNumber"></a>  

***
<br><br>[$privacyKeyPhoneP2P](/API_docs/constructors/privacyKeyPhoneP2P.md) = \[\];<a name="privacyKeyPhoneP2P"></a>  

***
<br><br>[$privacyKeyProfilePhoto](/API_docs/constructors/privacyKeyProfilePhoto.md) = \[\];<a name="privacyKeyProfilePhoto"></a>  

***
<br><br>[$privacyKeyStatusTimestamp](/API_docs/constructors/privacyKeyStatusTimestamp.md) = \[\];<a name="privacyKeyStatusTimestamp"></a>  

***
<br><br>[$privacyValueAllowAll](/API_docs/constructors/privacyValueAllowAll.md) = \[\];<a name="privacyValueAllowAll"></a>  

***
<br><br>[$privacyValueAllowChatParticipants](/API_docs/constructors/privacyValueAllowChatParticipants.md) = \['chats' => \[[long](/API_docs/types/long.md)\], \];<a name="privacyValueAllowChatParticipants"></a>  

***
<br><br>[$privacyValueAllowContacts](/API_docs/constructors/privacyValueAllowContacts.md) = \[\];<a name="privacyValueAllowContacts"></a>  

***
<br><br>[$privacyValueAllowUsers](/API_docs/constructors/privacyValueAllowUsers.md) = \['users' => \[[long](/API_docs/types/long.md)\], \];<a name="privacyValueAllowUsers"></a>  

***
<br><br>[$privacyValueDisallowAll](/API_docs/constructors/privacyValueDisallowAll.md) = \[\];<a name="privacyValueDisallowAll"></a>  

***
<br><br>[$privacyValueDisallowChatParticipants](/API_docs/constructors/privacyValueDisallowChatParticipants.md) = \['chats' => \[[long](/API_docs/types/long.md)\], \];<a name="privacyValueDisallowChatParticipants"></a>  

***
<br><br>[$privacyValueDisallowContacts](/API_docs/constructors/privacyValueDisallowContacts.md) = \[\];<a name="privacyValueDisallowContacts"></a>  

***
<br><br>[$privacyValueDisallowUsers](/API_docs/constructors/privacyValueDisallowUsers.md) = \['users' => \[[long](/API_docs/types/long.md)\], \];<a name="privacyValueDisallowUsers"></a>  

***
<br><br>[$reactionCount](/API_docs/constructors/reactionCount.md) = \['chosen' => [Bool](/API_docs/types/Bool.md), 'reaction' => [string](/API_docs/types/string.md), 'count' => [int](/API_docs/types/int.md), \];<a name="reactionCount"></a>  

***
<br><br>[$receivedNotifyMessage](/API_docs/constructors/receivedNotifyMessage.md) = \['id' => [int](/API_docs/types/int.md), \];<a name="receivedNotifyMessage"></a>  

***
<br><br>[$recentMeUrlChat](/API_docs/constructors/recentMeUrlChat.md) = \['url' => [string](/API_docs/types/string.md), 'chat_id' => [long](/API_docs/types/long.md), \];<a name="recentMeUrlChat"></a>  

***
<br><br>[$recentMeUrlChatInvite](/API_docs/constructors/recentMeUrlChatInvite.md) = \['url' => [string](/API_docs/types/string.md), 'chat_invite' => [ChatInvite](/API_docs/types/ChatInvite.md), \];<a name="recentMeUrlChatInvite"></a>  

***
<br><br>[$recentMeUrlStickerSet](/API_docs/constructors/recentMeUrlStickerSet.md) = \['url' => [string](/API_docs/types/string.md), 'set' => [StickerSetCovered](/API_docs/types/StickerSetCovered.md), \];<a name="recentMeUrlStickerSet"></a>  

***
<br><br>[$recentMeUrlUnknown](/API_docs/constructors/recentMeUrlUnknown.md) = \['url' => [string](/API_docs/types/string.md), \];<a name="recentMeUrlUnknown"></a>  

***
<br><br>[$recentMeUrlUser](/API_docs/constructors/recentMeUrlUser.md) = \['url' => [string](/API_docs/types/string.md), 'user_id' => [long](/API_docs/types/long.md), \];<a name="recentMeUrlUser"></a>  

***
<br><br>[$replyInlineMarkup](/API_docs/constructors/replyInlineMarkup.md) = \['rows' => \[[KeyboardButtonRow](/API_docs/types/KeyboardButtonRow.md)\], \];<a name="replyInlineMarkup"></a>  

***
<br><br>[$replyKeyboardForceReply](/API_docs/constructors/replyKeyboardForceReply.md) = \['single_use' => [Bool](/API_docs/types/Bool.md), 'selective' => [Bool](/API_docs/types/Bool.md), 'placeholder' => [string](/API_docs/types/string.md), \];<a name="replyKeyboardForceReply"></a>  

***
<br><br>[$replyKeyboardHide](/API_docs/constructors/replyKeyboardHide.md) = \['selective' => [Bool](/API_docs/types/Bool.md), \];<a name="replyKeyboardHide"></a>  

***
<br><br>[$replyKeyboardMarkup](/API_docs/constructors/replyKeyboardMarkup.md) = \['resize' => [Bool](/API_docs/types/Bool.md), 'single_use' => [Bool](/API_docs/types/Bool.md), 'selective' => [Bool](/API_docs/types/Bool.md), 'rows' => \[[KeyboardButtonRow](/API_docs/types/KeyboardButtonRow.md)\], 'placeholder' => [string](/API_docs/types/string.md), \];<a name="replyKeyboardMarkup"></a>  

***
<br><br>[$restrictionReason](/API_docs/constructors/restrictionReason.md) = \['platform' => [string](/API_docs/types/string.md), 'reason' => [string](/API_docs/types/string.md), 'text' => [string](/API_docs/types/string.md), \];<a name="restrictionReason"></a>  

***
<br><br>[$savedPhoneContact](/API_docs/constructors/savedPhoneContact.md) = \['phone' => [string](/API_docs/types/string.md), 'first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), 'date' => [int](/API_docs/types/int.md), \];<a name="savedPhoneContact"></a>  

***
<br><br>[$searchResultPosition](/API_docs/constructors/searchResultPosition.md) = \['msg_id' => [int](/API_docs/types/int.md), 'date' => [int](/API_docs/types/int.md), 'offset' => [int](/API_docs/types/int.md), \];<a name="searchResultPosition"></a>  

***
<br><br>[$searchResultsCalendarPeriod](/API_docs/constructors/searchResultsCalendarPeriod.md) = \['date' => [int](/API_docs/types/int.md), 'min_msg_id' => [int](/API_docs/types/int.md), 'max_msg_id' => [int](/API_docs/types/int.md), 'count' => [int](/API_docs/types/int.md), \];<a name="searchResultsCalendarPeriod"></a>  

***
<br><br>[$secureCredentialsEncrypted](/API_docs/constructors/secureCredentialsEncrypted.md) = \['data' => [bytes](/API_docs/types/bytes.md), 'hash' => [bytes](/API_docs/types/bytes.md), 'secret' => [bytes](/API_docs/types/bytes.md), \];<a name="secureCredentialsEncrypted"></a>  

***
<br><br>[$secureData](/API_docs/constructors/secureData.md) = \['data' => [bytes](/API_docs/types/bytes.md), 'data_hash' => [bytes](/API_docs/types/bytes.md), 'secret' => [bytes](/API_docs/types/bytes.md), \];<a name="secureData"></a>  

***
<br><br>[$secureFile](/API_docs/constructors/secureFile.md) = \['id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'size' => [int](/API_docs/types/int.md), 'dc_id' => [int](/API_docs/types/int.md), 'date' => [int](/API_docs/types/int.md), 'file_hash' => [bytes](/API_docs/types/bytes.md), 'secret' => [bytes](/API_docs/types/bytes.md), \];<a name="secureFile"></a>  

***
<br><br>[$secureFileEmpty](/API_docs/constructors/secureFileEmpty.md) = \[\];<a name="secureFileEmpty"></a>  

***
<br><br>[$securePasswordKdfAlgoPBKDF2HMACSHA512iter100000](/API_docs/constructors/securePasswordKdfAlgoPBKDF2HMACSHA512iter100000.md) = \['salt' => [bytes](/API_docs/types/bytes.md), \];<a name="securePasswordKdfAlgoPBKDF2HMACSHA512iter100000"></a>  

***
<br><br>[$securePasswordKdfAlgoSHA512](/API_docs/constructors/securePasswordKdfAlgoSHA512.md) = \['salt' => [bytes](/API_docs/types/bytes.md), \];<a name="securePasswordKdfAlgoSHA512"></a>  

***
<br><br>[$securePasswordKdfAlgoUnknown](/API_docs/constructors/securePasswordKdfAlgoUnknown.md) = \[\];<a name="securePasswordKdfAlgoUnknown"></a>  

***
<br><br>[$securePlainEmail](/API_docs/constructors/securePlainEmail.md) = \['email' => [string](/API_docs/types/string.md), \];<a name="securePlainEmail"></a>  

***
<br><br>[$securePlainPhone](/API_docs/constructors/securePlainPhone.md) = \['phone' => [string](/API_docs/types/string.md), \];<a name="securePlainPhone"></a>  

***
<br><br>[$secureRequiredType](/API_docs/constructors/secureRequiredType.md) = \['native_names' => [Bool](/API_docs/types/Bool.md), 'selfie_required' => [Bool](/API_docs/types/Bool.md), 'translation_required' => [Bool](/API_docs/types/Bool.md), 'type' => [SecureValueType](/API_docs/types/SecureValueType.md), \];<a name="secureRequiredType"></a>  

***
<br><br>[$secureRequiredTypeOneOf](/API_docs/constructors/secureRequiredTypeOneOf.md) = \['types' => \[[SecureRequiredType](/API_docs/types/SecureRequiredType.md)\], \];<a name="secureRequiredTypeOneOf"></a>  

***
<br><br>[$secureSecretSettings](/API_docs/constructors/secureSecretSettings.md) = \['secure_algo' => [SecurePasswordKdfAlgo](/API_docs/types/SecurePasswordKdfAlgo.md), 'secure_secret' => [bytes](/API_docs/types/bytes.md), 'secure_secret_id' => [long](/API_docs/types/long.md), \];<a name="secureSecretSettings"></a>  

***
<br><br>[$secureValue](/API_docs/constructors/secureValue.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'data' => [SecureData](/API_docs/types/SecureData.md), 'front_side' => [SecureFile](/API_docs/types/SecureFile.md), 'reverse_side' => [SecureFile](/API_docs/types/SecureFile.md), 'selfie' => [SecureFile](/API_docs/types/SecureFile.md), 'translation' => \[[SecureFile](/API_docs/types/SecureFile.md)\], 'files' => \[[SecureFile](/API_docs/types/SecureFile.md)\], 'plain_data' => [SecurePlainData](/API_docs/types/SecurePlainData.md), 'hash' => [bytes](/API_docs/types/bytes.md), \];<a name="secureValue"></a>  

***
<br><br>[$secureValueError](/API_docs/constructors/secureValueError.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'hash' => [bytes](/API_docs/types/bytes.md), 'text' => [string](/API_docs/types/string.md), \];<a name="secureValueError"></a>  

***
<br><br>[$secureValueErrorData](/API_docs/constructors/secureValueErrorData.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'data_hash' => [bytes](/API_docs/types/bytes.md), 'field' => [string](/API_docs/types/string.md), 'text' => [string](/API_docs/types/string.md), \];<a name="secureValueErrorData"></a>  

***
<br><br>[$secureValueErrorFile](/API_docs/constructors/secureValueErrorFile.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'file_hash' => [bytes](/API_docs/types/bytes.md), 'text' => [string](/API_docs/types/string.md), \];<a name="secureValueErrorFile"></a>  

***
<br><br>[$secureValueErrorFiles](/API_docs/constructors/secureValueErrorFiles.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'file_hash' => \[[bytes](/API_docs/types/bytes.md)\], 'text' => [string](/API_docs/types/string.md), \];<a name="secureValueErrorFiles"></a>  

***
<br><br>[$secureValueErrorFrontSide](/API_docs/constructors/secureValueErrorFrontSide.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'file_hash' => [bytes](/API_docs/types/bytes.md), 'text' => [string](/API_docs/types/string.md), \];<a name="secureValueErrorFrontSide"></a>  

***
<br><br>[$secureValueErrorReverseSide](/API_docs/constructors/secureValueErrorReverseSide.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'file_hash' => [bytes](/API_docs/types/bytes.md), 'text' => [string](/API_docs/types/string.md), \];<a name="secureValueErrorReverseSide"></a>  

***
<br><br>[$secureValueErrorSelfie](/API_docs/constructors/secureValueErrorSelfie.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'file_hash' => [bytes](/API_docs/types/bytes.md), 'text' => [string](/API_docs/types/string.md), \];<a name="secureValueErrorSelfie"></a>  

***
<br><br>[$secureValueErrorTranslationFile](/API_docs/constructors/secureValueErrorTranslationFile.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'file_hash' => [bytes](/API_docs/types/bytes.md), 'text' => [string](/API_docs/types/string.md), \];<a name="secureValueErrorTranslationFile"></a>  

***
<br><br>[$secureValueErrorTranslationFiles](/API_docs/constructors/secureValueErrorTranslationFiles.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'file_hash' => \[[bytes](/API_docs/types/bytes.md)\], 'text' => [string](/API_docs/types/string.md), \];<a name="secureValueErrorTranslationFiles"></a>  

***
<br><br>[$secureValueHash](/API_docs/constructors/secureValueHash.md) = \['type' => [SecureValueType](/API_docs/types/SecureValueType.md), 'hash' => [bytes](/API_docs/types/bytes.md), \];<a name="secureValueHash"></a>  

***
<br><br>[$secureValueTypeAddress](/API_docs/constructors/secureValueTypeAddress.md) = \[\];<a name="secureValueTypeAddress"></a>  

***
<br><br>[$secureValueTypeBankStatement](/API_docs/constructors/secureValueTypeBankStatement.md) = \[\];<a name="secureValueTypeBankStatement"></a>  

***
<br><br>[$secureValueTypeDriverLicense](/API_docs/constructors/secureValueTypeDriverLicense.md) = \[\];<a name="secureValueTypeDriverLicense"></a>  

***
<br><br>[$secureValueTypeEmail](/API_docs/constructors/secureValueTypeEmail.md) = \[\];<a name="secureValueTypeEmail"></a>  

***
<br><br>[$secureValueTypeIdentityCard](/API_docs/constructors/secureValueTypeIdentityCard.md) = \[\];<a name="secureValueTypeIdentityCard"></a>  

***
<br><br>[$secureValueTypeInternalPassport](/API_docs/constructors/secureValueTypeInternalPassport.md) = \[\];<a name="secureValueTypeInternalPassport"></a>  

***
<br><br>[$secureValueTypePassport](/API_docs/constructors/secureValueTypePassport.md) = \[\];<a name="secureValueTypePassport"></a>  

***
<br><br>[$secureValueTypePassportRegistration](/API_docs/constructors/secureValueTypePassportRegistration.md) = \[\];<a name="secureValueTypePassportRegistration"></a>  

***
<br><br>[$secureValueTypePersonalDetails](/API_docs/constructors/secureValueTypePersonalDetails.md) = \[\];<a name="secureValueTypePersonalDetails"></a>  

***
<br><br>[$secureValueTypePhone](/API_docs/constructors/secureValueTypePhone.md) = \[\];<a name="secureValueTypePhone"></a>  

***
<br><br>[$secureValueTypeRentalAgreement](/API_docs/constructors/secureValueTypeRentalAgreement.md) = \[\];<a name="secureValueTypeRentalAgreement"></a>  

***
<br><br>[$secureValueTypeTemporaryRegistration](/API_docs/constructors/secureValueTypeTemporaryRegistration.md) = \[\];<a name="secureValueTypeTemporaryRegistration"></a>  

***
<br><br>[$secureValueTypeUtilityBill](/API_docs/constructors/secureValueTypeUtilityBill.md) = \[\];<a name="secureValueTypeUtilityBill"></a>  

***
<br><br>[$sendMessageCancelAction](/API_docs/constructors/sendMessageCancelAction.md) = \[\];<a name="sendMessageCancelAction"></a>  

***
<br><br>[$sendMessageChooseContactAction](/API_docs/constructors/sendMessageChooseContactAction.md) = \[\];<a name="sendMessageChooseContactAction"></a>  

***
<br><br>[$sendMessageChooseStickerAction](/API_docs/constructors/sendMessageChooseStickerAction.md) = \[\];<a name="sendMessageChooseStickerAction"></a>  

***
<br><br>[$sendMessageEmojiInteraction](/API_docs/constructors/sendMessageEmojiInteraction.md) = \['emoticon' => [string](/API_docs/types/string.md), 'msg_id' => [int](/API_docs/types/int.md), 'interaction' => [DataJSON](/API_docs/types/DataJSON.md), \];<a name="sendMessageEmojiInteraction"></a>  

***
<br><br>[$sendMessageEmojiInteractionSeen](/API_docs/constructors/sendMessageEmojiInteractionSeen.md) = \['emoticon' => [string](/API_docs/types/string.md), \];<a name="sendMessageEmojiInteractionSeen"></a>  

***
<br><br>[$sendMessageGamePlayAction](/API_docs/constructors/sendMessageGamePlayAction.md) = \[\];<a name="sendMessageGamePlayAction"></a>  

***
<br><br>[$sendMessageGeoLocationAction](/API_docs/constructors/sendMessageGeoLocationAction.md) = \[\];<a name="sendMessageGeoLocationAction"></a>  

***
<br><br>[$sendMessageHistoryImportAction](/API_docs/constructors/sendMessageHistoryImportAction.md) = \['progress' => [int](/API_docs/types/int.md), \];<a name="sendMessageHistoryImportAction"></a>  

***
<br><br>[$sendMessageRecordAudioAction](/API_docs/constructors/sendMessageRecordAudioAction.md) = \[\];<a name="sendMessageRecordAudioAction"></a>  

***
<br><br>[$sendMessageRecordRoundAction](/API_docs/constructors/sendMessageRecordRoundAction.md) = \[\];<a name="sendMessageRecordRoundAction"></a>  

***
<br><br>[$sendMessageRecordVideoAction](/API_docs/constructors/sendMessageRecordVideoAction.md) = \[\];<a name="sendMessageRecordVideoAction"></a>  

***
<br><br>[$sendMessageTypingAction](/API_docs/constructors/sendMessageTypingAction.md) = \[\];<a name="sendMessageTypingAction"></a>  

***
<br><br>[$sendMessageUploadAudioAction\_17](/API_docs/constructors/sendMessageUploadAudioAction_17.md) = \[\];<a name="sendMessageUploadAudioAction_17"></a>  

***
<br><br>[$sendMessageUploadDocumentAction\_17](/API_docs/constructors/sendMessageUploadDocumentAction_17.md) = \[\];<a name="sendMessageUploadDocumentAction_17"></a>  

***
<br><br>[$sendMessageUploadPhotoAction\_17](/API_docs/constructors/sendMessageUploadPhotoAction_17.md) = \[\];<a name="sendMessageUploadPhotoAction_17"></a>  

***
<br><br>[$sendMessageUploadRoundAction](/API_docs/constructors/sendMessageUploadRoundAction.md) = \['progress' => [int](/API_docs/types/int.md), \];<a name="sendMessageUploadRoundAction"></a>  

***
<br><br>[$sendMessageUploadVideoAction\_17](/API_docs/constructors/sendMessageUploadVideoAction_17.md) = \[\];<a name="sendMessageUploadVideoAction_17"></a>  

***
<br><br>[$shippingOption](/API_docs/constructors/shippingOption.md) = \['id' => [string](/API_docs/types/string.md), 'title' => [string](/API_docs/types/string.md), 'prices' => \[[LabeledPrice](/API_docs/types/LabeledPrice.md)\], \];<a name="shippingOption"></a>  

***
<br><br>[$speakingInGroupCallAction](/API_docs/constructors/speakingInGroupCallAction.md) = \[\];<a name="speakingInGroupCallAction"></a>  

***
<br><br>[$sponsoredMessage](/API_docs/constructors/sponsoredMessage.md) = \['from_id' => [Peer](/API_docs/types/Peer.md), 'chat_invite' => [ChatInvite](/API_docs/types/ChatInvite.md), 'chat_invite_hash' => [string](/API_docs/types/string.md), 'channel_post' => [int](/API_docs/types/int.md), 'start_param' => [string](/API_docs/types/string.md), 'message' => [string](/API_docs/types/string.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], \];<a name="sponsoredMessage"></a>  

***
<br><br>[$stats.broadcastStats](/API_docs/constructors/stats.broadcastStats.md) = \['period' => [StatsDateRangeDays](/API_docs/types/StatsDateRangeDays.md), 'followers' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.md), 'views_per_post' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.md), 'shares_per_post' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.md), 'enabled_notifications' => [StatsPercentValue](/API_docs/types/StatsPercentValue.md), 'growth_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'followers_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'mute_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'top_hours_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'interactions_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'iv_interactions_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'views_by_source_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'new_followers_by_source_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'languages_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'recent_message_interactions' => \[[MessageInteractionCounters](/API_docs/types/MessageInteractionCounters.md)\], \];<a name="stats.broadcastStats"></a>  

***
<br><br>[$stats.megagroupStats](/API_docs/constructors/stats.megagroupStats.md) = \['period' => [StatsDateRangeDays](/API_docs/types/StatsDateRangeDays.md), 'members' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.md), 'messages' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.md), 'viewers' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.md), 'posters' => [StatsAbsValueAndPrev](/API_docs/types/StatsAbsValueAndPrev.md), 'growth_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'members_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'new_members_by_source_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'languages_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'messages_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'actions_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'top_hours_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'weekdays_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), 'top_posters' => \[[StatsGroupTopPoster](/API_docs/types/StatsGroupTopPoster.md)\], 'top_admins' => \[[StatsGroupTopAdmin](/API_docs/types/StatsGroupTopAdmin.md)\], 'top_inviters' => \[[StatsGroupTopInviter](/API_docs/types/StatsGroupTopInviter.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="stats.megagroupStats"></a>  

***
<br><br>[$stats.messageStats](/API_docs/constructors/stats.messageStats.md) = \['views_graph' => [StatsGraph](/API_docs/types/StatsGraph.md), \];<a name="stats.messageStats"></a>  

***
<br><br>[$statsAbsValueAndPrev](/API_docs/constructors/statsAbsValueAndPrev.md) = \['current' => [double](/API_docs/types/double.md), 'previous' => [double](/API_docs/types/double.md), \];<a name="statsAbsValueAndPrev"></a>  

***
<br><br>[$statsDateRangeDays](/API_docs/constructors/statsDateRangeDays.md) = \['min_date' => [int](/API_docs/types/int.md), 'max_date' => [int](/API_docs/types/int.md), \];<a name="statsDateRangeDays"></a>  

***
<br><br>[$statsGraph](/API_docs/constructors/statsGraph.md) = \['json' => [DataJSON](/API_docs/types/DataJSON.md), 'zoom_token' => [string](/API_docs/types/string.md), \];<a name="statsGraph"></a>  

***
<br><br>[$statsGraphAsync](/API_docs/constructors/statsGraphAsync.md) = \['token' => [string](/API_docs/types/string.md), \];<a name="statsGraphAsync"></a>  

***
<br><br>[$statsGraphError](/API_docs/constructors/statsGraphError.md) = \['error' => [string](/API_docs/types/string.md), \];<a name="statsGraphError"></a>  

***
<br><br>[$statsGroupTopAdmin](/API_docs/constructors/statsGroupTopAdmin.md) = \['user_id' => [long](/API_docs/types/long.md), 'deleted' => [int](/API_docs/types/int.md), 'kicked' => [int](/API_docs/types/int.md), 'banned' => [int](/API_docs/types/int.md), \];<a name="statsGroupTopAdmin"></a>  

***
<br><br>[$statsGroupTopInviter](/API_docs/constructors/statsGroupTopInviter.md) = \['user_id' => [long](/API_docs/types/long.md), 'invitations' => [int](/API_docs/types/int.md), \];<a name="statsGroupTopInviter"></a>  

***
<br><br>[$statsGroupTopPoster](/API_docs/constructors/statsGroupTopPoster.md) = \['user_id' => [long](/API_docs/types/long.md), 'messages' => [int](/API_docs/types/int.md), 'avg_chars' => [int](/API_docs/types/int.md), \];<a name="statsGroupTopPoster"></a>  

***
<br><br>[$statsPercentValue](/API_docs/constructors/statsPercentValue.md) = \['part' => [double](/API_docs/types/double.md), 'total' => [double](/API_docs/types/double.md), \];<a name="statsPercentValue"></a>  

***
<br><br>[$statsURL](/API_docs/constructors/statsURL.md) = \['url' => [string](/API_docs/types/string.md), \];<a name="statsURL"></a>  

***
<br><br>[$stickerPack](/API_docs/constructors/stickerPack.md) = \['emoticon' => [string](/API_docs/types/string.md), 'documents' => \[[long](/API_docs/types/long.md)\], \];<a name="stickerPack"></a>  

***
<br><br>[$stickerSet](/API_docs/constructors/stickerSet.md) = \['archived' => [Bool](/API_docs/types/Bool.md), 'official' => [Bool](/API_docs/types/Bool.md), 'masks' => [Bool](/API_docs/types/Bool.md), 'animated' => [Bool](/API_docs/types/Bool.md), 'installed_date' => [int](/API_docs/types/int.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'title' => [string](/API_docs/types/string.md), 'short_name' => [string](/API_docs/types/string.md), 'thumbs' => \[[PhotoSize](/API_docs/types/PhotoSize.md)\], 'thumb_dc_id' => [int](/API_docs/types/int.md), 'thumb_version' => [int](/API_docs/types/int.md), 'count' => [int](/API_docs/types/int.md), 'hash' => [int](/API_docs/types/int.md), \];<a name="stickerSet"></a>  

***
<br><br>[$stickerSetCovered](/API_docs/constructors/stickerSetCovered.md) = \['set' => [StickerSet](/API_docs/types/StickerSet.md), 'cover' => [Document](/API_docs/types/Document.md), \];<a name="stickerSetCovered"></a>  

***
<br><br>[$stickerSetMultiCovered](/API_docs/constructors/stickerSetMultiCovered.md) = \['set' => [StickerSet](/API_docs/types/StickerSet.md), 'covers' => \[[Document](/API_docs/types/Document.md)\], \];<a name="stickerSetMultiCovered"></a>  

***
<br><br>[$stickers.suggestedShortName](/API_docs/constructors/stickers.suggestedShortName.md) = \['short_name' => [string](/API_docs/types/string.md), \];<a name="stickers.suggestedShortName"></a>  

***
<br><br>[$storage.fileGif](/API_docs/constructors/storage.fileGif.md) = \[\];<a name="storage.fileGif"></a>  

***
<br><br>[$storage.fileJpeg](/API_docs/constructors/storage.fileJpeg.md) = \[\];<a name="storage.fileJpeg"></a>  

***
<br><br>[$storage.fileMov](/API_docs/constructors/storage.fileMov.md) = \[\];<a name="storage.fileMov"></a>  

***
<br><br>[$storage.fileMp3](/API_docs/constructors/storage.fileMp3.md) = \[\];<a name="storage.fileMp3"></a>  

***
<br><br>[$storage.fileMp4](/API_docs/constructors/storage.fileMp4.md) = \[\];<a name="storage.fileMp4"></a>  

***
<br><br>[$storage.filePartial](/API_docs/constructors/storage.filePartial.md) = \[\];<a name="storage.filePartial"></a>  

***
<br><br>[$storage.filePdf](/API_docs/constructors/storage.filePdf.md) = \[\];<a name="storage.filePdf"></a>  

***
<br><br>[$storage.filePng](/API_docs/constructors/storage.filePng.md) = \[\];<a name="storage.filePng"></a>  

***
<br><br>[$storage.fileUnknown](/API_docs/constructors/storage.fileUnknown.md) = \[\];<a name="storage.fileUnknown"></a>  

***
<br><br>[$storage.fileWebp](/API_docs/constructors/storage.fileWebp.md) = \[\];<a name="storage.fileWebp"></a>  

***
<br><br>[$textAnchor](/API_docs/constructors/textAnchor.md) = \['text' => [RichText](/API_docs/types/RichText.md), 'name' => [string](/API_docs/types/string.md), \];<a name="textAnchor"></a>  

***
<br><br>[$textBold](/API_docs/constructors/textBold.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="textBold"></a>  

***
<br><br>[$textConcat](/API_docs/constructors/textConcat.md) = \['texts' => \[[RichText](/API_docs/types/RichText.md)\], \];<a name="textConcat"></a>  

***
<br><br>[$textEmail](/API_docs/constructors/textEmail.md) = \['text' => [RichText](/API_docs/types/RichText.md), 'email' => [string](/API_docs/types/string.md), \];<a name="textEmail"></a>  

***
<br><br>[$textEmpty](/API_docs/constructors/textEmpty.md) = \[\];<a name="textEmpty"></a>  

***
<br><br>[$textFixed](/API_docs/constructors/textFixed.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="textFixed"></a>  

***
<br><br>[$textImage](/API_docs/constructors/textImage.md) = \['document_id' => [long](/API_docs/types/long.md), 'w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), \];<a name="textImage"></a>  

***
<br><br>[$textItalic](/API_docs/constructors/textItalic.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="textItalic"></a>  

***
<br><br>[$textMarked](/API_docs/constructors/textMarked.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="textMarked"></a>  

***
<br><br>[$textPhone](/API_docs/constructors/textPhone.md) = \['text' => [RichText](/API_docs/types/RichText.md), 'phone' => [string](/API_docs/types/string.md), \];<a name="textPhone"></a>  

***
<br><br>[$textPlain](/API_docs/constructors/textPlain.md) = \['text' => [string](/API_docs/types/string.md), \];<a name="textPlain"></a>  

***
<br><br>[$textStrike](/API_docs/constructors/textStrike.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="textStrike"></a>  

***
<br><br>[$textSubscript](/API_docs/constructors/textSubscript.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="textSubscript"></a>  

***
<br><br>[$textSuperscript](/API_docs/constructors/textSuperscript.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="textSuperscript"></a>  

***
<br><br>[$textUnderline](/API_docs/constructors/textUnderline.md) = \['text' => [RichText](/API_docs/types/RichText.md), \];<a name="textUnderline"></a>  

***
<br><br>[$textUrl](/API_docs/constructors/textUrl.md) = \['text' => [RichText](/API_docs/types/RichText.md), 'url' => [string](/API_docs/types/string.md), 'webpage_id' => [long](/API_docs/types/long.md), \];<a name="textUrl"></a>  

***
<br><br>[$theme](/API_docs/constructors/theme.md) = \['creator' => [Bool](/API_docs/types/Bool.md), 'default' => [Bool](/API_docs/types/Bool.md), 'for_chat' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'slug' => [string](/API_docs/types/string.md), 'title' => [string](/API_docs/types/string.md), 'document' => [Document](/API_docs/types/Document.md), 'settings' => \[[ThemeSettings](/API_docs/types/ThemeSettings.md)\], 'emoticon' => [string](/API_docs/types/string.md), 'installs_count' => [int](/API_docs/types/int.md), \];<a name="theme"></a>  

***
<br><br>[$themeSettings](/API_docs/constructors/themeSettings.md) = \['message_colors_animated' => [Bool](/API_docs/types/Bool.md), 'base_theme' => [BaseTheme](/API_docs/types/BaseTheme.md), 'accent_color' => [int](/API_docs/types/int.md), 'outbox_accent_color' => [int](/API_docs/types/int.md), 'message_colors' => \[[int](/API_docs/types/int.md)\], 'wallpaper' => [WallPaper](/API_docs/types/WallPaper.md), \];<a name="themeSettings"></a>  

***
<br><br>[$topPeer](/API_docs/constructors/topPeer.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'rating' => [double](/API_docs/types/double.md), \];<a name="topPeer"></a>  

***
<br><br>[$topPeerCategoryBotsInline](/API_docs/constructors/topPeerCategoryBotsInline.md) = \[\];<a name="topPeerCategoryBotsInline"></a>  

***
<br><br>[$topPeerCategoryBotsPM](/API_docs/constructors/topPeerCategoryBotsPM.md) = \[\];<a name="topPeerCategoryBotsPM"></a>  

***
<br><br>[$topPeerCategoryChannels](/API_docs/constructors/topPeerCategoryChannels.md) = \[\];<a name="topPeerCategoryChannels"></a>  

***
<br><br>[$topPeerCategoryCorrespondents](/API_docs/constructors/topPeerCategoryCorrespondents.md) = \[\];<a name="topPeerCategoryCorrespondents"></a>  

***
<br><br>[$topPeerCategoryForwardChats](/API_docs/constructors/topPeerCategoryForwardChats.md) = \[\];<a name="topPeerCategoryForwardChats"></a>  

***
<br><br>[$topPeerCategoryForwardUsers](/API_docs/constructors/topPeerCategoryForwardUsers.md) = \[\];<a name="topPeerCategoryForwardUsers"></a>  

***
<br><br>[$topPeerCategoryGroups](/API_docs/constructors/topPeerCategoryGroups.md) = \[\];<a name="topPeerCategoryGroups"></a>  

***
<br><br>[$topPeerCategoryPeers](/API_docs/constructors/topPeerCategoryPeers.md) = \['category' => [TopPeerCategory](/API_docs/types/TopPeerCategory.md), 'count' => [int](/API_docs/types/int.md), 'peers' => \[[TopPeer](/API_docs/types/TopPeer.md)\], \];<a name="topPeerCategoryPeers"></a>  

***
<br><br>[$topPeerCategoryPhoneCalls](/API_docs/constructors/topPeerCategoryPhoneCalls.md) = \[\];<a name="topPeerCategoryPhoneCalls"></a>  

***
<br><br>[$true](/API_docs/constructors/true.md) = \[\];<a name="true"></a>  

***
<br><br>[$updateBotCallbackQuery](/API_docs/constructors/updateBotCallbackQuery.md) = \['query_id' => [long](/API_docs/types/long.md), 'user_id' => [long](/API_docs/types/long.md), 'peer' => [Peer](/API_docs/types/Peer.md), 'msg_id' => [int](/API_docs/types/int.md), 'chat_instance' => [long](/API_docs/types/long.md), 'data' => [bytes](/API_docs/types/bytes.md), 'game_short_name' => [string](/API_docs/types/string.md), \];<a name="updateBotCallbackQuery"></a>  

***
<br><br>[$updateBotChatInviteRequester](/API_docs/constructors/updateBotChatInviteRequester.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'date' => [int](/API_docs/types/int.md), 'user_id' => [long](/API_docs/types/long.md), 'about' => [string](/API_docs/types/string.md), 'invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), 'qts' => [int](/API_docs/types/int.md), \];<a name="updateBotChatInviteRequester"></a>  

***
<br><br>[$updateBotCommands](/API_docs/constructors/updateBotCommands.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'bot_id' => [long](/API_docs/types/long.md), 'commands' => \[[BotCommand](/API_docs/types/BotCommand.md)\], \];<a name="updateBotCommands"></a>  

***
<br><br>[$updateBotInlineQuery](/API_docs/constructors/updateBotInlineQuery.md) = \['query_id' => [long](/API_docs/types/long.md), 'user_id' => [long](/API_docs/types/long.md), 'query' => [string](/API_docs/types/string.md), 'geo' => [GeoPoint](/API_docs/types/GeoPoint.md), 'peer_type' => [InlineQueryPeerType](/API_docs/types/InlineQueryPeerType.md), 'offset' => [string](/API_docs/types/string.md), \];<a name="updateBotInlineQuery"></a>  

***
<br><br>[$updateBotInlineSend](/API_docs/constructors/updateBotInlineSend.md) = \['user_id' => [long](/API_docs/types/long.md), 'query' => [string](/API_docs/types/string.md), 'geo' => [GeoPoint](/API_docs/types/GeoPoint.md), 'id' => [string](/API_docs/types/string.md), 'msg_id' => [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.md), \];<a name="updateBotInlineSend"></a>  

***
<br><br>[$updateBotPrecheckoutQuery](/API_docs/constructors/updateBotPrecheckoutQuery.md) = \['query_id' => [long](/API_docs/types/long.md), 'user_id' => [long](/API_docs/types/long.md), 'payload' => [bytes](/API_docs/types/bytes.md), 'info' => [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.md), 'shipping_option_id' => [string](/API_docs/types/string.md), 'currency' => [string](/API_docs/types/string.md), 'total_amount' => [long](/API_docs/types/long.md), \];<a name="updateBotPrecheckoutQuery"></a>  

***
<br><br>[$updateBotShippingQuery](/API_docs/constructors/updateBotShippingQuery.md) = \['query_id' => [long](/API_docs/types/long.md), 'user_id' => [long](/API_docs/types/long.md), 'payload' => [bytes](/API_docs/types/bytes.md), 'shipping_address' => [PostAddress](/API_docs/types/PostAddress.md), \];<a name="updateBotShippingQuery"></a>  

***
<br><br>[$updateBotStopped](/API_docs/constructors/updateBotStopped.md) = \['user_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'stopped' => [Bool](/API_docs/types/Bool.md), 'qts' => [int](/API_docs/types/int.md), \];<a name="updateBotStopped"></a>  

***
<br><br>[$updateBotWebhookJSON](/API_docs/constructors/updateBotWebhookJSON.md) = \['data' => [DataJSON](/API_docs/types/DataJSON.md), \];<a name="updateBotWebhookJSON"></a>  

***
<br><br>[$updateBotWebhookJSONQuery](/API_docs/constructors/updateBotWebhookJSONQuery.md) = \['query_id' => [long](/API_docs/types/long.md), 'data' => [DataJSON](/API_docs/types/DataJSON.md), 'timeout' => [int](/API_docs/types/int.md), \];<a name="updateBotWebhookJSONQuery"></a>  

***
<br><br>[$updateChannel](/API_docs/constructors/updateChannel.md) = \['channel_id' => [long](/API_docs/types/long.md), \];<a name="updateChannel"></a>  

***
<br><br>[$updateChannelAvailableMessages](/API_docs/constructors/updateChannelAvailableMessages.md) = \['channel_id' => [long](/API_docs/types/long.md), 'available_min_id' => [int](/API_docs/types/int.md), \];<a name="updateChannelAvailableMessages"></a>  

***
<br><br>[$updateChannelMessageForwards](/API_docs/constructors/updateChannelMessageForwards.md) = \['channel_id' => [long](/API_docs/types/long.md), 'id' => [int](/API_docs/types/int.md), 'forwards' => [int](/API_docs/types/int.md), \];<a name="updateChannelMessageForwards"></a>  

***
<br><br>[$updateChannelMessageViews](/API_docs/constructors/updateChannelMessageViews.md) = \['channel_id' => [long](/API_docs/types/long.md), 'id' => [int](/API_docs/types/int.md), 'views' => [int](/API_docs/types/int.md), \];<a name="updateChannelMessageViews"></a>  

***
<br><br>[$updateChannelParticipant](/API_docs/constructors/updateChannelParticipant.md) = \['channel_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'actor_id' => [long](/API_docs/types/long.md), 'user_id' => [long](/API_docs/types/long.md), 'prev_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.md), 'new_participant' => [ChannelParticipant](/API_docs/types/ChannelParticipant.md), 'invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), 'qts' => [int](/API_docs/types/int.md), \];<a name="updateChannelParticipant"></a>  

***
<br><br>[$updateChannelReadMessagesContents](/API_docs/constructors/updateChannelReadMessagesContents.md) = \['channel_id' => [long](/API_docs/types/long.md), 'messages' => \[[int](/API_docs/types/int.md)\], \];<a name="updateChannelReadMessagesContents"></a>  

***
<br><br>[$updateChannelTooLong](/API_docs/constructors/updateChannelTooLong.md) = \['channel_id' => [long](/API_docs/types/long.md), 'pts' => [int](/API_docs/types/int.md), \];<a name="updateChannelTooLong"></a>  

***
<br><br>[$updateChannelUserTyping](/API_docs/constructors/updateChannelUserTyping.md) = \['channel_id' => [long](/API_docs/types/long.md), 'top_msg_id' => [int](/API_docs/types/int.md), 'from_id' => [Peer](/API_docs/types/Peer.md), 'action' => [SendMessageAction](/API_docs/types/SendMessageAction.md), \];<a name="updateChannelUserTyping"></a>  

***
<br><br>[$updateChannelWebPage](/API_docs/constructors/updateChannelWebPage.md) = \['channel_id' => [long](/API_docs/types/long.md), 'webpage' => [WebPage](/API_docs/types/WebPage.md), 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateChannelWebPage"></a>  

***
<br><br>[$updateChat](/API_docs/constructors/updateChat.md) = \['chat_id' => [long](/API_docs/types/long.md), \];<a name="updateChat"></a>  

***
<br><br>[$updateChatDefaultBannedRights](/API_docs/constructors/updateChatDefaultBannedRights.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'default_banned_rights' => [ChatBannedRights](/API_docs/types/ChatBannedRights.md), 'version' => [int](/API_docs/types/int.md), \];<a name="updateChatDefaultBannedRights"></a>  

***
<br><br>[$updateChatParticipant](/API_docs/constructors/updateChatParticipant.md) = \['chat_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'actor_id' => [long](/API_docs/types/long.md), 'user_id' => [long](/API_docs/types/long.md), 'prev_participant' => [ChatParticipant](/API_docs/types/ChatParticipant.md), 'new_participant' => [ChatParticipant](/API_docs/types/ChatParticipant.md), 'invite' => [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md), 'qts' => [int](/API_docs/types/int.md), \];<a name="updateChatParticipant"></a>  

***
<br><br>[$updateChatParticipantAdd](/API_docs/constructors/updateChatParticipantAdd.md) = \['chat_id' => [long](/API_docs/types/long.md), 'user_id' => [long](/API_docs/types/long.md), 'inviter_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'version' => [int](/API_docs/types/int.md), \];<a name="updateChatParticipantAdd"></a>  

***
<br><br>[$updateChatParticipantAdmin](/API_docs/constructors/updateChatParticipantAdmin.md) = \['chat_id' => [long](/API_docs/types/long.md), 'user_id' => [long](/API_docs/types/long.md), 'is_admin' => [Bool](/API_docs/types/Bool.md), 'version' => [int](/API_docs/types/int.md), \];<a name="updateChatParticipantAdmin"></a>  

***
<br><br>[$updateChatParticipantDelete](/API_docs/constructors/updateChatParticipantDelete.md) = \['chat_id' => [long](/API_docs/types/long.md), 'user_id' => [long](/API_docs/types/long.md), 'version' => [int](/API_docs/types/int.md), \];<a name="updateChatParticipantDelete"></a>  

***
<br><br>[$updateChatParticipants](/API_docs/constructors/updateChatParticipants.md) = \['participants' => [ChatParticipants](/API_docs/types/ChatParticipants.md), \];<a name="updateChatParticipants"></a>  

***
<br><br>[$updateChatUserTyping](/API_docs/constructors/updateChatUserTyping.md) = \['chat_id' => [long](/API_docs/types/long.md), 'from_id' => [Peer](/API_docs/types/Peer.md), 'action' => [SendMessageAction](/API_docs/types/SendMessageAction.md), \];<a name="updateChatUserTyping"></a>  

***
<br><br>[$updateConfig](/API_docs/constructors/updateConfig.md) = \[\];<a name="updateConfig"></a>  

***
<br><br>[$updateContactsReset](/API_docs/constructors/updateContactsReset.md) = \[\];<a name="updateContactsReset"></a>  

***
<br><br>[$updateDcOptions](/API_docs/constructors/updateDcOptions.md) = \['dc_options' => \[[DcOption](/API_docs/types/DcOption.md)\], \];<a name="updateDcOptions"></a>  

***
<br><br>[$updateDeleteChannelMessages](/API_docs/constructors/updateDeleteChannelMessages.md) = \['channel_id' => [long](/API_docs/types/long.md), 'messages' => \[[int](/API_docs/types/int.md)\], 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateDeleteChannelMessages"></a>  

***
<br><br>[$updateDeleteMessages](/API_docs/constructors/updateDeleteMessages.md) = \['messages' => \[[int](/API_docs/types/int.md)\], 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateDeleteMessages"></a>  

***
<br><br>[$updateDeleteScheduledMessages](/API_docs/constructors/updateDeleteScheduledMessages.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'messages' => \[[int](/API_docs/types/int.md)\], \];<a name="updateDeleteScheduledMessages"></a>  

***
<br><br>[$updateDialogFilter](/API_docs/constructors/updateDialogFilter.md) = \['id' => [int](/API_docs/types/int.md), 'filter' => [DialogFilter](/API_docs/types/DialogFilter.md), \];<a name="updateDialogFilter"></a>  

***
<br><br>[$updateDialogFilterOrder](/API_docs/constructors/updateDialogFilterOrder.md) = \['order' => \[[int](/API_docs/types/int.md)\], \];<a name="updateDialogFilterOrder"></a>  

***
<br><br>[$updateDialogFilters](/API_docs/constructors/updateDialogFilters.md) = \[\];<a name="updateDialogFilters"></a>  

***
<br><br>[$updateDialogPinned](/API_docs/constructors/updateDialogPinned.md) = \['pinned' => [Bool](/API_docs/types/Bool.md), 'folder_id' => [int](/API_docs/types/int.md), 'peer' => [DialogPeer](/API_docs/types/DialogPeer.md), \];<a name="updateDialogPinned"></a>  

***
<br><br>[$updateDialogUnreadMark](/API_docs/constructors/updateDialogUnreadMark.md) = \['unread' => [Bool](/API_docs/types/Bool.md), 'peer' => [DialogPeer](/API_docs/types/DialogPeer.md), \];<a name="updateDialogUnreadMark"></a>  

***
<br><br>[$updateDraftMessage](/API_docs/constructors/updateDraftMessage.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'draft' => [DraftMessage](/API_docs/types/DraftMessage.md), \];<a name="updateDraftMessage"></a>  

***
<br><br>[$updateEditChannelMessage](/API_docs/constructors/updateEditChannelMessage.md) = \['message' => [Message](/API_docs/types/Message.md), 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateEditChannelMessage"></a>  

***
<br><br>[$updateEditMessage](/API_docs/constructors/updateEditMessage.md) = \['message' => [Message](/API_docs/types/Message.md), 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateEditMessage"></a>  

***
<br><br>[$updateEncryptedChatTyping](/API_docs/constructors/updateEncryptedChatTyping.md) = \['chat_id' => [int](/API_docs/types/int.md), \];<a name="updateEncryptedChatTyping"></a>  

***
<br><br>[$updateEncryptedMessagesRead](/API_docs/constructors/updateEncryptedMessagesRead.md) = \['chat_id' => [int](/API_docs/types/int.md), 'max_date' => [int](/API_docs/types/int.md), 'date' => [int](/API_docs/types/int.md), \];<a name="updateEncryptedMessagesRead"></a>  

***
<br><br>[$updateEncryption](/API_docs/constructors/updateEncryption.md) = \['chat' => [EncryptedChat](/API_docs/types/EncryptedChat.md), 'date' => [int](/API_docs/types/int.md), \];<a name="updateEncryption"></a>  

***
<br><br>[$updateFavedStickers](/API_docs/constructors/updateFavedStickers.md) = \[\];<a name="updateFavedStickers"></a>  

***
<br><br>[$updateFolderPeers](/API_docs/constructors/updateFolderPeers.md) = \['folder_peers' => \[[FolderPeer](/API_docs/types/FolderPeer.md)\], 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateFolderPeers"></a>  

***
<br><br>[$updateGeoLiveViewed](/API_docs/constructors/updateGeoLiveViewed.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'msg_id' => [int](/API_docs/types/int.md), \];<a name="updateGeoLiveViewed"></a>  

***
<br><br>[$updateGroupCall](/API_docs/constructors/updateGroupCall.md) = \['chat_id' => [long](/API_docs/types/long.md), 'call' => [GroupCall](/API_docs/types/GroupCall.md), \];<a name="updateGroupCall"></a>  

***
<br><br>[$updateGroupCallConnection](/API_docs/constructors/updateGroupCallConnection.md) = \['presentation' => [Bool](/API_docs/types/Bool.md), 'params' => [DataJSON](/API_docs/types/DataJSON.md), \];<a name="updateGroupCallConnection"></a>  

***
<br><br>[$updateGroupCallParticipants](/API_docs/constructors/updateGroupCallParticipants.md) = \['call' => [InputGroupCall](/API_docs/types/InputGroupCall.md), 'participants' => \[[GroupCallParticipant](/API_docs/types/GroupCallParticipant.md)\], 'version' => [int](/API_docs/types/int.md), \];<a name="updateGroupCallParticipants"></a>  

***
<br><br>[$updateInlineBotCallbackQuery](/API_docs/constructors/updateInlineBotCallbackQuery.md) = \['query_id' => [long](/API_docs/types/long.md), 'user_id' => [long](/API_docs/types/long.md), 'msg_id' => [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.md), 'chat_instance' => [long](/API_docs/types/long.md), 'data' => [bytes](/API_docs/types/bytes.md), 'game_short_name' => [string](/API_docs/types/string.md), \];<a name="updateInlineBotCallbackQuery"></a>  

***
<br><br>[$updateLangPack](/API_docs/constructors/updateLangPack.md) = \['difference' => [LangPackDifference](/API_docs/types/LangPackDifference.md), \];<a name="updateLangPack"></a>  

***
<br><br>[$updateLangPackTooLong](/API_docs/constructors/updateLangPackTooLong.md) = \['lang_code' => [string](/API_docs/types/string.md), \];<a name="updateLangPackTooLong"></a>  

***
<br><br>[$updateLoginToken](/API_docs/constructors/updateLoginToken.md) = \[\];<a name="updateLoginToken"></a>  

***
<br><br>[$updateMessageID](/API_docs/constructors/updateMessageID.md) = \['id' => [int](/API_docs/types/int.md), \];<a name="updateMessageID"></a>  

***
<br><br>[$updateMessagePoll](/API_docs/constructors/updateMessagePoll.md) = \['poll_id' => [long](/API_docs/types/long.md), 'poll' => [Poll](/API_docs/types/Poll.md), 'results' => [PollResults](/API_docs/types/PollResults.md), \];<a name="updateMessagePoll"></a>  

***
<br><br>[$updateMessagePollVote](/API_docs/constructors/updateMessagePollVote.md) = \['poll_id' => [long](/API_docs/types/long.md), 'user_id' => [long](/API_docs/types/long.md), 'options' => \[[bytes](/API_docs/types/bytes.md)\], 'qts' => [int](/API_docs/types/int.md), \];<a name="updateMessagePollVote"></a>  

***
<br><br>[$updateMessageReactions](/API_docs/constructors/updateMessageReactions.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'msg_id' => [int](/API_docs/types/int.md), 'reactions' => [MessageReactions](/API_docs/types/MessageReactions.md), \];<a name="updateMessageReactions"></a>  

***
<br><br>[$updateNewChannelMessage](/API_docs/constructors/updateNewChannelMessage.md) = \['message' => [Message](/API_docs/types/Message.md), 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateNewChannelMessage"></a>  

***
<br><br>[$updateNewEncryptedMessage](/API_docs/constructors/updateNewEncryptedMessage.md) = \['message' => [EncryptedMessage](/API_docs/types/EncryptedMessage.md), 'qts' => [int](/API_docs/types/int.md), \];<a name="updateNewEncryptedMessage"></a>  

***
<br><br>[$updateNewMessage](/API_docs/constructors/updateNewMessage.md) = \['message' => [Message](/API_docs/types/Message.md), 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateNewMessage"></a>  

***
<br><br>[$updateNewScheduledMessage](/API_docs/constructors/updateNewScheduledMessage.md) = \['message' => [Message](/API_docs/types/Message.md), \];<a name="updateNewScheduledMessage"></a>  

***
<br><br>[$updateNewStickerSet](/API_docs/constructors/updateNewStickerSet.md) = \['stickerset' => [messages.StickerSet](/API_docs/types/messages.StickerSet.md), \];<a name="updateNewStickerSet"></a>  

***
<br><br>[$updateNotifySettings](/API_docs/constructors/updateNotifySettings.md) = \['peer' => [NotifyPeer](/API_docs/types/NotifyPeer.md), 'notify_settings' => [PeerNotifySettings](/API_docs/types/PeerNotifySettings.md), \];<a name="updateNotifySettings"></a>  

***
<br><br>[$updatePeerBlocked](/API_docs/constructors/updatePeerBlocked.md) = \['peer_id' => [Peer](/API_docs/types/Peer.md), 'blocked' => [Bool](/API_docs/types/Bool.md), \];<a name="updatePeerBlocked"></a>  

***
<br><br>[$updatePeerHistoryTTL](/API_docs/constructors/updatePeerHistoryTTL.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'ttl_period' => [int](/API_docs/types/int.md), \];<a name="updatePeerHistoryTTL"></a>  

***
<br><br>[$updatePeerLocated](/API_docs/constructors/updatePeerLocated.md) = \['peers' => \[[PeerLocated](/API_docs/types/PeerLocated.md)\], \];<a name="updatePeerLocated"></a>  

***
<br><br>[$updatePeerSettings](/API_docs/constructors/updatePeerSettings.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'settings' => [PeerSettings](/API_docs/types/PeerSettings.md), \];<a name="updatePeerSettings"></a>  

***
<br><br>[$updatePendingJoinRequests](/API_docs/constructors/updatePendingJoinRequests.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'requests_pending' => [int](/API_docs/types/int.md), 'recent_requesters' => \[[long](/API_docs/types/long.md)\], \];<a name="updatePendingJoinRequests"></a>  

***
<br><br>[$updatePhoneCall](/API_docs/constructors/updatePhoneCall.md) = \['phone_call' => [PhoneCall](/API_docs/types/PhoneCall.md), \];<a name="updatePhoneCall"></a>  

***
<br><br>[$updatePhoneCallSignalingData](/API_docs/constructors/updatePhoneCallSignalingData.md) = \['phone_call_id' => [long](/API_docs/types/long.md), 'data' => [bytes](/API_docs/types/bytes.md), \];<a name="updatePhoneCallSignalingData"></a>  

***
<br><br>[$updatePinnedChannelMessages](/API_docs/constructors/updatePinnedChannelMessages.md) = \['pinned' => [Bool](/API_docs/types/Bool.md), 'channel_id' => [long](/API_docs/types/long.md), 'messages' => \[[int](/API_docs/types/int.md)\], 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updatePinnedChannelMessages"></a>  

***
<br><br>[$updatePinnedDialogs](/API_docs/constructors/updatePinnedDialogs.md) = \['folder_id' => [int](/API_docs/types/int.md), 'order' => \[[DialogPeer](/API_docs/types/DialogPeer.md)\], \];<a name="updatePinnedDialogs"></a>  

***
<br><br>[$updatePinnedMessages](/API_docs/constructors/updatePinnedMessages.md) = \['pinned' => [Bool](/API_docs/types/Bool.md), 'peer' => [Peer](/API_docs/types/Peer.md), 'messages' => \[[int](/API_docs/types/int.md)\], 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updatePinnedMessages"></a>  

***
<br><br>[$updatePrivacy](/API_docs/constructors/updatePrivacy.md) = \['key' => [PrivacyKey](/API_docs/types/PrivacyKey.md), 'rules' => \[[PrivacyRule](/API_docs/types/PrivacyRule.md)\], \];<a name="updatePrivacy"></a>  

***
<br><br>[$updatePtsChanged](/API_docs/constructors/updatePtsChanged.md) = \[\];<a name="updatePtsChanged"></a>  

***
<br><br>[$updateReadChannelDiscussionInbox](/API_docs/constructors/updateReadChannelDiscussionInbox.md) = \['channel_id' => [long](/API_docs/types/long.md), 'top_msg_id' => [int](/API_docs/types/int.md), 'read_max_id' => [int](/API_docs/types/int.md), 'broadcast_id' => [long](/API_docs/types/long.md), 'broadcast_post' => [int](/API_docs/types/int.md), \];<a name="updateReadChannelDiscussionInbox"></a>  

***
<br><br>[$updateReadChannelDiscussionOutbox](/API_docs/constructors/updateReadChannelDiscussionOutbox.md) = \['channel_id' => [long](/API_docs/types/long.md), 'top_msg_id' => [int](/API_docs/types/int.md), 'read_max_id' => [int](/API_docs/types/int.md), \];<a name="updateReadChannelDiscussionOutbox"></a>  

***
<br><br>[$updateReadChannelInbox](/API_docs/constructors/updateReadChannelInbox.md) = \['folder_id' => [int](/API_docs/types/int.md), 'channel_id' => [long](/API_docs/types/long.md), 'max_id' => [int](/API_docs/types/int.md), 'still_unread_count' => [int](/API_docs/types/int.md), 'pts' => [int](/API_docs/types/int.md), \];<a name="updateReadChannelInbox"></a>  

***
<br><br>[$updateReadChannelOutbox](/API_docs/constructors/updateReadChannelOutbox.md) = \['channel_id' => [long](/API_docs/types/long.md), 'max_id' => [int](/API_docs/types/int.md), \];<a name="updateReadChannelOutbox"></a>  

***
<br><br>[$updateReadFeaturedStickers](/API_docs/constructors/updateReadFeaturedStickers.md) = \[\];<a name="updateReadFeaturedStickers"></a>  

***
<br><br>[$updateReadHistoryInbox](/API_docs/constructors/updateReadHistoryInbox.md) = \['folder_id' => [int](/API_docs/types/int.md), 'peer' => [Peer](/API_docs/types/Peer.md), 'max_id' => [int](/API_docs/types/int.md), 'still_unread_count' => [int](/API_docs/types/int.md), 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateReadHistoryInbox"></a>  

***
<br><br>[$updateReadHistoryOutbox](/API_docs/constructors/updateReadHistoryOutbox.md) = \['peer' => [Peer](/API_docs/types/Peer.md), 'max_id' => [int](/API_docs/types/int.md), 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateReadHistoryOutbox"></a>  

***
<br><br>[$updateReadMessagesContents](/API_docs/constructors/updateReadMessagesContents.md) = \['messages' => \[[int](/API_docs/types/int.md)\], 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateReadMessagesContents"></a>  

***
<br><br>[$updateRecentStickers](/API_docs/constructors/updateRecentStickers.md) = \[\];<a name="updateRecentStickers"></a>  

***
<br><br>[$updateSavedGifs](/API_docs/constructors/updateSavedGifs.md) = \[\];<a name="updateSavedGifs"></a>  

***
<br><br>[$updateServiceNotification](/API_docs/constructors/updateServiceNotification.md) = \['popup' => [Bool](/API_docs/types/Bool.md), 'inbox_date' => [int](/API_docs/types/int.md), 'type' => [string](/API_docs/types/string.md), 'message' => [string](/API_docs/types/string.md), 'media' => [MessageMedia](/API_docs/types/MessageMedia.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], \];<a name="updateServiceNotification"></a>  

***
<br><br>[$updateShort](/API_docs/constructors/updateShort.md) = \['update' => [Update](/API_docs/types/Update.md), 'date' => [int](/API_docs/types/int.md), \];<a name="updateShort"></a>  

***
<br><br>[$updateShortChatMessage](/API_docs/constructors/updateShortChatMessage.md) = \['out' => [Bool](/API_docs/types/Bool.md), 'mentioned' => [Bool](/API_docs/types/Bool.md), 'media_unread' => [Bool](/API_docs/types/Bool.md), 'silent' => [Bool](/API_docs/types/Bool.md), 'id' => [int](/API_docs/types/int.md), 'from_id' => [long](/API_docs/types/long.md), 'chat_id' => [long](/API_docs/types/long.md), 'message' => [string](/API_docs/types/string.md), 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), 'date' => [int](/API_docs/types/int.md), 'fwd_from' => [MessageFwdHeader](/API_docs/types/MessageFwdHeader.md), 'via_bot_id' => [long](/API_docs/types/long.md), 'reply_to' => [MessageReplyHeader](/API_docs/types/MessageReplyHeader.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'ttl_period' => [int](/API_docs/types/int.md), \];<a name="updateShortChatMessage"></a>  

***
<br><br>[$updateShortMessage](/API_docs/constructors/updateShortMessage.md) = \['out' => [Bool](/API_docs/types/Bool.md), 'mentioned' => [Bool](/API_docs/types/Bool.md), 'media_unread' => [Bool](/API_docs/types/Bool.md), 'silent' => [Bool](/API_docs/types/Bool.md), 'id' => [int](/API_docs/types/int.md), 'user_id' => [long](/API_docs/types/long.md), 'message' => [string](/API_docs/types/string.md), 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), 'date' => [int](/API_docs/types/int.md), 'fwd_from' => [MessageFwdHeader](/API_docs/types/MessageFwdHeader.md), 'via_bot_id' => [long](/API_docs/types/long.md), 'reply_to' => [MessageReplyHeader](/API_docs/types/MessageReplyHeader.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'ttl_period' => [int](/API_docs/types/int.md), \];<a name="updateShortMessage"></a>  

***
<br><br>[$updateShortSentMessage](/API_docs/constructors/updateShortSentMessage.md) = \['out' => [Bool](/API_docs/types/Bool.md), 'id' => [int](/API_docs/types/int.md), 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), 'date' => [int](/API_docs/types/int.md), 'media' => [MessageMedia](/API_docs/types/MessageMedia.md), 'entities' => \[[MessageEntity](/API_docs/types/MessageEntity.md)\], 'ttl_period' => [int](/API_docs/types/int.md), \];<a name="updateShortSentMessage"></a>  

***
<br><br>[$updateStickerSets](/API_docs/constructors/updateStickerSets.md) = \[\];<a name="updateStickerSets"></a>  

***
<br><br>[$updateStickerSetsOrder](/API_docs/constructors/updateStickerSetsOrder.md) = \['masks' => [Bool](/API_docs/types/Bool.md), 'order' => \[[long](/API_docs/types/long.md)\], \];<a name="updateStickerSetsOrder"></a>  

***
<br><br>[$updateTheme](/API_docs/constructors/updateTheme.md) = \['theme' => [Theme](/API_docs/types/Theme.md), \];<a name="updateTheme"></a>  

***
<br><br>[$updateUserName](/API_docs/constructors/updateUserName.md) = \['user_id' => [long](/API_docs/types/long.md), 'first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), 'username' => [string](/API_docs/types/string.md), \];<a name="updateUserName"></a>  

***
<br><br>[$updateUserPhone](/API_docs/constructors/updateUserPhone.md) = \['user_id' => [long](/API_docs/types/long.md), 'phone' => [string](/API_docs/types/string.md), \];<a name="updateUserPhone"></a>  

***
<br><br>[$updateUserPhoto](/API_docs/constructors/updateUserPhoto.md) = \['user_id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), 'photo' => [UserProfilePhoto](/API_docs/types/UserProfilePhoto.md), 'previous' => [Bool](/API_docs/types/Bool.md), \];<a name="updateUserPhoto"></a>  

***
<br><br>[$updateUserStatus](/API_docs/constructors/updateUserStatus.md) = \['user_id' => [long](/API_docs/types/long.md), 'status' => [UserStatus](/API_docs/types/UserStatus.md), \];<a name="updateUserStatus"></a>  

***
<br><br>[$updateUserTyping](/API_docs/constructors/updateUserTyping.md) = \['user_id' => [long](/API_docs/types/long.md), 'action' => [SendMessageAction](/API_docs/types/SendMessageAction.md), \];<a name="updateUserTyping"></a>  

***
<br><br>[$updateWebPage](/API_docs/constructors/updateWebPage.md) = \['webpage' => [WebPage](/API_docs/types/WebPage.md), 'pts' => [int](/API_docs/types/int.md), 'pts_count' => [int](/API_docs/types/int.md), \];<a name="updateWebPage"></a>  

***
<br><br>[$updates](/API_docs/constructors/updates.md) = \['updates' => \[[Update](/API_docs/types/Update.md)\], 'users' => \[[User](/API_docs/types/User.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'date' => [int](/API_docs/types/int.md), 'seq' => [int](/API_docs/types/int.md), \];<a name="updates"></a>  

***
<br><br>[$updates.channelDifference](/API_docs/constructors/updates.channelDifference.md) = \['final' => [Bool](/API_docs/types/Bool.md), 'pts' => [int](/API_docs/types/int.md), 'timeout' => [int](/API_docs/types/int.md), 'new_messages' => \[[Message](/API_docs/types/Message.md)\], 'other_updates' => \[[Update](/API_docs/types/Update.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="updates.channelDifference"></a>  

***
<br><br>[$updates.channelDifferenceEmpty](/API_docs/constructors/updates.channelDifferenceEmpty.md) = \['final' => [Bool](/API_docs/types/Bool.md), 'pts' => [int](/API_docs/types/int.md), 'timeout' => [int](/API_docs/types/int.md), \];<a name="updates.channelDifferenceEmpty"></a>  

***
<br><br>[$updates.channelDifferenceTooLong](/API_docs/constructors/updates.channelDifferenceTooLong.md) = \['final' => [Bool](/API_docs/types/Bool.md), 'timeout' => [int](/API_docs/types/int.md), 'dialog' => [Dialog](/API_docs/types/Dialog.md), 'messages' => \[[Message](/API_docs/types/Message.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="updates.channelDifferenceTooLong"></a>  

***
<br><br>[$updates.difference](/API_docs/constructors/updates.difference.md) = \['new_messages' => \[[Message](/API_docs/types/Message.md)\], 'new_encrypted_messages' => \[[EncryptedMessage](/API_docs/types/EncryptedMessage.md)\], 'other_updates' => \[[Update](/API_docs/types/Update.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], 'state' => [updates.State](/API_docs/types/updates.State.md), \];<a name="updates.difference"></a>  

***
<br><br>[$updates.differenceEmpty](/API_docs/constructors/updates.differenceEmpty.md) = \['date' => [int](/API_docs/types/int.md), 'seq' => [int](/API_docs/types/int.md), \];<a name="updates.differenceEmpty"></a>  

***
<br><br>[$updates.differenceSlice](/API_docs/constructors/updates.differenceSlice.md) = \['new_messages' => \[[Message](/API_docs/types/Message.md)\], 'new_encrypted_messages' => \[[EncryptedMessage](/API_docs/types/EncryptedMessage.md)\], 'other_updates' => \[[Update](/API_docs/types/Update.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], 'intermediate_state' => [updates.State](/API_docs/types/updates.State.md), \];<a name="updates.differenceSlice"></a>  

***
<br><br>[$updates.differenceTooLong](/API_docs/constructors/updates.differenceTooLong.md) = \['pts' => [int](/API_docs/types/int.md), \];<a name="updates.differenceTooLong"></a>  

***
<br><br>[$updates.state](/API_docs/constructors/updates.state.md) = \['pts' => [int](/API_docs/types/int.md), 'qts' => [int](/API_docs/types/int.md), 'date' => [int](/API_docs/types/int.md), 'seq' => [int](/API_docs/types/int.md), 'unread_count' => [int](/API_docs/types/int.md), \];<a name="updates.state"></a>  

***
<br><br>[$updatesCombined](/API_docs/constructors/updatesCombined.md) = \['updates' => \[[Update](/API_docs/types/Update.md)\], 'users' => \[[User](/API_docs/types/User.md)\], 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'date' => [int](/API_docs/types/int.md), 'seq_start' => [int](/API_docs/types/int.md), 'seq' => [int](/API_docs/types/int.md), \];<a name="updatesCombined"></a>  

***
<br><br>[$updatesTooLong](/API_docs/constructors/updatesTooLong.md) = \[\];<a name="updatesTooLong"></a>  

***
<br><br>[$upload.cdnFile](/API_docs/constructors/upload.cdnFile.md) = \['bytes' => [bytes](/API_docs/types/bytes.md), \];<a name="upload.cdnFile"></a>  

***
<br><br>[$upload.cdnFileReuploadNeeded](/API_docs/constructors/upload.cdnFileReuploadNeeded.md) = \['request_token' => [bytes](/API_docs/types/bytes.md), \];<a name="upload.cdnFileReuploadNeeded"></a>  

***
<br><br>[$upload.file](/API_docs/constructors/upload.file.md) = \['type' => [storage.FileType](/API_docs/types/storage.FileType.md), 'mtime' => [int](/API_docs/types/int.md), 'bytes' => [bytes](/API_docs/types/bytes.md), \];<a name="upload.file"></a>  

***
<br><br>[$upload.fileCdnRedirect](/API_docs/constructors/upload.fileCdnRedirect.md) = \['dc_id' => [int](/API_docs/types/int.md), 'file_token' => [bytes](/API_docs/types/bytes.md), 'encryption_key' => [bytes](/API_docs/types/bytes.md), 'encryption_iv' => [bytes](/API_docs/types/bytes.md), 'file_hashes' => \[[FileHash](/API_docs/types/FileHash.md)\], \];<a name="upload.fileCdnRedirect"></a>  

***
<br><br>[$upload.webFile](/API_docs/constructors/upload.webFile.md) = \['size' => [int](/API_docs/types/int.md), 'mime_type' => [string](/API_docs/types/string.md), 'file_type' => [storage.FileType](/API_docs/types/storage.FileType.md), 'mtime' => [int](/API_docs/types/int.md), 'bytes' => [bytes](/API_docs/types/bytes.md), \];<a name="upload.webFile"></a>  

***
<br><br>[$urlAuthResultAccepted](/API_docs/constructors/urlAuthResultAccepted.md) = \['url' => [string](/API_docs/types/string.md), \];<a name="urlAuthResultAccepted"></a>  

***
<br><br>[$urlAuthResultDefault](/API_docs/constructors/urlAuthResultDefault.md) = \[\];<a name="urlAuthResultDefault"></a>  

***
<br><br>[$urlAuthResultRequest](/API_docs/constructors/urlAuthResultRequest.md) = \['request_write_access' => [Bool](/API_docs/types/Bool.md), 'bot' => [User](/API_docs/types/User.md), 'domain' => [string](/API_docs/types/string.md), \];<a name="urlAuthResultRequest"></a>  

***
<br><br>[$user](/API_docs/constructors/user.md) = \['self' => [Bool](/API_docs/types/Bool.md), 'contact' => [Bool](/API_docs/types/Bool.md), 'mutual_contact' => [Bool](/API_docs/types/Bool.md), 'deleted' => [Bool](/API_docs/types/Bool.md), 'bot' => [Bool](/API_docs/types/Bool.md), 'bot_chat_history' => [Bool](/API_docs/types/Bool.md), 'bot_nochats' => [Bool](/API_docs/types/Bool.md), 'verified' => [Bool](/API_docs/types/Bool.md), 'restricted' => [Bool](/API_docs/types/Bool.md), 'min' => [Bool](/API_docs/types/Bool.md), 'bot_inline_geo' => [Bool](/API_docs/types/Bool.md), 'support' => [Bool](/API_docs/types/Bool.md), 'scam' => [Bool](/API_docs/types/Bool.md), 'apply_min_photo' => [Bool](/API_docs/types/Bool.md), 'fake' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'access_hash' => [long](/API_docs/types/long.md), 'first_name' => [string](/API_docs/types/string.md), 'last_name' => [string](/API_docs/types/string.md), 'username' => [string](/API_docs/types/string.md), 'phone' => [string](/API_docs/types/string.md), 'photo' => [UserProfilePhoto](/API_docs/types/UserProfilePhoto.md), 'status' => [UserStatus](/API_docs/types/UserStatus.md), 'bot_info_version' => [int](/API_docs/types/int.md), 'restriction_reason' => \[[RestrictionReason](/API_docs/types/RestrictionReason.md)\], 'bot_inline_placeholder' => [string](/API_docs/types/string.md), 'lang_code' => [string](/API_docs/types/string.md), \];<a name="user"></a>  

***
<br><br>[$userEmpty](/API_docs/constructors/userEmpty.md) = \['id' => [long](/API_docs/types/long.md), \];<a name="userEmpty"></a>  

***
<br><br>[$userFull](/API_docs/constructors/userFull.md) = \['blocked' => [Bool](/API_docs/types/Bool.md), 'phone_calls_available' => [Bool](/API_docs/types/Bool.md), 'phone_calls_private' => [Bool](/API_docs/types/Bool.md), 'can_pin_message' => [Bool](/API_docs/types/Bool.md), 'has_scheduled' => [Bool](/API_docs/types/Bool.md), 'video_calls_available' => [Bool](/API_docs/types/Bool.md), 'id' => [long](/API_docs/types/long.md), 'about' => [string](/API_docs/types/string.md), 'settings' => [PeerSettings](/API_docs/types/PeerSettings.md), 'profile_photo' => [Photo](/API_docs/types/Photo.md), 'notify_settings' => [PeerNotifySettings](/API_docs/types/PeerNotifySettings.md), 'bot_info' => [BotInfo](/API_docs/types/BotInfo.md), 'pinned_msg_id' => [int](/API_docs/types/int.md), 'common_chats_count' => [int](/API_docs/types/int.md), 'folder_id' => [int](/API_docs/types/int.md), 'ttl_period' => [int](/API_docs/types/int.md), 'theme_emoticon' => [string](/API_docs/types/string.md), 'private_forward_name' => [string](/API_docs/types/string.md), \];<a name="userFull"></a>  

***
<br><br>[$userProfilePhoto](/API_docs/constructors/userProfilePhoto.md) = \['has_video' => [Bool](/API_docs/types/Bool.md), 'photo_id' => [long](/API_docs/types/long.md), 'stripped_thumb' => [bytes](/API_docs/types/bytes.md), 'dc_id' => [int](/API_docs/types/int.md), \];<a name="userProfilePhoto"></a>  

***
<br><br>[$userProfilePhotoEmpty](/API_docs/constructors/userProfilePhotoEmpty.md) = \[\];<a name="userProfilePhotoEmpty"></a>  

***
<br><br>[$userStatusEmpty](/API_docs/constructors/userStatusEmpty.md) = \[\];<a name="userStatusEmpty"></a>  

***
<br><br>[$userStatusLastMonth](/API_docs/constructors/userStatusLastMonth.md) = \[\];<a name="userStatusLastMonth"></a>  

***
<br><br>[$userStatusLastWeek](/API_docs/constructors/userStatusLastWeek.md) = \[\];<a name="userStatusLastWeek"></a>  

***
<br><br>[$userStatusOffline](/API_docs/constructors/userStatusOffline.md) = \['was_online' => [int](/API_docs/types/int.md), \];<a name="userStatusOffline"></a>  

***
<br><br>[$userStatusOnline](/API_docs/constructors/userStatusOnline.md) = \['expires' => [int](/API_docs/types/int.md), \];<a name="userStatusOnline"></a>  

***
<br><br>[$userStatusRecently](/API_docs/constructors/userStatusRecently.md) = \[\];<a name="userStatusRecently"></a>  

***
<br><br>[$users.userFull](/API_docs/constructors/users.userFull.md) = \['full_user' => [UserFull](/API_docs/types/UserFull.md), 'chats' => \[[Chat](/API_docs/types/Chat.md)\], 'users' => \[[User](/API_docs/types/User.md)\], \];<a name="users.userFull"></a>  

***
<br><br>[$videoSize](/API_docs/constructors/videoSize.md) = \['type' => [string](/API_docs/types/string.md), 'w' => [int](/API_docs/types/int.md), 'h' => [int](/API_docs/types/int.md), 'size' => [int](/API_docs/types/int.md), 'video_start_ts' => [double](/API_docs/types/double.md), \];<a name="videoSize"></a>  

***
<br><br>[$wallPaper](/API_docs/constructors/wallPaper.md) = \['id' => [long](/API_docs/types/long.md), 'creator' => [Bool](/API_docs/types/Bool.md), 'default' => [Bool](/API_docs/types/Bool.md), 'pattern' => [Bool](/API_docs/types/Bool.md), 'dark' => [Bool](/API_docs/types/Bool.md), 'access_hash' => [long](/API_docs/types/long.md), 'slug' => [string](/API_docs/types/string.md), 'document' => [Document](/API_docs/types/Document.md), 'settings' => [WallPaperSettings](/API_docs/types/WallPaperSettings.md), \];<a name="wallPaper"></a>  

***
<br><br>[$wallPaperNoFile](/API_docs/constructors/wallPaperNoFile.md) = \['id' => [long](/API_docs/types/long.md), 'default' => [Bool](/API_docs/types/Bool.md), 'dark' => [Bool](/API_docs/types/Bool.md), 'settings' => [WallPaperSettings](/API_docs/types/WallPaperSettings.md), \];<a name="wallPaperNoFile"></a>  

***
<br><br>[$wallPaperSettings](/API_docs/constructors/wallPaperSettings.md) = \['blur' => [Bool](/API_docs/types/Bool.md), 'motion' => [Bool](/API_docs/types/Bool.md), 'background_color' => [int](/API_docs/types/int.md), 'second_background_color' => [int](/API_docs/types/int.md), 'third_background_color' => [int](/API_docs/types/int.md), 'fourth_background_color' => [int](/API_docs/types/int.md), 'intensity' => [int](/API_docs/types/int.md), 'rotation' => [int](/API_docs/types/int.md), \];<a name="wallPaperSettings"></a>  

***
<br><br>[$webAuthorization](/API_docs/constructors/webAuthorization.md) = \['hash' => [long](/API_docs/types/long.md), 'bot_id' => [long](/API_docs/types/long.md), 'domain' => [string](/API_docs/types/string.md), 'browser' => [string](/API_docs/types/string.md), 'platform' => [string](/API_docs/types/string.md), 'date_created' => [int](/API_docs/types/int.md), 'date_active' => [int](/API_docs/types/int.md), 'ip' => [string](/API_docs/types/string.md), 'region' => [string](/API_docs/types/string.md), \];<a name="webAuthorization"></a>  

***
<br><br>[$webDocument](/API_docs/constructors/webDocument.md) = \['url' => [string](/API_docs/types/string.md), 'access_hash' => [long](/API_docs/types/long.md), 'size' => [int](/API_docs/types/int.md), 'mime_type' => [string](/API_docs/types/string.md), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.md)\], \];<a name="webDocument"></a>  

***
<br><br>[$webDocumentNoProxy](/API_docs/constructors/webDocumentNoProxy.md) = \['url' => [string](/API_docs/types/string.md), 'size' => [int](/API_docs/types/int.md), 'mime_type' => [string](/API_docs/types/string.md), 'attributes' => \[[DocumentAttribute](/API_docs/types/DocumentAttribute.md)\], \];<a name="webDocumentNoProxy"></a>  

***
<br><br>[$webPage](/API_docs/constructors/webPage.md) = \['id' => [long](/API_docs/types/long.md), 'url' => [string](/API_docs/types/string.md), 'display_url' => [string](/API_docs/types/string.md), 'hash' => [int](/API_docs/types/int.md), 'type' => [string](/API_docs/types/string.md), 'site_name' => [string](/API_docs/types/string.md), 'title' => [string](/API_docs/types/string.md), 'description' => [string](/API_docs/types/string.md), 'photo' => [Photo](/API_docs/types/Photo.md), 'embed_url' => [string](/API_docs/types/string.md), 'embed_type' => [string](/API_docs/types/string.md), 'embed_width' => [int](/API_docs/types/int.md), 'embed_height' => [int](/API_docs/types/int.md), 'duration' => [int](/API_docs/types/int.md), 'author' => [string](/API_docs/types/string.md), 'document' => [Document](/API_docs/types/Document.md), 'cached_page' => [Page](/API_docs/types/Page.md), 'attributes' => \[[WebPageAttribute](/API_docs/types/WebPageAttribute.md)\], \];<a name="webPage"></a>  

***
<br><br>[$webPageAttributeTheme](/API_docs/constructors/webPageAttributeTheme.md) = \['documents' => \[[Document](/API_docs/types/Document.md)\], 'settings' => [ThemeSettings](/API_docs/types/ThemeSettings.md), \];<a name="webPageAttributeTheme"></a>  

***
<br><br>[$webPageEmpty](/API_docs/constructors/webPageEmpty.md) = \['id' => [long](/API_docs/types/long.md), \];<a name="webPageEmpty"></a>  

***
<br><br>[$webPageNotModified](/API_docs/constructors/webPageNotModified.md) = \['cached_page_views' => [int](/API_docs/types/int.md), \];<a name="webPageNotModified"></a>  

***
<br><br>[$webPagePending](/API_docs/constructors/webPagePending.md) = \['id' => [long](/API_docs/types/long.md), 'date' => [int](/API_docs/types/int.md), \];<a name="webPagePending"></a>  


