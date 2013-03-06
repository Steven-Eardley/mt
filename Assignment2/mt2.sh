#! /bin/bash
cd /group/project/statmt13/mt-class
time ./moses -f model/de-en/moses.ini < test/test.de > ~/mt/standard 2> ~/mt/standard-out
time ./moses -f model/de-en/moses.ini -dl 0 < test/test.de > ~/mt/reorder0 2> ~/mt/reorder0-out
time ./moses -f model/de-en/moses.ini -dl 1 < test/test.de > ~/mt/reorder1 2> ~/mt/reorder1-out
time ./moses -f model/de-en/moses.ini -dl 2 < test/test.de > ~/mt/reorder2 2> ~/mt/reorder2-out
time ./moses -f model/de-en/moses.ini -dl 3 < test/test.de > ~/mt/reorder3 2> ~/mt/reorder3-out
time ./moses -f model/de-en/moses.ini -dl 4 < test/test.de > ~/mt/reorder4 2> ~/mt/reorder4-out
time ./moses -f model/de-en/moses.ini -dl 5 < test/test.de > ~/mt/reorder5 2> ~/mt/reorder5-out
time ./moses -f model/de-en/moses.ini -dl 6 < test/test.de > ~/mt/reorder6 2> ~/mt/reorder6-out
time ./moses -f model/de-en/moses.ini -dl 7 < test/test.de > ~/mt/reorder7 2> ~/mt/reorder7-out

#multi-bleu.perl test/test.en test/test.en < ~/mt/test