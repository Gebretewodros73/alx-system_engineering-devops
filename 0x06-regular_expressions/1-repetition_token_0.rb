#!/usr/bin/env ruby
input_string = ARGV[0]
regex = input_string.scan(/hbt+t+n/)

if regex.length > 0
  match = regex[0]
  if match.count("t") < 6
    puts match
  end
end
