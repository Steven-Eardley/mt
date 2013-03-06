#! /bin/bash
cd /group/project/statmt13/mt-class
echo "starting standard"
time ./moses -f model/de-en/moses.ini < test/test.de > ~/mt/standard 2> ~/mt/standard-out
echo "starting reorder0"
time ./moses -f model/de-en/moses.ini -dl 0 < test/test.de > ~/mt/reorder0 2> ~/mt/reorder0-out
echo "starting reorder1"
time ./moses -f model/de-en/moses.ini -dl 1 < test/test.de > ~/mt/reorder1 2> ~/mt/reorder1-out
echo "starting reorder2"
time ./moses -f model/de-en/moses.ini -dl 2 < test/test.de > ~/mt/reorder2 2> ~/mt/reorder2-out
echo "starting reorder3"
time ./moses -f model/de-en/moses.ini -dl 3 < test/test.de > ~/mt/reorder3 2> ~/mt/reorder3-out
echo "starting reorder4"
time ./moses -f model/de-en/moses.ini -dl 4 < test/test.de > ~/mt/reorder4 2> ~/mt/reorder4-out
echo "starting reorder5"
time ./moses -f model/de-en/moses.ini -dl 5 < test/test.de > ~/mt/reorder5 2> ~/mt/reorder5-out
echo "starting reorder6"
time ./moses -f model/de-en/moses.ini -dl 6 < test/test.de > ~/mt/reorder6 2> ~/mt/reorder6-out
echo "starting reorder7"
time ./moses -f model/de-en/moses.ini -dl 7 < test/test.de > ~/mt/reorder7 2> ~/mt/reorder7-out
echo "finished"

#multi-bleu.perl test/test.en test/test.en < ~/mt/test