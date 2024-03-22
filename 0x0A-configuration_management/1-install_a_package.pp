# Kill process named killmenow
exec { 'pkill_killmenow':
  command  => 'pkill killmenow',
  provider => shell,
}
