# Explicitly declare the package provider to ensure consistency
Package { provider => 'pip3' }

# Install the Flask package with specific version
package { 'Flask':
  ensure => '2.1.0',
}

