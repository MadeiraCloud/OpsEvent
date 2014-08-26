event_remote = {
	'remote'	:	{
		# handle remote file
		'file'	:	{
			'module'	:	'remote.file',
			'distro'	:	None,
			'reference'	:	{
				'en'	:	'''
### Description
Trigger change on remote file

### Parameters

*   **`URL`** (*required*): the url of the file

		example:
			http:///host/path/to/file

	>note: currently supported protocols: http, https, ftp

*   **`username`** (*optional*): username if authentication is required

*   **`password`** (*optional*): password if authentication is required

*   **`action`** (*optional*): action to execute if the event is triggered

		example:
			@{host.action.1}
				''',
				'cn'	:	''''''
			},
			'parameter'	:	{
				'URL'		:	{
					'type'		:	'line',
					'required'	:	True,
					'visible'	:	True
				},
				'username'	:	{
					'type'		:	'line',
					'required'	:	False,
					'visible'	:	True
				},
				'password'	:	{
					'type'		:	'line',
					'required'	:	False,
					'visible'	:	True
				},
				'action'	:	{
					'type'		:	'action',#state?
					'required'	:	False,
					'visible'	:	True
				}
			}
		},

		# handle remote git repo
		'git'	:	{
			'module'	:	'remote.git',
			'distro'	:	None,
			'reference'	:	{
				'en'	:	'''
### Description
Trigger change on remote git repository

### Parameters

*   **`repo`** (*required*): the URI of the git repo

		example:
			https:///host/path/to/git/repo

*   **`branch`** (*optional*): repository branch to watch

	>note: default: master

*   **`username`** (*optional*): username if authentication is required

*   **`password`** (*optional*): password if authentication is required

*   **`action`** (*optional*): action to execute if the event is triggered

		example:
			@{host.action.1}
				''',
				'cn'	:	''''''
			},
			'parameter'	:	{
				'repo'		:	{
					'type'		:	'line',
					'required'	:	True,
					'visible'	:	True
				},
				'branch'	:	{
					'type'		:	'line',
					'required'	:	False,
					'visible'	:	True
				},
				'username'	:	{
					'type'		:	'line',
					'required'	:	False,
					'visible'	:	True
				},
				'password'	:	{
					'type'		:	'line',
					'required'	:	False,
					'visible'	:	True
				},
				'action'	:	{
					'type'		:	'action',#state?
					'required'	:	False,
					'visible'	:	True
				}
			}
		},

		# handle remote hg repo
		'hg'	:	{
			'module'	:	'remote.hg',
			'distro'	:	None,
			'reference'	:	{
				'en'	:	'''
### Description
Trigger change on remote Mercurial (hg) repository

### Parameters

*   **`repo`** (*required*): the URI of the hg repo

		example:
			https:///host/path/to/hg/repo

*   **`branch`** (*optional*): repository branch to watch

	>note: default: master

*   **`username`** (*optional*): username if authentication is required

*   **`password`** (*optional*): password if authentication is required

*   **`action`** (*optional*): action to execute if the event is triggered

		example:
			@{host.action.1}
				''',
				'cn'	:	''''''
			},
			'parameter'	:	{
				'repo'		:	{
					'type'		:	'line',
					'required'	:	True,
					'visible'	:	True
				},
				'branch'	:	{
					'type'		:	'line',
					'required'	:	False,
					'visible'	:	True
				},
				'username'	:	{
					'type'		:	'line',
					'required'	:	False,
					'visible'	:	True
				},
				'password'	:	{
					'type'		:	'line',
					'required'	:	False,
					'visible'	:	True
				},
				'action'	:	{
					'type'		:	'action',#state?
					'required'	:	False,
					'visible'	:	True
				}
			}
		},

		# handle remote svn repo
		'svn'	:	{
			'module'	:	'remote.svn',
			'distro'	:	None,
			'reference'	:	{
				'en'	:	'''
### Description
Trigger change on remote Subversion (svn) repository

### Parameters

*   **`repo`** (*required*): the URI of the svn repo

		example:
			https:///host/path/to/svn/repo

*   **`branch`** (*optional*): repository branch to watch

	>note: default: master

*   **`username`** (*optional*): username if authentication is required

*   **`password`** (*optional*): password if authentication is required

*   **`action`** (*optional*): action to execute if the event is triggered

		example:
			@{host.action.1}
				''',
				'cn'	:	''''''
			},
			'parameter'	:	{
				'repo'		:	{
					'type'		:	'line',
					'required'	:	True,
					'visible'	:	True
				},
				'branch'	:	{
					'type'		:	'line',
					'required'	:	False,
					'visible'	:	True
				},
				'username'	:	{
					'type'		:	'line',
					'required'	:	False,
					'visible'	:	True
				},
				'password'	:	{
					'type'		:	'line',
					'required'	:	False,
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
