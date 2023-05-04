#!/usr/bin/env ruby
input_string = ARGV[0]
regex = input_string.match(/School/, nil, Oniguruma::OPTION_NONE)
if regex
  puts regex[0]
else
  puts ""
end
