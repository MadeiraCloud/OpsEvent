action_internal = {
	'internal'	:	{
		# send an email
		'email'	:	{
			'module'	:	'internal.email',
			'distro'	:	None,
			'reference'	:	{
				'en'	:	'''
### Description
Send a report by email

### Parameters
				''',
				'cn'	:	''''''
			},
			'parameter'	:	{
			}
		},

		# reload states
		'reload'	:	{
			'module'	:	'internal.reload',
			'distro'	:	None,
			'reference'	:	{
				'en'	:	'''
### Description
Reload states of current application

### Parameters
				''',
				'cn'	:	''''''
			},
			'parameter'	:	{
			}
		}
	}
}
