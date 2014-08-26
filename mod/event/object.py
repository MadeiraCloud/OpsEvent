event_object = {
	'object'	:	{
		# handle local file
		'file'	:	{
			'module'	:	'object.file',
			'distro'	:	None,
			'reference'	:	{
				'en'	:	'''
### Description
Trigger change on local file

### Parameters

*   **`path`** (*required*): the path to the file

		example:
			/path/to/file

*   **`action`** (*optional*): action to execute if the event is triggered

		example:
			@{host.action.1}
				''',
				'cn'	:	''''''
			},
			'parameter'	:	{
				'path'		:	{
					'type'		:	'line',
					'required'	:	True,
					'visible'	:	True
				},
				'action'	:	{
					'type'		:	'action',#state?
					'required'	:	False,
					'visible'	:	True
				}
			}
		}
	}
}
