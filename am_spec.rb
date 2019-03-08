require 'rspec'
require_relative './am.rb'

RSpec.describe AM, "stuff" do
  let(:url) { 'https://www.am.com.mx/noticias/Arriba-Guaido-a-Buenos-Aires-sigue-desafiando-a-Maduro-20190302-0008.html' }
  let(:article) { AM.new url }

  describe "#new" do
    it "parses the article's title correctly" do
      expect(article.title).to match(/Arriba Guaidó a Buenos Aires/)
    end

    it "parses the article's date correctly" do
      expect(article.date).to match(/02 de Marzo/)
    end

    it "parses the article's author correctly" do
      expect(article.author).to match(/Redacción AM/)
    end

    it "parses the article's tags correctly" do
      expect(article.tags.first).to match(/NOTICIAS/)
    end
     
    it "parses the article's content correctly" do
      expect(article.content).to match(/El titular de la Asamblea Nacional/)
    end
  end
end
