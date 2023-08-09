# Corrects a typo in WordPress settings to fix the 500 error
exec { 'fix_typo_in_wp_settings':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/bin',
  onlyif  => 'grep -q "phpp" /var/www/html/wp-settings.php',
}
