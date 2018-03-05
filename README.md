# Sample configuration (~/.aws/config)

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
