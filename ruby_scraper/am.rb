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
      @doc.xpath('/html/body/main/article/div/header/h1').children.text
    end

    def get_author
      @doc.xpath('/html/body/main/article/div/header/div[2]/p/span').text.strip
    end

    def get_date
      @doc.xpath('/html/body/main/article/div/header/div[2]/div[2]/time').text
    end

    def get_content
      @doc.css('/html/body/main/article/div/div/div[2]/div[2]/p').text
    end

    def get_tags
      path = @doc.xpath('//*[@class="tags__content"]/li').children
      path.map { |element| element.text.capitalize }
    end
end

