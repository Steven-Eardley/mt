#! /bin/bash
cd /group/project/statmt13/mt-class
time moses -f model/de-en/moses.ini < test/test.de > ~/mt/standard
time moses -f model/de-en/moses.ini -dl 0 < test/test.de > ~/mt/reorder0
time moses -f model/de-en/moses.ini -dl 1 < test/test.de > ~/mt/reorder1
time moses -f model/de-en/moses.ini -dl 2 < test/test.de > ~/mt/reorder2
time moses -f model/de-en/moses.ini -dl 3 < test/test.de > ~/mt/reorder3
time moses -f model/de-en/moses.ini -dl 4 < test/test.de > ~/mt/reorder4
time moses -f model/de-en/moses.ini -dl 5 < test/test.de > ~/mt/reorder5
time moses -f model/de-en/moses.ini -dl 6 < test/test.de > ~/mt/reorder6
time moses -f model/de-en/moses.ini -dl 7 < test/test.de > ~/mt/reorder7

#multi-bleu.perl test/test.en test/test.en < ~/mt/test