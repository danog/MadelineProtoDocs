---
title: Methods
description: List of methods
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Methods  
[Back to API documentation index](..)

[Go to the new description-version method index](index.md)

$MadelineProto->[logout](https://docs.madelineproto.xyz/logout.html)();

$MadelineProto->[phone_login](https://docs.madelineproto.xyz/phone_login.html)($number);

$MadelineProto->[complete_phone_login](https://docs.madelineproto.xyz/complete_phone_login.html)($code);

$MadelineProto->[complete_2FA_login](https://docs.madelineproto.xyz/complete_2FA_login.html)($password);

$MadelineProto->[bot_login](https://docs.madelineproto.xyz/bot_login.html)($token);


$MadelineProto->[get_dialogs](https://docs.madelineproto.xyz/get_dialogs.html)();

$MadelineProto->[get_pwr_chat](https://docs.madelineproto.xyz/get_pwr_chat.html)($id);

$MadelineProto->[get_info](https://docs.madelineproto.xyz/get_info.html)($id);

$MadelineProto->[get_full_info](https://docs.madelineproto.xyz/get_full_info.html)($id);

$MadelineProto->[get_self](https://docs.madelineproto.xyz/get_self.html)();


$MadelineProto->[request_call](https://docs.madelineproto.xyz/request_call.html)($id);

$MadelineProto->[request_secret_chat](https://docs.madelineproto.xyz/request_secret_chat.html)($id);

***
<br><br>
$MadelineProto->[account->acceptAuthorization](account_acceptAuthorization.md)(\['bot_id' => [int](../types/int.md), 'scope' => [string](../types/string.md), 'public_key' => [string](../types/string.md), 'value_hashes' => \[[SecureValueHash](../types/SecureValueHash.md)\], 'credentials' => [SecureCredentialsEncrypted](../types/SecureCredentialsEncrypted.md), \]) === [$Bool](../types/Bool.md)<a name="account_acceptAuthorization"></a>  

$MadelineProto->[account->cancelPasswordEmail](account_cancelPasswordEmail.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account_cancelPasswordEmail"></a>  

$MadelineProto->[account->changePhone](account_changePhone.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), 'phone_code' => [string](../types/string.md), \]) === [$User](../types/User.md)<a name="account_changePhone"></a>  

$MadelineProto->[account->checkUsername](account_checkUsername.md)(\['username' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account_checkUsername"></a>  

$MadelineProto->[account->confirmPasswordEmail](account_confirmPasswordEmail.md)(\['code' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account_confirmPasswordEmail"></a>  

$MadelineProto->[account->confirmPhone](account_confirmPhone.md)(\['phone_code_hash' => [string](../types/string.md), 'phone_code' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account_confirmPhone"></a>  

$MadelineProto->[account->deleteAccount](account_deleteAccount.md)(\['reason' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account_deleteAccount"></a>  

$MadelineProto->[account->deleteSecureValue](account_deleteSecureValue.md)(\['types' => \[[SecureValueType](../types/SecureValueType.md)\], \]) === [$Bool](../types/Bool.md)<a name="account_deleteSecureValue"></a>  

$MadelineProto->[account->finishTakeoutSession](account_finishTakeoutSession.md)(\['success' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="account_finishTakeoutSession"></a>  

$MadelineProto->[account->getAccountTTL](account_getAccountTTL.md)(\[\]) === [$AccountDaysTTL](../types/AccountDaysTTL.md)<a name="account_getAccountTTL"></a>  

$MadelineProto->[account->getAllSecureValues](account_getAllSecureValues.md)(\[\]) === [$Vector\_of\_SecureValue](../types/SecureValue.md)<a name="account_getAllSecureValues"></a>  

$MadelineProto->[account->getAuthorizationForm](account_getAuthorizationForm.md)(\['bot_id' => [int](../types/int.md), 'scope' => [string](../types/string.md), 'public_key' => [string](../types/string.md), \]) === [$account\_AuthorizationForm](../types/account_AuthorizationForm.md)<a name="account_getAuthorizationForm"></a>  

$MadelineProto->[account->getAuthorizations](account_getAuthorizations.md)(\[\]) === [$account\_Authorizations](../types/account_Authorizations.md)<a name="account_getAuthorizations"></a>  

$MadelineProto->[account->getAutoDownloadSettings](account_getAutoDownloadSettings.md)(\[\]) === [$account\_AutoDownloadSettings](../types/account_AutoDownloadSettings.md)<a name="account_getAutoDownloadSettings"></a>  

$MadelineProto->[account->getContactSignUpNotification](account_getContactSignUpNotification.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account_getContactSignUpNotification"></a>  

$MadelineProto->[account->getNotifyExceptions](account_getNotifyExceptions.md)(\['compare_sound' => [Bool](../types/Bool.md), 'peer' => [InputNotifyPeer](../types/InputNotifyPeer.md), \]) === [$Updates](../types/Updates.md)<a name="account_getNotifyExceptions"></a>  

$MadelineProto->[account->getNotifySettings](account_getNotifySettings.md)(\['peer' => [InputNotifyPeer](../types/InputNotifyPeer.md), \]) === [$PeerNotifySettings](../types/PeerNotifySettings.md)<a name="account_getNotifySettings"></a>  

$MadelineProto->[account->getPassword](account_getPassword.md)(\[\]) === [$account\_Password](../types/account_Password.md)<a name="account_getPassword"></a>  

$MadelineProto->[account->getPasswordSettings](account_getPasswordSettings.md)(\['password' => [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md), \]) === [$account\_PasswordSettings](../types/account_PasswordSettings.md)<a name="account_getPasswordSettings"></a>  

$MadelineProto->[account->getPrivacy](account_getPrivacy.md)(\['key' => [InputPrivacyKey](../types/InputPrivacyKey.md), \]) === [$account\_PrivacyRules](../types/account_PrivacyRules.md)<a name="account_getPrivacy"></a>  

$MadelineProto->[account->getSecureValue](account_getSecureValue.md)(\['types' => \[[SecureValueType](../types/SecureValueType.md)\], \]) === [$Vector\_of\_SecureValue](../types/SecureValue.md)<a name="account_getSecureValue"></a>  

$MadelineProto->[account->getTmpPassword](account_getTmpPassword.md)(\['password' => [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md), 'period' => [int](../types/int.md), \]) === [$account\_TmpPassword](../types/account_TmpPassword.md)<a name="account_getTmpPassword"></a>  

$MadelineProto->[account->getWallPaper](account_getWallPaper.md)(\['wallpaper' => [InputWallPaper](../types/InputWallPaper.md), \]) === [$WallPaper](../types/WallPaper.md)<a name="account_getWallPaper"></a>  

$MadelineProto->[account->getWallPapers](account_getWallPapers.md)(\['hash' => [int](../types/int.md), \]) === [$account\_WallPapers](../types/account_WallPapers.md)<a name="account_getWallPapers"></a>  

$MadelineProto->[account->getWebAuthorizations](account_getWebAuthorizations.md)(\[\]) === [$account\_WebAuthorizations](../types/account_WebAuthorizations.md)<a name="account_getWebAuthorizations"></a>  

$MadelineProto->[account->initTakeoutSession](account_initTakeoutSession.md)(\['contacts' => [Bool](../types/Bool.md), 'message_users' => [Bool](../types/Bool.md), 'message_chats' => [Bool](../types/Bool.md), 'message_megagroups' => [Bool](../types/Bool.md), 'message_channels' => [Bool](../types/Bool.md), 'files' => [Bool](../types/Bool.md), 'file_max_size' => [int](../types/int.md), \]) === [$account\_Takeout](../types/account_Takeout.md)<a name="account_initTakeoutSession"></a>  

$MadelineProto->[account->installWallPaper](account_installWallPaper.md)(\['wallpaper' => [InputWallPaper](../types/InputWallPaper.md), 'settings' => [WallPaperSettings](../types/WallPaperSettings.md), \]) === [$Bool](../types/Bool.md)<a name="account_installWallPaper"></a>  

$MadelineProto->[account->registerDevice](account_registerDevice.md)(\['token_type' => [int](../types/int.md), 'token' => [string](../types/string.md), 'app_sandbox' => [Bool](../types/Bool.md), 'secret' => [bytes](../types/bytes.md), 'other_uids' => \[[int](../types/int.md)\], \]) === [$Bool](../types/Bool.md)<a name="account_registerDevice"></a>  

$MadelineProto->[account->reportPeer](account_reportPeer.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'reason' => [ReportReason](../types/ReportReason.md), \]) === [$Bool](../types/Bool.md)<a name="account_reportPeer"></a>  

$MadelineProto->[account->resendPasswordEmail](account_resendPasswordEmail.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account_resendPasswordEmail"></a>  

$MadelineProto->[account->resetAuthorization](account_resetAuthorization.md)(\['hash' => [long](../types/long.md), \]) === [$Bool](../types/Bool.md)<a name="account_resetAuthorization"></a>  

$MadelineProto->[account->resetNotifySettings](account_resetNotifySettings.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account_resetNotifySettings"></a>  

$MadelineProto->[account->resetWallPapers](account_resetWallPapers.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account_resetWallPapers"></a>  

$MadelineProto->[account->resetWebAuthorization](account_resetWebAuthorization.md)(\['hash' => [long](../types/long.md), \]) === [$Bool](../types/Bool.md)<a name="account_resetWebAuthorization"></a>  

$MadelineProto->[account->resetWebAuthorizations](account_resetWebAuthorizations.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account_resetWebAuthorizations"></a>  

$MadelineProto->[account->saveAutoDownloadSettings](account_saveAutoDownloadSettings.md)(\['low' => [Bool](../types/Bool.md), 'high' => [Bool](../types/Bool.md), 'settings' => [AutoDownloadSettings](../types/AutoDownloadSettings.md), \]) === [$Bool](../types/Bool.md)<a name="account_saveAutoDownloadSettings"></a>  

$MadelineProto->[account->saveSecureValue](account_saveSecureValue.md)(\['value' => [InputSecureValue](../types/InputSecureValue.md), 'secure_secret_id' => [long](../types/long.md), \]) === [$SecureValue](../types/SecureValue.md)<a name="account_saveSecureValue"></a>  

$MadelineProto->[account->saveWallPaper](account_saveWallPaper.md)(\['wallpaper' => [InputWallPaper](../types/InputWallPaper.md), 'unsave' => [Bool](../types/Bool.md), 'settings' => [WallPaperSettings](../types/WallPaperSettings.md), \]) === [$Bool](../types/Bool.md)<a name="account_saveWallPaper"></a>  

$MadelineProto->[account->sendChangePhoneCode](account_sendChangePhoneCode.md)(\['phone_number' => [string](../types/string.md), 'settings' => [CodeSettings](../types/CodeSettings.md), \]) === [$auth\_SentCode](../types/auth_SentCode.md)<a name="account_sendChangePhoneCode"></a>  

$MadelineProto->[account->sendConfirmPhoneCode](account_sendConfirmPhoneCode.md)(\['hash' => [string](../types/string.md), 'settings' => [CodeSettings](../types/CodeSettings.md), \]) === [$auth\_SentCode](../types/auth_SentCode.md)<a name="account_sendConfirmPhoneCode"></a>  

$MadelineProto->[account->sendVerifyEmailCode](account_sendVerifyEmailCode.md)(\['email' => [string](../types/string.md), \]) === [$account\_SentEmailCode](../types/account_SentEmailCode.md)<a name="account_sendVerifyEmailCode"></a>  

$MadelineProto->[account->sendVerifyPhoneCode](account_sendVerifyPhoneCode.md)(\['phone_number' => [string](../types/string.md), 'settings' => [CodeSettings](../types/CodeSettings.md), \]) === [$auth\_SentCode](../types/auth_SentCode.md)<a name="account_sendVerifyPhoneCode"></a>  

$MadelineProto->[account->setAccountTTL](account_setAccountTTL.md)(\['ttl' => [AccountDaysTTL](../types/AccountDaysTTL.md), \]) === [$Bool](../types/Bool.md)<a name="account_setAccountTTL"></a>  

$MadelineProto->[account->setContactSignUpNotification](account_setContactSignUpNotification.md)(\['silent' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="account_setContactSignUpNotification"></a>  

$MadelineProto->[account->setPrivacy](account_setPrivacy.md)(\['key' => [InputPrivacyKey](../types/InputPrivacyKey.md), 'rules' => \[[InputPrivacyRule](../types/InputPrivacyRule.md)\], \]) === [$account\_PrivacyRules](../types/account_PrivacyRules.md)<a name="account_setPrivacy"></a>  

$MadelineProto->[account->unregisterDevice](account_unregisterDevice.md)(\['token_type' => [int](../types/int.md), 'token' => [string](../types/string.md), 'other_uids' => \[[int](../types/int.md)\], \]) === [$Bool](../types/Bool.md)<a name="account_unregisterDevice"></a>  

$MadelineProto->[account->updateDeviceLocked](account_updateDeviceLocked.md)(\['period' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="account_updateDeviceLocked"></a>  

$MadelineProto->[account->updateNotifySettings](account_updateNotifySettings.md)(\['peer' => [InputNotifyPeer](../types/InputNotifyPeer.md), 'settings' => [InputPeerNotifySettings](../types/InputPeerNotifySettings.md), \]) === [$Bool](../types/Bool.md)<a name="account_updateNotifySettings"></a>  

$MadelineProto->[account->updatePasswordSettings](account_updatePasswordSettings.md)(\['password' => [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md), 'new_settings' => [account\_PasswordInputSettings](../types/account_PasswordInputSettings.md), \]) === [$Bool](../types/Bool.md)<a name="account_updatePasswordSettings"></a>  

$MadelineProto->[account->updateProfile](account_updateProfile.md)(\['first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'about' => [string](../types/string.md), \]) === [$User](../types/User.md)<a name="account_updateProfile"></a>  

$MadelineProto->[account->updateStatus](account_updateStatus.md)(\['offline' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="account_updateStatus"></a>  

$MadelineProto->[account->updateUsername](account_updateUsername.md)(\['username' => [string](../types/string.md), \]) === [$User](../types/User.md)<a name="account_updateUsername"></a>  

$MadelineProto->[account->uploadWallPaper](account_uploadWallPaper.md)(\['file' => [InputFile](../types/InputFile.md), 'mime_type' => [string](../types/string.md), 'settings' => [WallPaperSettings](../types/WallPaperSettings.md), \]) === [$WallPaper](../types/WallPaper.md)<a name="account_uploadWallPaper"></a>  

$MadelineProto->[account->verifyEmail](account_verifyEmail.md)(\['email' => [string](../types/string.md), 'code' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account_verifyEmail"></a>  

$MadelineProto->[account->verifyPhone](account_verifyPhone.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), 'phone_code' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account_verifyPhone"></a>  

***
<br><br>
$MadelineProto->[auth->bindTempAuthKey](auth_bindTempAuthKey.md)(\['perm_auth_key_id' => [long](../types/long.md), 'nonce' => [long](../types/long.md), 'expires_at' => [int](../types/int.md), 'encrypted_message' => [bytes](../types/bytes.md), \]) === [$Bool](../types/Bool.md)<a name="auth_bindTempAuthKey"></a>  

$MadelineProto->[auth->cancelCode](auth_cancelCode.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="auth_cancelCode"></a>  

$MadelineProto->[auth->checkPassword](auth_checkPassword.md)(\['password' => [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md), \]) === [$auth\_Authorization](../types/auth_Authorization.md)<a name="auth_checkPassword"></a>  

$MadelineProto->[auth->dropTempAuthKeys](auth_dropTempAuthKeys.md)(\['except_auth_keys' => \[[long](../types/long.md)\], \]) === [$Bool](../types/Bool.md)<a name="auth_dropTempAuthKeys"></a>  

$MadelineProto->[auth->exportAuthorization](auth_exportAuthorization.md)(\['dc_id' => [int](../types/int.md), \]) === [$auth\_ExportedAuthorization](../types/auth_ExportedAuthorization.md)<a name="auth_exportAuthorization"></a>  

$MadelineProto->[auth->importAuthorization](auth_importAuthorization.md)(\['id' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \]) === [$auth\_Authorization](../types/auth_Authorization.md)<a name="auth_importAuthorization"></a>  

$MadelineProto->[auth->importBotAuthorization](auth_importBotAuthorization.md)(\['api_id' => [int](../types/int.md), 'api_hash' => [string](../types/string.md), 'bot_auth_token' => [string](../types/string.md), \]) === [$auth\_Authorization](../types/auth_Authorization.md)<a name="auth_importBotAuthorization"></a>  

$MadelineProto->[auth->logOut](auth_logOut.md)(\[\]) === [$Bool](../types/Bool.md)<a name="auth_logOut"></a>  

$MadelineProto->[auth->recoverPassword](auth_recoverPassword.md)(\['code' => [string](../types/string.md), \]) === [$auth\_Authorization](../types/auth_Authorization.md)<a name="auth_recoverPassword"></a>  

$MadelineProto->[auth->requestPasswordRecovery](auth_requestPasswordRecovery.md)(\[\]) === [$auth\_PasswordRecovery](../types/auth_PasswordRecovery.md)<a name="auth_requestPasswordRecovery"></a>  

$MadelineProto->[auth->resendCode](auth_resendCode.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), \]) === [$auth\_SentCode](../types/auth_SentCode.md)<a name="auth_resendCode"></a>  

$MadelineProto->[auth->resetAuthorizations](auth_resetAuthorizations.md)(\[\]) === [$Bool](../types/Bool.md)<a name="auth_resetAuthorizations"></a>  

$MadelineProto->[auth->sendCode](auth_sendCode.md)(\['phone_number' => [string](../types/string.md), 'api_id' => [int](../types/int.md), 'api_hash' => [string](../types/string.md), 'settings' => [CodeSettings](../types/CodeSettings.md), \]) === [$auth\_SentCode](../types/auth_SentCode.md)<a name="auth_sendCode"></a>  

$MadelineProto->[auth->signIn](auth_signIn.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), 'phone_code' => [string](../types/string.md), \]) === [$auth\_Authorization](../types/auth_Authorization.md)<a name="auth_signIn"></a>  

$MadelineProto->[auth->signUp](auth_signUp.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), 'phone_code' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), \]) === [$auth\_Authorization](../types/auth_Authorization.md)<a name="auth_signUp"></a>  

***
<br><br>
$MadelineProto->[bots->answerWebhookJSONQuery](bots_answerWebhookJSONQuery.md)(\['query_id' => [long](../types/long.md), 'data' => [DataJSON](../types/DataJSON.md), \]) === [$Bool](../types/Bool.md)<a name="bots_answerWebhookJSONQuery"></a>  

$MadelineProto->[bots->sendCustomRequest](bots_sendCustomRequest.md)(\['custom_method' => [string](../types/string.md), 'params' => [DataJSON](../types/DataJSON.md), \]) === [$DataJSON](../types/DataJSON.md)<a name="bots_sendCustomRequest"></a>  

***
<br><br>
$MadelineProto->[channels->checkUsername](channels_checkUsername.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'username' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="channels_checkUsername"></a>  

$MadelineProto->[channels->createChannel](channels_createChannel.md)(\['broadcast' => [Bool](../types/Bool.md), 'megagroup' => [Bool](../types/Bool.md), 'title' => [string](../types/string.md), 'about' => [string](../types/string.md), 'geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'address' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="channels_createChannel"></a>  

$MadelineProto->[channels->deleteChannel](channels_deleteChannel.md)(\['channel' => [InputChannel](../types/InputChannel.md), \]) === [$Updates](../types/Updates.md)<a name="channels_deleteChannel"></a>  

$MadelineProto->[channels->deleteHistory](channels_deleteHistory.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'max_id' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="channels_deleteHistory"></a>  

$MadelineProto->[channels->deleteMessages](channels_deleteMessages.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'id' => \[[int](../types/int.md)\], \]) === [$messages\_AffectedMessages](../types/messages_AffectedMessages.md)<a name="channels_deleteMessages"></a>  

$MadelineProto->[channels->deleteUserHistory](channels_deleteUserHistory.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), \]) === [$messages\_AffectedHistory](../types/messages_AffectedHistory.md)<a name="channels_deleteUserHistory"></a>  

$MadelineProto->[channels->editAdmin](channels_editAdmin.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), 'admin_rights' => [ChatAdminRights](../types/ChatAdminRights.md), \]) === [$Updates](../types/Updates.md)<a name="channels_editAdmin"></a>  

$MadelineProto->[channels->editBanned](channels_editBanned.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), 'banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), \]) === [$Updates](../types/Updates.md)<a name="channels_editBanned"></a>  

$MadelineProto->[channels->editCreator](channels_editCreator.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), 'password' => [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md), \]) === [$Updates](../types/Updates.md)<a name="channels_editCreator"></a>  

$MadelineProto->[channels->editLocation](channels_editLocation.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'address' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="channels_editLocation"></a>  

$MadelineProto->[channels->editPhoto](channels_editPhoto.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'photo' => [InputChatPhoto](../types/InputChatPhoto.md), \]) === [$Updates](../types/Updates.md)<a name="channels_editPhoto"></a>  

$MadelineProto->[channels->editTitle](channels_editTitle.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'title' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="channels_editTitle"></a>  

$MadelineProto->[channels->exportMessageLink](channels_exportMessageLink.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'id' => [int](../types/int.md), 'grouped' => [Bool](../types/Bool.md), \]) === [$ExportedMessageLink](../types/ExportedMessageLink.md)<a name="channels_exportMessageLink"></a>  

$MadelineProto->[channels->getAdminLog](channels_getAdminLog.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'q' => [string](../types/string.md), 'events_filter' => [ChannelAdminLogEventsFilter](../types/ChannelAdminLogEventsFilter.md), 'admins' => \[[InputUser](../types/InputUser.md)\], 'max_id' => [long](../types/long.md), 'min_id' => [long](../types/long.md), 'limit' => [int](../types/int.md), \]) === [$channels\_AdminLogResults](../types/channels_AdminLogResults.md)<a name="channels_getAdminLog"></a>  

$MadelineProto->[channels->getAdminedPublicChannels](channels_getAdminedPublicChannels.md)(\['by_location' => [Bool](../types/Bool.md), 'check_limit' => [Bool](../types/Bool.md), \]) === [$messages\_Chats](../types/messages_Chats.md)<a name="channels_getAdminedPublicChannels"></a>  

$MadelineProto->[channels->getChannels](channels_getChannels.md)(\['id' => \[[InputChannel](../types/InputChannel.md)\], \]) === [$messages\_Chats](../types/messages_Chats.md)<a name="channels_getChannels"></a>  

$MadelineProto->[channels->getFullChannel](channels_getFullChannel.md)(\['channel' => [InputChannel](../types/InputChannel.md), \]) === [$messages\_ChatFull](../types/messages_ChatFull.md)<a name="channels_getFullChannel"></a>  

$MadelineProto->[channels->getGroupsForDiscussion](channels_getGroupsForDiscussion.md)(\[\]) === [$messages\_Chats](../types/messages_Chats.md)<a name="channels_getGroupsForDiscussion"></a>  

$MadelineProto->[channels->getLeftChannels](channels_getLeftChannels.md)(\['offset' => [int](../types/int.md), \]) === [$messages\_Chats](../types/messages_Chats.md)<a name="channels_getLeftChannels"></a>  

$MadelineProto->[channels->getMessages](channels_getMessages.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'id' => \[[InputMessage](../types/InputMessage.md)\], \]) === [$messages\_Messages](../types/messages_Messages.md)<a name="channels_getMessages"></a>  

$MadelineProto->[channels->getParticipant](channels_getParticipant.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), \]) === [$channels\_ChannelParticipant](../types/channels_ChannelParticipant.md)<a name="channels_getParticipant"></a>  

$MadelineProto->[channels->getParticipants](channels_getParticipants.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'filter' => [ChannelParticipantsFilter](../types/ChannelParticipantsFilter.md), 'offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$channels\_ChannelParticipants](../types/channels_ChannelParticipants.md)<a name="channels_getParticipants"></a>  

$MadelineProto->[channels->inviteToChannel](channels_inviteToChannel.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'users' => \[[InputUser](../types/InputUser.md)\], \]) === [$Updates](../types/Updates.md)<a name="channels_inviteToChannel"></a>  

$MadelineProto->[channels->joinChannel](channels_joinChannel.md)(\['channel' => [InputChannel](../types/InputChannel.md), \]) === [$Updates](../types/Updates.md)<a name="channels_joinChannel"></a>  

$MadelineProto->[channels->leaveChannel](channels_leaveChannel.md)(\['channel' => [InputChannel](../types/InputChannel.md), \]) === [$Updates](../types/Updates.md)<a name="channels_leaveChannel"></a>  

$MadelineProto->[channels->readHistory](channels_readHistory.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'max_id' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="channels_readHistory"></a>  

$MadelineProto->[channels->readMessageContents](channels_readMessageContents.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'id' => \[[int](../types/int.md)\], \]) === [$Bool](../types/Bool.md)<a name="channels_readMessageContents"></a>  

$MadelineProto->[channels->reportSpam](channels_reportSpam.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), 'id' => \[[int](../types/int.md)\], \]) === [$Bool](../types/Bool.md)<a name="channels_reportSpam"></a>  

$MadelineProto->[channels->setDiscussionGroup](channels_setDiscussionGroup.md)(\['broadcast' => [InputChannel](../types/InputChannel.md), 'group' => [InputChannel](../types/InputChannel.md), \]) === [$Bool](../types/Bool.md)<a name="channels_setDiscussionGroup"></a>  

$MadelineProto->[channels->setStickers](channels_setStickers.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'stickerset' => [InputStickerSet](../types/InputStickerSet.md), \]) === [$Bool](../types/Bool.md)<a name="channels_setStickers"></a>  

$MadelineProto->[channels->togglePreHistoryHidden](channels_togglePreHistoryHidden.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'enabled' => [Bool](../types/Bool.md), \]) === [$Updates](../types/Updates.md)<a name="channels_togglePreHistoryHidden"></a>  

$MadelineProto->[channels->toggleSignatures](channels_toggleSignatures.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'enabled' => [Bool](../types/Bool.md), \]) === [$Updates](../types/Updates.md)<a name="channels_toggleSignatures"></a>  

$MadelineProto->[channels->updateUsername](channels_updateUsername.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'username' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="channels_updateUsername"></a>  

***
<br><br>
$MadelineProto->[contacts->acceptContact](contacts_acceptContact.md)(\['id' => [InputUser](../types/InputUser.md), \]) === [$Updates](../types/Updates.md)<a name="contacts_acceptContact"></a>  

$MadelineProto->[contacts->addContact](contacts_addContact.md)(\['add_phone_privacy_exception' => [Bool](../types/Bool.md), 'id' => [InputUser](../types/InputUser.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'phone' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="contacts_addContact"></a>  

$MadelineProto->[contacts->block](contacts_block.md)(\['id' => [InputUser](../types/InputUser.md), \]) === [$Bool](../types/Bool.md)<a name="contacts_block"></a>  

$MadelineProto->[contacts->deleteByPhones](contacts_deleteByPhones.md)(\['phones' => \[[string](../types/string.md)\], \]) === [$Bool](../types/Bool.md)<a name="contacts_deleteByPhones"></a>  

$MadelineProto->[contacts->deleteContacts](contacts_deleteContacts.md)(\['id' => \[[InputUser](../types/InputUser.md)\], \]) === [$Updates](../types/Updates.md)<a name="contacts_deleteContacts"></a>  

$MadelineProto->[contacts->getBlocked](contacts_getBlocked.md)(\['offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$contacts\_Blocked](../types/contacts_Blocked.md)<a name="contacts_getBlocked"></a>  

$MadelineProto->[contacts->getContactIDs](contacts_getContactIDs.md)(\['hash' => [int](../types/int.md), \]) === [$Vector\_of\_int](../types/int.md)<a name="contacts_getContactIDs"></a>  

$MadelineProto->[contacts->getContacts](contacts_getContacts.md)(\['hash' => [int](../types/int.md), \]) === [$contacts\_Contacts](../types/contacts_Contacts.md)<a name="contacts_getContacts"></a>  

$MadelineProto->[contacts->getLocated](contacts_getLocated.md)(\['geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), \]) === [$Updates](../types/Updates.md)<a name="contacts_getLocated"></a>  

$MadelineProto->[contacts->getSaved](contacts_getSaved.md)(\[\]) === [$Vector\_of\_SavedContact](../types/SavedContact.md)<a name="contacts_getSaved"></a>  

$MadelineProto->[contacts->getStatuses](contacts_getStatuses.md)(\[\]) === [$Vector\_of\_ContactStatus](../types/ContactStatus.md)<a name="contacts_getStatuses"></a>  

$MadelineProto->[contacts->getTopPeers](contacts_getTopPeers.md)(\['correspondents' => [Bool](../types/Bool.md), 'bots_pm' => [Bool](../types/Bool.md), 'bots_inline' => [Bool](../types/Bool.md), 'phone_calls' => [Bool](../types/Bool.md), 'forward_users' => [Bool](../types/Bool.md), 'forward_chats' => [Bool](../types/Bool.md), 'groups' => [Bool](../types/Bool.md), 'channels' => [Bool](../types/Bool.md), 'offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$contacts\_TopPeers](../types/contacts_TopPeers.md)<a name="contacts_getTopPeers"></a>  

$MadelineProto->[contacts->importContacts](contacts_importContacts.md)(\['contacts' => \[[InputContact](../types/InputContact.md)\], \]) === [$contacts\_ImportedContacts](../types/contacts_ImportedContacts.md)<a name="contacts_importContacts"></a>  

$MadelineProto->[contacts->resetSaved](contacts_resetSaved.md)(\[\]) === [$Bool](../types/Bool.md)<a name="contacts_resetSaved"></a>  

$MadelineProto->[contacts->resetTopPeerRating](contacts_resetTopPeerRating.md)(\['category' => [TopPeerCategory](../types/TopPeerCategory.md), 'peer' => [InputPeer](../types/InputPeer.md), \]) === [$Bool](../types/Bool.md)<a name="contacts_resetTopPeerRating"></a>  

$MadelineProto->[contacts->resolveUsername](contacts_resolveUsername.md)(\['username' => [string](../types/string.md), \]) === [$contacts\_ResolvedPeer](../types/contacts_ResolvedPeer.md)<a name="contacts_resolveUsername"></a>  

$MadelineProto->[contacts->search](contacts_search.md)(\['q' => [string](../types/string.md), 'limit' => [int](../types/int.md), \]) === [$contacts\_Found](../types/contacts_Found.md)<a name="contacts_search"></a>  

$MadelineProto->[contacts->toggleTopPeers](contacts_toggleTopPeers.md)(\['enabled' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="contacts_toggleTopPeers"></a>  

$MadelineProto->[contacts->unblock](contacts_unblock.md)(\['id' => [InputUser](../types/InputUser.md), \]) === [$Bool](../types/Bool.md)<a name="contacts_unblock"></a>  

***
<br><br>
$MadelineProto->[folders->deleteFolder](folders_deleteFolder.md)(\['folder_id' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="folders_deleteFolder"></a>  

$MadelineProto->[folders->editPeerFolders](folders_editPeerFolders.md)(\['folder_peers' => \[[InputFolderPeer](../types/InputFolderPeer.md)\], \]) === [$Updates](../types/Updates.md)<a name="folders_editPeerFolders"></a>  

***
<br><br>
$MadelineProto->[help->acceptTermsOfService](help_acceptTermsOfService.md)(\['id' => [DataJSON](../types/DataJSON.md), \]) === [$Bool](../types/Bool.md)<a name="help_acceptTermsOfService"></a>  

$MadelineProto->[help->editUserInfo](help_editUserInfo.md)(\['user_id' => [InputUser](../types/InputUser.md), 'message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \]) === [$help\_UserInfo](../types/help_UserInfo.md)<a name="help_editUserInfo"></a>  

$MadelineProto->[help->getAppChangelog](help_getAppChangelog.md)(\['prev_app_version' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="help_getAppChangelog"></a>  

$MadelineProto->[help->getAppConfig](help_getAppConfig.md)(\[\]) === [$JSONValue](../types/JSONValue.md)<a name="help_getAppConfig"></a>  

$MadelineProto->[help->getAppUpdate](help_getAppUpdate.md)(\['source' => [string](../types/string.md), \]) === [$help\_AppUpdate](../types/help_AppUpdate.md)<a name="help_getAppUpdate"></a>  

$MadelineProto->[help->getCdnConfig](help_getCdnConfig.md)(\[\]) === [$CdnConfig](../types/CdnConfig.md)<a name="help_getCdnConfig"></a>  

$MadelineProto->[help->getConfig](help_getConfig.md)(\[\]) === [$Config](../types/Config.md)<a name="help_getConfig"></a>  

$MadelineProto->[help->getDeepLinkInfo](help_getDeepLinkInfo.md)(\['path' => [string](../types/string.md), \]) === [$help\_DeepLinkInfo](../types/help_DeepLinkInfo.md)<a name="help_getDeepLinkInfo"></a>  

$MadelineProto->[help->getInviteText](help_getInviteText.md)(\[\]) === [$help\_InviteText](../types/help_InviteText.md)<a name="help_getInviteText"></a>  

$MadelineProto->[help->getNearestDc](help_getNearestDc.md)(\[\]) === [$NearestDc](../types/NearestDc.md)<a name="help_getNearestDc"></a>  

$MadelineProto->[help->getPassportConfig](help_getPassportConfig.md)(\['hash' => [int](../types/int.md), \]) === [$help\_PassportConfig](../types/help_PassportConfig.md)<a name="help_getPassportConfig"></a>  

$MadelineProto->[help->getProxyData](help_getProxyData.md)(\[\]) === [$help\_ProxyData](../types/help_ProxyData.md)<a name="help_getProxyData"></a>  

$MadelineProto->[help->getRecentMeUrls](help_getRecentMeUrls.md)(\['referer' => [string](../types/string.md), \]) === [$help\_RecentMeUrls](../types/help_RecentMeUrls.md)<a name="help_getRecentMeUrls"></a>  

$MadelineProto->[help->getSupport](help_getSupport.md)(\[\]) === [$help\_Support](../types/help_Support.md)<a name="help_getSupport"></a>  

$MadelineProto->[help->getSupportName](help_getSupportName.md)(\[\]) === [$help\_SupportName](../types/help_SupportName.md)<a name="help_getSupportName"></a>  

$MadelineProto->[help->getTermsOfServiceUpdate](help_getTermsOfServiceUpdate.md)(\[\]) === [$help\_TermsOfServiceUpdate](../types/help_TermsOfServiceUpdate.md)<a name="help_getTermsOfServiceUpdate"></a>  

$MadelineProto->[help->getUserInfo](help_getUserInfo.md)(\['user_id' => [InputUser](../types/InputUser.md), \]) === [$help\_UserInfo](../types/help_UserInfo.md)<a name="help_getUserInfo"></a>  

$MadelineProto->[help->saveAppLog](help_saveAppLog.md)(\['events' => \[[InputAppEvent](../types/InputAppEvent.md)\], \]) === [$Bool](../types/Bool.md)<a name="help_saveAppLog"></a>  

$MadelineProto->[help->setBotUpdatesStatus](help_setBotUpdatesStatus.md)(\['pending_updates_count' => [int](../types/int.md), 'message' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="help_setBotUpdatesStatus"></a>  

***
<br><br>
$MadelineProto->[initConnection](initConnection.md)(\['api_id' => [int](../types/int.md), 'device_model' => [string](../types/string.md), 'system_version' => [string](../types/string.md), 'app_version' => [string](../types/string.md), 'system_lang_code' => [string](../types/string.md), 'lang_pack' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), 'proxy' => [InputClientProxy](../types/InputClientProxy.md), 'query' => [!X](../types/!X.md), \]) === [$X](../types/X.md)<a name="initConnection"></a>  

***
<br><br>
$MadelineProto->[invokeAfterMsg](invokeAfterMsg.md)(\['msg_id' => [long](../types/long.md), 'query' => [!X](../types/!X.md), \]) === [$X](../types/X.md)<a name="invokeAfterMsg"></a>  

***
<br><br>
$MadelineProto->[invokeAfterMsgs](invokeAfterMsgs.md)(\['msg_ids' => \[[long](../types/long.md)\], 'query' => [!X](../types/!X.md), \]) === [$X](../types/X.md)<a name="invokeAfterMsgs"></a>  

***
<br><br>
$MadelineProto->[invokeWithLayer](invokeWithLayer.md)(\['layer' => [int](../types/int.md), 'query' => [!X](../types/!X.md), \]) === [$X](../types/X.md)<a name="invokeWithLayer"></a>  

***
<br><br>
$MadelineProto->[invokeWithMessagesRange](invokeWithMessagesRange.md)(\['range' => [MessageRange](../types/MessageRange.md), 'query' => [!X](../types/!X.md), \]) === [$X](../types/X.md)<a name="invokeWithMessagesRange"></a>  

***
<br><br>
$MadelineProto->[invokeWithTakeout](invokeWithTakeout.md)(\['takeout_id' => [long](../types/long.md), 'query' => [!X](../types/!X.md), \]) === [$X](../types/X.md)<a name="invokeWithTakeout"></a>  

***
<br><br>
$MadelineProto->[invokeWithoutUpdates](invokeWithoutUpdates.md)(\['query' => [!X](../types/!X.md), \]) === [$X](../types/X.md)<a name="invokeWithoutUpdates"></a>  

***
<br><br>
$MadelineProto->[langpack->getDifference](langpack_getDifference.md)(\['lang_pack' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), 'from_version' => [int](../types/int.md), \]) === [$LangPackDifference](../types/LangPackDifference.md)<a name="langpack_getDifference"></a>  

$MadelineProto->[langpack->getLangPack](langpack_getLangPack.md)(\['lang_pack' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), \]) === [$LangPackDifference](../types/LangPackDifference.md)<a name="langpack_getLangPack"></a>  

$MadelineProto->[langpack->getLanguage](langpack_getLanguage.md)(\['lang_pack' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), \]) === [$LangPackLanguage](../types/LangPackLanguage.md)<a name="langpack_getLanguage"></a>  

$MadelineProto->[langpack->getLanguages](langpack_getLanguages.md)(\['lang_pack' => [string](../types/string.md), \]) === [$Vector\_of\_LangPackLanguage](../types/LangPackLanguage.md)<a name="langpack_getLanguages"></a>  

$MadelineProto->[langpack->getStrings](langpack_getStrings.md)(\['lang_pack' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), 'keys' => \[[string](../types/string.md)\], \]) === [$Vector\_of\_LangPackString](../types/LangPackString.md)<a name="langpack_getStrings"></a>  

***
<br><br>
$MadelineProto->[messages->acceptEncryption](messages_acceptEncryption.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'g_b' => [bytes](../types/bytes.md), 'key_fingerprint' => [long](../types/long.md), \]) === [$EncryptedChat](../types/EncryptedChat.md)<a name="messages_acceptEncryption"></a>  

$MadelineProto->[messages->acceptUrlAuth](messages_acceptUrlAuth.md)(\['write_allowed' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'button_id' => [int](../types/int.md), \]) === [$UrlAuthResult](../types/UrlAuthResult.md)<a name="messages_acceptUrlAuth"></a>  

$MadelineProto->[messages->addChatUser](messages_addChatUser.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), 'user_id' => [InputUser](../types/InputUser.md), 'fwd_limit' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages_addChatUser"></a>  

$MadelineProto->[messages->checkChatInvite](messages_checkChatInvite.md)(\['hash' => [string](../types/string.md), \]) === [$ChatInvite](../types/ChatInvite.md)<a name="messages_checkChatInvite"></a>  

$MadelineProto->[messages->clearAllDrafts](messages_clearAllDrafts.md)(\[\]) === [$Bool](../types/Bool.md)<a name="messages_clearAllDrafts"></a>  

$MadelineProto->[messages->clearRecentStickers](messages_clearRecentStickers.md)(\['attached' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages_clearRecentStickers"></a>  

$MadelineProto->[messages->createChat](messages_createChat.md)(\['users' => \[[InputUser](../types/InputUser.md)\], 'title' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="messages_createChat"></a>  

$MadelineProto->[messages->deleteChatUser](messages_deleteChatUser.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), 'user_id' => [InputUser](../types/InputUser.md), \]) === [$Updates](../types/Updates.md)<a name="messages_deleteChatUser"></a>  

$MadelineProto->[messages->deleteHistory](messages_deleteHistory.md)(\['just_clear' => [Bool](../types/Bool.md), 'revoke' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'max_id' => [int](../types/int.md), \]) === [$messages\_AffectedHistory](../types/messages_AffectedHistory.md)<a name="messages_deleteHistory"></a>  

$MadelineProto->[messages->deleteMessages](messages_deleteMessages.md)(\['revoke' => [Bool](../types/Bool.md), 'id' => \[[int](../types/int.md)\], \]) === [$messages\_AffectedMessages](../types/messages_AffectedMessages.md)<a name="messages_deleteMessages"></a>  

$MadelineProto->[messages->discardEncryption](messages_discardEncryption.md)(\['chat_id' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="messages_discardEncryption"></a>  

$MadelineProto->[messages->editChatAbout](messages_editChatAbout.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'about' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="messages_editChatAbout"></a>  

$MadelineProto->[messages->editChatAdmin](messages_editChatAdmin.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), 'user_id' => [InputUser](../types/InputUser.md), 'is_admin' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages_editChatAdmin"></a>  

$MadelineProto->[messages->editChatDefaultBannedRights](messages_editChatDefaultBannedRights.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), \]) === [$Updates](../types/Updates.md)<a name="messages_editChatDefaultBannedRights"></a>  

$MadelineProto->[messages->editChatPhoto](messages_editChatPhoto.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), 'photo' => [InputChatPhoto](../types/InputChatPhoto.md), \]) === [$Updates](../types/Updates.md)<a name="messages_editChatPhoto"></a>  

$MadelineProto->[messages->editChatTitle](messages_editChatTitle.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), 'title' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="messages_editChatTitle"></a>  

$MadelineProto->[messages->editInlineBotMessage](messages_editInlineBotMessage.md)(\['no_webpage' => [Bool](../types/Bool.md), 'id' => [InputBotInlineMessageID](../types/InputBotInlineMessageID.md), 'message' => [string](../types/string.md), 'media' => [InputMedia](../types/InputMedia.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages_editInlineBotMessage"></a>  

$MadelineProto->[messages->editMessage](messages_editMessage.md)(\['no_webpage' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'id' => [int](../types/int.md), 'message' => [string](../types/string.md), 'media' => [InputMedia](../types/InputMedia.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \]) === [$Updates](../types/Updates.md)<a name="messages_editMessage"></a>  

$MadelineProto->[messages->exportChatInvite](messages_exportChatInvite.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$ExportedChatInvite](../types/ExportedChatInvite.md)<a name="messages_exportChatInvite"></a>  

$MadelineProto->[messages->faveSticker](messages_faveSticker.md)(\['id' => [InputDocument](../types/InputDocument.md), 'unfave' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages_faveSticker"></a>  

$MadelineProto->[messages->forwardMessages](messages_forwardMessages.md)(\['silent' => [Bool](../types/Bool.md), 'background' => [Bool](../types/Bool.md), 'with_my_score' => [Bool](../types/Bool.md), 'grouped' => [Bool](../types/Bool.md), 'from_peer' => [InputPeer](../types/InputPeer.md), 'id' => \[[int](../types/int.md)\], 'to_peer' => [InputPeer](../types/InputPeer.md), \]) === [$Updates](../types/Updates.md)<a name="messages_forwardMessages"></a>  

$MadelineProto->[messages->getAllChats](messages_getAllChats.md)(\['except_ids' => \[[int](../types/int.md)\], \]) === [$messages\_Chats](../types/messages_Chats.md)<a name="messages_getAllChats"></a>  

$MadelineProto->[messages->getAllDrafts](messages_getAllDrafts.md)(\[\]) === [$Updates](../types/Updates.md)<a name="messages_getAllDrafts"></a>  

$MadelineProto->[messages->getAllStickers](messages_getAllStickers.md)(\['hash' => [int](../types/int.md), \]) === [$messages\_AllStickers](../types/messages_AllStickers.md)<a name="messages_getAllStickers"></a>  

$MadelineProto->[messages->getArchivedStickers](messages_getArchivedStickers.md)(\['masks' => [Bool](../types/Bool.md), 'offset_id' => [long](../types/long.md), 'limit' => [int](../types/int.md), \]) === [$messages\_ArchivedStickers](../types/messages_ArchivedStickers.md)<a name="messages_getArchivedStickers"></a>  

$MadelineProto->[messages->getAttachedStickers](messages_getAttachedStickers.md)(\['media' => [InputStickeredMedia](../types/InputStickeredMedia.md), \]) === [$Vector\_of\_StickerSetCovered](../types/StickerSetCovered.md)<a name="messages_getAttachedStickers"></a>  

$MadelineProto->[messages->getBotCallbackAnswer](messages_getBotCallbackAnswer.md)(\['game' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'data' => [bytes](../types/bytes.md), \]) === [$messages\_BotCallbackAnswer](../types/messages_BotCallbackAnswer.md)<a name="messages_getBotCallbackAnswer"></a>  

$MadelineProto->[messages->getChats](messages_getChats.md)(\['id' => \[[int](../types/int.md)\], \]) === [$messages\_Chats](../types/messages_Chats.md)<a name="messages_getChats"></a>  

$MadelineProto->[messages->getCommonChats](messages_getCommonChats.md)(\['user_id' => [InputUser](../types/InputUser.md), 'max_id' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$messages\_Chats](../types/messages_Chats.md)<a name="messages_getCommonChats"></a>  

$MadelineProto->[messages->getDhConfig](messages_getDhConfig.md)(\['version' => [int](../types/int.md), 'random_length' => [int](../types/int.md), \]) === [$messages\_DhConfig](../types/messages_DhConfig.md)<a name="messages_getDhConfig"></a>  

$MadelineProto->[messages->getDialogUnreadMarks](messages_getDialogUnreadMarks.md)(\[\]) === [$Vector\_of\_DialogPeer](../types/DialogPeer.md)<a name="messages_getDialogUnreadMarks"></a>  

$MadelineProto->[messages->getDialogs](messages_getDialogs.md)(\['exclude_pinned' => [Bool](../types/Bool.md), 'folder_id' => [int](../types/int.md), 'offset_date' => [int](../types/int.md), 'offset_id' => [int](../types/int.md), 'offset_peer' => [InputPeer](../types/InputPeer.md), 'limit' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$messages\_Dialogs](../types/messages_Dialogs.md)<a name="messages_getDialogs"></a>  

$MadelineProto->[messages->getDocumentByHash](messages_getDocumentByHash.md)(\['sha256' => [bytes](../types/bytes.md), 'size' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), \]) === [$Document](../types/Document.md)<a name="messages_getDocumentByHash"></a>  

$MadelineProto->[messages->getEmojiKeywords](messages_getEmojiKeywords.md)(\['lang_code' => [string](../types/string.md), \]) === [$EmojiKeywordsDifference](../types/EmojiKeywordsDifference.md)<a name="messages_getEmojiKeywords"></a>  

$MadelineProto->[messages->getEmojiKeywordsDifference](messages_getEmojiKeywordsDifference.md)(\['lang_code' => [string](../types/string.md), 'from_version' => [int](../types/int.md), \]) === [$EmojiKeywordsDifference](../types/EmojiKeywordsDifference.md)<a name="messages_getEmojiKeywordsDifference"></a>  

$MadelineProto->[messages->getEmojiKeywordsLanguages](messages_getEmojiKeywordsLanguages.md)(\['lang_codes' => \[[string](../types/string.md)\], \]) === [$Vector\_of\_EmojiLanguage](../types/EmojiLanguage.md)<a name="messages_getEmojiKeywordsLanguages"></a>  

$MadelineProto->[messages->getEmojiURL](messages_getEmojiURL.md)(\['lang_code' => [string](../types/string.md), \]) === [$EmojiURL](../types/EmojiURL.md)<a name="messages_getEmojiURL"></a>  

$MadelineProto->[messages->getFavedStickers](messages_getFavedStickers.md)(\['hash' => [int](../types/int.md), \]) === [$messages\_FavedStickers](../types/messages_FavedStickers.md)<a name="messages_getFavedStickers"></a>  

$MadelineProto->[messages->getFeaturedStickers](messages_getFeaturedStickers.md)(\['hash' => [int](../types/int.md), \]) === [$messages\_FeaturedStickers](../types/messages_FeaturedStickers.md)<a name="messages_getFeaturedStickers"></a>  

$MadelineProto->[messages->getFullChat](messages_getFullChat.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), \]) === [$messages\_ChatFull](../types/messages_ChatFull.md)<a name="messages_getFullChat"></a>  

$MadelineProto->[messages->getGameHighScores](messages_getGameHighScores.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'id' => [int](../types/int.md), 'user_id' => [InputUser](../types/InputUser.md), \]) === [$messages\_HighScores](../types/messages_HighScores.md)<a name="messages_getGameHighScores"></a>  

$MadelineProto->[messages->getHistory](messages_getHistory.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'offset_id' => [int](../types/int.md), 'offset_date' => [int](../types/int.md), 'add_offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), 'max_id' => [int](../types/int.md), 'min_id' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$messages\_Messages](../types/messages_Messages.md)<a name="messages_getHistory"></a>  

$MadelineProto->[messages->getInlineBotResults](messages_getInlineBotResults.md)(\['bot' => [InputUser](../types/InputUser.md), 'peer' => [InputPeer](../types/InputPeer.md), 'geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'query' => [string](../types/string.md), 'offset' => [string](../types/string.md), \]) === [$messages\_BotResults](../types/messages_BotResults.md)<a name="messages_getInlineBotResults"></a>  

$MadelineProto->[messages->getInlineGameHighScores](messages_getInlineGameHighScores.md)(\['id' => [InputBotInlineMessageID](../types/InputBotInlineMessageID.md), 'user_id' => [InputUser](../types/InputUser.md), \]) === [$messages\_HighScores](../types/messages_HighScores.md)<a name="messages_getInlineGameHighScores"></a>  

$MadelineProto->[messages->getMaskStickers](messages_getMaskStickers.md)(\['hash' => [int](../types/int.md), \]) === [$messages\_AllStickers](../types/messages_AllStickers.md)<a name="messages_getMaskStickers"></a>  

$MadelineProto->[messages->getMessageEditData](messages_getMessageEditData.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'id' => [int](../types/int.md), \]) === [$messages\_MessageEditData](../types/messages_MessageEditData.md)<a name="messages_getMessageEditData"></a>  

$MadelineProto->[messages->getMessages](messages_getMessages.md)(\['id' => \[[InputMessage](../types/InputMessage.md)\], \]) === [$messages\_Messages](../types/messages_Messages.md)<a name="messages_getMessages"></a>  

$MadelineProto->[messages->getMessagesViews](messages_getMessagesViews.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'id' => \[[int](../types/int.md)\], 'increment' => [Bool](../types/Bool.md), \]) === [$Vector\_of\_int](../types/int.md)<a name="messages_getMessagesViews"></a>  

$MadelineProto->[messages->getOnlines](messages_getOnlines.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$ChatOnlines](../types/ChatOnlines.md)<a name="messages_getOnlines"></a>  

$MadelineProto->[messages->getPeerDialogs](messages_getPeerDialogs.md)(\['peers' => \[[InputDialogPeer](../types/InputDialogPeer.md)\], \]) === [$messages\_PeerDialogs](../types/messages_PeerDialogs.md)<a name="messages_getPeerDialogs"></a>  

$MadelineProto->[messages->getPeerSettings](messages_getPeerSettings.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$PeerSettings](../types/PeerSettings.md)<a name="messages_getPeerSettings"></a>  

$MadelineProto->[messages->getPinnedDialogs](messages_getPinnedDialogs.md)(\['folder_id' => [int](../types/int.md), \]) === [$messages\_PeerDialogs](../types/messages_PeerDialogs.md)<a name="messages_getPinnedDialogs"></a>  

$MadelineProto->[messages->getPollResults](messages_getPollResults.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages_getPollResults"></a>  

$MadelineProto->[messages->getRecentLocations](messages_getRecentLocations.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'limit' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$messages\_Messages](../types/messages_Messages.md)<a name="messages_getRecentLocations"></a>  

$MadelineProto->[messages->getRecentStickers](messages_getRecentStickers.md)(\['attached' => [Bool](../types/Bool.md), 'hash' => [int](../types/int.md), \]) === [$messages\_RecentStickers](../types/messages_RecentStickers.md)<a name="messages_getRecentStickers"></a>  

$MadelineProto->[messages->getSavedGifs](messages_getSavedGifs.md)(\['hash' => [int](../types/int.md), \]) === [$messages\_SavedGifs](../types/messages_SavedGifs.md)<a name="messages_getSavedGifs"></a>  

$MadelineProto->[messages->getSearchCounters](messages_getSearchCounters.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'filters' => \[[MessagesFilter](../types/MessagesFilter.md)\], \]) === [$Vector\_of\_messages\_SearchCounter](../types/messages_SearchCounter.md)<a name="messages_getSearchCounters"></a>  

$MadelineProto->[messages->getSplitRanges](messages_getSplitRanges.md)(\[\]) === [$Vector\_of\_MessageRange](../types/MessageRange.md)<a name="messages_getSplitRanges"></a>  

$MadelineProto->[messages->getStatsURL](messages_getStatsURL.md)(\['dark' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'params' => [string](../types/string.md), \]) === [$StatsURL](../types/StatsURL.md)<a name="messages_getStatsURL"></a>  

$MadelineProto->[messages->getStickerSet](messages_getStickerSet.md)(\['stickerset' => [InputStickerSet](../types/InputStickerSet.md), \]) === [$messages\_StickerSet](../types/messages_StickerSet.md)<a name="messages_getStickerSet"></a>  

$MadelineProto->[messages->getStickers](messages_getStickers.md)(\['emoticon' => [string](../types/string.md), 'hash' => [int](../types/int.md), \]) === [$messages\_Stickers](../types/messages_Stickers.md)<a name="messages_getStickers"></a>  

$MadelineProto->[messages->getUnreadMentions](messages_getUnreadMentions.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'offset_id' => [int](../types/int.md), 'add_offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), 'max_id' => [int](../types/int.md), 'min_id' => [int](../types/int.md), \]) === [$messages\_Messages](../types/messages_Messages.md)<a name="messages_getUnreadMentions"></a>  

$MadelineProto->[messages->getWebPage](messages_getWebPage.md)(\['url' => [string](../types/string.md), 'hash' => [int](../types/int.md), \]) === [$WebPage](../types/WebPage.md)<a name="messages_getWebPage"></a>  

$MadelineProto->[messages->getWebPagePreview](messages_getWebPagePreview.md)(\['message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \]) === [$MessageMedia](../types/MessageMedia.md)<a name="messages_getWebPagePreview"></a>  

$MadelineProto->[messages->hidePeerSettingsBar](messages_hidePeerSettingsBar.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$Bool](../types/Bool.md)<a name="messages_hidePeerSettingsBar"></a>  

$MadelineProto->[messages->importChatInvite](messages_importChatInvite.md)(\['hash' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="messages_importChatInvite"></a>  

$MadelineProto->[messages->installStickerSet](messages_installStickerSet.md)(\['stickerset' => [InputStickerSet](../types/InputStickerSet.md), 'archived' => [Bool](../types/Bool.md), \]) === [$messages\_StickerSetInstallResult](../types/messages_StickerSetInstallResult.md)<a name="messages_installStickerSet"></a>  

$MadelineProto->[messages->markDialogUnread](messages_markDialogUnread.md)(\['unread' => [Bool](../types/Bool.md), 'peer' => [InputDialogPeer](../types/InputDialogPeer.md), \]) === [$Bool](../types/Bool.md)<a name="messages_markDialogUnread"></a>  

$MadelineProto->[messages->migrateChat](messages_migrateChat.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), \]) === [$Updates](../types/Updates.md)<a name="messages_migrateChat"></a>  

$MadelineProto->[messages->readEncryptedHistory](messages_readEncryptedHistory.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'max_date' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="messages_readEncryptedHistory"></a>  

$MadelineProto->[messages->readFeaturedStickers](messages_readFeaturedStickers.md)(\['id' => \[[long](../types/long.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages_readFeaturedStickers"></a>  

$MadelineProto->[messages->readHistory](messages_readHistory.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'max_id' => [int](../types/int.md), \]) === [$messages\_AffectedMessages](../types/messages_AffectedMessages.md)<a name="messages_readHistory"></a>  

$MadelineProto->[messages->readMentions](messages_readMentions.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$messages\_AffectedHistory](../types/messages_AffectedHistory.md)<a name="messages_readMentions"></a>  

$MadelineProto->[messages->readMessageContents](messages_readMessageContents.md)(\['id' => \[[int](../types/int.md)\], \]) === [$messages\_AffectedMessages](../types/messages_AffectedMessages.md)<a name="messages_readMessageContents"></a>  

$MadelineProto->[messages->receivedMessages](messages_receivedMessages.md)(\['max_id' => [int](../types/int.md), \]) === [$Vector\_of\_ReceivedNotifyMessage](../types/ReceivedNotifyMessage.md)<a name="messages_receivedMessages"></a>  

$MadelineProto->[messages->receivedQueue](messages_receivedQueue.md)(\['max_qts' => [int](../types/int.md), \]) === [$Vector\_of\_long](../types/long.md)<a name="messages_receivedQueue"></a>  

$MadelineProto->[messages->reorderPinnedDialogs](messages_reorderPinnedDialogs.md)(\['force' => [Bool](../types/Bool.md), 'folder_id' => [int](../types/int.md), 'order' => \[[InputDialogPeer](../types/InputDialogPeer.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages_reorderPinnedDialogs"></a>  

$MadelineProto->[messages->reorderStickerSets](messages_reorderStickerSets.md)(\['masks' => [Bool](../types/Bool.md), 'order' => \[[long](../types/long.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages_reorderStickerSets"></a>  

$MadelineProto->[messages->report](messages_report.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'id' => \[[int](../types/int.md)\], 'reason' => [ReportReason](../types/ReportReason.md), \]) === [$Bool](../types/Bool.md)<a name="messages_report"></a>  

$MadelineProto->[messages->reportEncryptedSpam](messages_reportEncryptedSpam.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), \]) === [$Bool](../types/Bool.md)<a name="messages_reportEncryptedSpam"></a>  

$MadelineProto->[messages->reportSpam](messages_reportSpam.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$Bool](../types/Bool.md)<a name="messages_reportSpam"></a>  

$MadelineProto->[messages->requestEncryption](messages_requestEncryption.md)(\['user_id' => [InputUser](../types/InputUser.md), 'g_a' => [bytes](../types/bytes.md), \]) === [$EncryptedChat](../types/EncryptedChat.md)<a name="messages_requestEncryption"></a>  

$MadelineProto->[messages->requestUrlAuth](messages_requestUrlAuth.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'button_id' => [int](../types/int.md), \]) === [$UrlAuthResult](../types/UrlAuthResult.md)<a name="messages_requestUrlAuth"></a>  

$MadelineProto->[messages->saveDraft](messages_saveDraft.md)(\['no_webpage' => [Bool](../types/Bool.md), 'reply_to_msg_id' => [int](../types/int.md), 'peer' => [InputPeer](../types/InputPeer.md), 'message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages_saveDraft"></a>  

$MadelineProto->[messages->saveGif](messages_saveGif.md)(\['id' => [InputDocument](../types/InputDocument.md), 'unsave' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages_saveGif"></a>  

$MadelineProto->[messages->saveRecentSticker](messages_saveRecentSticker.md)(\['attached' => [Bool](../types/Bool.md), 'id' => [InputDocument](../types/InputDocument.md), 'unsave' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages_saveRecentSticker"></a>  

$MadelineProto->[messages->search](messages_search.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'q' => [string](../types/string.md), 'from_id' => [InputUser](../types/InputUser.md), 'filter' => [MessagesFilter](../types/MessagesFilter.md), 'min_date' => [int](../types/int.md), 'max_date' => [int](../types/int.md), 'offset_id' => [int](../types/int.md), 'add_offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), 'max_id' => [int](../types/int.md), 'min_id' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$messages\_Messages](../types/messages_Messages.md)<a name="messages_search"></a>  

$MadelineProto->[messages->searchGifs](messages_searchGifs.md)(\['q' => [string](../types/string.md), 'offset' => [int](../types/int.md), \]) === [$messages\_FoundGifs](../types/messages_FoundGifs.md)<a name="messages_searchGifs"></a>  

$MadelineProto->[messages->searchGlobal](messages_searchGlobal.md)(\['folder_id' => [int](../types/int.md), 'q' => [string](../types/string.md), 'offset_rate' => [int](../types/int.md), 'offset_peer' => [InputPeer](../types/InputPeer.md), 'offset_id' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$messages\_Messages](../types/messages_Messages.md)<a name="messages_searchGlobal"></a>  

$MadelineProto->[messages->searchStickerSets](messages_searchStickerSets.md)(\['exclude_featured' => [Bool](../types/Bool.md), 'q' => [string](../types/string.md), 'hash' => [int](../types/int.md), \]) === [$messages\_FoundStickerSets](../types/messages_FoundStickerSets.md)<a name="messages_searchStickerSets"></a>  

$MadelineProto->[messages->sendEncrypted](messages_sendEncrypted.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'message' => [DecryptedMessage](../types/DecryptedMessage.md), \]) === [$messages\_SentEncryptedMessage](../types/messages_SentEncryptedMessage.md)<a name="messages_sendEncrypted"></a>  

$MadelineProto->[messages->sendEncryptedFile](messages_sendEncryptedFile.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'message' => [DecryptedMessage](../types/DecryptedMessage.md), 'file' => [InputEncryptedFile](../types/InputEncryptedFile.md), \]) === [$messages\_SentEncryptedMessage](../types/messages_SentEncryptedMessage.md)<a name="messages_sendEncryptedFile"></a>  

$MadelineProto->[messages->sendEncryptedService](messages_sendEncryptedService.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'message' => [DecryptedMessage](../types/DecryptedMessage.md), \]) === [$messages\_SentEncryptedMessage](../types/messages_SentEncryptedMessage.md)<a name="messages_sendEncryptedService"></a>  

$MadelineProto->[messages->sendInlineBotResult](messages_sendInlineBotResult.md)(\['silent' => [Bool](../types/Bool.md), 'background' => [Bool](../types/Bool.md), 'clear_draft' => [Bool](../types/Bool.md), 'hide_via' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'reply_to_msg_id' => [int](../types/int.md), 'query_id' => [long](../types/long.md), 'id' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="messages_sendInlineBotResult"></a>  

$MadelineProto->[messages->sendMedia](messages_sendMedia.md)(\['silent' => [Bool](../types/Bool.md), 'background' => [Bool](../types/Bool.md), 'clear_draft' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'reply_to_msg_id' => [int](../types/int.md), 'media' => [InputMedia](../types/InputMedia.md), 'message' => [string](../types/string.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \]) === [$Updates](../types/Updates.md)<a name="messages_sendMedia"></a>  

$MadelineProto->[messages->sendMessage](messages_sendMessage.md)(\['no_webpage' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'background' => [Bool](../types/Bool.md), 'clear_draft' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'reply_to_msg_id' => [int](../types/int.md), 'message' => [string](../types/string.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \]) === [$Updates](../types/Updates.md)<a name="messages_sendMessage"></a>  

$MadelineProto->[messages->sendMultiMedia](messages_sendMultiMedia.md)(\['silent' => [Bool](../types/Bool.md), 'background' => [Bool](../types/Bool.md), 'clear_draft' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'reply_to_msg_id' => [int](../types/int.md), 'multi_media' => \[[InputSingleMedia](../types/InputSingleMedia.md)\], \]) === [$Updates](../types/Updates.md)<a name="messages_sendMultiMedia"></a>  

$MadelineProto->[messages->sendScreenshotNotification](messages_sendScreenshotNotification.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'reply_to_msg_id' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages_sendScreenshotNotification"></a>  

$MadelineProto->[messages->sendVote](messages_sendVote.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'options' => \[[bytes](../types/bytes.md)\], \]) === [$Updates](../types/Updates.md)<a name="messages_sendVote"></a>  

$MadelineProto->[messages->setBotCallbackAnswer](messages_setBotCallbackAnswer.md)(\['alert' => [Bool](../types/Bool.md), 'query_id' => [long](../types/long.md), 'message' => [string](../types/string.md), 'url' => [string](../types/string.md), 'cache_time' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="messages_setBotCallbackAnswer"></a>  

$MadelineProto->[messages->setBotPrecheckoutResults](messages_setBotPrecheckoutResults.md)(\['success' => [Bool](../types/Bool.md), 'query_id' => [long](../types/long.md), 'error' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="messages_setBotPrecheckoutResults"></a>  

$MadelineProto->[messages->setBotShippingResults](messages_setBotShippingResults.md)(\['query_id' => [long](../types/long.md), 'error' => [string](../types/string.md), 'shipping_options' => \[[ShippingOption](../types/ShippingOption.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages_setBotShippingResults"></a>  

$MadelineProto->[messages->setEncryptedTyping](messages_setEncryptedTyping.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'typing' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages_setEncryptedTyping"></a>  

$MadelineProto->[messages->setGameScore](messages_setGameScore.md)(\['edit_message' => [Bool](../types/Bool.md), 'force' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'id' => [int](../types/int.md), 'user_id' => [InputUser](../types/InputUser.md), 'score' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages_setGameScore"></a>  

$MadelineProto->[messages->setInlineBotResults](messages_setInlineBotResults.md)(\['gallery' => [Bool](../types/Bool.md), 'private' => [Bool](../types/Bool.md), 'query_id' => [long](../types/long.md), 'results' => \[[InputBotInlineResult](../types/InputBotInlineResult.md)\], 'cache_time' => [int](../types/int.md), 'next_offset' => [string](../types/string.md), 'switch_pm' => [InlineBotSwitchPM](../types/InlineBotSwitchPM.md), \]) === [$Bool](../types/Bool.md)<a name="messages_setInlineBotResults"></a>  

$MadelineProto->[messages->setInlineGameScore](messages_setInlineGameScore.md)(\['edit_message' => [Bool](../types/Bool.md), 'force' => [Bool](../types/Bool.md), 'id' => [InputBotInlineMessageID](../types/InputBotInlineMessageID.md), 'user_id' => [InputUser](../types/InputUser.md), 'score' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="messages_setInlineGameScore"></a>  

$MadelineProto->[messages->setTyping](messages_setTyping.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'action' => [SendMessageAction](../types/SendMessageAction.md), \]) === [$Bool](../types/Bool.md)<a name="messages_setTyping"></a>  

$MadelineProto->[messages->startBot](messages_startBot.md)(\['bot' => [InputUser](../types/InputUser.md), 'peer' => [InputPeer](../types/InputPeer.md), 'start_param' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="messages_startBot"></a>  

$MadelineProto->[messages->toggleDialogPin](messages_toggleDialogPin.md)(\['pinned' => [Bool](../types/Bool.md), 'peer' => [InputDialogPeer](../types/InputDialogPeer.md), \]) === [$Bool](../types/Bool.md)<a name="messages_toggleDialogPin"></a>  

$MadelineProto->[messages->uninstallStickerSet](messages_uninstallStickerSet.md)(\['stickerset' => [InputStickerSet](../types/InputStickerSet.md), \]) === [$Bool](../types/Bool.md)<a name="messages_uninstallStickerSet"></a>  

$MadelineProto->[messages->updatePinnedMessage](messages_updatePinnedMessage.md)(\['silent' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'id' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages_updatePinnedMessage"></a>  

$MadelineProto->[messages->uploadEncryptedFile](messages_uploadEncryptedFile.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'file' => [InputEncryptedFile](../types/InputEncryptedFile.md), \]) === [$EncryptedFile](../types/EncryptedFile.md)<a name="messages_uploadEncryptedFile"></a>  

$MadelineProto->[messages->uploadMedia](messages_uploadMedia.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'media' => [InputMedia](../types/InputMedia.md), \]) === [$MessageMedia](../types/MessageMedia.md)<a name="messages_uploadMedia"></a>  

***
<br><br>
$MadelineProto->[payments->clearSavedInfo](payments_clearSavedInfo.md)(\['credentials' => [Bool](../types/Bool.md), 'info' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="payments_clearSavedInfo"></a>  

$MadelineProto->[payments->getPaymentForm](payments_getPaymentForm.md)(\['msg_id' => [int](../types/int.md), \]) === [$payments\_PaymentForm](../types/payments_PaymentForm.md)<a name="payments_getPaymentForm"></a>  

$MadelineProto->[payments->getPaymentReceipt](payments_getPaymentReceipt.md)(\['msg_id' => [int](../types/int.md), \]) === [$payments\_PaymentReceipt](../types/payments_PaymentReceipt.md)<a name="payments_getPaymentReceipt"></a>  

$MadelineProto->[payments->getSavedInfo](payments_getSavedInfo.md)(\[\]) === [$payments\_SavedInfo](../types/payments_SavedInfo.md)<a name="payments_getSavedInfo"></a>  

$MadelineProto->[payments->sendPaymentForm](payments_sendPaymentForm.md)(\['msg_id' => [int](../types/int.md), 'requested_info_id' => [string](../types/string.md), 'shipping_option_id' => [string](../types/string.md), 'credentials' => [InputPaymentCredentials](../types/InputPaymentCredentials.md), \]) === [$payments\_PaymentResult](../types/payments_PaymentResult.md)<a name="payments_sendPaymentForm"></a>  

$MadelineProto->[payments->validateRequestedInfo](payments_validateRequestedInfo.md)(\['save' => [Bool](../types/Bool.md), 'msg_id' => [int](../types/int.md), 'info' => [PaymentRequestedInfo](../types/PaymentRequestedInfo.md), \]) === [$payments\_ValidatedRequestedInfo](../types/payments_ValidatedRequestedInfo.md)<a name="payments_validateRequestedInfo"></a>  

***
<br><br>
$MadelineProto->[phone->acceptCall](phone_acceptCall.md)(\['peer' => [InputPhoneCall](../types/InputPhoneCall.md), 'g_b' => [bytes](../types/bytes.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), \]) === [$phone\_PhoneCall](../types/phone_PhoneCall.md)<a name="phone_acceptCall"></a>  

$MadelineProto->[phone->confirmCall](phone_confirmCall.md)(\['peer' => [InputPhoneCall](../types/InputPhoneCall.md), 'g_a' => [bytes](../types/bytes.md), 'key_fingerprint' => [long](../types/long.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), \]) === [$phone\_PhoneCall](../types/phone_PhoneCall.md)<a name="phone_confirmCall"></a>  

$MadelineProto->[phone->discardCall](phone_discardCall.md)(\['video' => [Bool](../types/Bool.md), 'peer' => [InputPhoneCall](../types/InputPhoneCall.md), 'duration' => [int](../types/int.md), 'reason' => [PhoneCallDiscardReason](../types/PhoneCallDiscardReason.md), 'connection_id' => [long](../types/long.md), \]) === [$Updates](../types/Updates.md)<a name="phone_discardCall"></a>  

$MadelineProto->[phone->getCallConfig](phone_getCallConfig.md)(\[\]) === [$DataJSON](../types/DataJSON.md)<a name="phone_getCallConfig"></a>  

$MadelineProto->[phone->receivedCall](phone_receivedCall.md)(\['peer' => [InputPhoneCall](../types/InputPhoneCall.md), \]) === [$Bool](../types/Bool.md)<a name="phone_receivedCall"></a>  

$MadelineProto->[phone->requestCall](phone_requestCall.md)(\['video' => [Bool](../types/Bool.md), 'user_id' => [InputUser](../types/InputUser.md), 'g_a_hash' => [bytes](../types/bytes.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), \]) === [$phone\_PhoneCall](../types/phone_PhoneCall.md)<a name="phone_requestCall"></a>  

$MadelineProto->[phone->saveCallDebug](phone_saveCallDebug.md)(\['peer' => [InputPhoneCall](../types/InputPhoneCall.md), 'debug' => [DataJSON](../types/DataJSON.md), \]) === [$Bool](../types/Bool.md)<a name="phone_saveCallDebug"></a>  

$MadelineProto->[phone->setCallRating](phone_setCallRating.md)(\['user_initiative' => [Bool](../types/Bool.md), 'peer' => [InputPhoneCall](../types/InputPhoneCall.md), 'rating' => [int](../types/int.md), 'comment' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="phone_setCallRating"></a>  

***
<br><br>
$MadelineProto->[photos->deletePhotos](photos_deletePhotos.md)(\['id' => \[[InputPhoto](../types/InputPhoto.md)\], \]) === [$Vector\_of\_long](../types/long.md)<a name="photos_deletePhotos"></a>  

$MadelineProto->[photos->getUserPhotos](photos_getUserPhotos.md)(\['user_id' => [InputUser](../types/InputUser.md), 'offset' => [int](../types/int.md), 'max_id' => [long](../types/long.md), 'limit' => [int](../types/int.md), \]) === [$photos\_Photos](../types/photos_Photos.md)<a name="photos_getUserPhotos"></a>  

$MadelineProto->[photos->updateProfilePhoto](photos_updateProfilePhoto.md)(\['id' => [InputPhoto](../types/InputPhoto.md), \]) === [$UserProfilePhoto](../types/UserProfilePhoto.md)<a name="photos_updateProfilePhoto"></a>  

$MadelineProto->[photos->uploadProfilePhoto](photos_uploadProfilePhoto.md)(\['file' => [InputFile](../types/InputFile.md), \]) === [$photos\_Photo](../types/photos_Photo.md)<a name="photos_uploadProfilePhoto"></a>  

***
<br><br>
$MadelineProto->[stickers->addStickerToSet](stickers_addStickerToSet.md)(\['stickerset' => [InputStickerSet](../types/InputStickerSet.md), 'sticker' => [InputStickerSetItem](../types/InputStickerSetItem.md), \]) === [$messages\_StickerSet](../types/messages_StickerSet.md)<a name="stickers_addStickerToSet"></a>  

$MadelineProto->[stickers->changeStickerPosition](stickers_changeStickerPosition.md)(\['sticker' => [InputDocument](../types/InputDocument.md), 'position' => [int](../types/int.md), \]) === [$messages\_StickerSet](../types/messages_StickerSet.md)<a name="stickers_changeStickerPosition"></a>  

$MadelineProto->[stickers->createStickerSet](stickers_createStickerSet.md)(\['masks' => [Bool](../types/Bool.md), 'user_id' => [InputUser](../types/InputUser.md), 'title' => [string](../types/string.md), 'short_name' => [string](../types/string.md), 'stickers' => \[[InputStickerSetItem](../types/InputStickerSetItem.md)\], \]) === [$messages\_StickerSet](../types/messages_StickerSet.md)<a name="stickers_createStickerSet"></a>  

$MadelineProto->[stickers->removeStickerFromSet](stickers_removeStickerFromSet.md)(\['sticker' => [InputDocument](../types/InputDocument.md), \]) === [$messages\_StickerSet](../types/messages_StickerSet.md)<a name="stickers_removeStickerFromSet"></a>  

***
<br><br>
$MadelineProto->[updates->getChannelDifference](updates_getChannelDifference.md)(\['force' => [Bool](../types/Bool.md), 'channel' => [InputChannel](../types/InputChannel.md), 'filter' => [ChannelMessagesFilter](../types/ChannelMessagesFilter.md), 'pts' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$updates\_ChannelDifference](../types/updates_ChannelDifference.md)<a name="updates_getChannelDifference"></a>  

$MadelineProto->[updates->getDifference](updates_getDifference.md)(\['pts' => [int](../types/int.md), 'pts_total_limit' => [int](../types/int.md), 'date' => [int](../types/int.md), 'qts' => [int](../types/int.md), \]) === [$updates\_Difference](../types/updates_Difference.md)<a name="updates_getDifference"></a>  

$MadelineProto->[updates->getState](updates_getState.md)(\[\]) === [$updates\_State](../types/updates_State.md)<a name="updates_getState"></a>  

***
<br><br>
$MadelineProto->[upload->getCdnFile](upload_getCdnFile.md)(\['file_token' => [bytes](../types/bytes.md), 'offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$upload\_CdnFile](../types/upload_CdnFile.md)<a name="upload_getCdnFile"></a>  

$MadelineProto->[upload->getCdnFileHashes](upload_getCdnFileHashes.md)(\['file_token' => [bytes](../types/bytes.md), 'offset' => [int](../types/int.md), \]) === [$Vector\_of\_FileHash](../types/FileHash.md)<a name="upload_getCdnFileHashes"></a>  

$MadelineProto->[upload->getFile](upload_getFile.md)(\['location' => [InputFileLocation](../types/InputFileLocation.md), 'offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$upload\_File](../types/upload_File.md)<a name="upload_getFile"></a>  

$MadelineProto->[upload->getFileHashes](upload_getFileHashes.md)(\['location' => [InputFileLocation](../types/InputFileLocation.md), 'offset' => [int](../types/int.md), \]) === [$Vector\_of\_FileHash](../types/FileHash.md)<a name="upload_getFileHashes"></a>  

$MadelineProto->[upload->getWebFile](upload_getWebFile.md)(\['location' => [InputWebFileLocation](../types/InputWebFileLocation.md), 'offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$upload\_WebFile](../types/upload_WebFile.md)<a name="upload_getWebFile"></a>  

$MadelineProto->[upload->reuploadCdnFile](upload_reuploadCdnFile.md)(\['file_token' => [bytes](../types/bytes.md), 'request_token' => [bytes](../types/bytes.md), \]) === [$Vector\_of\_FileHash](../types/FileHash.md)<a name="upload_reuploadCdnFile"></a>  

$MadelineProto->[upload->saveBigFilePart](upload_saveBigFilePart.md)(\['file_id' => [long](../types/long.md), 'file_part' => [int](../types/int.md), 'file_total_parts' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \]) === [$Bool](../types/Bool.md)<a name="upload_saveBigFilePart"></a>  

$MadelineProto->[upload->saveFilePart](upload_saveFilePart.md)(\['file_id' => [long](../types/long.md), 'file_part' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \]) === [$Bool](../types/Bool.md)<a name="upload_saveFilePart"></a>  

***
<br><br>
$MadelineProto->[users->getFullUser](users_getFullUser.md)(\['id' => [InputUser](../types/InputUser.md), \]) === [$UserFull](../types/UserFull.md)<a name="users_getFullUser"></a>  

$MadelineProto->[users->getUsers](users_getUsers.md)(\['id' => \[[InputUser](../types/InputUser.md)\], \]) === [$Vector\_of\_User](../types/User.md)<a name="users_getUsers"></a>  

$MadelineProto->[users->setSecureValueErrors](users_setSecureValueErrors.md)(\['id' => [InputUser](../types/InputUser.md), 'errors' => \[[SecureValueError](../types/SecureValueError.md)\], \]) === [$Bool](../types/Bool.md)<a name="users_setSecureValueErrors"></a>  

