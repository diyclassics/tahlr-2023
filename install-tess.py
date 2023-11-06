from cltk.data.fetch import FetchCorpus
corpus_downloader = FetchCorpus(language='lat')
corpus_downloader.import_corpus('lat_text_tesserae')
corpus_downloader.import_corpus('lat_models_cltk')
corpus_downloader = FetchCorpus(language='grc')
corpus_downloader.import_corpus('grc_text_tesserae')
corpus_downloader.import_corpus('grc_models_cltk')
