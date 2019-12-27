---
title: Methods
description: List of methods
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Methods  
[Back to API documentation index](..)

[Go to the new description-version method index](README.md)

$MadelineProto->[logout](https://docs.madelineproto.xyz/logout.html)();

$MadelineProto->[phoneLogin](https://docs.madelineproto.xyz/phoneLogin.html)($number);

$MadelineProto->[completePhoneLogin](https://docs.madelineproto.xyz/completePhoneLogin.html)($code);

$MadelineProto->[complete2FALogin](https://docs.madelineproto.xyz/complete2FAlogin.html)($password);

$MadelineProto->[botLogin](https://docs.madelineproto.xyz/botLogin.html)($token);


$MadelineProto->[getDialogs](https://docs.madelineproto.xyz/getDialogs.html)();

$MadelineProto->[getPwrChat](https://docs.madelineproto.xyz/getPwrChat.html)($id);

$MadelineProto->[getInfo](https://docs.madelineproto.xyz/getInfo.html)($id);

$MadelineProto->[getFullInfo](https://docs.madelineproto.xyz/getFullInfo.html)($id);

$MadelineProto->[getSelf](https://docs.madelineproto.xyz/getSelf.html)();


$MadelineProto->[requestCall](https://docs.madelineproto.xyz/requestCall.html)($id);

$MadelineProto->[requestSecretChat](https://docs.madelineproto.xyz/requestSecretChat.html)($id);

***
<br><br>
$MadelineProto->[account->acceptAuthorization](account.acceptAuthorization.md)(\['bot_id' => [int](../types/int.md), 'scope' => [string](../types/string.md), 'public_key' => [string](../types/string.md), 'value_hashes' => \[[SecureValueHash](../types/SecureValueHash.md)\], 'credentials' => [SecureCredentialsEncrypted](../types/SecureCredentialsEncrypted.md), \]) === [$Bool](../types/Bool.md)<a name="account.acceptAuthorization"></a>  

***
<br><br>
$MadelineProto->[account->cancelPasswordEmail](account.cancelPasswordEmail.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account.cancelPasswordEmail"></a>  

***
<br><br>
$MadelineProto->[account->changePhone](account.changePhone.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), 'phone_code' => [string](../types/string.md), \]) === [$User](../types/User.md)<a name="account.changePhone"></a>  

***
<br><br>
$MadelineProto->[account->checkUsername](account.checkUsername.md)(\['username' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account.checkUsername"></a>  

***
<br><br>
$MadelineProto->[account->confirmPasswordEmail](account.confirmPasswordEmail.md)(\['code' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account.confirmPasswordEmail"></a>  

***
<br><br>
$MadelineProto->[account->confirmPhone](account.confirmPhone.md)(\['phone_code_hash' => [string](../types/string.md), 'phone_code' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account.confirmPhone"></a>  

***
<br><br>
$MadelineProto->[account->createTheme](account.createTheme.md)(\['slug' => [string](../types/string.md), 'title' => [string](../types/string.md), 'document' => [InputDocument](../types/InputDocument.md), \]) === [$Theme](../types/Theme.md)<a name="account.createTheme"></a>  

***
<br><br>
$MadelineProto->[account->deleteAccount](account.deleteAccount.md)(\['reason' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account.deleteAccount"></a>  

***
<br><br>
$MadelineProto->[account->deleteSecureValue](account.deleteSecureValue.md)(\['types' => \[[SecureValueType](../types/SecureValueType.md)\], \]) === [$Bool](../types/Bool.md)<a name="account.deleteSecureValue"></a>  

***
<br><br>
$MadelineProto->[account->finishTakeoutSession](account.finishTakeoutSession.md)(\['success' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="account.finishTakeoutSession"></a>  

***
<br><br>
$MadelineProto->[account->getAccountTTL](account.getAccountTTL.md)(\[\]) === [$AccountDaysTTL](../types/AccountDaysTTL.md)<a name="account.getAccountTTL"></a>  

***
<br><br>
$MadelineProto->[account->getAllSecureValues](account.getAllSecureValues.md)(\[\]) === [$Vector\_of\_SecureValue](../types/SecureValue.md)<a name="account.getAllSecureValues"></a>  

***
<br><br>
$MadelineProto->[account->getAuthorizationForm](account.getAuthorizationForm.md)(\['bot_id' => [int](../types/int.md), 'scope' => [string](../types/string.md), 'public_key' => [string](../types/string.md), \]) === [$account.AuthorizationForm](../types/account.AuthorizationForm.md)<a name="account.getAuthorizationForm"></a>  

***
<br><br>
$MadelineProto->[account->getAuthorizations](account.getAuthorizations.md)(\[\]) === [$account.Authorizations](../types/account.Authorizations.md)<a name="account.getAuthorizations"></a>  

***
<br><br>
$MadelineProto->[account->getAutoDownloadSettings](account.getAutoDownloadSettings.md)(\[\]) === [$account.AutoDownloadSettings](../types/account.AutoDownloadSettings.md)<a name="account.getAutoDownloadSettings"></a>  

***
<br><br>
$MadelineProto->[account->getContactSignUpNotification](account.getContactSignUpNotification.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account.getContactSignUpNotification"></a>  

***
<br><br>
$MadelineProto->[account->getNotifyExceptions](account.getNotifyExceptions.md)(\['compare_sound' => [Bool](../types/Bool.md), 'peer' => [InputNotifyPeer](../types/InputNotifyPeer.md), \]) === [$Updates](../types/Updates.md)<a name="account.getNotifyExceptions"></a>  

***
<br><br>
$MadelineProto->[account->getNotifySettings](account.getNotifySettings.md)(\['peer' => [InputNotifyPeer](../types/InputNotifyPeer.md), \]) === [$PeerNotifySettings](../types/PeerNotifySettings.md)<a name="account.getNotifySettings"></a>  

***
<br><br>
$MadelineProto->[account->getPassword](account.getPassword.md)(\[\]) === [$account.Password](../types/account.Password.md)<a name="account.getPassword"></a>  

***
<br><br>
$MadelineProto->[account->getPasswordSettings](account.getPasswordSettings.md)(\['password' => [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md), \]) === [$account.PasswordSettings](../types/account.PasswordSettings.md)<a name="account.getPasswordSettings"></a>  

***
<br><br>
$MadelineProto->[account->getPrivacy](account.getPrivacy.md)(\['key' => [InputPrivacyKey](../types/InputPrivacyKey.md), \]) === [$account.PrivacyRules](../types/account.PrivacyRules.md)<a name="account.getPrivacy"></a>  

***
<br><br>
$MadelineProto->[account->getSecureValue](account.getSecureValue.md)(\['types' => \[[SecureValueType](../types/SecureValueType.md)\], \]) === [$Vector\_of\_SecureValue](../types/SecureValue.md)<a name="account.getSecureValue"></a>  

***
<br><br>
$MadelineProto->[account->getTheme](account.getTheme.md)(\['format' => [string](../types/string.md), 'theme' => [InputTheme](../types/InputTheme.md), 'document_id' => [long](../types/long.md), \]) === [$Theme](../types/Theme.md)<a name="account.getTheme"></a>  

***
<br><br>
$MadelineProto->[account->getThemes](account.getThemes.md)(\['format' => [string](../types/string.md), 'hash' => [int](../types/int.md), \]) === [$account.Themes](../types/account.Themes.md)<a name="account.getThemes"></a>  

***
<br><br>
$MadelineProto->[account->getTmpPassword](account.getTmpPassword.md)(\['password' => [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md), 'period' => [int](../types/int.md), \]) === [$account.TmpPassword](../types/account.TmpPassword.md)<a name="account.getTmpPassword"></a>  

***
<br><br>
$MadelineProto->[account->getWallPaper](account.getWallPaper.md)(\['wallpaper' => [InputWallPaper](../types/InputWallPaper.md), \]) === [$WallPaper](../types/WallPaper.md)<a name="account.getWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->getWallPapers](account.getWallPapers.md)(\['hash' => [int](../types/int.md), \]) === [$account.WallPapers](../types/account.WallPapers.md)<a name="account.getWallPapers"></a>  

***
<br><br>
$MadelineProto->[account->getWebAuthorizations](account.getWebAuthorizations.md)(\[\]) === [$account.WebAuthorizations](../types/account.WebAuthorizations.md)<a name="account.getWebAuthorizations"></a>  

***
<br><br>
$MadelineProto->[account->initTakeoutSession](account.initTakeoutSession.md)(\['contacts' => [Bool](../types/Bool.md), 'message_users' => [Bool](../types/Bool.md), 'message_chats' => [Bool](../types/Bool.md), 'message_megagroups' => [Bool](../types/Bool.md), 'message_channels' => [Bool](../types/Bool.md), 'files' => [Bool](../types/Bool.md), 'file_max_size' => [int](../types/int.md), \]) === [$account.Takeout](../types/account.Takeout.md)<a name="account.initTakeoutSession"></a>  

***
<br><br>
$MadelineProto->[account->installTheme](account.installTheme.md)(\['dark' => [Bool](../types/Bool.md), 'format' => [string](../types/string.md), 'theme' => [InputTheme](../types/InputTheme.md), \]) === [$Bool](../types/Bool.md)<a name="account.installTheme"></a>  

***
<br><br>
$MadelineProto->[account->installWallPaper](account.installWallPaper.md)(\['wallpaper' => [InputWallPaper](../types/InputWallPaper.md), 'settings' => [WallPaperSettings](../types/WallPaperSettings.md), \]) === [$Bool](../types/Bool.md)<a name="account.installWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->registerDevice](account.registerDevice.md)(\['no_muted' => [Bool](../types/Bool.md), 'token_type' => [int](../types/int.md), 'token' => [string](../types/string.md), 'app_sandbox' => [Bool](../types/Bool.md), 'secret' => [bytes](../types/bytes.md), 'other_uids' => \[[int](../types/int.md)\], \]) === [$Bool](../types/Bool.md)<a name="account.registerDevice"></a>  

***
<br><br>
$MadelineProto->[account->reportPeer](account.reportPeer.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'reason' => [ReportReason](../types/ReportReason.md), \]) === [$Bool](../types/Bool.md)<a name="account.reportPeer"></a>  

***
<br><br>
$MadelineProto->[account->resendPasswordEmail](account.resendPasswordEmail.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account.resendPasswordEmail"></a>  

***
<br><br>
$MadelineProto->[account->resetAuthorization](account.resetAuthorization.md)(\['hash' => [long](../types/long.md), \]) === [$Bool](../types/Bool.md)<a name="account.resetAuthorization"></a>  

***
<br><br>
$MadelineProto->[account->resetNotifySettings](account.resetNotifySettings.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account.resetNotifySettings"></a>  

***
<br><br>
$MadelineProto->[account->resetWallPapers](account.resetWallPapers.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account.resetWallPapers"></a>  

***
<br><br>
$MadelineProto->[account->resetWebAuthorization](account.resetWebAuthorization.md)(\['hash' => [long](../types/long.md), \]) === [$Bool](../types/Bool.md)<a name="account.resetWebAuthorization"></a>  

***
<br><br>
$MadelineProto->[account->resetWebAuthorizations](account.resetWebAuthorizations.md)(\[\]) === [$Bool](../types/Bool.md)<a name="account.resetWebAuthorizations"></a>  

***
<br><br>
$MadelineProto->[account->saveAutoDownloadSettings](account.saveAutoDownloadSettings.md)(\['low' => [Bool](../types/Bool.md), 'high' => [Bool](../types/Bool.md), 'settings' => [AutoDownloadSettings](../types/AutoDownloadSettings.md), \]) === [$Bool](../types/Bool.md)<a name="account.saveAutoDownloadSettings"></a>  

***
<br><br>
$MadelineProto->[account->saveSecureValue](account.saveSecureValue.md)(\['value' => [InputSecureValue](../types/InputSecureValue.md), 'secure_secret_id' => [long](../types/long.md), \]) === [$SecureValue](../types/SecureValue.md)<a name="account.saveSecureValue"></a>  

***
<br><br>
$MadelineProto->[account->saveTheme](account.saveTheme.md)(\['theme' => [InputTheme](../types/InputTheme.md), 'unsave' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="account.saveTheme"></a>  

***
<br><br>
$MadelineProto->[account->saveWallPaper](account.saveWallPaper.md)(\['wallpaper' => [InputWallPaper](../types/InputWallPaper.md), 'unsave' => [Bool](../types/Bool.md), 'settings' => [WallPaperSettings](../types/WallPaperSettings.md), \]) === [$Bool](../types/Bool.md)<a name="account.saveWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->sendChangePhoneCode](account.sendChangePhoneCode.md)(\['phone_number' => [string](../types/string.md), 'settings' => [CodeSettings](../types/CodeSettings.md), \]) === [$auth.SentCode](../types/auth.SentCode.md)<a name="account.sendChangePhoneCode"></a>  

***
<br><br>
$MadelineProto->[account->sendConfirmPhoneCode](account.sendConfirmPhoneCode.md)(\['hash' => [string](../types/string.md), 'settings' => [CodeSettings](../types/CodeSettings.md), \]) === [$auth.SentCode](../types/auth.SentCode.md)<a name="account.sendConfirmPhoneCode"></a>  

***
<br><br>
$MadelineProto->[account->sendVerifyEmailCode](account.sendVerifyEmailCode.md)(\['email' => [string](../types/string.md), \]) === [$account.SentEmailCode](../types/account.SentEmailCode.md)<a name="account.sendVerifyEmailCode"></a>  

***
<br><br>
$MadelineProto->[account->sendVerifyPhoneCode](account.sendVerifyPhoneCode.md)(\['phone_number' => [string](../types/string.md), 'settings' => [CodeSettings](../types/CodeSettings.md), \]) === [$auth.SentCode](../types/auth.SentCode.md)<a name="account.sendVerifyPhoneCode"></a>  

***
<br><br>
$MadelineProto->[account->setAccountTTL](account.setAccountTTL.md)(\['ttl' => [AccountDaysTTL](../types/AccountDaysTTL.md), \]) === [$Bool](../types/Bool.md)<a name="account.setAccountTTL"></a>  

***
<br><br>
$MadelineProto->[account->setContactSignUpNotification](account.setContactSignUpNotification.md)(\['silent' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="account.setContactSignUpNotification"></a>  

***
<br><br>
$MadelineProto->[account->setPrivacy](account.setPrivacy.md)(\['key' => [InputPrivacyKey](../types/InputPrivacyKey.md), 'rules' => \[[InputPrivacyRule](../types/InputPrivacyRule.md)\], \]) === [$account.PrivacyRules](../types/account.PrivacyRules.md)<a name="account.setPrivacy"></a>  

***
<br><br>
$MadelineProto->[account->unregisterDevice](account.unregisterDevice.md)(\['token_type' => [int](../types/int.md), 'token' => [string](../types/string.md), 'other_uids' => \[[int](../types/int.md)\], \]) === [$Bool](../types/Bool.md)<a name="account.unregisterDevice"></a>  

***
<br><br>
$MadelineProto->[account->updateDeviceLocked](account.updateDeviceLocked.md)(\['period' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="account.updateDeviceLocked"></a>  

***
<br><br>
$MadelineProto->[account->updateNotifySettings](account.updateNotifySettings.md)(\['peer' => [InputNotifyPeer](../types/InputNotifyPeer.md), 'settings' => [InputPeerNotifySettings](../types/InputPeerNotifySettings.md), \]) === [$Bool](../types/Bool.md)<a name="account.updateNotifySettings"></a>  

***
<br><br>
$MadelineProto->[account->updatePasswordSettings](account.updatePasswordSettings.md)(\['password' => [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md), 'new_settings' => [account.PasswordInputSettings](../types/account.PasswordInputSettings.md), \]) === [$Bool](../types/Bool.md)<a name="account.updatePasswordSettings"></a>  

***
<br><br>
$MadelineProto->[account->updateProfile](account.updateProfile.md)(\['first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'about' => [string](../types/string.md), \]) === [$User](../types/User.md)<a name="account.updateProfile"></a>  

***
<br><br>
$MadelineProto->[account->updateStatus](account.updateStatus.md)(\['offline' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="account.updateStatus"></a>  

***
<br><br>
$MadelineProto->[account->updateTheme](account.updateTheme.md)(\['format' => [string](../types/string.md), 'theme' => [InputTheme](../types/InputTheme.md), 'slug' => [string](../types/string.md), 'title' => [string](../types/string.md), 'document' => [InputDocument](../types/InputDocument.md), \]) === [$Theme](../types/Theme.md)<a name="account.updateTheme"></a>  

***
<br><br>
$MadelineProto->[account->updateUsername](account.updateUsername.md)(\['username' => [string](../types/string.md), \]) === [$User](../types/User.md)<a name="account.updateUsername"></a>  

***
<br><br>
$MadelineProto->[account->uploadTheme](account.uploadTheme.md)(\['file' => [InputFile](../types/InputFile.md), 'thumb' => [InputFile](../types/InputFile.md), 'file_name' => [string](../types/string.md), 'mime_type' => [string](../types/string.md), \]) === [$Document](../types/Document.md)<a name="account.uploadTheme"></a>  

***
<br><br>
$MadelineProto->[account->uploadWallPaper](account.uploadWallPaper.md)(\['file' => [InputFile](../types/InputFile.md), 'mime_type' => [string](../types/string.md), 'settings' => [WallPaperSettings](../types/WallPaperSettings.md), \]) === [$WallPaper](../types/WallPaper.md)<a name="account.uploadWallPaper"></a>  

***
<br><br>
$MadelineProto->[account->verifyEmail](account.verifyEmail.md)(\['email' => [string](../types/string.md), 'code' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account.verifyEmail"></a>  

***
<br><br>
$MadelineProto->[account->verifyPhone](account.verifyPhone.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), 'phone_code' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="account.verifyPhone"></a>  

***
<br><br>
$MadelineProto->[auth->bindTempAuthKey](auth.bindTempAuthKey.md)(\['perm_auth_key_id' => [long](../types/long.md), 'nonce' => [long](../types/long.md), 'expires_at' => [int](../types/int.md), 'encrypted_message' => [bytes](../types/bytes.md), \]) === [$Bool](../types/Bool.md)<a name="auth.bindTempAuthKey"></a>  

***
<br><br>
$MadelineProto->[auth->cancelCode](auth.cancelCode.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="auth.cancelCode"></a>  

***
<br><br>
$MadelineProto->[auth->checkPassword](auth.checkPassword.md)(\['password' => [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md), \]) === [$auth.Authorization](../types/auth.Authorization.md)<a name="auth.checkPassword"></a>  

***
<br><br>
$MadelineProto->[auth->dropTempAuthKeys](auth.dropTempAuthKeys.md)(\['except_auth_keys' => \[[long](../types/long.md)\], \]) === [$Bool](../types/Bool.md)<a name="auth.dropTempAuthKeys"></a>  

***
<br><br>
$MadelineProto->[auth->exportAuthorization](auth.exportAuthorization.md)(\['dc_id' => [int](../types/int.md), \]) === [$auth.ExportedAuthorization](../types/auth.ExportedAuthorization.md)<a name="auth.exportAuthorization"></a>  

***
<br><br>
$MadelineProto->[auth->importAuthorization](auth.importAuthorization.md)(\['id' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \]) === [$auth.Authorization](../types/auth.Authorization.md)<a name="auth.importAuthorization"></a>  

***
<br><br>
$MadelineProto->[auth->importBotAuthorization](auth.importBotAuthorization.md)(\['api_id' => [int](../types/int.md), 'api_hash' => [string](../types/string.md), 'bot_auth_token' => [string](../types/string.md), \]) === [$auth.Authorization](../types/auth.Authorization.md)<a name="auth.importBotAuthorization"></a>  

***
<br><br>
$MadelineProto->[auth->logOut](auth.logOut.md)(\[\]) === [$Bool](../types/Bool.md)<a name="auth.logOut"></a>  

***
<br><br>
$MadelineProto->[auth->recoverPassword](auth.recoverPassword.md)(\['code' => [string](../types/string.md), \]) === [$auth.Authorization](../types/auth.Authorization.md)<a name="auth.recoverPassword"></a>  

***
<br><br>
$MadelineProto->[auth->requestPasswordRecovery](auth.requestPasswordRecovery.md)(\[\]) === [$auth.PasswordRecovery](../types/auth.PasswordRecovery.md)<a name="auth.requestPasswordRecovery"></a>  

***
<br><br>
$MadelineProto->[auth->resendCode](auth.resendCode.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), \]) === [$auth.SentCode](../types/auth.SentCode.md)<a name="auth.resendCode"></a>  

***
<br><br>
$MadelineProto->[auth->resetAuthorizations](auth.resetAuthorizations.md)(\[\]) === [$Bool](../types/Bool.md)<a name="auth.resetAuthorizations"></a>  

***
<br><br>
$MadelineProto->[auth->sendCode](auth.sendCode.md)(\['phone_number' => [string](../types/string.md), 'api_id' => [int](../types/int.md), 'api_hash' => [string](../types/string.md), 'settings' => [CodeSettings](../types/CodeSettings.md), \]) === [$auth.SentCode](../types/auth.SentCode.md)<a name="auth.sendCode"></a>  

***
<br><br>
$MadelineProto->[auth->signIn](auth.signIn.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), 'phone_code' => [string](../types/string.md), \]) === [$auth.Authorization](../types/auth.Authorization.md)<a name="auth.signIn"></a>  

***
<br><br>
$MadelineProto->[auth->signUp](auth.signUp.md)(\['phone_number' => [string](../types/string.md), 'phone_code_hash' => [string](../types/string.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), \]) === [$auth.Authorization](../types/auth.Authorization.md)<a name="auth.signUp"></a>  

***
<br><br>
$MadelineProto->[bots->answerWebhookJSONQuery](bots.answerWebhookJSONQuery.md)(\['query_id' => [long](../types/long.md), 'data' => [DataJSON](../types/DataJSON.md), \]) === [$Bool](../types/Bool.md)<a name="bots.answerWebhookJSONQuery"></a>  

***
<br><br>
$MadelineProto->[bots->sendCustomRequest](bots.sendCustomRequest.md)(\['custom_method' => [string](../types/string.md), 'params' => [DataJSON](../types/DataJSON.md), \]) === [$DataJSON](../types/DataJSON.md)<a name="bots.sendCustomRequest"></a>  

***
<br><br>
$MadelineProto->[channels->checkUsername](channels.checkUsername.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'username' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="channels.checkUsername"></a>  

***
<br><br>
$MadelineProto->[channels->createChannel](channels.createChannel.md)(\['broadcast' => [Bool](../types/Bool.md), 'megagroup' => [Bool](../types/Bool.md), 'title' => [string](../types/string.md), 'about' => [string](../types/string.md), 'geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'address' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="channels.createChannel"></a>  

***
<br><br>
$MadelineProto->[channels->deleteChannel](channels.deleteChannel.md)(\['channel' => [InputChannel](../types/InputChannel.md), \]) === [$Updates](../types/Updates.md)<a name="channels.deleteChannel"></a>  

***
<br><br>
$MadelineProto->[channels->deleteHistory](channels.deleteHistory.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'max_id' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="channels.deleteHistory"></a>  

***
<br><br>
$MadelineProto->[channels->deleteMessages](channels.deleteMessages.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'id' => \[[int](../types/int.md)\], \]) === [$messages.AffectedMessages](../types/messages.AffectedMessages.md)<a name="channels.deleteMessages"></a>  

***
<br><br>
$MadelineProto->[channels->deleteUserHistory](channels.deleteUserHistory.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), \]) === [$messages.AffectedHistory](../types/messages.AffectedHistory.md)<a name="channels.deleteUserHistory"></a>  

***
<br><br>
$MadelineProto->[channels->editAdmin](channels.editAdmin.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), 'admin_rights' => [ChatAdminRights](../types/ChatAdminRights.md), 'rank' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="channels.editAdmin"></a>  

***
<br><br>
$MadelineProto->[channels->editBanned](channels.editBanned.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), 'banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), \]) === [$Updates](../types/Updates.md)<a name="channels.editBanned"></a>  

***
<br><br>
$MadelineProto->[channels->editCreator](channels.editCreator.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), 'password' => [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md), \]) === [$Updates](../types/Updates.md)<a name="channels.editCreator"></a>  

***
<br><br>
$MadelineProto->[channels->editLocation](channels.editLocation.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'address' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="channels.editLocation"></a>  

***
<br><br>
$MadelineProto->[channels->editPhoto](channels.editPhoto.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'photo' => [InputChatPhoto](../types/InputChatPhoto.md), \]) === [$Updates](../types/Updates.md)<a name="channels.editPhoto"></a>  

***
<br><br>
$MadelineProto->[channels->editTitle](channels.editTitle.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'title' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="channels.editTitle"></a>  

***
<br><br>
$MadelineProto->[channels->exportMessageLink](channels.exportMessageLink.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'id' => [int](../types/int.md), 'grouped' => [Bool](../types/Bool.md), \]) === [$ExportedMessageLink](../types/ExportedMessageLink.md)<a name="channels.exportMessageLink"></a>  

***
<br><br>
$MadelineProto->[channels->getAdminLog](channels.getAdminLog.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'q' => [string](../types/string.md), 'events_filter' => [ChannelAdminLogEventsFilter](../types/ChannelAdminLogEventsFilter.md), 'admins' => \[[InputUser](../types/InputUser.md)\], 'max_id' => [long](../types/long.md), 'min_id' => [long](../types/long.md), 'limit' => [int](../types/int.md), \]) === [$channels.AdminLogResults](../types/channels.AdminLogResults.md)<a name="channels.getAdminLog"></a>  

***
<br><br>
$MadelineProto->[channels->getAdminedPublicChannels](channels.getAdminedPublicChannels.md)(\['by_location' => [Bool](../types/Bool.md), 'check_limit' => [Bool](../types/Bool.md), \]) === [$messages.Chats](../types/messages.Chats.md)<a name="channels.getAdminedPublicChannels"></a>  

***
<br><br>
$MadelineProto->[channels->getChannels](channels.getChannels.md)(\['id' => \[[InputChannel](../types/InputChannel.md)\], \]) === [$messages.Chats](../types/messages.Chats.md)<a name="channels.getChannels"></a>  

***
<br><br>
$MadelineProto->[channels->getFullChannel](channels.getFullChannel.md)(\['channel' => [InputChannel](../types/InputChannel.md), \]) === [$messages.ChatFull](../types/messages.ChatFull.md)<a name="channels.getFullChannel"></a>  

***
<br><br>
$MadelineProto->[channels->getGroupsForDiscussion](channels.getGroupsForDiscussion.md)(\[\]) === [$messages.Chats](../types/messages.Chats.md)<a name="channels.getGroupsForDiscussion"></a>  

***
<br><br>
$MadelineProto->[channels->getLeftChannels](channels.getLeftChannels.md)(\['offset' => [int](../types/int.md), \]) === [$messages.Chats](../types/messages.Chats.md)<a name="channels.getLeftChannels"></a>  

***
<br><br>
$MadelineProto->[channels->getMessages](channels.getMessages.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'id' => \[[InputMessage](../types/InputMessage.md)\], \]) === [$messages.Messages](../types/messages.Messages.md)<a name="channels.getMessages"></a>  

***
<br><br>
$MadelineProto->[channels->getParticipant](channels.getParticipant.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), \]) === [$channels.ChannelParticipant](../types/channels.ChannelParticipant.md)<a name="channels.getParticipant"></a>  

***
<br><br>
$MadelineProto->[channels->getParticipants](channels.getParticipants.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'filter' => [ChannelParticipantsFilter](../types/ChannelParticipantsFilter.md), 'offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$channels.ChannelParticipants](../types/channels.ChannelParticipants.md)<a name="channels.getParticipants"></a>  

***
<br><br>
$MadelineProto->[channels->inviteToChannel](channels.inviteToChannel.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'users' => \[[InputUser](../types/InputUser.md)\], \]) === [$Updates](../types/Updates.md)<a name="channels.inviteToChannel"></a>  

***
<br><br>
$MadelineProto->[channels->joinChannel](channels.joinChannel.md)(\['channel' => [InputChannel](../types/InputChannel.md), \]) === [$Updates](../types/Updates.md)<a name="channels.joinChannel"></a>  

***
<br><br>
$MadelineProto->[channels->leaveChannel](channels.leaveChannel.md)(\['channel' => [InputChannel](../types/InputChannel.md), \]) === [$Updates](../types/Updates.md)<a name="channels.leaveChannel"></a>  

***
<br><br>
$MadelineProto->[channels->readHistory](channels.readHistory.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'max_id' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="channels.readHistory"></a>  

***
<br><br>
$MadelineProto->[channels->readMessageContents](channels.readMessageContents.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'id' => \[[int](../types/int.md)\], \]) === [$Bool](../types/Bool.md)<a name="channels.readMessageContents"></a>  

***
<br><br>
$MadelineProto->[channels->reportSpam](channels.reportSpam.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'user_id' => [InputUser](../types/InputUser.md), 'id' => \[[int](../types/int.md)\], \]) === [$Bool](../types/Bool.md)<a name="channels.reportSpam"></a>  

***
<br><br>
$MadelineProto->[channels->setDiscussionGroup](channels.setDiscussionGroup.md)(\['broadcast' => [InputChannel](../types/InputChannel.md), 'group' => [InputChannel](../types/InputChannel.md), \]) === [$Bool](../types/Bool.md)<a name="channels.setDiscussionGroup"></a>  

***
<br><br>
$MadelineProto->[channels->setStickers](channels.setStickers.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'stickerset' => [InputStickerSet](../types/InputStickerSet.md), \]) === [$Bool](../types/Bool.md)<a name="channels.setStickers"></a>  

***
<br><br>
$MadelineProto->[channels->togglePreHistoryHidden](channels.togglePreHistoryHidden.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'enabled' => [Bool](../types/Bool.md), \]) === [$Updates](../types/Updates.md)<a name="channels.togglePreHistoryHidden"></a>  

***
<br><br>
$MadelineProto->[channels->toggleSignatures](channels.toggleSignatures.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'enabled' => [Bool](../types/Bool.md), \]) === [$Updates](../types/Updates.md)<a name="channels.toggleSignatures"></a>  

***
<br><br>
$MadelineProto->[channels->toggleSlowMode](channels.toggleSlowMode.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'seconds' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="channels.toggleSlowMode"></a>  

***
<br><br>
$MadelineProto->[channels->updateUsername](channels.updateUsername.md)(\['channel' => [InputChannel](../types/InputChannel.md), 'username' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="channels.updateUsername"></a>  

***
<br><br>
$MadelineProto->[contacts->acceptContact](contacts.acceptContact.md)(\['id' => [InputUser](../types/InputUser.md), \]) === [$Updates](../types/Updates.md)<a name="contacts.acceptContact"></a>  

***
<br><br>
$MadelineProto->[contacts->addContact](contacts.addContact.md)(\['add_phone_privacy_exception' => [Bool](../types/Bool.md), 'id' => [InputUser](../types/InputUser.md), 'first_name' => [string](../types/string.md), 'last_name' => [string](../types/string.md), 'phone' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="contacts.addContact"></a>  

***
<br><br>
$MadelineProto->[contacts->block](contacts.block.md)(\['id' => [InputUser](../types/InputUser.md), \]) === [$Bool](../types/Bool.md)<a name="contacts.block"></a>  

***
<br><br>
$MadelineProto->[contacts->deleteByPhones](contacts.deleteByPhones.md)(\['phones' => \[[string](../types/string.md)\], \]) === [$Bool](../types/Bool.md)<a name="contacts.deleteByPhones"></a>  

***
<br><br>
$MadelineProto->[contacts->deleteContacts](contacts.deleteContacts.md)(\['id' => \[[InputUser](../types/InputUser.md)\], \]) === [$Updates](../types/Updates.md)<a name="contacts.deleteContacts"></a>  

***
<br><br>
$MadelineProto->[contacts->getBlocked](contacts.getBlocked.md)(\['offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$contacts.Blocked](../types/contacts.Blocked.md)<a name="contacts.getBlocked"></a>  

***
<br><br>
$MadelineProto->[contacts->getContactIDs](contacts.getContactIDs.md)(\['hash' => [int](../types/int.md), \]) === [$Vector\_of\_int](../types/int.md)<a name="contacts.getContactIDs"></a>  

***
<br><br>
$MadelineProto->[contacts->getContacts](contacts.getContacts.md)(\['hash' => [int](../types/int.md), \]) === [$contacts.Contacts](../types/contacts.Contacts.md)<a name="contacts.getContacts"></a>  

***
<br><br>
$MadelineProto->[contacts->getLocated](contacts.getLocated.md)(\['geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), \]) === [$Updates](../types/Updates.md)<a name="contacts.getLocated"></a>  

***
<br><br>
$MadelineProto->[contacts->getSaved](contacts.getSaved.md)(\[\]) === [$Vector\_of\_SavedContact](../types/SavedContact.md)<a name="contacts.getSaved"></a>  

***
<br><br>
$MadelineProto->[contacts->getStatuses](contacts.getStatuses.md)(\[\]) === [$Vector\_of\_ContactStatus](../types/ContactStatus.md)<a name="contacts.getStatuses"></a>  

***
<br><br>
$MadelineProto->[contacts->getTopPeers](contacts.getTopPeers.md)(\['correspondents' => [Bool](../types/Bool.md), 'bots_pm' => [Bool](../types/Bool.md), 'bots_inline' => [Bool](../types/Bool.md), 'phone_calls' => [Bool](../types/Bool.md), 'forward_users' => [Bool](../types/Bool.md), 'forward_chats' => [Bool](../types/Bool.md), 'groups' => [Bool](../types/Bool.md), 'channels' => [Bool](../types/Bool.md), 'offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$contacts.TopPeers](../types/contacts.TopPeers.md)<a name="contacts.getTopPeers"></a>  

***
<br><br>
$MadelineProto->[contacts->importContacts](contacts.importContacts.md)(\['contacts' => \[[InputContact](../types/InputContact.md)\], \]) === [$contacts.ImportedContacts](../types/contacts.ImportedContacts.md)<a name="contacts.importContacts"></a>  

***
<br><br>
$MadelineProto->[contacts->resetSaved](contacts.resetSaved.md)(\[\]) === [$Bool](../types/Bool.md)<a name="contacts.resetSaved"></a>  

***
<br><br>
$MadelineProto->[contacts->resetTopPeerRating](contacts.resetTopPeerRating.md)(\['category' => [TopPeerCategory](../types/TopPeerCategory.md), 'peer' => [InputPeer](../types/InputPeer.md), \]) === [$Bool](../types/Bool.md)<a name="contacts.resetTopPeerRating"></a>  

***
<br><br>
$MadelineProto->[contacts->resolveUsername](contacts.resolveUsername.md)(\['username' => [string](../types/string.md), \]) === [$contacts.ResolvedPeer](../types/contacts.ResolvedPeer.md)<a name="contacts.resolveUsername"></a>  

***
<br><br>
$MadelineProto->[contacts->search](contacts.search.md)(\['q' => [string](../types/string.md), 'limit' => [int](../types/int.md), \]) === [$contacts.Found](../types/contacts.Found.md)<a name="contacts.search"></a>  

***
<br><br>
$MadelineProto->[contacts->toggleTopPeers](contacts.toggleTopPeers.md)(\['enabled' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="contacts.toggleTopPeers"></a>  

***
<br><br>
$MadelineProto->[contacts->unblock](contacts.unblock.md)(\['id' => [InputUser](../types/InputUser.md), \]) === [$Bool](../types/Bool.md)<a name="contacts.unblock"></a>  

***
<br><br>
$MadelineProto->[folders->deleteFolder](folders.deleteFolder.md)(\['folder_id' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="folders.deleteFolder"></a>  

***
<br><br>
$MadelineProto->[folders->editPeerFolders](folders.editPeerFolders.md)(\['folder_peers' => \[[InputFolderPeer](../types/InputFolderPeer.md)\], \]) === [$Updates](../types/Updates.md)<a name="folders.editPeerFolders"></a>  

***
<br><br>
$MadelineProto->[help->acceptTermsOfService](help.acceptTermsOfService.md)(\['id' => [DataJSON](../types/DataJSON.md), \]) === [$Bool](../types/Bool.md)<a name="help.acceptTermsOfService"></a>  

***
<br><br>
$MadelineProto->[help->editUserInfo](help.editUserInfo.md)(\['user_id' => [InputUser](../types/InputUser.md), 'message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \]) === [$help.UserInfo](../types/help.UserInfo.md)<a name="help.editUserInfo"></a>  

***
<br><br>
$MadelineProto->[help->getAppChangelog](help.getAppChangelog.md)(\['prev_app_version' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="help.getAppChangelog"></a>  

***
<br><br>
$MadelineProto->[help->getAppConfig](help.getAppConfig.md)(\[\]) === [$JSONValue](../types/JSONValue.md)<a name="help.getAppConfig"></a>  

***
<br><br>
$MadelineProto->[help->getAppUpdate](help.getAppUpdate.md)(\['source' => [string](../types/string.md), \]) === [$help.AppUpdate](../types/help.AppUpdate.md)<a name="help.getAppUpdate"></a>  

***
<br><br>
$MadelineProto->[help->getCdnConfig](help.getCdnConfig.md)(\[\]) === [$CdnConfig](../types/CdnConfig.md)<a name="help.getCdnConfig"></a>  

***
<br><br>
$MadelineProto->[help->getConfig](help.getConfig.md)(\[\]) === [$Config](../types/Config.md)<a name="help.getConfig"></a>  

***
<br><br>
$MadelineProto->[help->getDeepLinkInfo](help.getDeepLinkInfo.md)(\['path' => [string](../types/string.md), \]) === [$help.DeepLinkInfo](../types/help.DeepLinkInfo.md)<a name="help.getDeepLinkInfo"></a>  

***
<br><br>
$MadelineProto->[help->getInviteText](help.getInviteText.md)(\[\]) === [$help.InviteText](../types/help.InviteText.md)<a name="help.getInviteText"></a>  

***
<br><br>
$MadelineProto->[help->getNearestDc](help.getNearestDc.md)(\[\]) === [$NearestDc](../types/NearestDc.md)<a name="help.getNearestDc"></a>  

***
<br><br>
$MadelineProto->[help->getPassportConfig](help.getPassportConfig.md)(\['hash' => [int](../types/int.md), \]) === [$help.PassportConfig](../types/help.PassportConfig.md)<a name="help.getPassportConfig"></a>  

***
<br><br>
$MadelineProto->[help->getProxyData](help.getProxyData.md)(\[\]) === [$help.ProxyData](../types/help.ProxyData.md)<a name="help.getProxyData"></a>  

***
<br><br>
$MadelineProto->[help->getRecentMeUrls](help.getRecentMeUrls.md)(\['referer' => [string](../types/string.md), \]) === [$help.RecentMeUrls](../types/help.RecentMeUrls.md)<a name="help.getRecentMeUrls"></a>  

***
<br><br>
$MadelineProto->[help->getSupport](help.getSupport.md)(\[\]) === [$help.Support](../types/help.Support.md)<a name="help.getSupport"></a>  

***
<br><br>
$MadelineProto->[help->getSupportName](help.getSupportName.md)(\[\]) === [$help.SupportName](../types/help.SupportName.md)<a name="help.getSupportName"></a>  

***
<br><br>
$MadelineProto->[help->getTermsOfServiceUpdate](help.getTermsOfServiceUpdate.md)(\[\]) === [$help.TermsOfServiceUpdate](../types/help.TermsOfServiceUpdate.md)<a name="help.getTermsOfServiceUpdate"></a>  

***
<br><br>
$MadelineProto->[help->getUserInfo](help.getUserInfo.md)(\['user_id' => [InputUser](../types/InputUser.md), \]) === [$help.UserInfo](../types/help.UserInfo.md)<a name="help.getUserInfo"></a>  

***
<br><br>
$MadelineProto->[help->saveAppLog](help.saveAppLog.md)(\['events' => \[[InputAppEvent](../types/InputAppEvent.md)\], \]) === [$Bool](../types/Bool.md)<a name="help.saveAppLog"></a>  

***
<br><br>
$MadelineProto->[help->setBotUpdatesStatus](help.setBotUpdatesStatus.md)(\['pending_updates_count' => [int](../types/int.md), 'message' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="help.setBotUpdatesStatus"></a>  

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
$MadelineProto->[langpack->getDifference](langpack.getDifference.md)(\['lang_pack' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), 'from_version' => [int](../types/int.md), \]) === [$LangPackDifference](../types/LangPackDifference.md)<a name="langpack.getDifference"></a>  

***
<br><br>
$MadelineProto->[langpack->getLangPack](langpack.getLangPack.md)(\['lang_pack' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), \]) === [$LangPackDifference](../types/LangPackDifference.md)<a name="langpack.getLangPack"></a>  

***
<br><br>
$MadelineProto->[langpack->getLanguage](langpack.getLanguage.md)(\['lang_pack' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), \]) === [$LangPackLanguage](../types/LangPackLanguage.md)<a name="langpack.getLanguage"></a>  

***
<br><br>
$MadelineProto->[langpack->getLanguages](langpack.getLanguages.md)(\['lang_pack' => [string](../types/string.md), \]) === [$Vector\_of\_LangPackLanguage](../types/LangPackLanguage.md)<a name="langpack.getLanguages"></a>  

***
<br><br>
$MadelineProto->[langpack->getStrings](langpack.getStrings.md)(\['lang_pack' => [string](../types/string.md), 'lang_code' => [string](../types/string.md), 'keys' => \[[string](../types/string.md)\], \]) === [$Vector\_of\_LangPackString](../types/LangPackString.md)<a name="langpack.getStrings"></a>  

***
<br><br>
$MadelineProto->[messages->acceptEncryption](messages.acceptEncryption.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'g_b' => [bytes](../types/bytes.md), 'key_fingerprint' => [long](../types/long.md), \]) === [$EncryptedChat](../types/EncryptedChat.md)<a name="messages.acceptEncryption"></a>  

***
<br><br>
$MadelineProto->[messages->acceptUrlAuth](messages.acceptUrlAuth.md)(\['write_allowed' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'button_id' => [int](../types/int.md), \]) === [$UrlAuthResult](../types/UrlAuthResult.md)<a name="messages.acceptUrlAuth"></a>  

***
<br><br>
$MadelineProto->[messages->addChatUser](messages.addChatUser.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), 'user_id' => [InputUser](../types/InputUser.md), 'fwd_limit' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages.addChatUser"></a>  

***
<br><br>
$MadelineProto->[messages->checkChatInvite](messages.checkChatInvite.md)(\['hash' => [string](../types/string.md), \]) === [$ChatInvite](../types/ChatInvite.md)<a name="messages.checkChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->clearAllDrafts](messages.clearAllDrafts.md)(\[\]) === [$Bool](../types/Bool.md)<a name="messages.clearAllDrafts"></a>  

***
<br><br>
$MadelineProto->[messages->clearRecentStickers](messages.clearRecentStickers.md)(\['attached' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages.clearRecentStickers"></a>  

***
<br><br>
$MadelineProto->[messages->createChat](messages.createChat.md)(\['users' => \[[InputUser](../types/InputUser.md)\], 'title' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="messages.createChat"></a>  

***
<br><br>
$MadelineProto->[messages->deleteChatUser](messages.deleteChatUser.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), 'user_id' => [InputUser](../types/InputUser.md), \]) === [$Updates](../types/Updates.md)<a name="messages.deleteChatUser"></a>  

***
<br><br>
$MadelineProto->[messages->deleteHistory](messages.deleteHistory.md)(\['just_clear' => [Bool](../types/Bool.md), 'revoke' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'max_id' => [int](../types/int.md), \]) === [$messages.AffectedHistory](../types/messages.AffectedHistory.md)<a name="messages.deleteHistory"></a>  

***
<br><br>
$MadelineProto->[messages->deleteMessages](messages.deleteMessages.md)(\['revoke' => [Bool](../types/Bool.md), 'id' => \[[int](../types/int.md)\], \]) === [$messages.AffectedMessages](../types/messages.AffectedMessages.md)<a name="messages.deleteMessages"></a>  

***
<br><br>
$MadelineProto->[messages->deleteScheduledMessages](messages.deleteScheduledMessages.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'id' => \[[int](../types/int.md)\], \]) === [$Updates](../types/Updates.md)<a name="messages.deleteScheduledMessages"></a>  

***
<br><br>
$MadelineProto->[messages->discardEncryption](messages.discardEncryption.md)(\['chat_id' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="messages.discardEncryption"></a>  

***
<br><br>
$MadelineProto->[messages->editChatAbout](messages.editChatAbout.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'about' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="messages.editChatAbout"></a>  

***
<br><br>
$MadelineProto->[messages->editChatAdmin](messages.editChatAdmin.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), 'user_id' => [InputUser](../types/InputUser.md), 'is_admin' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages.editChatAdmin"></a>  

***
<br><br>
$MadelineProto->[messages->editChatDefaultBannedRights](messages.editChatDefaultBannedRights.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'banned_rights' => [ChatBannedRights](../types/ChatBannedRights.md), \]) === [$Updates](../types/Updates.md)<a name="messages.editChatDefaultBannedRights"></a>  

***
<br><br>
$MadelineProto->[messages->editChatPhoto](messages.editChatPhoto.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), 'photo' => [InputChatPhoto](../types/InputChatPhoto.md), \]) === [$Updates](../types/Updates.md)<a name="messages.editChatPhoto"></a>  

***
<br><br>
$MadelineProto->[messages->editChatTitle](messages.editChatTitle.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), 'title' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="messages.editChatTitle"></a>  

***
<br><br>
$MadelineProto->[messages->editInlineBotMessage](messages.editInlineBotMessage.md)(\['no_webpage' => [Bool](../types/Bool.md), 'id' => [InputBotInlineMessageID](../types/InputBotInlineMessageID.md), 'message' => [string](../types/string.md), 'media' => [InputMedia](../types/InputMedia.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages.editInlineBotMessage"></a>  

***
<br><br>
$MadelineProto->[messages->editMessage](messages.editMessage.md)(\['no_webpage' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'id' => [int](../types/int.md), 'message' => [string](../types/string.md), 'media' => [InputMedia](../types/InputMedia.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'schedule_date' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages.editMessage"></a>  

***
<br><br>
$MadelineProto->[messages->exportChatInvite](messages.exportChatInvite.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$ExportedChatInvite](../types/ExportedChatInvite.md)<a name="messages.exportChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->faveSticker](messages.faveSticker.md)(\['id' => [InputDocument](../types/InputDocument.md), 'unfave' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages.faveSticker"></a>  

***
<br><br>
$MadelineProto->[messages->forwardMessages](messages.forwardMessages.md)(\['silent' => [Bool](../types/Bool.md), 'background' => [Bool](../types/Bool.md), 'with_my_score' => [Bool](../types/Bool.md), 'grouped' => [Bool](../types/Bool.md), 'from_peer' => [InputPeer](../types/InputPeer.md), 'id' => \[[int](../types/int.md)\], 'to_peer' => [InputPeer](../types/InputPeer.md), 'schedule_date' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages.forwardMessages"></a>  

***
<br><br>
$MadelineProto->[messages->getAllChats](messages.getAllChats.md)(\['except_ids' => \[[int](../types/int.md)\], \]) === [$messages.Chats](../types/messages.Chats.md)<a name="messages.getAllChats"></a>  

***
<br><br>
$MadelineProto->[messages->getAllDrafts](messages.getAllDrafts.md)(\[\]) === [$Updates](../types/Updates.md)<a name="messages.getAllDrafts"></a>  

***
<br><br>
$MadelineProto->[messages->getAllStickers](messages.getAllStickers.md)(\['hash' => [int](../types/int.md), \]) === [$messages.AllStickers](../types/messages.AllStickers.md)<a name="messages.getAllStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getArchivedStickers](messages.getArchivedStickers.md)(\['masks' => [Bool](../types/Bool.md), 'offset_id' => [long](../types/long.md), 'limit' => [int](../types/int.md), \]) === [$messages.ArchivedStickers](../types/messages.ArchivedStickers.md)<a name="messages.getArchivedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getAttachedStickers](messages.getAttachedStickers.md)(\['media' => [InputStickeredMedia](../types/InputStickeredMedia.md), \]) === [$Vector\_of\_StickerSetCovered](../types/StickerSetCovered.md)<a name="messages.getAttachedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getBotCallbackAnswer](messages.getBotCallbackAnswer.md)(\['game' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'data' => [bytes](../types/bytes.md), \]) === [$messages.BotCallbackAnswer](../types/messages.BotCallbackAnswer.md)<a name="messages.getBotCallbackAnswer"></a>  

***
<br><br>
$MadelineProto->[messages->getChats](messages.getChats.md)(\['id' => \[[int](../types/int.md)\], \]) === [$messages.Chats](../types/messages.Chats.md)<a name="messages.getChats"></a>  

***
<br><br>
$MadelineProto->[messages->getCommonChats](messages.getCommonChats.md)(\['user_id' => [InputUser](../types/InputUser.md), 'max_id' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$messages.Chats](../types/messages.Chats.md)<a name="messages.getCommonChats"></a>  

***
<br><br>
$MadelineProto->[messages->getDhConfig](messages.getDhConfig.md)(\['version' => [int](../types/int.md), 'random_length' => [int](../types/int.md), \]) === [$messages.DhConfig](../types/messages.DhConfig.md)<a name="messages.getDhConfig"></a>  

***
<br><br>
$MadelineProto->[messages->getDialogUnreadMarks](messages.getDialogUnreadMarks.md)(\[\]) === [$Vector\_of\_DialogPeer](../types/DialogPeer.md)<a name="messages.getDialogUnreadMarks"></a>  

***
<br><br>
$MadelineProto->[messages->getDialogs](messages.getDialogs.md)(\['exclude_pinned' => [Bool](../types/Bool.md), 'folder_id' => [int](../types/int.md), 'offset_date' => [int](../types/int.md), 'offset_id' => [int](../types/int.md), 'offset_peer' => [InputPeer](../types/InputPeer.md), 'limit' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$messages.Dialogs](../types/messages.Dialogs.md)<a name="messages.getDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->getDocumentByHash](messages.getDocumentByHash.md)(\['sha256' => [bytes](../types/bytes.md), 'size' => [int](../types/int.md), 'mime_type' => [string](../types/string.md), \]) === [$Document](../types/Document.md)<a name="messages.getDocumentByHash"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiKeywords](messages.getEmojiKeywords.md)(\['lang_code' => [string](../types/string.md), \]) === [$EmojiKeywordsDifference](../types/EmojiKeywordsDifference.md)<a name="messages.getEmojiKeywords"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiKeywordsDifference](messages.getEmojiKeywordsDifference.md)(\['lang_code' => [string](../types/string.md), 'from_version' => [int](../types/int.md), \]) === [$EmojiKeywordsDifference](../types/EmojiKeywordsDifference.md)<a name="messages.getEmojiKeywordsDifference"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiKeywordsLanguages](messages.getEmojiKeywordsLanguages.md)(\['lang_codes' => \[[string](../types/string.md)\], \]) === [$Vector\_of\_EmojiLanguage](../types/EmojiLanguage.md)<a name="messages.getEmojiKeywordsLanguages"></a>  

***
<br><br>
$MadelineProto->[messages->getEmojiURL](messages.getEmojiURL.md)(\['lang_code' => [string](../types/string.md), \]) === [$EmojiURL](../types/EmojiURL.md)<a name="messages.getEmojiURL"></a>  

***
<br><br>
$MadelineProto->[messages->getFavedStickers](messages.getFavedStickers.md)(\['hash' => [int](../types/int.md), \]) === [$messages.FavedStickers](../types/messages.FavedStickers.md)<a name="messages.getFavedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getFeaturedStickers](messages.getFeaturedStickers.md)(\['hash' => [int](../types/int.md), \]) === [$messages.FeaturedStickers](../types/messages.FeaturedStickers.md)<a name="messages.getFeaturedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getFullChat](messages.getFullChat.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), \]) === [$messages.ChatFull](../types/messages.ChatFull.md)<a name="messages.getFullChat"></a>  

***
<br><br>
$MadelineProto->[messages->getGameHighScores](messages.getGameHighScores.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'id' => [int](../types/int.md), 'user_id' => [InputUser](../types/InputUser.md), \]) === [$messages.HighScores](../types/messages.HighScores.md)<a name="messages.getGameHighScores"></a>  

***
<br><br>
$MadelineProto->[messages->getHistory](messages.getHistory.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'offset_id' => [int](../types/int.md), 'offset_date' => [int](../types/int.md), 'add_offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), 'max_id' => [int](../types/int.md), 'min_id' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$messages.Messages](../types/messages.Messages.md)<a name="messages.getHistory"></a>  

***
<br><br>
$MadelineProto->[messages->getInlineBotResults](messages.getInlineBotResults.md)(\['bot' => [InputUser](../types/InputUser.md), 'peer' => [InputPeer](../types/InputPeer.md), 'geo_point' => [InputGeoPoint](../types/InputGeoPoint.md), 'query' => [string](../types/string.md), 'offset' => [string](../types/string.md), \]) === [$messages.BotResults](../types/messages.BotResults.md)<a name="messages.getInlineBotResults"></a>  

***
<br><br>
$MadelineProto->[messages->getInlineGameHighScores](messages.getInlineGameHighScores.md)(\['id' => [InputBotInlineMessageID](../types/InputBotInlineMessageID.md), 'user_id' => [InputUser](../types/InputUser.md), \]) === [$messages.HighScores](../types/messages.HighScores.md)<a name="messages.getInlineGameHighScores"></a>  

***
<br><br>
$MadelineProto->[messages->getMaskStickers](messages.getMaskStickers.md)(\['hash' => [int](../types/int.md), \]) === [$messages.AllStickers](../types/messages.AllStickers.md)<a name="messages.getMaskStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getMessageEditData](messages.getMessageEditData.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'id' => [int](../types/int.md), \]) === [$messages.MessageEditData](../types/messages.MessageEditData.md)<a name="messages.getMessageEditData"></a>  

***
<br><br>
$MadelineProto->[messages->getMessages](messages.getMessages.md)(\['id' => \[[InputMessage](../types/InputMessage.md)\], \]) === [$messages.Messages](../types/messages.Messages.md)<a name="messages.getMessages"></a>  

***
<br><br>
$MadelineProto->[messages->getMessagesViews](messages.getMessagesViews.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'id' => \[[int](../types/int.md)\], 'increment' => [Bool](../types/Bool.md), \]) === [$Vector\_of\_int](../types/int.md)<a name="messages.getMessagesViews"></a>  

***
<br><br>
$MadelineProto->[messages->getOnlines](messages.getOnlines.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$ChatOnlines](../types/ChatOnlines.md)<a name="messages.getOnlines"></a>  

***
<br><br>
$MadelineProto->[messages->getPeerDialogs](messages.getPeerDialogs.md)(\['peers' => \[[InputDialogPeer](../types/InputDialogPeer.md)\], \]) === [$messages.PeerDialogs](../types/messages.PeerDialogs.md)<a name="messages.getPeerDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->getPeerSettings](messages.getPeerSettings.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$PeerSettings](../types/PeerSettings.md)<a name="messages.getPeerSettings"></a>  

***
<br><br>
$MadelineProto->[messages->getPinnedDialogs](messages.getPinnedDialogs.md)(\['folder_id' => [int](../types/int.md), \]) === [$messages.PeerDialogs](../types/messages.PeerDialogs.md)<a name="messages.getPinnedDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->getPollResults](messages.getPollResults.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages.getPollResults"></a>  

***
<br><br>
$MadelineProto->[messages->getRecentLocations](messages.getRecentLocations.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'limit' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$messages.Messages](../types/messages.Messages.md)<a name="messages.getRecentLocations"></a>  

***
<br><br>
$MadelineProto->[messages->getRecentStickers](messages.getRecentStickers.md)(\['attached' => [Bool](../types/Bool.md), 'hash' => [int](../types/int.md), \]) === [$messages.RecentStickers](../types/messages.RecentStickers.md)<a name="messages.getRecentStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getSavedGifs](messages.getSavedGifs.md)(\['hash' => [int](../types/int.md), \]) === [$messages.SavedGifs](../types/messages.SavedGifs.md)<a name="messages.getSavedGifs"></a>  

***
<br><br>
$MadelineProto->[messages->getScheduledHistory](messages.getScheduledHistory.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'hash' => [int](../types/int.md), \]) === [$messages.Messages](../types/messages.Messages.md)<a name="messages.getScheduledHistory"></a>  

***
<br><br>
$MadelineProto->[messages->getScheduledMessages](messages.getScheduledMessages.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'id' => \[[int](../types/int.md)\], \]) === [$messages.Messages](../types/messages.Messages.md)<a name="messages.getScheduledMessages"></a>  

***
<br><br>
$MadelineProto->[messages->getSearchCounters](messages.getSearchCounters.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'filters' => \[[MessagesFilter](../types/MessagesFilter.md)\], \]) === [$Vector\_of\_messages.SearchCounter](../types/messages.SearchCounter.md)<a name="messages.getSearchCounters"></a>  

***
<br><br>
$MadelineProto->[messages->getSplitRanges](messages.getSplitRanges.md)(\[\]) === [$Vector\_of\_MessageRange](../types/MessageRange.md)<a name="messages.getSplitRanges"></a>  

***
<br><br>
$MadelineProto->[messages->getStatsURL](messages.getStatsURL.md)(\['dark' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'params' => [string](../types/string.md), \]) === [$StatsURL](../types/StatsURL.md)<a name="messages.getStatsURL"></a>  

***
<br><br>
$MadelineProto->[messages->getStickerSet](messages.getStickerSet.md)(\['stickerset' => [InputStickerSet](../types/InputStickerSet.md), \]) === [$messages.StickerSet](../types/messages.StickerSet.md)<a name="messages.getStickerSet"></a>  

***
<br><br>
$MadelineProto->[messages->getStickers](messages.getStickers.md)(\['emoticon' => [string](../types/string.md), 'hash' => [int](../types/int.md), \]) === [$messages.Stickers](../types/messages.Stickers.md)<a name="messages.getStickers"></a>  

***
<br><br>
$MadelineProto->[messages->getUnreadMentions](messages.getUnreadMentions.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'offset_id' => [int](../types/int.md), 'add_offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), 'max_id' => [int](../types/int.md), 'min_id' => [int](../types/int.md), \]) === [$messages.Messages](../types/messages.Messages.md)<a name="messages.getUnreadMentions"></a>  

***
<br><br>
$MadelineProto->[messages->getWebPage](messages.getWebPage.md)(\['url' => [string](../types/string.md), 'hash' => [int](../types/int.md), \]) === [$WebPage](../types/WebPage.md)<a name="messages.getWebPage"></a>  

***
<br><br>
$MadelineProto->[messages->getWebPagePreview](messages.getWebPagePreview.md)(\['message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \]) === [$MessageMedia](../types/MessageMedia.md)<a name="messages.getWebPagePreview"></a>  

***
<br><br>
$MadelineProto->[messages->hidePeerSettingsBar](messages.hidePeerSettingsBar.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$Bool](../types/Bool.md)<a name="messages.hidePeerSettingsBar"></a>  

***
<br><br>
$MadelineProto->[messages->importChatInvite](messages.importChatInvite.md)(\['hash' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="messages.importChatInvite"></a>  

***
<br><br>
$MadelineProto->[messages->installStickerSet](messages.installStickerSet.md)(\['stickerset' => [InputStickerSet](../types/InputStickerSet.md), 'archived' => [Bool](../types/Bool.md), \]) === [$messages.StickerSetInstallResult](../types/messages.StickerSetInstallResult.md)<a name="messages.installStickerSet"></a>  

***
<br><br>
$MadelineProto->[messages->markDialogUnread](messages.markDialogUnread.md)(\['unread' => [Bool](../types/Bool.md), 'peer' => [InputDialogPeer](../types/InputDialogPeer.md), \]) === [$Bool](../types/Bool.md)<a name="messages.markDialogUnread"></a>  

***
<br><br>
$MadelineProto->[messages->migrateChat](messages.migrateChat.md)(\['chat_id' => [InputPeer](../types/InputPeer.md), \]) === [$Updates](../types/Updates.md)<a name="messages.migrateChat"></a>  

***
<br><br>
$MadelineProto->[messages->readEncryptedHistory](messages.readEncryptedHistory.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'max_date' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="messages.readEncryptedHistory"></a>  

***
<br><br>
$MadelineProto->[messages->readFeaturedStickers](messages.readFeaturedStickers.md)(\['id' => \[[long](../types/long.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages.readFeaturedStickers"></a>  

***
<br><br>
$MadelineProto->[messages->readHistory](messages.readHistory.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'max_id' => [int](../types/int.md), \]) === [$messages.AffectedMessages](../types/messages.AffectedMessages.md)<a name="messages.readHistory"></a>  

***
<br><br>
$MadelineProto->[messages->readMentions](messages.readMentions.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$messages.AffectedHistory](../types/messages.AffectedHistory.md)<a name="messages.readMentions"></a>  

***
<br><br>
$MadelineProto->[messages->readMessageContents](messages.readMessageContents.md)(\['id' => \[[int](../types/int.md)\], \]) === [$messages.AffectedMessages](../types/messages.AffectedMessages.md)<a name="messages.readMessageContents"></a>  

***
<br><br>
$MadelineProto->[messages->receivedMessages](messages.receivedMessages.md)(\['max_id' => [int](../types/int.md), \]) === [$Vector\_of\_ReceivedNotifyMessage](../types/ReceivedNotifyMessage.md)<a name="messages.receivedMessages"></a>  

***
<br><br>
$MadelineProto->[messages->receivedQueue](messages.receivedQueue.md)(\['max_qts' => [int](../types/int.md), \]) === [$Vector\_of\_long](../types/long.md)<a name="messages.receivedQueue"></a>  

***
<br><br>
$MadelineProto->[messages->reorderPinnedDialogs](messages.reorderPinnedDialogs.md)(\['force' => [Bool](../types/Bool.md), 'folder_id' => [int](../types/int.md), 'order' => \[[InputDialogPeer](../types/InputDialogPeer.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages.reorderPinnedDialogs"></a>  

***
<br><br>
$MadelineProto->[messages->reorderStickerSets](messages.reorderStickerSets.md)(\['masks' => [Bool](../types/Bool.md), 'order' => \[[long](../types/long.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages.reorderStickerSets"></a>  

***
<br><br>
$MadelineProto->[messages->report](messages.report.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'id' => \[[int](../types/int.md)\], 'reason' => [ReportReason](../types/ReportReason.md), \]) === [$Bool](../types/Bool.md)<a name="messages.report"></a>  

***
<br><br>
$MadelineProto->[messages->reportEncryptedSpam](messages.reportEncryptedSpam.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), \]) === [$Bool](../types/Bool.md)<a name="messages.reportEncryptedSpam"></a>  

***
<br><br>
$MadelineProto->[messages->reportSpam](messages.reportSpam.md)(\['peer' => [InputPeer](../types/InputPeer.md), \]) === [$Bool](../types/Bool.md)<a name="messages.reportSpam"></a>  

***
<br><br>
$MadelineProto->[messages->requestEncryption](messages.requestEncryption.md)(\['user_id' => [InputUser](../types/InputUser.md), 'g_a' => [bytes](../types/bytes.md), \]) === [$EncryptedChat](../types/EncryptedChat.md)<a name="messages.requestEncryption"></a>  

***
<br><br>
$MadelineProto->[messages->requestUrlAuth](messages.requestUrlAuth.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'button_id' => [int](../types/int.md), \]) === [$UrlAuthResult](../types/UrlAuthResult.md)<a name="messages.requestUrlAuth"></a>  

***
<br><br>
$MadelineProto->[messages->saveDraft](messages.saveDraft.md)(\['no_webpage' => [Bool](../types/Bool.md), 'reply_to_msg_id' => [int](../types/int.md), 'peer' => [InputPeer](../types/InputPeer.md), 'message' => [string](../types/string.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages.saveDraft"></a>  

***
<br><br>
$MadelineProto->[messages->saveGif](messages.saveGif.md)(\['id' => [InputDocument](../types/InputDocument.md), 'unsave' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages.saveGif"></a>  

***
<br><br>
$MadelineProto->[messages->saveRecentSticker](messages.saveRecentSticker.md)(\['attached' => [Bool](../types/Bool.md), 'id' => [InputDocument](../types/InputDocument.md), 'unsave' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages.saveRecentSticker"></a>  

***
<br><br>
$MadelineProto->[messages->search](messages.search.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'q' => [string](../types/string.md), 'from_id' => [InputUser](../types/InputUser.md), 'filter' => [MessagesFilter](../types/MessagesFilter.md), 'min_date' => [int](../types/int.md), 'max_date' => [int](../types/int.md), 'offset_id' => [int](../types/int.md), 'add_offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), 'max_id' => [int](../types/int.md), 'min_id' => [int](../types/int.md), 'hash' => [int](../types/int.md), \]) === [$messages.Messages](../types/messages.Messages.md)<a name="messages.search"></a>  

***
<br><br>
$MadelineProto->[messages->searchGifs](messages.searchGifs.md)(\['q' => [string](../types/string.md), 'offset' => [int](../types/int.md), \]) === [$messages.FoundGifs](../types/messages.FoundGifs.md)<a name="messages.searchGifs"></a>  

***
<br><br>
$MadelineProto->[messages->searchGlobal](messages.searchGlobal.md)(\['folder_id' => [int](../types/int.md), 'q' => [string](../types/string.md), 'offset_rate' => [int](../types/int.md), 'offset_peer' => [InputPeer](../types/InputPeer.md), 'offset_id' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$messages.Messages](../types/messages.Messages.md)<a name="messages.searchGlobal"></a>  

***
<br><br>
$MadelineProto->[messages->searchStickerSets](messages.searchStickerSets.md)(\['exclude_featured' => [Bool](../types/Bool.md), 'q' => [string](../types/string.md), 'hash' => [int](../types/int.md), \]) === [$messages.FoundStickerSets](../types/messages.FoundStickerSets.md)<a name="messages.searchStickerSets"></a>  

***
<br><br>
$MadelineProto->[messages->sendEncrypted](messages.sendEncrypted.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'data' => [bytes](../types/bytes.md), \]) === [$messages.SentEncryptedMessage](../types/messages.SentEncryptedMessage.md)<a name="messages.sendEncrypted"></a>  

***
<br><br>
$MadelineProto->[messages->sendEncryptedFile](messages.sendEncryptedFile.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'data' => [bytes](../types/bytes.md), 'file' => [InputEncryptedFile](../types/InputEncryptedFile.md), \]) === [$messages.SentEncryptedMessage](../types/messages.SentEncryptedMessage.md)<a name="messages.sendEncryptedFile"></a>  

***
<br><br>
$MadelineProto->[messages->sendEncryptedService](messages.sendEncryptedService.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'data' => [bytes](../types/bytes.md), \]) === [$messages.SentEncryptedMessage](../types/messages.SentEncryptedMessage.md)<a name="messages.sendEncryptedService"></a>  

***
<br><br>
$MadelineProto->[messages->sendInlineBotResult](messages.sendInlineBotResult.md)(\['silent' => [Bool](../types/Bool.md), 'background' => [Bool](../types/Bool.md), 'clear_draft' => [Bool](../types/Bool.md), 'hide_via' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'reply_to_msg_id' => [int](../types/int.md), 'query_id' => [long](../types/long.md), 'id' => [string](../types/string.md), 'schedule_date' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages.sendInlineBotResult"></a>  

***
<br><br>
$MadelineProto->[messages->sendMedia](messages.sendMedia.md)(\['silent' => [Bool](../types/Bool.md), 'background' => [Bool](../types/Bool.md), 'clear_draft' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'reply_to_msg_id' => [int](../types/int.md), 'media' => [InputMedia](../types/InputMedia.md), 'message' => [string](../types/string.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'schedule_date' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages.sendMedia"></a>  

***
<br><br>
$MadelineProto->[messages->sendMessage](messages.sendMessage.md)(\['no_webpage' => [Bool](../types/Bool.md), 'silent' => [Bool](../types/Bool.md), 'background' => [Bool](../types/Bool.md), 'clear_draft' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'reply_to_msg_id' => [int](../types/int.md), 'message' => [string](../types/string.md), 'reply_markup' => [ReplyMarkup](../types/ReplyMarkup.md), 'entities' => \[[MessageEntity](../types/MessageEntity.md)\], 'schedule_date' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages.sendMessage"></a>  

***
<br><br>
$MadelineProto->[messages->sendMultiMedia](messages.sendMultiMedia.md)(\['silent' => [Bool](../types/Bool.md), 'background' => [Bool](../types/Bool.md), 'clear_draft' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'reply_to_msg_id' => [int](../types/int.md), 'multi_media' => \[[InputSingleMedia](../types/InputSingleMedia.md)\], 'schedule_date' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages.sendMultiMedia"></a>  

***
<br><br>
$MadelineProto->[messages->sendScheduledMessages](messages.sendScheduledMessages.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'id' => \[[int](../types/int.md)\], \]) === [$Updates](../types/Updates.md)<a name="messages.sendScheduledMessages"></a>  

***
<br><br>
$MadelineProto->[messages->sendScreenshotNotification](messages.sendScreenshotNotification.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'reply_to_msg_id' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages.sendScreenshotNotification"></a>  

***
<br><br>
$MadelineProto->[messages->sendVote](messages.sendVote.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'msg_id' => [int](../types/int.md), 'options' => \[[bytes](../types/bytes.md)\], \]) === [$Updates](../types/Updates.md)<a name="messages.sendVote"></a>  

***
<br><br>
$MadelineProto->[messages->setBotCallbackAnswer](messages.setBotCallbackAnswer.md)(\['alert' => [Bool](../types/Bool.md), 'query_id' => [long](../types/long.md), 'message' => [string](../types/string.md), 'url' => [string](../types/string.md), 'cache_time' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="messages.setBotCallbackAnswer"></a>  

***
<br><br>
$MadelineProto->[messages->setBotPrecheckoutResults](messages.setBotPrecheckoutResults.md)(\['success' => [Bool](../types/Bool.md), 'query_id' => [long](../types/long.md), 'error' => [string](../types/string.md), \]) === [$Bool](../types/Bool.md)<a name="messages.setBotPrecheckoutResults"></a>  

***
<br><br>
$MadelineProto->[messages->setBotShippingResults](messages.setBotShippingResults.md)(\['query_id' => [long](../types/long.md), 'error' => [string](../types/string.md), 'shipping_options' => \[[ShippingOption](../types/ShippingOption.md)\], \]) === [$Bool](../types/Bool.md)<a name="messages.setBotShippingResults"></a>  

***
<br><br>
$MadelineProto->[messages->setEncryptedTyping](messages.setEncryptedTyping.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'typing' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="messages.setEncryptedTyping"></a>  

***
<br><br>
$MadelineProto->[messages->setGameScore](messages.setGameScore.md)(\['edit_message' => [Bool](../types/Bool.md), 'force' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'id' => [int](../types/int.md), 'user_id' => [InputUser](../types/InputUser.md), 'score' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages.setGameScore"></a>  

***
<br><br>
$MadelineProto->[messages->setInlineBotResults](messages.setInlineBotResults.md)(\['gallery' => [Bool](../types/Bool.md), 'private' => [Bool](../types/Bool.md), 'query_id' => [long](../types/long.md), 'results' => \[[InputBotInlineResult](../types/InputBotInlineResult.md)\], 'cache_time' => [int](../types/int.md), 'next_offset' => [string](../types/string.md), 'switch_pm' => [InlineBotSwitchPM](../types/InlineBotSwitchPM.md), \]) === [$Bool](../types/Bool.md)<a name="messages.setInlineBotResults"></a>  

***
<br><br>
$MadelineProto->[messages->setInlineGameScore](messages.setInlineGameScore.md)(\['edit_message' => [Bool](../types/Bool.md), 'force' => [Bool](../types/Bool.md), 'id' => [InputBotInlineMessageID](../types/InputBotInlineMessageID.md), 'user_id' => [InputUser](../types/InputUser.md), 'score' => [int](../types/int.md), \]) === [$Bool](../types/Bool.md)<a name="messages.setInlineGameScore"></a>  

***
<br><br>
$MadelineProto->[messages->setTyping](messages.setTyping.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'action' => [SendMessageAction](../types/SendMessageAction.md), \]) === [$Bool](../types/Bool.md)<a name="messages.setTyping"></a>  

***
<br><br>
$MadelineProto->[messages->startBot](messages.startBot.md)(\['bot' => [InputUser](../types/InputUser.md), 'peer' => [InputPeer](../types/InputPeer.md), 'start_param' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="messages.startBot"></a>  

***
<br><br>
$MadelineProto->[messages->toggleDialogPin](messages.toggleDialogPin.md)(\['pinned' => [Bool](../types/Bool.md), 'peer' => [InputDialogPeer](../types/InputDialogPeer.md), \]) === [$Bool](../types/Bool.md)<a name="messages.toggleDialogPin"></a>  

***
<br><br>
$MadelineProto->[messages->uninstallStickerSet](messages.uninstallStickerSet.md)(\['stickerset' => [InputStickerSet](../types/InputStickerSet.md), \]) === [$Bool](../types/Bool.md)<a name="messages.uninstallStickerSet"></a>  

***
<br><br>
$MadelineProto->[messages->updatePinnedMessage](messages.updatePinnedMessage.md)(\['silent' => [Bool](../types/Bool.md), 'peer' => [InputPeer](../types/InputPeer.md), 'id' => [int](../types/int.md), \]) === [$Updates](../types/Updates.md)<a name="messages.updatePinnedMessage"></a>  

***
<br><br>
$MadelineProto->[messages->uploadEncryptedFile](messages.uploadEncryptedFile.md)(\['peer' => [InputEncryptedChat](../types/InputEncryptedChat.md), 'file' => [InputEncryptedFile](../types/InputEncryptedFile.md), \]) === [$EncryptedFile](../types/EncryptedFile.md)<a name="messages.uploadEncryptedFile"></a>  

***
<br><br>
$MadelineProto->[messages->uploadMedia](messages.uploadMedia.md)(\['peer' => [InputPeer](../types/InputPeer.md), 'media' => [InputMedia](../types/InputMedia.md), \]) === [$MessageMedia](../types/MessageMedia.md)<a name="messages.uploadMedia"></a>  

***
<br><br>
$MadelineProto->[payments->clearSavedInfo](payments.clearSavedInfo.md)(\['credentials' => [Bool](../types/Bool.md), 'info' => [Bool](../types/Bool.md), \]) === [$Bool](../types/Bool.md)<a name="payments.clearSavedInfo"></a>  

***
<br><br>
$MadelineProto->[payments->getPaymentForm](payments.getPaymentForm.md)(\['msg_id' => [int](../types/int.md), \]) === [$payments.PaymentForm](../types/payments.PaymentForm.md)<a name="payments.getPaymentForm"></a>  

***
<br><br>
$MadelineProto->[payments->getPaymentReceipt](payments.getPaymentReceipt.md)(\['msg_id' => [int](../types/int.md), \]) === [$payments.PaymentReceipt](../types/payments.PaymentReceipt.md)<a name="payments.getPaymentReceipt"></a>  

***
<br><br>
$MadelineProto->[payments->getSavedInfo](payments.getSavedInfo.md)(\[\]) === [$payments.SavedInfo](../types/payments.SavedInfo.md)<a name="payments.getSavedInfo"></a>  

***
<br><br>
$MadelineProto->[payments->sendPaymentForm](payments.sendPaymentForm.md)(\['msg_id' => [int](../types/int.md), 'requested_info_id' => [string](../types/string.md), 'shipping_option_id' => [string](../types/string.md), 'credentials' => [InputPaymentCredentials](../types/InputPaymentCredentials.md), \]) === [$payments.PaymentResult](../types/payments.PaymentResult.md)<a name="payments.sendPaymentForm"></a>  

***
<br><br>
$MadelineProto->[payments->validateRequestedInfo](payments.validateRequestedInfo.md)(\['save' => [Bool](../types/Bool.md), 'msg_id' => [int](../types/int.md), 'info' => [PaymentRequestedInfo](../types/PaymentRequestedInfo.md), \]) === [$payments.ValidatedRequestedInfo](../types/payments.ValidatedRequestedInfo.md)<a name="payments.validateRequestedInfo"></a>  

***
<br><br>
$MadelineProto->[phone->acceptCall](phone.acceptCall.md)(\['peer' => [InputPhoneCall](../types/InputPhoneCall.md), 'g_b' => [bytes](../types/bytes.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), \]) === [$phone.PhoneCall](../types/phone.PhoneCall.md)<a name="phone.acceptCall"></a>  

***
<br><br>
$MadelineProto->[phone->confirmCall](phone.confirmCall.md)(\['peer' => [InputPhoneCall](../types/InputPhoneCall.md), 'g_a' => [bytes](../types/bytes.md), 'key_fingerprint' => [long](../types/long.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), \]) === [$phone.PhoneCall](../types/phone.PhoneCall.md)<a name="phone.confirmCall"></a>  

***
<br><br>
$MadelineProto->[phone->discardCall](phone.discardCall.md)(\['video' => [Bool](../types/Bool.md), 'peer' => [InputPhoneCall](../types/InputPhoneCall.md), 'duration' => [int](../types/int.md), 'reason' => [PhoneCallDiscardReason](../types/PhoneCallDiscardReason.md), 'connection_id' => [long](../types/long.md), \]) === [$Updates](../types/Updates.md)<a name="phone.discardCall"></a>  

***
<br><br>
$MadelineProto->[phone->getCallConfig](phone.getCallConfig.md)(\[\]) === [$DataJSON](../types/DataJSON.md)<a name="phone.getCallConfig"></a>  

***
<br><br>
$MadelineProto->[phone->receivedCall](phone.receivedCall.md)(\['peer' => [InputPhoneCall](../types/InputPhoneCall.md), \]) === [$Bool](../types/Bool.md)<a name="phone.receivedCall"></a>  

***
<br><br>
$MadelineProto->[phone->requestCall](phone.requestCall.md)(\['video' => [Bool](../types/Bool.md), 'user_id' => [InputUser](../types/InputUser.md), 'g_a_hash' => [bytes](../types/bytes.md), 'protocol' => [PhoneCallProtocol](../types/PhoneCallProtocol.md), \]) === [$phone.PhoneCall](../types/phone.PhoneCall.md)<a name="phone.requestCall"></a>  

***
<br><br>
$MadelineProto->[phone->saveCallDebug](phone.saveCallDebug.md)(\['peer' => [InputPhoneCall](../types/InputPhoneCall.md), 'debug' => [DataJSON](../types/DataJSON.md), \]) === [$Bool](../types/Bool.md)<a name="phone.saveCallDebug"></a>  

***
<br><br>
$MadelineProto->[phone->setCallRating](phone.setCallRating.md)(\['user_initiative' => [Bool](../types/Bool.md), 'peer' => [InputPhoneCall](../types/InputPhoneCall.md), 'rating' => [int](../types/int.md), 'comment' => [string](../types/string.md), \]) === [$Updates](../types/Updates.md)<a name="phone.setCallRating"></a>  

***
<br><br>
$MadelineProto->[photos->deletePhotos](photos.deletePhotos.md)(\['id' => \[[InputPhoto](../types/InputPhoto.md)\], \]) === [$Vector\_of\_long](../types/long.md)<a name="photos.deletePhotos"></a>  

***
<br><br>
$MadelineProto->[photos->getUserPhotos](photos.getUserPhotos.md)(\['user_id' => [InputUser](../types/InputUser.md), 'offset' => [int](../types/int.md), 'max_id' => [long](../types/long.md), 'limit' => [int](../types/int.md), \]) === [$photos.Photos](../types/photos.Photos.md)<a name="photos.getUserPhotos"></a>  

***
<br><br>
$MadelineProto->[photos->updateProfilePhoto](photos.updateProfilePhoto.md)(\['id' => [InputPhoto](../types/InputPhoto.md), \]) === [$UserProfilePhoto](../types/UserProfilePhoto.md)<a name="photos.updateProfilePhoto"></a>  

***
<br><br>
$MadelineProto->[photos->uploadProfilePhoto](photos.uploadProfilePhoto.md)(\['file' => [InputFile](../types/InputFile.md), \]) === [$photos.Photo](../types/photos.Photo.md)<a name="photos.uploadProfilePhoto"></a>  

***
<br><br>
$MadelineProto->[stickers->addStickerToSet](stickers.addStickerToSet.md)(\['stickerset' => [InputStickerSet](../types/InputStickerSet.md), 'sticker' => [InputStickerSetItem](../types/InputStickerSetItem.md), \]) === [$messages.StickerSet](../types/messages.StickerSet.md)<a name="stickers.addStickerToSet"></a>  

***
<br><br>
$MadelineProto->[stickers->changeStickerPosition](stickers.changeStickerPosition.md)(\['sticker' => [InputDocument](../types/InputDocument.md), 'position' => [int](../types/int.md), \]) === [$messages.StickerSet](../types/messages.StickerSet.md)<a name="stickers.changeStickerPosition"></a>  

***
<br><br>
$MadelineProto->[stickers->createStickerSet](stickers.createStickerSet.md)(\['masks' => [Bool](../types/Bool.md), 'user_id' => [InputUser](../types/InputUser.md), 'title' => [string](../types/string.md), 'short_name' => [string](../types/string.md), 'stickers' => \[[InputStickerSetItem](../types/InputStickerSetItem.md)\], \]) === [$messages.StickerSet](../types/messages.StickerSet.md)<a name="stickers.createStickerSet"></a>  

***
<br><br>
$MadelineProto->[stickers->removeStickerFromSet](stickers.removeStickerFromSet.md)(\['sticker' => [InputDocument](../types/InputDocument.md), \]) === [$messages.StickerSet](../types/messages.StickerSet.md)<a name="stickers.removeStickerFromSet"></a>  

***
<br><br>
$MadelineProto->[updates->getChannelDifference](updates.getChannelDifference.md)(\['force' => [Bool](../types/Bool.md), 'channel' => [InputChannel](../types/InputChannel.md), 'filter' => [ChannelMessagesFilter](../types/ChannelMessagesFilter.md), 'pts' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$updates.ChannelDifference](../types/updates.ChannelDifference.md)<a name="updates.getChannelDifference"></a>  

***
<br><br>
$MadelineProto->[updates->getDifference](updates.getDifference.md)(\['pts' => [int](../types/int.md), 'pts_total_limit' => [int](../types/int.md), 'date' => [int](../types/int.md), 'qts' => [int](../types/int.md), \]) === [$updates.Difference](../types/updates.Difference.md)<a name="updates.getDifference"></a>  

***
<br><br>
$MadelineProto->[updates->getState](updates.getState.md)(\[\]) === [$updates.State](../types/updates.State.md)<a name="updates.getState"></a>  

***
<br><br>
$MadelineProto->[upload->getCdnFile](upload.getCdnFile.md)(\['file_token' => [bytes](../types/bytes.md), 'offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$upload.CdnFile](../types/upload.CdnFile.md)<a name="upload.getCdnFile"></a>  

***
<br><br>
$MadelineProto->[upload->getCdnFileHashes](upload.getCdnFileHashes.md)(\['file_token' => [bytes](../types/bytes.md), 'offset' => [int](../types/int.md), \]) === [$Vector\_of\_FileHash](../types/FileHash.md)<a name="upload.getCdnFileHashes"></a>  

***
<br><br>
$MadelineProto->[upload->getFile](upload.getFile.md)(\['precise' => [Bool](../types/Bool.md), 'location' => [InputFileLocation](../types/InputFileLocation.md), 'offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$upload.File](../types/upload.File.md)<a name="upload.getFile"></a>  

***
<br><br>
$MadelineProto->[upload->getFileHashes](upload.getFileHashes.md)(\['location' => [InputFileLocation](../types/InputFileLocation.md), 'offset' => [int](../types/int.md), \]) === [$Vector\_of\_FileHash](../types/FileHash.md)<a name="upload.getFileHashes"></a>  

***
<br><br>
$MadelineProto->[upload->getWebFile](upload.getWebFile.md)(\['location' => [InputWebFileLocation](../types/InputWebFileLocation.md), 'offset' => [int](../types/int.md), 'limit' => [int](../types/int.md), \]) === [$upload.WebFile](../types/upload.WebFile.md)<a name="upload.getWebFile"></a>  

***
<br><br>
$MadelineProto->[upload->reuploadCdnFile](upload.reuploadCdnFile.md)(\['file_token' => [bytes](../types/bytes.md), 'request_token' => [bytes](../types/bytes.md), \]) === [$Vector\_of\_FileHash](../types/FileHash.md)<a name="upload.reuploadCdnFile"></a>  

***
<br><br>
$MadelineProto->[upload->saveBigFilePart](upload.saveBigFilePart.md)(\['file_id' => [long](../types/long.md), 'file_part' => [int](../types/int.md), 'file_total_parts' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \]) === [$Bool](../types/Bool.md)<a name="upload.saveBigFilePart"></a>  

***
<br><br>
$MadelineProto->[upload->saveFilePart](upload.saveFilePart.md)(\['file_id' => [long](../types/long.md), 'file_part' => [int](../types/int.md), 'bytes' => [bytes](../types/bytes.md), \]) === [$Bool](../types/Bool.md)<a name="upload.saveFilePart"></a>  

***
<br><br>
$MadelineProto->[users->getFullUser](users.getFullUser.md)(\['id' => [InputUser](../types/InputUser.md), \]) === [$UserFull](../types/UserFull.md)<a name="users.getFullUser"></a>  

***
<br><br>
$MadelineProto->[users->getUsers](users.getUsers.md)(\['id' => \[[InputUser](../types/InputUser.md)\], \]) === [$Vector\_of\_User](../types/User.md)<a name="users.getUsers"></a>  

***
<br><br>
$MadelineProto->[users->setSecureValueErrors](users.setSecureValueErrors.md)(\['id' => [InputUser](../types/InputUser.md), 'errors' => \[[SecureValueError](../types/SecureValueError.md)\], \]) === [$Bool](../types/Bool.md)<a name="users.setSecureValueErrors"></a>  

