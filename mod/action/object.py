action_object = {
	'object'	:	{
		# append a file
		'file'	:	{
			'module'	:	'object.file',
			'distro'	:	None,
			'reference'	:	{
				'en'	:	'''
### Description
Add the associated event's timestamp to a specified file

### Parameters

*   **`path`** (*required*): the path to the file

		example:
			/path/to/file
				''',
				'cn'	:	''''''
			},
			'parameter'	:	{
				'path'		:	{
					'type'		:	'line',
					'required'	:	True,
					'visible'	:	True
				}
			}
		},

		# execute a script
		'script'	:	{
			'module'	:	'object.script',
			'distro'	:	None,
			'reference'	:	{
				'en'	:	'''
### Description
Run a script

### Parameters

*   **`path`** (*required*): the path to the script

		example:
			/path/to/script
				''',
				'cn'	:	''''''
			},
			'parameter'	:	{
				'path'		:	{
					'type'		:	'line',
					'required'	:	True,
					'visible'	:	True
				}
			}
		}
	}
}
