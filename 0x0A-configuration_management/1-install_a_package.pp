# Install flask for python
package{ 'flask':
    require => Exec['pip3 install flask'],

    }
