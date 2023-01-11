# Install flask for python
exec{ 'pip-install':
    command => '/usr/bin/pip3 install flask'
    }
package{ 'flask':
    ensure  => installed,
    require => Exec['pip-install'],

    }
