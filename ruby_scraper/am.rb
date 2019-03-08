require 'nokogiri'
require 'open-uri'
require 'pry'

class AM
  attr_reader :title, :author, :date, :content, :doc, :tags

  def initialize(url)
    @doc = Nokogiri::HTML(open(url))
    @title = get_title
    @author = get_author
    @date = get_date
    @content = get_content
    @tags = get_tags
  end

  def to_csv_row
    [title, author, date, content, tags]
  end

  private

    def get_title
      @doc.xpath('//*[@class="newsfull__title"]').children.text
    end

    def get_author
      @doc.xpath('//*[@class="newsfull__author"]/span').text.strip
    end

    def get_date
      @doc.xpath('//*[@class="newsfull__time"]/@datetime').first.value
    end

    def get_content
      @doc.xpath('//div[@class="newsfull__body"]/p').text
    end

    def get_tags
      path = @doc.xpath('//*[@class="tags__content"]/li').children
      path.map { |element| element.text.capitalize }
    end
end

