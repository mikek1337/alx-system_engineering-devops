class mymodule::create_file{
file { "/tmp/school" :
    ensure => file,
    mode => '0744',
    owner => www-data,
    group => www-data,
    source => "I Love Puppet"
}
}
