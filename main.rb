#!/usr/bin/env ruby

require_relative 'ruby_scraper/am.rb'

ARGV.each do|url|
  article = AM.new url
  print article.to_csv_row 
end
