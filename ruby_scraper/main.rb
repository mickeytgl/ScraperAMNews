#!/usr/bin/env ruby

require_relative 'am.rb'

ARGV.each do|url|
  article = AM.new url
  print article.to_csv_row 
end
