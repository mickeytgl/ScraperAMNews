class AmCSV
  def self.parse(urls)
    rows = urls.map do |url|
      AM.new(url).to_csv_row
    end

    CSV.open("periodico_am_articles.csv", "wb") do
      
    end
  end


end
