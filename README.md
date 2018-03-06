ws-cli-adfs
This project provides *aws-adfs-login* script which can be used to get AWS session credentials using authentication based on SAML and Active Directory Federation Services.
To use this script you have to have your Active Directory Federation Services configured and working and please make sure you are able to login to AWS Console before you try to use the script.

## Installation

The project is available as pip package, so to install it just invoke pip:
```
pip install aws-cli-adfs
```

## Basic usage
* Create a new profile in *~/.aws/config* file. You can find sample configuration below
* Make sure to put proper *idp_entry_url* and *idp_role_arn*. These two are required. *idp_username* is not required and you will be asked for it if you do not specify it in the config file. If you are unsure about the values, ask your administrator.
* Select the above configured AWS CLI profile: ```export AWS_PROFILE=dev```
* Invoke aws-adfs-login. You will be asked for the password and MFA token (for details about MFA - see below):
```
$ /aws-adfs-login
Password:
Signing in as example\luktom
MFA token: 123456

------------------------------------------------------------------------------------
Your are now signed in. The token will expire at 2018-03-06T09:57:38Z.
After this time, you may safely rerun this script to refresh your access key pair.
------------------------------------------------------------------------------------
```
* The script has saved credentials to *~/.aws/credentials* file, under the profile section, so now you are able to run any AWS CLI command.

## Sample configuration (~/.aws/config)
```
[profile dev]
idp_entry_url = https://adfs.example.luktom.net/adfs/ls/idpInitiatedSignOn.aspx?loginToRp=urn:amazon:webservices
idp_username = domain\luktom
idp_role_arn = arn:aws:iam::123456789012:role/administrators

[profile prod]
idp_entry_url = https://adfs.example.luktom.net/adfs/ls/idpInitiatedSignOn.aspx?loginToRp=urn:amazon:webservices
idp_username = domain\luktom
idp_role_arn = arn:aws:iam::123456789013:role/administrators
```
## MFA support
The script is compatible and was tested with [AdfsTotpAuthenticationProvider](https://github.com/tomaszkiewicz/AdfsTotpAuthenticationProvider) - the other project I have developed which provides easy to use TOTP-based (Google Authenticator, Authy and others) adapter for MFA.

## Compatibility
The script was written with ADFS in mind but it's possible that it will work also with other IdP.
The script was tested with ADFS working on Windows Server 2016.
The script is compatible with [AdfsTotpAuthenticationProvider](https://github.com/tomaszkiewicz/AdfsTotpAuthenticationProvider) for TOTP-based MFA. It was not tested with other MFA adapters.

## Credits
The code is based on [the article](https://aws.amazon.com/blogs/security/how-to-implement-a-general-solution-for-federated-apicli-access-using-saml-2-0/) and sample code provided there.

## License
MIT, see [details](LICENSE).
