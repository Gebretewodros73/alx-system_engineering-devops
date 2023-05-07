#!/usr/bin/env ruby
input_string = ARGV[0]
regex = input_string.scan(/School/)

if regex.length > 0
  puts regex.join

else
  puts ""
end
