A Python Persian Text Sentiment Analyser
=======================

A package for determining sentiment score of Persian texts. I used NLTK, Hazm packages and Naive Bayes classifier for this purpose.

Please contribute to this project because this is the first python package in this field, i'm at the first of the road and absolutely it has a few bugs.


Example
--------

    >>> from pertimental.sentiment import PersianSentiment
    >>> print(PersianSentiment().score("سلام دنیا. این یک متن خیلی خوب برای تست است."))
    0.6


See also
--------
Special thanks to Sepidarr.ir team Sina Sadrzadeh and Masoud Mirzaei.