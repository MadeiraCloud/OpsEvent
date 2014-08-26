event_internal = {
	'internal'	:	{
		# handle state failure change
		'state_failure'	:	{
			'module'	:	'internal.state_failure',
			'distro'	:	None,
			'reference'	:	{
				'en'	:	'''
### Description
Trigger change specified state from `Succeed` or `None` to `Failure`

### Parameters

*   **`states`** (*required*): State(s) to watch

		example:
			@{host.state.1}

*   **`action`** (*optional*): action to execute if the state fails

		example:
			@{host.action.1}
				''',
				'cn'	:	''''''
			},
			'parameter'	:	{
				'states'	:	{
					'type'		:	'array',
					'required'	:	True,
					'visible'	:	True
				},
				'action'	:	{
					'type'		:	'action',#state?
					'required'	:	False,
					'visible'	:	True
				}
			}
		},

		# handle SNS event
		'sns'	:	{
			'module'	:	'internal.sns',
			'distro'	:	None,
			'reference'	:	{
				'en'	:	'''
### Description
Trigger AWS SNS message

### Parameters

*   **`id`** (*required*): Topic subscription ID(s)

		example:
			id-xxx

		example:
			id-xxx
			id-yyy

*   **`action`** (*optional*): action to execute if the state fails

		example:
			@{host.action.1}
				''',
				'cn'	:	''''''
			},
			'parameter'	:	{
				'id'	:	{
					'type'		:	'array',
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
